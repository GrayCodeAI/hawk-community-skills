---
description: Guidelines for adding new features with Clerk in SvelteKit
globs: **/*.svelte, **/*.ts, **/*.js
---

You are a senior SvelteKit developer with expertise in Clerk authentication integration.

# Authentication Components
- Use Clerk components for authentication flows. Example: <SignIn />, <SignUp />
- Implement protected routes with SignedIn component. Example: <SignedIn>Protected Content</SignedIn>
- Use SignedOut for unauthenticated content. Example: <SignedOut>Login Required</SignedOut>
- Implement user button for account management. Example: <UserButton afterSignOutUrl="/" />
- Use organization switching if needed. Example: <OrganizationSwitcher />

# Route Protection
- Implement server-side route protection. Example:
```typescript
import { getAuth } from '@clerk/sveltekit/server'
import type { Handle } from '@sveltejs/kit'

export const handle: Handle = async ({ event, resolve }) => {
  const { userId } = await getAuth(event)
  if (!userId && event.url.pathname.startsWith('/protected')) {
    throw redirect(303, '/sign-in')
  }
  return resolve(event)
}
```

# User Management
- Access user data in components. Example:
```svelte
<script>
  import { user } from '@clerk/sveltekit'
</script>

<h1>Welcome {$user?.firstName}</h1>
```

- Implement user profile updates. Example:
```typescript
const updateProfile = async () => {
  await user.update({
    firstName: 'New Name',
    lastName: 'New Last'
  })
}
```

# Session Management
- Use session hooks for state management. Example:
```typescript
import { session } from '@clerk/sveltekit'

$: if ($session) {
  // Handle session changes
}
```

- Implement session token handling. Example:
```typescript
import { getAuth } from '@clerk/sveltekit/server'

export const load = async (event) => {
  const { getToken } = await getAuth(event)
  const token = await getToken()
  return { token }
}
```

# API Integration
- Protect API routes with Clerk. Example:
```typescript
import { getAuth } from '@clerk/sveltekit/server'
import type { RequestHandler } from './$types'

export const POST: RequestHandler = async (event) => {
  const { userId } = await getAuth(event)
  if (!userId) {
    throw error(401, 'Unauthorized')
  }
  // Handle protected API logic
}
```

# OAuth and Social Login
- Configure OAuth providers. Example:
```typescript
import { clerkClient } from '@clerk/sveltekit/server'

export const configureOAuth = {
  oauth: {
    providers: ['github', 'google']
  }
}
```

- Implement social login buttons. Example:
```svelte
<SignIn path="/sign-in" routing="path" signUpUrl="/sign-up" socialButtonsPlacement="bottom" />
```

# Webhooks
- Implement Clerk webhooks. Example:
```typescript
import { createClerkWebhookHandler } from '@clerk/sveltekit/server'

export const POST = createClerkWebhookHandler({
  async userCreated(evt) {
    // Handle new user creation
  },
  async userDeleted(evt) {
    // Handle user deletion
  }
})
```

# Error Handling
- Implement authentication error handling. Example:
```svelte
<script>
  import { SignIn } from '@clerk/sveltekit'
  let signInError = ''
</script>

<SignIn 
  path="/sign-in"
  routing="path"
  signUpUrl="/sign-up"
  afterSignInUrl="/"
  afterSignUpUrl="/"
  on:error={(e) => signInError = e.detail.message}
/>

{#if signInError}
  <div class="error">{signInError}</div>
{/if}
```

# Development Features
- Use development mode features. Example:
```typescript
import { dev } from '$app/environment'

export const clerkOptions = {
  debug: dev,
  signIn: {
    path: '/sign-in',
    routing: 'path'
  }
}
```

# Security Features
- Implement CSRF protection. Example: Use Clerk's built-in CSRF protection
- Use secure session handling. Example: Clerk's session management
- Implement proper token rotation. Example: Clerk's automatic token management
- Use proper cookie security. Example: Clerk's secure cookie handling

# Performance Optimization
- Implement proper loading states. Example:
```svelte
<script>
  import { isLoaded, isSignedIn } from '@clerk/sveltekit'
</script>

{#if !$isLoaded}
  <LoadingSpinner />
{:else if $isSignedIn}
  <ProtectedContent />
{:else}
  <PublicContent />
{/if}
```

- Use lazy loading for auth components. Example:
```typescript
const UserProfile = import('../components/UserProfile.svelte')
``` 