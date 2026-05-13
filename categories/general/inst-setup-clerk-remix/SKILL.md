---
description: Guidelines for writing Remix apps with Clerk Auth
globs: **/*.ts, **/*.tsx
---

# Bootstrap Remix app with Clerk Auth

## Overview of implementing Clerk Auth

1. Install @clerk/remix package
2. Configure environment variables
3. Set up root authentication loader
4. Implement authentication components
5. Add route protection

## Critical Instructions for AI Language Models

As an AI language model, you MUST follow these guidelines when implementing Clerk with Remix:

1. Always use the latest @clerk/remix package
2. Implement proper TypeScript types for type safety
3. Handle environment variables securely
4. Follow Remix best practices and patterns
5. Implement proper error handling

## Correct Root Configuration

```typescript
// root.tsx
import { rootAuthLoader } from '@clerk/remix/ssr.server'
import { ClerkApp } from '@clerk/remix'
import type { LoaderFunction } from '@remix-run/node'

export const loader: LoaderFunction = args => rootAuthLoader(args)

function App() {
  return (
    <html>
      <head>
        <Meta />
        <Links />
      </head>
      <body>
        <Outlet />
        <ScrollRestoration />
        <Scripts />
        <LiveReload />
      </body>
    </html>
  )
}

export default ClerkApp(App)
```

## Correct Authentication Components

```typescript
// routes/auth.tsx
import { SignIn, SignUp, UserButton } from '@clerk/remix'
import { useUser } from '@clerk/remix'

export default function Auth() {
  const { isSignedIn, user } = useUser()

  return (
    <div>
      {isSignedIn ? (
        <div>
          <p>Welcome, {user.firstName}</p>
          <UserButton afterSignOutUrl="/login" />
        </div>
      ) : (
        <div>
          <SignIn routing="path" path="/sign-in" />
          <SignUp routing="path" path="/sign-up" />
        </div>
      )}
    </div>
  )
}
```

## Route Protection Implementation

```typescript
// routes/protected.tsx
import { getAuth } from '@clerk/remix/ssr.server'
import { redirect } from '@remix-run/node'
import type { LoaderFunction } from '@remix-run/node'

export const loader: LoaderFunction = async args => {
  const { userId } = await getAuth(args)
  
  if (!userId) {
    return redirect('/sign-in')
  }

  return json({ userId })
}

export default function Protected() {
  const { userId } = useLoaderData<typeof loader>()

  return (
    <div>
      <h1>Protected Route</h1>
      <p>User ID: {userId}</p>
    </div>
  )
}
```

## Middleware Implementation

```typescript
// middleware.ts
import { createClerkClient } from '@clerk/remix/api.server'
import { getAuth } from '@clerk/remix/ssr.server'
import { redirect } from '@remix-run/node'
import type { LoaderFunction } from '@remix-run/node'

const clerk = createClerkClient()

export const protectedLoader: LoaderFunction = async args => {
  const { userId } = await getAuth(args)

  if (!userId) {
    return redirect('/sign-in')
  }

  const user = await clerk.users.getUser(userId)
  return { user }
}

export const adminLoader: LoaderFunction = async args => {
  const { userId } = await getAuth(args)

  if (!userId) {
    return redirect('/sign-in')
  }

  const user = await clerk.users.getUser(userId)
  
  if (!user.publicMetadata.isAdmin) {
    return redirect('/')
  }

  return { user }
}
```

## Environment Variables Setup

Create a `.env` file:

```
CLERK_PUBLISHABLE_KEY=your-publishable-key
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

When implementing Clerk Auth for Remix, you MUST:
1. Use TypeScript for type safety
2. Implement proper error handling
3. Follow Remix loader/action patterns
4. Configure secure route protection
5. Handle environment variables properly 