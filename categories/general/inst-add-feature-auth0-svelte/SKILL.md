---
description: Guidelines for adding new features with Auth0 in Svelte applications
globs: **/*.ts, **/*.js, **/*.svelte
---

You are a senior Svelte developer with expertise in Auth0 integration and building secure applications.

# Authentication Features

## User Authentication
- Implement login with redirect flow using Auth0 SPA SDK
```typescript
const login = async () => {
  await auth0Client.loginWithRedirect({
    appState: { returnTo: window.location.pathname }
  });
};
```

- Add logout functionality with proper redirect
```typescript
const logout = async () => {
  await auth0Client.logout({
    logoutParams: {
      returnTo: window.location.origin
    }
  });
};
```

- Handle authentication callback
```typescript
if (window.location.search.includes('code=')) {
  const { appState } = await auth0Client.handleRedirectCallback();
  window.history.replaceState({}, document.title, appState?.returnTo || window.location.pathname);
}
```

## Protected Routes
- Create authentication guard using SvelteKit hooks
```typescript
// src/hooks.server.ts
import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
  const session = event.cookies.get('auth_session');
  event.locals.authenticated = Boolean(session);
  return resolve(event);
};
```

- Implement client-side route protection
```typescript
// src/routes/protected/+page.ts
import { redirect } from '@sveltejs/kit';
import type { PageLoad } from './$types';

export const load: PageLoad = async ({ parent }) => {
  const { session } = await parent();
  if (!session) {
    throw redirect(307, '/login');
  }
};
```

# API Integration

## Token Management
- Implement secure token storage
```typescript
const getAccessToken = async () => {
  try {
    return await auth0Client.getTokenSilently();
  } catch (error) {
    console.error('Error getting access token:', error);
    throw error;
  }
};
```

- Add token refresh logic
```typescript
const refreshToken = async () => {
  try {
    await auth0Client.checkSession();
  } catch (error) {
    console.error('Error refreshing token:', error);
    throw error;
  }
};
```

## API Authorization
- Create authenticated fetch utility
```typescript
const authFetch = async (url: string, options: RequestInit = {}) => {
  const token = await getAccessToken();
  return fetch(url, {
    ...options,
    headers: {
      ...options.headers,
      Authorization: `Bearer ${token}`
    }
  });
};
```

# User Profile Features

## Profile Management
- Implement user profile retrieval
```typescript
const getUserProfile = async () => {
  try {
    const user = await auth0Client.getUser();
    return user;
  } catch (error) {
    console.error('Error getting user profile:', error);
    throw error;
  }
};
```

- Add profile update functionality
```typescript
const updateUserMetadata = async (metadata: Record<string, any>) => {
  const token = await getAccessToken();
  const domain = import.meta.env.VITE_AUTH0_DOMAIN;
  const userId = (await auth0Client.getUser()).sub;
  
  return fetch(`https://${domain}/api/v2/users/${userId}`, {
    method: 'PATCH',
    headers: {
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ user_metadata: metadata })
  });
};
```

# Role-Based Access Control

## Role Management
- Implement role checking
```typescript
const hasRole = (roles: string[]) => {
  const userRoles = user?.['https://my-app.com/roles'] || [];
  return roles.some(role => userRoles.includes(role));
};
```

- Create role-based component guard
```typescript
// src/lib/components/RoleGuard.svelte
<script lang="ts">
  import { user } from '$lib/stores/auth';
  
  export let roles: string[] = [];
  
  $: hasAccess = roles.some(role => 
    $user?.['https://my-app.com/roles']?.includes(role)
  );
</script>

{#if hasAccess}
  <slot />
{/if}
```

# Error Handling

## Authentication Errors
- Implement error boundaries for auth operations
```typescript
const handleAuthError = (error: Error) => {
  if (error.message.includes('login_required')) {
    auth0Client.loginWithRedirect();
  } else if (error.message.includes('consent_required')) {
    console.error('Consent required for this operation');
  } else {
    console.error('Authentication error:', error);
  }
};
```

## Token Errors
- Add token error handling
```typescript
const handleTokenError = async (error: Error) => {
  if (error.message.includes('invalid_grant')) {
    await auth0Client.logout({
      logoutParams: {
        returnTo: window.location.origin
      }
    });
  } else {
    console.error('Token error:', error);
  }
};
```

# Security Features

## CSRF Protection
- Implement state parameter validation
```typescript
const generateState = () => {
  const array = new Uint32Array(5);
  window.crypto.getRandomValues(array);
  return Array.from(array, dec => dec.toString(36)).join('');
};

const login = async () => {
  const state = generateState();
  sessionStorage.setItem('auth_state', state);
  await auth0Client.loginWithRedirect({
    appState: { state }
  });
};
```

## Session Management
- Add session monitoring
```typescript
auth0Client.checkSession().catch(error => {
  if (error.error === 'login_required') {
    auth0Client.loginWithRedirect();
  }
});
```

# Testing Features

## Authentication Mocking
- Create auth mock for testing
```typescript
// src/lib/test/mockAuth.ts
export const mockAuth0Client = {
  isAuthenticated: () => Promise.resolve(true),
  getUser: () => Promise.resolve({
    sub: 'test-user',
    email: 'test@example.com',
    'https://my-app.com/roles': ['user']
  }),
  getTokenSilently: () => Promise.resolve('mock-token')
};
```

## Integration Testing
- Implement auth integration tests
```typescript
// src/routes/protected/+page.test.ts
import { render, screen } from '@testing-library/svelte';
import Protected from './+page.svelte';
import { auth } from '$lib/stores/auth';

test('protected route requires authentication', async () => {
  auth.set({ isAuthenticated: false });
  render(Protected);
  expect(screen.getByText('Please log in')).toBeInTheDocument();
});
``` 