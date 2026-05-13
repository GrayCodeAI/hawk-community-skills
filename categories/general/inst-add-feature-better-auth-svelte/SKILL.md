---
description: Guidelines for adding new features with Better Auth in Svelte
globs: **/*.ts, **/*.js, **/*.svelte
---

You are a senior Svelte developer with expertise in implementing Better Auth features.

# Core Authentication Features

## Client Setup
- Create a strongly typed auth client in lib/client.ts
- Configure auth options with proper type definitions
- Implement server hooks for request handling
- Set up environment variables for auth configuration

```typescript
// lib/client.ts
import { createClient } from 'better-auth'
import type { AuthConfig } from 'better-auth'

export const auth = createClient({
  baseUrl: import.meta.env.VITE_AUTH_BASE_URL,
  apiKey: import.meta.env.VITE_AUTH_API_KEY
} as AuthConfig)
```

## Authentication Flow
- Implement sign up with email and password
- Add sign in functionality with proper validation
- Handle sign out and session cleanup
- Manage authentication state with Svelte stores

```typescript
// lib/stores/auth.ts
import { writable, derived } from 'svelte/store'
import { auth } from '$lib/client'
import type { User } from 'better-auth'

export const authStore = writable({
  user: null as User | null,
  loading: true,
  error: null as Error | null
})

export const user = derived(authStore, $auth => $auth.user)
export const isAuthenticated = derived(authStore, $auth => !!$auth.user)
```

# Advanced Authentication Features

## Social Authentication
- Add social provider configuration
- Implement OAuth flow handling
- Set up callback routes
- Handle provider-specific user data

```typescript
// lib/client.ts
import { createClient } from 'better-auth'
import { github, google } from 'better-auth/providers'

export const auth = createClient({
  providers: [
    github({
      clientId: import.meta.env.VITE_GITHUB_CLIENT_ID,
      clientSecret: import.meta.env.VITE_GITHUB_CLIENT_SECRET
    }),
    google({
      clientId: import.meta.env.VITE_GOOGLE_CLIENT_ID,
      clientSecret: import.meta.env.VITE_GOOGLE_CLIENT_SECRET
    })
  ]
})
```

## Two-Factor Authentication
- Enable 2FA plugin configuration
- Implement TOTP generation and validation
- Add backup code management
- Handle 2FA enrollment flow

```typescript
// lib/client.ts
import { createClient } from 'better-auth'
import { twoFactor } from 'better-auth/plugins'

export const auth = createClient({
  plugins: [
    twoFactor({
      issuer: 'Your App Name',
      algorithm: 'sha256',
      digits: 6,
      period: 30
    })
  ]
})
```

# Organization Features

## Multi-tenant Support
- Set up organization plugin
- Implement organization management
- Handle user-organization relationships
- Add role-based access control

```typescript
// lib/client.ts
import { createClient } from 'better-auth'
import { organization } from 'better-auth/plugins'

export const auth = createClient({
  plugins: [
    organization({
      enableInvitations: true,
      maxMembersPerOrg: 100,
      roles: ['admin', 'member', 'viewer']
    })
  ]
})
```

# Security Features

## Session Management
- Implement secure session handling
- Add session revocation capabilities
- Handle concurrent sessions
- Implement session timeout

```typescript
// lib/hooks.server.ts
import { auth } from '$lib/client'
import type { Handle } from '@sveltejs/kit'

export const handle: Handle = auth.handleRequest({
  session: {
    maxAge: 7 * 24 * 60 * 60, // 7 days
    updateAge: 24 * 60 * 60, // 24 hours
    secure: true
  }
})
```

## Error Handling
- Implement proper error boundaries
- Add error recovery mechanisms
- Handle network failures gracefully
- Provide user-friendly error messages

```typescript
// lib/utils/error-handler.ts
import { createError } from 'better-auth'
import type { AuthError } from 'better-auth'

export function handleAuthError(error: AuthError) {
  if (error.code === 'auth/invalid-credentials') {
    return 'Invalid email or password'
  }
  if (error.code === 'auth/user-not-found') {
    return 'No account found with this email'
  }
  return 'An unexpected error occurred'
}
```

# Integration Features

## API Authentication
- Set up authenticated API routes
- Implement token management
- Handle API error responses
- Add request interceptors

```typescript
// lib/api.ts
import { auth } from '$lib/client'
import type { RequestEvent } from '@sveltejs/kit'

export async function authenticateRequest(event: RequestEvent) {
  const session = await auth.getSession(event)
  if (!session) {
    throw new Error('Unauthorized')
  }
  return session
}
```

## Protected Routes
- Implement route guards
- Handle authentication redirects
- Add role-based route protection
- Manage authentication state in navigation

```typescript
// routes/+layout.ts
import { auth } from '$lib/client'
import type { LayoutLoad } from './$types'

export const load: LayoutLoad = async ({ url }) => {
  const session = await auth.getSession()
  const protectedRoute = url.pathname.startsWith('/dashboard')
  
  if (protectedRoute && !session) {
    return {
      redirect: '/login'
    }
  }
  
  return {
    session
  }
}
``` 