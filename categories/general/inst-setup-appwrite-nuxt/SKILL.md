---
description: Guidelines for writing Nuxt 3 apps with Appwrite
globs: src/**/*.ts, src/**/*.vue
---

# Appwrite + Nuxt 3 Integration Setup Guide

## Prerequisites
- Node.js and npm installed
- Nuxt 3 project initialized
- Appwrite account and project created

## Installation

Install required dependencies:
```bash
npm install appwrite @nuxtjs/appwrite
```

## Core Configuration

Create Appwrite configuration (nuxt.config.ts):
```typescript
export default defineNuxtConfig({
  modules: ['@nuxtjs/appwrite'],
  appwrite: {
    endpoint: process.env.NUXT_PUBLIC_APPWRITE_ENDPOINT || 'https://cloud.appwrite.io/v1',
    projectId: process.env.NUXT_PUBLIC_APPWRITE_PROJECT_ID || '',
  },
  runtimeConfig: {
    public: {
      appwriteEndpoint: process.env.NUXT_PUBLIC_APPWRITE_ENDPOINT,
      appwriteProjectId: process.env.NUXT_PUBLIC_APPWRITE_PROJECT_ID,
    },
  },
});
```

## Authentication Implementation

Create authentication composable (composables/useAuth.ts):
```typescript
import { ID } from 'appwrite';

export const useAuth = () => {
  const { $appwrite } = useNuxtApp();
  const user = useState('user', () => null);
  const loading = useState('loading', () => true);

  const checkAuth = async () => {
    try {
      const account = await $appwrite.account.get();
      user.value = account;
      return account;
    } catch (error) {
      user.value = null;
      console.error('Check auth error:', error);
    } finally {
      loading.value = false;
    }
  };

  const login = async (email: string, password: string) => {
    try {
      await $appwrite.account.createEmailSession(email, password);
      return checkAuth();
    } catch (error) {
      console.error('Login error:', error);
      throw error;
    }
  };

  const register = async (email: string, password: string, name: string) => {
    try {
      await $appwrite.account.create(ID.unique(), email, password, name);
      return login(email, password);
    } catch (error) {
      console.error('Register error:', error);
      throw error;
    }
  };

  const logout = async () => {
    try {
      await $appwrite.account.deleteSession('current');
      user.value = null;
    } catch (error) {
      console.error('Logout error:', error);
      throw error;
    }
  };

  return {
    user,
    loading,
    checkAuth,
    login,
    register,
    logout,
  };
};
```

## Database Implementation

Create database composable (composables/useDatabase.ts):
```typescript
import { ID, Query } from 'appwrite';

export const useDatabase = (databaseId: string, collectionId: string) => {
  const { $appwrite } = useNuxtApp();
  const loading = useState('dbLoading', () => false);
  const error = useState('dbError', () => null);

  const listDocuments = async (queries: any[] = []) => {
    loading.value = true;
    error.value = null;
    try {
      return await $appwrite.databases.listDocuments(
        databaseId,
        collectionId,
        [
          Query.limit(20),
          Query.orderDesc('$createdAt'),
          ...queries,
        ]
      );
    } catch (err) {
      error.value = err;
      throw err;
    } finally {
      loading.value = false;
    }
  };

  const getDocument = async (documentId: string) => {
    loading.value = true;
    error.value = null;
    try {
      return await $appwrite.databases.getDocument(
        databaseId,
        collectionId,
        documentId
      );
    } catch (err) {
      error.value = err;
      throw err;
    } finally {
      loading.value = false;
    }
  };

  const createDocument = async (data: any) => {
    loading.value = true;
    error.value = null;
    try {
      return await $appwrite.databases.createDocument(
        databaseId,
        collectionId,
        ID.unique(),
        data
      );
    } catch (err) {
      error.value = err;
      throw err;
    } finally {
      loading.value = false;
    }
  };

  const updateDocument = async (documentId: string, data: any) => {
    loading.value = true;
    error.value = null;
    try {
      return await $appwrite.databases.updateDocument(
        databaseId,
        collectionId,
        documentId,
        data
      );
    } catch (err) {
      error.value = err;
      throw err;
    } finally {
      loading.value = false;
    }
  };

  const deleteDocument = async (documentId: string) => {
    loading.value = true;
    error.value = null;
    try {
      await $appwrite.databases.deleteDocument(
        databaseId,
        collectionId,
        documentId
      );
    } catch (err) {
      error.value = err;
      throw err;
    } finally {
      loading.value = false;
    }
  };

  return {
    loading,
    error,
    listDocuments,
    getDocument,
    createDocument,
    updateDocument,
    deleteDocument,
  };
};
```

## Usage Examples

Authentication Component (components/Auth.vue):
```vue
<script setup lang="ts">
const { login, register, logout, user, loading } = useAuth();
const email = ref('');
const password = ref('');
const name = ref('');
const isRegistering = ref(false);

const handleSubmit = async () => {
  try {
    if (isRegistering.value) {
      await register(email.value, password.value, name.value);
    } else {
      await login(email.value, password.value);
    }
    email.value = '';
    password.value = '';
    name.value = '';
  } catch (error) {
    console.error('Auth error:', error);
  }
};
</script>

<template>
  <div v-if="loading">Loading...</div>
  <div v-else-if="user">
    <p>Welcome, {{ user.name }}!</p>
    <button @click="logout">Logout</button>
  </div>
  <form v-else @submit.prevent="handleSubmit">
    <div>
      <label>Email:</label>
      <input v-model="email" type="email" required />
    </div>
    <div>
      <label>Password:</label>
      <input v-model="password" type="password" required />
    </div>
    <div v-if="isRegistering">
      <label>Name:</label>
      <input v-model="name" type="text" required />
    </div>
    <button type="submit">
      {{ isRegistering ? 'Register' : 'Login' }}
    </button>
    <button type="button" @click="isRegistering = !isRegistering">
      {{ isRegistering ? 'Switch to Login' : 'Switch to Register' }}
    </button>
  </form>
</template>
```

Document List Component (components/DocumentList.vue):
```vue
<script setup lang="ts">
const props = defineProps<{
  databaseId: string;
  collectionId: string;
}>();

const {
  loading,
  error,
  listDocuments,
  createDocument,
  deleteDocument,
} = useDatabase(props.databaseId, props.collectionId);

const documents = ref([]);
const newTitle = ref('');

onMounted(async () => {
  try {
    const response = await listDocuments();
    documents.value = response.documents;
  } catch (error) {
    console.error('Failed to fetch documents:', error);
  }
});

const handleCreate = async () => {
  if (!newTitle.value) return;
  
  try {
    const doc = await createDocument({ title: newTitle.value });
    documents.value.unshift(doc);
    newTitle.value = '';
  } catch (error) {
    console.error('Failed to create document:', error);
  }
};

const handleDelete = async (documentId: string) => {
  try {
    await deleteDocument(documentId);
    documents.value = documents.value.filter(doc => doc.$id !== documentId);
  } catch (error) {
    console.error('Failed to delete document:', error);
  }
};
</script>

<template>
  <div>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">Error: {{ error.message }}</div>
    <div v-else>
      <form @submit.prevent="handleCreate">
        <input v-model="newTitle" placeholder="New document title" required />
        <button type="submit">Create</button>
      </form>

      <div class="documents">
        <div v-for="doc in documents" :key="doc.$id" class="document">
          <h3>{{ doc.title }}</h3>
          <button @click="handleDelete(doc.$id)">Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>
```

## Security Guidelines

1. Store sensitive configuration in environment variables
2. Implement proper error handling for all operations
3. Set appropriate collection permissions in Appwrite Console
4. Use API keys with minimal required scopes
5. Enable HTTPS for production deployments

## Implementation Guidelines

1. Use Nuxt composables for better code organization
2. Implement proper error handling and loading states
3. Use TypeScript for better type safety
4. Keep Appwrite configuration in server-only files
5. Handle loading and error states consistently
6. Use Nuxt's built-in state management

## Error Handling Example

Create error utility (utils/error.ts):
```typescript
export class AppwriteError extends Error {
  constructor(message: string, public originalError: any) {
    super(message);
    this.name = 'AppwriteError';
  }
}

export function handleError(error: any, customMessage = 'Operation failed') {
  console.error(customMessage, error);
  
  if (error.response) {
    throw new AppwriteError(
      `${customMessage}: ${error.response.message}`,
      error
    );
  }
  
  throw new AppwriteError(customMessage, error);
} 