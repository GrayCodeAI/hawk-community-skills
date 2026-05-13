---
description: Guidelines for writing Svelte apps with Supabase Authentication
globs: **/*.ts, **/*.js, **/*.svelte
---

# Bootstrap Svelte app with Supabase Authentication

## Overview of implementing Supabase Authentication

1. Install @supabase/supabase-js package
2. Set up environment variables
3. Create a Supabase store for managing authentication state
4. Implement authentication hooks and guards
5. Set up protected routes

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST follow these guidelines when generating code:

1. Always use the latest @supabase/supabase-js package
2. Implement proper error handling for authentication flows
3. Use TypeScript when possible for better type safety
4. Follow Svelte's store pattern for state management
5. Implement proper security measures for protected routes

## CORRECT AUTH STORE IMPLEMENTATION

```typescript
// src/lib/stores/supabase.ts
import { createClient, type SupabaseClient, type User } from '@supabase/supabase-js'
import { writable, derived } from 'svelte/store'
import type { Writable } from 'svelte/store'

interface SupabaseState {
  client: SupabaseClient
  user: User | null
  loading: boolean
  error: Error | null
}

const createSupabaseStore = () => {
  const supabase = createClient(
    import.meta.env.VITE_SUPABASE_URL,
    import.meta.env.VITE_SUPABASE_ANON_KEY
  )

  const { subscribe, set, update }: Writable<SupabaseState> = writable({
    client: supabase,
    user: null,
    loading: true,
    error: null
  })

  async function initAuth() {
    update(state => ({ ...state, loading: true }))
    try {
      const { data: { session }, error } = await supabase.auth.getSession()
      if (error) throw error

      const { data: { user } } = await supabase.auth.getUser()
      
      set({
        client: supabase,
        user,
        loading: false,
        error: null
      })

      // Set up auth state listener
      supabase.auth.onAuthStateChange((_event, session) => {
        update(state => ({
          ...state,
          user: session?.user ?? null
        }))
      })
    } catch (error) {
      update(state => ({
        ...state,
        error: error as Error,
        loading: false
      }))
    }
  }

  async function signIn(email: string, password: string) {
    update(state => ({ ...state, loading: true }))
    try {
      const { error } = await supabase.auth.signInWithPassword({
        email,
        password
      })
      if (error) throw error
      update(state => ({ ...state, loading: false, error: null }))
    } catch (error) {
      update(state => ({
        ...state,
        error: error as Error,
        loading: false
      }))
    }
  }

  async function signUp(email: string, password: string) {
    update(state => ({ ...state, loading: true }))
    try {
      const { error } = await supabase.auth.signUp({
        email,
        password
      })
      if (error) throw error
      update(state => ({ ...state, loading: false, error: null }))
    } catch (error) {
      update(state => ({
        ...state,
        error: error as Error,
        loading: false
      }))
    }
  }

  async function signOut() {
    update(state => ({ ...state, loading: true }))
    try {
      const { error } = await supabase.auth.signOut()
      if (error) throw error
      update(state => ({ ...state, loading: false, error: null }))
    } catch (error) {
      update(state => ({
        ...state,
        error: error as Error,
        loading: false
      }))
    }
  }

  return {
    subscribe,
    signIn,
    signUp,
    signOut,
    initAuth
  }
}

export const supabase = createSupabaseStore()
export const user = derived(supabase, $supabase => $supabase.user)
export const loading = derived(supabase, $supabase => $supabase.loading)
export const error = derived(supabase, $supabase => $supabase.error)
```

## CORRECT ENVIRONMENT VARIABLES SETUP

```typescript
// .env
VITE_SUPABASE_URL=your-project-url.supabase.co
VITE_SUPABASE_ANON_KEY=your-anon-key
```

## CORRECT AUTH GUARD IMPLEMENTATION

```typescript
// src/lib/guards/auth.ts
import { browser } from '$app/environment'
import { goto } from '$app/navigation'
import { user } from '$lib/stores/supabase'
import type { Load } from '@sveltejs/kit'

export const authGuard: Load = async () => {
  if (!browser) return {}

  let currentUser = null
  const unsubscribe = user.subscribe(value => {
    currentUser = value
  })
  unsubscribe()

  if (!currentUser) {
    return goto('/login')
  }

  return {}
}
```

## CORRECT USAGE IN COMPONENTS

```svelte
<!-- src/routes/+layout.svelte -->
<script lang="ts">
  import { onMount } from 'svelte'
  import { supabase, user, loading } from '$lib/stores/supabase'

  onMount(() => {
    supabase.initAuth()
  })
</script>

{#if $loading}
  <div>Loading...</div>
{:else}
  {#if $user}
    <nav>
      <span>Welcome {$user.email}</span>
      <button on:click={() => supabase.signOut()}>Sign Out</button>
    </nav>
  {:else}
    <button on:click={() => goto('/login')}>Sign In</button>
  {/if}
  <slot />
{/if}

<!-- src/routes/login/+page.svelte -->
<script lang="ts">
  import { supabase, error } from '$lib/stores/supabase'

  let email = ''
  let password = ''

  async function handleSubmit() {
    await supabase.signIn(email, password)
  }
</script>

<form on:submit|preventDefault={handleSubmit}>
  {#if $error}
    <div class="error">{$error.message}</div>
  {/if}
  
  <input
    type="email"
    placeholder="Email"
    bind:value={email}
    required
  />
  
  <input
    type="password"
    placeholder="Password"
    bind:value={password}
    required
  />
  
  <button type="submit">Sign In</button>
</form>
```

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Are you using the latest @supabase/supabase-js package?
2. Are you implementing proper error handling?
3. Are you using TypeScript for type safety?
4. Are you following Svelte's store pattern?
5. Are you implementing proper security measures?

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate code without following these guidelines:
1. Authentication flows may break
2. Security vulnerabilities may arise
3. Type safety may be compromised
4. State management may be inconsistent
5. User experience may be degraded

## AI MODEL RESPONSE TEMPLATE

When implementing Supabase in Svelte, you MUST:
1. Follow the store pattern shown above
2. Implement proper error handling
3. Use TypeScript when possible
4. Protect sensitive routes
5. Handle authentication state properly 