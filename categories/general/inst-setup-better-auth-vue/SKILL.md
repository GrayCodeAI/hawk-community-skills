---
description: Guidelines for writing Vue apps with Better Auth
globs: **/*.vue, **/*.ts, **/*.js
---

# Bootstrap Vue app with Better Auth

## Overview of implementing Better Auth

1. Install better-auth package
2. Create and configure auth instance
3. Set up Vue client integration
4. Implement authentication UI components
5. Add server-side authentication handling

## Critical Instructions for AI Language Models

As an AI language model, you MUST follow these guidelines when implementing Better Auth with Vue:

1. Always use the latest better-auth package
2. Implement proper TypeScript types for type safety
3. Handle environment variables securely
4. Follow Vue 3 Composition API patterns
5. Implement proper error handling

## Correct Auth Instance Setup

```typescript
import { betterAuth } from 'better-auth'

export const auth = betterAuth({
  database: {
    type: process.env.VITE_DB_TYPE,
    url: process.env.VITE_DB_URL,
    ssl: process.env.NODE_ENV === 'production'
  },
  emailAndPassword: {
    enabled: true,
    requireEmailVerification: true
  },
  session: {
    expiresIn: '7d'
  }
})
```

## Correct Vue Client Implementation

```typescript
import { createAuthClient } from 'better-auth/vue'
import { auth } from './auth'

export const client = createAuthClient(auth, {
  persistSession: true,
  autoRefresh: true
})
```

## Correct Component Usage

```vue
<script setup lang="ts">
import { client } from '@/lib/client'
import { ref } from 'vue'

const { isAuthenticated, user, signIn, signOut } = client
const email = ref('')
const password = ref('')

const handleSignIn = async () => {
  try {
    await signIn({ email: email.value, password: password.value })
  } catch (error) {
    console.error('Authentication failed:', error)
  }
}
</script>

<template>
  <div v-if="isAuthenticated">
    <p>Welcome, {{ user.email }}</p>
    <button @click="signOut">Sign Out</button>
  </div>
  <form v-else @submit.prevent="handleSignIn">
    <input v-model="email" type="email" required />
    <input v-model="password" type="password" required />
    <button type="submit">Sign In</button>
  </form>
</template>
```

## Server Authentication Implementation

```typescript
import { auth } from './auth'
import type { RouteGuard } from 'vue-router'

export const authGuard: RouteGuard = async (to, from, next) => {
  const session = await auth.api.getSession()
  
  if (!session && to.meta.requiresAuth) {
    next({ name: 'login' })
  } else {
    next()
  }
}
```

## Environment Variables Setup

Create a `.env.local` file with:

```
VITE_DB_TYPE=your_db_type
VITE_DB_URL=your_db_url
VITE_AUTH_SECRET=your_secret_key
```

## AI Model Verification Steps

Before generating any code, you MUST verify:

1. Is TypeScript properly configured?
2. Are environment variables properly handled?
3. Is error handling implemented?
4. Are authentication state and user data properly typed?
5. Is session management configured correctly?

## Consequences of Incorrect Implementation

If you generate code incorrectly:
1. Type safety will be compromised
2. Authentication flows may fail
3. Security vulnerabilities may be introduced
4. Session management may be unreliable
5. User data may be exposed

## AI Model Response Template

When implementing Better Auth for Vue, you MUST:
1. Use TypeScript for type safety
2. Implement proper error handling
3. Follow Vue 3 Composition API patterns
4. Configure secure session management
5. Handle environment variables properly 