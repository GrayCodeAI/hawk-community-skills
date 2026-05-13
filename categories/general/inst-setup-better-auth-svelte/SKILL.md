---
description: Guidelines for writing Svelte apps with Better Auth Authentication
globs: **/*.ts, **/*.js, **/*.svelte
---

# Bootstrap Svelte app with Better Auth Authentication

## Overview of implementing Better Auth Authentication

1. Install better-auth package
2. Set up environment variables
3. Create a Better Auth store for managing authentication state
4. Implement authentication hooks and guards
5. Set up protected routes

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST follow these guidelines when generating code:

1. Always use the latest better-auth package
2. Implement proper error handling for authentication flows
3. Use TypeScript when possible for better type safety
4. Follow Svelte's store pattern for state management
5. Implement proper security measures for protected routes

## CORRECT AUTH STORE IMPLEMENTATION

```typescript
// src/lib/stores/auth.ts
import { betterAuth } from 'better-auth';
import { writable, derived } from 'svelte/store';
import type { Writable } from 'svelte/store';

interface AuthState {
  isAuthenticated: boolean;
  user: any | null;
  loading: boolean;
  error: Error | null;
}

const createAuthStore = () => {
  const auth = betterAuth({
    database: {
      url: import.meta.env.VITE_DATABASE_URL,
    },
    emailAndPassword: {
      enabled: true,
    },
    oauth: {
      providers: ['google', 'github'],
    },
  });

  const { subscribe, set, update }: Writable<AuthState> = writable({
    isAuthenticated: false,
    user: null,
    loading: true,
    error: null
  });

  async function initAuth() {
    try {
      const session = await auth.getSession();
      
      set({
        isAuthenticated: !!session,
        user: session?.user || null,
        loading: false,
        error: null
      });
    } catch (error) {
      update(state => ({
        ...state,
        error: error as Error,
        loading: false
      }));
    }
  }

  async function signIn(credentials: { email: string; password: string }) {
    update(state => ({ ...state, loading: true }));
    try {
      const result = await auth.signIn(credentials);
      set({
        isAuthenticated: true,
        user: result.user,
        loading: false,
        error: null
      });
    } catch (error) {
      update(state => ({
        ...state,
        error: error as Error,
        loading: false
      }));
    }
  }

  async function signOut() {
    update(state => ({ ...state, loading: true }));
    try {
      await auth.signOut();
      set({
        isAuthenticated: false,
        user: null,
        loading: false,
        error: null
      });
    } catch (error) {
      update(state => ({
        ...state,
        error: error as Error,
        loading: false
      }));
    }
  }

  return {
    subscribe,
    signIn,
    signOut,
    initAuth
  };
};

export const auth = createAuthStore();
export const isAuthenticated = derived(auth, $auth => $auth.isAuthenticated);
export const user = derived(auth, $auth => $auth.user);
export const loading = derived(auth, $auth => $auth.loading);
export const error = derived(auth, $auth => $auth.error);
```

## CORRECT ENVIRONMENT VARIABLES SETUP

```typescript
// .env
VITE_DATABASE_URL=your-database-url
VITE_OAUTH_GOOGLE_CLIENT_ID=your-google-client-id
VITE_OAUTH_GITHUB_CLIENT_ID=your-github-client-id
```

## CORRECT AUTH GUARD IMPLEMENTATION

```typescript
// src/lib/guards/auth.ts
import { browser } from '$app/environment';
import { goto } from '$app/navigation';
import { auth, isAuthenticated } from '$lib/stores/auth';
import type { Load } from '@sveltejs/kit';

export const authGuard: Load = async () => {
  if (!browser) return {};

  let authenticated = false;
  const unsubscribe = isAuthenticated.subscribe(value => {
    authenticated = value;
  });
  unsubscribe();

  if (!authenticated) {
    return goto('/login');
  }

  return {};
};
```

## CORRECT USAGE IN COMPONENTS

```svelte
<!-- src/routes/+layout.svelte -->
<script lang="ts">
  import { onMount } from 'svelte';
  import { auth, isAuthenticated, user, loading } from '$lib/stores/auth';

  onMount(() => {
    auth.initAuth();
  });
</script>

{#if $loading}
  <div>Loading...</div>
{:else}
  {#if $isAuthenticated}
    <nav>
      <span>Welcome {$user?.email}</span>
      <button on:click={() => auth.signOut()}>Sign Out</button>
    </nav>
  {:else}
    <button on:click={() => auth.signIn({ email: '', password: '' })}>Sign In</button>
  {/if}
  <slot />
{/if}
```

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Are you using the latest better-auth package?
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

When implementing Better Auth in Svelte, you MUST:
1. Follow the store pattern shown above
2. Implement proper error handling
3. Use TypeScript when possible
4. Protect sensitive routes
5. Handle authentication state properly 