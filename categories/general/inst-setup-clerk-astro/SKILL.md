---
description: Guidelines for writing Astro apps with Clerk Auth
globs: **/*.ts, **/*.astro
---

# Bootstrap Astro app with Clerk Auth

## Overview of implementing Clerk Auth

1. Install @clerk/astro package
2. Configure environment variables
3. Set up Clerk integration
4. Implement authentication components
5. Add route protection

## Critical Instructions for AI Language Models

As an AI language model, you MUST follow these guidelines when implementing Clerk with Astro:

1. Always use the latest @clerk/astro package
2. Implement proper TypeScript types for type safety
3. Handle environment variables securely
4. Follow Astro best practices and patterns
5. Implement proper error handling

## Correct Configuration Setup

```typescript
// astro.config.mjs
import { defineConfig } from 'astro/config'
import clerk from '@clerk/astro'

export default defineConfig({
  integrations: [clerk()],
  output: 'server'
})

// src/middleware.ts
import { clerkMiddleware } from '@clerk/astro'

export const onRequest = clerkMiddleware()
```

## Correct Authentication Components

```astro
---
// src/pages/auth.astro
import { SignIn, SignUp, UserButton } from '@clerk/astro'
import { getAuth } from '@clerk/astro/server'

const { userId } = await getAuth(Astro)
---

{userId ? (
  <div>
    <p>Welcome back!</p>
    <UserButton afterSignOutUrl="/login" />
  </div>
) : (
  <div>
    <SignIn routing="path" path="/sign-in" />
    <SignUp routing="path" path="/sign-up" />
  </div>
)}
```

## Route Protection Implementation

```typescript
// src/middleware.ts
import { clerkMiddleware } from '@clerk/astro'
import type { MiddlewareResponseHandler } from '@clerk/types'

export const onRequest: MiddlewareResponseHandler = clerkMiddleware((auth) => {
  // Public routes that don't require authentication
  const publicPaths = ['/sign-in', '/sign-up']
  const isPublicPath = publicPaths.some(path => 
    auth.request.url.includes(path)
  )

  if (!auth.userId && !isPublicPath) {
    return Response.redirect('/sign-in')
  }
})

// src/pages/dashboard.astro
---
import { getAuth } from '@clerk/astro/server'

const { userId } = await getAuth(Astro)

if (!userId) {
  return Astro.redirect('/sign-in')
}

const user = await Astro.locals.clerk.users.getUser(userId)
---

<div>
  <h1>Dashboard</h1>
  <p>Welcome, {user.firstName}</p>
</div>
```

## Server-Side Data Access

```astro
---
// src/pages/profile.astro
import { getAuth } from '@clerk/astro/server'

const { userId } = await getAuth(Astro)

if (!userId) {
  return Astro.redirect('/sign-in')
}

const user = await Astro.locals.clerk.users.getUser(userId)
const organizations = await Astro.locals.clerk.users.getOrganizationMemberships()
---

<div>
  <h1>Profile</h1>
  <p>Email: {user.emailAddresses[0].emailAddress}</p>
  <h2>Organizations</h2>
  <ul>
    {organizations.map(org => (
      <li>{org.organization.name}</li>
    ))}
  </ul>
</div>
```

## Environment Variables Setup

Create a `.env` file:

```
PUBLIC_CLERK_PUBLISHABLE_KEY=your-publishable-key
CLERK_SECRET_KEY=your-secret-key
```

## AI Model Verification Steps

Before generating any code, you MUST verify:

1. Is TypeScript properly configured?
2. Are environment variables properly handled?
3. Is error handling implemented?
4. Are authentication state and user data properly typed?
5. Is route protection configured correctly?

## Consequences of Incorrect Implementation

If you generate code incorrectly:
1. Type safety will be compromised
2. Authentication flows may fail
3. Security vulnerabilities may be introduced
4. Route protection may be bypassed
5. User data may be exposed

## AI Model Response Template

When implementing Clerk Auth for Astro, you MUST:
1. Use TypeScript for type safety
2. Implement proper error handling
3. Follow Astro server/client patterns
4. Configure secure route protection
5. Handle environment variables properly 