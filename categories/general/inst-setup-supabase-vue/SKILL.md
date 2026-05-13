---
description: Guidelines for writing Vue apps with Supabase Auth
globs: **/*.vue, **/*.ts, **/*.js
---

# Bootstrap Vue app with Supabase Auth

## Overview of implementing Supabase Auth

1. Install @supabase/supabase-js package
2. Configure Supabase project settings
3. Create Supabase client instance
4. Implement authentication UI components
5. Add route protection and session management

## Critical Instructions for AI Language Models

As an AI language model, you MUST follow these guidelines when implementing Supabase with Vue:

1. Always use the latest @supabase/supabase-js package
2. Implement proper TypeScript types for type safety
3. Handle environment variables securely
4. Follow Vue 3 Composition API patterns
5. Implement proper error handling

## Correct Client Setup

```typescript
import { createClient } from '@supabase/supabase-js'
import type { Database } from '@/types/supabase'

export const supabase = createClient<Database>(
  import.meta.env.VITE_SUPABASE_URL,
  import.meta.env.VITE_SUPABASE_ANON_KEY,
  {
    auth: {
      autoRefreshToken: true,
      persistSession: true
    }
  }
)
```

## Correct Authentication Implementation

```typescript
// composables/useAuth.ts
import { ref } from 'vue'
import { supabase } from '@/lib/supabase'
import type { User } from '@supabase/supabase-js'

export function useAuth() {
  const user = ref<User | null>(null)
  const loading = ref(true)

  async function signIn(email: string, password: string) {
    try {
      const { error } = await supabase.auth.signInWithPassword({
        email,
        password
      })
      if (error) throw error
    } catch (error) {
      console.error('Error signing in:', error)
      throw error
    }
  }

  async function signOut() {
    try {
      const { error } = await supabase.auth.signOut()
      if (error) throw error
    } catch (error) {
      console.error('Error signing out:', error)
      throw error
    }
  }

  async function getSession() {
    try {
      const { data: { session }, error } = await supabase.auth.getSession()
      if (error) throw error
      user.value = session?.user ?? null
    } catch (error) {
      console.error('Error getting session:', error)
      user.value = null
    } finally {
      loading.value = false
    }
  }

  return {
    user,
    loading,
    signIn,
    signOut,
    getSession
  }
}
```

## Correct Component Usage

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { useAuth } from '@/composables/useAuth'

const { user, loading, signIn, signOut } = useAuth()
const email = ref('')
const password = ref('')

const handleSignIn = async () => {
  try {
    await signIn(email.value, password.value)
  } catch (error) {
    console.error('Authentication failed:', error)
  }
}
</script>

<template>
  <div v-if="loading">Loading...</div>
  <div v-else-if="user">
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

## Route Protection Implementation

```typescript
import { createRouter } from 'vue-router'
import { supabase } from '@/lib/supabase'

const router = createRouter({
  // ... your routes configuration
})

router.beforeEach(async (to, from, next) => {
  const { data: { session } } = await supabase.auth.getSession()

  if (to.meta.requiresAuth && !session) {
    next({ name: 'login' })
  } else {
    next()
  }
})
```

## Environment Variables Setup

Create a `.env.local` file with:

```
VITE_SUPABASE_URL=your-project-url
VITE_SUPABASE_ANON_KEY=your-anon-key
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

When implementing Supabase Auth for Vue, you MUST:
1. Use TypeScript for type safety
2. Implement proper error handling
3. Follow Vue 3 Composition API patterns
4. Configure secure session management
5. Handle environment variables properly 