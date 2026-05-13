---
description: Guidelines for writing Svelte apps with Auth0 Authentication
globs: **/*.ts, **/*.js, **/*.svelte
---

# Bootstrap Svelte app with Auth0 Authentication

## Overview of implementing Auth0 Authentication

1. Install @auth0/auth0-spa-js package
2. Set up environment variables
3. Create an Auth0 store for managing authentication state
4. Implement authentication hooks and guards
5. Set up protected routes

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST follow these guidelines when generating code:

1. Always use the latest @auth0/auth0-spa-js package
2. Implement proper error handling for authentication flows
3. Use TypeScript when possible for better type safety
4. Follow Svelte's store pattern for state management
5. Implement proper security measures for protected routes

## CORRECT AUTH STORE IMPLEMENTATION

```typescript
// src/lib/stores/auth.ts
import { createAuth0Client, Auth0Client, User } from '@auth0/auth0-spa-js';
import { writable, derived } from 'svelte/store';
import type { Writable } from 'svelte/store';

interface AuthState {
  client: Auth0Client | null;
  isAuthenticated: boolean;
  user: User | null;
  loading: boolean;
  error: Error | null;
}

const createAuthStore = () => {
  const { subscribe, set, update }: Writable<AuthState> = writable({
    client: null,
    isAuthenticated: false,
    user: null,
    loading: true,
    error: null
  });

  async function initAuth() {
    try {
      const auth0 = await createAuth0Client({
        domain: import.meta.env.VITE_AUTH0_DOMAIN,
        clientId: import.meta.env.VITE_AUTH0_CLIENT_ID,
        authorizationParams: {
          redirect_uri: window.location.origin
        }
      });

      update(state => ({ ...state, client: auth0 }));

      // Handle redirect callback
      if (window.location.search.includes('code=')) {
        await auth0.handleRedirectCallback();
        window.history.replaceState({}, document.title, window.location.pathname);
      }

      const isAuthenticated = await auth0.isAuthenticated();
      const user = isAuthenticated ? await auth0.getUser() : null;

      set({
        client: auth0,
        isAuthenticated,
        user,
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

  async function login() {
    update(state => ({ ...state, loading: true }));
    try {
      const client = await getClient();
      await client.loginWithRedirect();
    } catch (error) {
      update(state => ({
        ...state,
        error: error as Error,
        loading: false
      }));
    }
  }

  async function logout() {
    update(state => ({ ...state, loading: true }));
    try {
      const client = await getClient();
      await client.logout({
        logoutParams: {
          returnTo: window.location.origin
        }
      });
    } catch (error) {
      update(state => ({
        ...state,
        error: error as Error,
        loading: false
      }));
    }
  }

  async function getClient(): Promise<Auth0Client> {
    const state = await get();
    if (!state.client) {
      throw new Error('Auth0 client not initialized');
    }
    return state.client;
  }

  return {
    subscribe,
    login,
    logout,
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
VITE_AUTH0_DOMAIN=your-auth0-domain.auth0.com
VITE_AUTH0_CLIENT_ID=your-auth0-client-id
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
      <span>Welcome {$user?.name}</span>
      <button on:click={() => auth.logout()}>Logout</button>
    </nav>
  {:else}
    <button on:click={() => auth.login()}>Login</button>
  {/if}
  <slot />
{/if}
```

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Are you using the latest @auth0/auth0-spa-js package?
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

When implementing Auth0 in Svelte, you MUST:
1. Follow the store pattern shown above
2. Implement proper error handling
3. Use TypeScript when possible
4. Protect sensitive routes
5. Handle authentication state properly 