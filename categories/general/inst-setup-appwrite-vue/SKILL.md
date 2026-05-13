---
description: Guidelines for writing Vue apps with Appwrite
globs: **/*.ts, **/*.vue, **/*.js
---

# Bootstrap Vue app with Appwrite

## Overview of implementing Appwrite

1. Install the Appwrite SDK package and configure environment variables
2. Initialize the Appwrite client with proper configuration
3. Create utility functions for authentication and database operations
4. Implement authentication flow in Vue components
5. Set up proper error handling and session management

## Project Setup

Install the required dependencies:

```bash
npm install appwrite
```

Create a .env file in your project root:

```env
VITE_APPWRITE_ENDPOINT=https://cloud.appwrite.io/v1
VITE_APPWRITE_PROJECT_ID=your-project-id
```

## Client Configuration

Create src/lib/appwrite.ts for client configuration:

```typescript
import { Client, Account, Databases } from 'appwrite'

const client = new Client()

client
  .setEndpoint(import.meta.env.VITE_APPWRITE_ENDPOINT)
  .setProject(import.meta.env.VITE_APPWRITE_PROJECT_ID)

export const account = new Account(client)
export const databases = new Databases(client)
```

## Authentication Implementation

Create an auth store in src/stores/auth.ts:

```typescript
import { ref } from 'vue'
import { account } from '@/lib/appwrite'
import type { Models } from 'appwrite'

export const useAuthStore = () => {
  const user = ref<Models.User<Models.Preferences> | null>(null)
  const loading = ref(true)

  const checkSession = async () => {
    try {
      const session = await account.getSession('current')
      if (session) {
        user.value = await account.get()
      }
    } catch (error) {
      user.value = null
    } finally {
      loading.value = false
    }
  }

  const login = async (email: string, password: string) => {
    await account.createEmailSession(email, password)
    await checkSession()
  }

  const logout = async () => {
    await account.deleteSession('current')
    user.value = null
  }

  return {
    user,
    loading,
    checkSession,
    login,
    logout
  }
}
```

## Database Operations

Create a database utility in src/lib/database.ts:

```typescript
import { databases } from '@/lib/appwrite'
import { Query } from 'appwrite'
import type { Models } from 'appwrite'

export interface DatabaseOptions {
  databaseId: string
  collectionId: string
}

export class DatabaseService {
  constructor(private options: DatabaseOptions) {}

  async createDocument<T extends object>(
    data: T,
    permissions: string[] = []
  ): Promise<Models.Document> {
    return await databases.createDocument(
      this.options.databaseId,
      this.options.collectionId,
      'unique()',
      data,
      permissions
    )
  }

  async listDocuments<T>(queries: string[] = []): Promise<Models.DocumentList<T>> {
    return await databases.listDocuments(
      this.options.databaseId,
      this.options.collectionId,
      queries
    )
  }

  async updateDocument<T extends object>(
    documentId: string,
    data: Partial<T>
  ): Promise<Models.Document> {
    return await databases.updateDocument(
      this.options.databaseId,
      this.options.collectionId,
      documentId,
      data
    )
  }

  async deleteDocument(documentId: string): Promise<void> {
    await databases.deleteDocument(
      this.options.databaseId,
      this.options.collectionId,
      documentId
    )
  }
}
```

## Usage in Vue Components

Example of a login component:

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'

const email = ref('')
const password = ref('')
const error = ref('')
const { login } = useAuthStore()

const handleLogin = async () => {
  try {
    error.value = ''
    await login(email.value, password.value)
  } catch (e) {
    error.value = e instanceof Error ? e.message : 'An error occurred'
  }
}
</script>

<template>
  <form @submit.prevent="handleLogin">
    <input v-model="email" type="email" required />
    <input v-model="password" type="password" required />
    <p v-if="error" class="error">{{ error }}</p>
    <button type="submit">Login</button>
  </form>
</template>
```

Example of using database operations:

```vue
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { DatabaseService } from '@/lib/database'

interface Item {
  name: string
}

const items = ref<Item[]>([])
const newItem = ref('')

const db = new DatabaseService({
  databaseId: 'your-database-id',
  collectionId: 'your-collection-id'
})

onMounted(async () => {
  const response = await db.listDocuments<Item>()
  items.value = response.documents
})

const addItem = async () => {
  const item = await db.createDocument<Item>({ name: newItem.value })
  items.value.push(item as Item)
  newItem.value = ''
}
</script>

<template>
  <div>
    <ul>
      <li v-for="item in items" :key="item.$id">
        {{ item.name }}
      </li>
    </ul>
    <input v-model="newItem" />
    <button @click="addItem">Add Item</button>
  </div>
</template>
```

## Critical Implementation Notes

1. Always handle loading states and errors appropriately
2. Implement proper session management and token refresh
3. Use environment variables for sensitive configuration
4. Implement proper error boundaries and fallback UI
5. Use TypeScript for better type safety
6. Implement proper data validation before sending to Appwrite
7. Set up appropriate database security rules

## Security Considerations

1. Never expose project ID in client-side code without proper security measures
2. Implement proper session management
3. Use environment variables for sensitive configuration
4. Set up appropriate database security rules

## Troubleshooting

1. Ensure project ID and endpoint are correct
2. Check network requests in browser developer tools
3. Verify proper CORS configuration in Appwrite console
4. Monitor Appwrite logs for potential issues

## Additional Resources
- [Appwrite Documentation](https://appwrite.io/docs)
- [Vue Documentation](https://vuejs.org/)
- [Appwrite Discord Community](https://discord.gg/appwrite) 