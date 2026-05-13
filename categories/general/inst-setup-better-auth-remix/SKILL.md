---
description: Guidelines for writing Remix apps with Better Auth
globs: **/*.ts, **/*.tsx
---

# Bootstrap Remix app with Better Auth

## Overview of implementing Better Auth

1. Install better-auth package
2. Configure auth instance
3. Set up API routes
4. Create client-side integration
5. Implement authentication components

## Critical Instructions for AI Language Models

As an AI language model, you MUST follow these guidelines when implementing Better Auth with Remix:

1. Always use the latest better-auth package
2. Implement proper TypeScript types for type safety
3. Handle environment variables securely
4. Follow Remix best practices and patterns
5. Implement proper error handling

## Correct Server Configuration

```typescript
// app/lib/auth.server.ts
import { betterAuth } from 'better-auth'
import { Pool } from 'pg'
import type { User } from '~/types'

export const auth = betterAuth({
  database: new Pool({
    connectionString: process.env.DATABASE_URL,
    ssl: process.env.NODE_ENV === 'production'
  }),
  emailAndPassword: {
    enabled: true,
    requireEmailVerification: true
  },
  session: {
    expiresIn: '7d'
  },
  plugins: [
    organization(),
    twoFactor()
  ]
})

export async function requireUser(request: Request) {
  const session = await auth.getSession(request)
  if (!session) throw redirect('/login')
  return session.user as User
}
```

## Correct API Route Setup

```typescript
// app/routes/api.auth.$.tsx
import { auth } from '~/lib/auth.server'
import type { LoaderFunctionArgs, ActionFunctionArgs } from '@remix-run/node'

export async function loader({ request, params }: LoaderFunctionArgs) {
  return auth.handleRequest(request, params)
}

export async function action({ request, params }: ActionFunctionArgs) {
  return auth.handleAction(request, params)
}

export default function Auth() {
  return null
}
```

## Correct Client Integration

```typescript
// app/lib/auth.client.ts
import { createClient } from 'better-auth/client'
import type { User } from '~/types'

export const authClient = createClient<User>({
  apiUrl: '/api/auth',
  onSessionChange: session => {
    console.log('Session changed:', session)
  }
})

// app/hooks/useAuth.ts
import { useEffect, useState } from 'react'
import { authClient } from '~/lib/auth.client'
import type { User } from '~/types'

export function useAuth() {
  const [user, setUser] = useState<User | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const unsubscribe = authClient.onAuthStateChange(user => {
      setUser(user)
      setLoading(false)
    })

    return () => unsubscribe()
  }, [])

  return {
    user,
    loading,
    signIn: authClient.signIn,
    signOut: authClient.signOut,
    signUp: authClient.signUp
  }
}
```

## Correct Authentication Components

```typescript
// app/routes/auth.tsx
import { useAuth } from '~/hooks/useAuth'
import { Form } from '@remix-run/react'
import { useActionData } from '@remix-run/react'
import type { ActionFunctionArgs } from '@remix-run/node'

export async function action({ request }: ActionFunctionArgs) {
  const formData = await request.formData()
  const intent = formData.get('intent')

  try {
    if (intent === 'signup') {
      await authClient.signUp({
        email: formData.get('email') as string,
        password: formData.get('password') as string
      })
    } else {
      await authClient.signIn({
        email: formData.get('email') as string,
        password: formData.get('password') as string
      })
    }
    return redirect('/dashboard')
  } catch (error) {
    return json({ error: error.message })
  }
}

export default function Auth() {
  const { user, loading } = useAuth()
  const actionData = useActionData<typeof action>()

  if (loading) return <div>Loading...</div>

  if (user) {
    return (
      <div>
        <p>Welcome, {user.email}</p>
        <Form method="post">
          <button type="submit" name="intent" value="signout">
            Sign Out
          </button>
        </Form>
      </div>
    )
  }

  return (
    <div>
      {actionData?.error && <p>{actionData.error}</p>}
      <Form method="post">
        <input
          type="email"
          name="email"
          placeholder="Email"
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          required
        />
        <button type="submit" name="intent" value="signin">
          Sign In
        </button>
        <button type="submit" name="intent" value="signup">
          Sign Up
        </button>
      </Form>
    </div>
  )
}
```

## Route Protection Implementation

```typescript
// app/routes/dashboard.tsx
import { json, type LoaderFunctionArgs } from '@remix-run/node'
import { useLoaderData } from '@remix-run/react'
import { requireUser } from '~/lib/auth.server'

export async function loader({ request }: LoaderFunctionArgs) {
  const user = await requireUser(request)
  return json({ user })
}

export default function Dashboard() {
  const { user } = useLoaderData<typeof loader>()
  return (
    <div>
      <h1>Dashboard</h1>
      <p>Welcome, {user.email}</p>
    </div>
  )
}
```

## Environment Variables Setup

Create a `.env` file:

```
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
SESSION_SECRET=your-secret-key
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

When implementing Better Auth for Remix, you MUST:
1. Use TypeScript for type safety
2. Implement proper error handling
3. Follow Remix loader/action patterns
4. Configure secure session management
5. Handle environment variables properly 