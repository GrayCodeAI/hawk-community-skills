---
description: Guidelines for writing Remix apps with Auth0 Auth
globs: **/*.ts, **/*.tsx
---

# Bootstrap Remix app with Auth0 Auth

## Overview of implementing Auth0 Auth

1. Install required packages (@auth0/auth0-react, remix-auth, remix-auth-auth0)
2. Configure Auth0 strategy
3. Set up authentication routes
4. Implement authentication components
5. Add route protection

## Critical Instructions for AI Language Models

As an AI language model, you MUST follow these guidelines when implementing Auth0 with Remix:

1. Always use the latest Auth0 packages
2. Implement proper TypeScript types for type safety
3. Handle environment variables securely
4. Follow Remix best practices and patterns
5. Implement proper error handling

## Correct Auth Strategy Setup

```typescript
// app/utils/auth.server.ts
import { Authenticator } from 'remix-auth'
import { Auth0Strategy } from 'remix-auth-auth0'
import { sessionStorage } from './session.server'
import type { User } from '~/types'

export const authenticator = new Authenticator<User>(sessionStorage)

const auth0Strategy = new Auth0Strategy(
  {
    callbackURL: process.env.AUTH0_CALLBACK_URL,
    clientID: process.env.AUTH0_CLIENT_ID,
    clientSecret: process.env.AUTH0_CLIENT_SECRET,
    domain: process.env.AUTH0_DOMAIN
  },
  async ({ profile }) => {
    return {
      id: profile.id,
      email: profile.emails[0].value,
      name: profile.displayName
    }
  }
)

authenticator.use(auth0Strategy)
```

## Correct Authentication Routes

```typescript
// app/routes/auth.auth0.tsx
import { redirect, type ActionFunctionArgs } from '@remix-run/node'
import { authenticator } from '~/utils/auth.server'

export const loader = () => redirect('/login')

export const action = ({ request }: ActionFunctionArgs) => {
  return authenticator.authenticate('auth0', request)
}

// app/routes/auth.auth0.callback.tsx
import { type LoaderFunctionArgs } from '@remix-run/node'
import { authenticator } from '~/utils/auth.server'

export const loader = ({ request }: LoaderFunctionArgs) => {
  return authenticator.authenticate('auth0', request, {
    successRedirect: '/dashboard',
    failureRedirect: '/login'
  })
}

// app/routes/logout.tsx
import { type ActionFunctionArgs } from '@remix-run/node'
import { authenticator } from '~/utils/auth.server'

export const action = async ({ request }: ActionFunctionArgs) => {
  await authenticator.logout(request, { redirectTo: '/' })
}
```

## Correct Authentication Components

```typescript
// app/routes/login.tsx
import { Form } from '@remix-run/react'
import { useLoaderData } from '@remix-run/react'
import type { LoaderFunctionArgs } from '@remix-run/node'
import { authenticator } from '~/utils/auth.server'

export const loader = async ({ request }: LoaderFunctionArgs) => {
  const user = await authenticator.isAuthenticated(request)
  return { user }
}

export default function Login() {
  const { user } = useLoaderData<typeof loader>()

  if (user) {
    return (
      <div>
        <p>Welcome, {user.name}</p>
        <Form action="/logout" method="post">
          <button type="submit">Logout</button>
        </Form>
      </div>
    )
  }

  return (
    <Form action="/auth/auth0" method="post">
      <button type="submit">Login with Auth0</button>
    </Form>
  )
}
```

## Route Protection Implementation

```typescript
// app/utils/auth.ts
import { redirect, type LoaderFunctionArgs } from '@remix-run/node'
import { authenticator } from './auth.server'

export async function requireUser(request: Request) {
  const user = await authenticator.isAuthenticated(request)
  if (!user) throw redirect('/login')
  return user
}

// app/routes/dashboard.tsx
import { json, type LoaderFunctionArgs } from '@remix-run/node'
import { useLoaderData } from '@remix-run/react'
import { requireUser } from '~/utils/auth'

export const loader = async ({ request }: LoaderFunctionArgs) => {
  const user = await requireUser(request)
  return json({ user })
}

export default function Dashboard() {
  const { user } = useLoaderData<typeof loader>()
  return (
    <div>
      <h1>Dashboard</h1>
      <p>Welcome, {user.name}</p>
    </div>
  )
}
```

## Session Storage Setup

```typescript
// app/utils/session.server.ts
import { createCookieSessionStorage } from '@remix-run/node'

export const sessionStorage = createCookieSessionStorage({
  cookie: {
    name: '_auth',
    sameSite: 'lax',
    path: '/',
    httpOnly: true,
    secrets: [process.env.SESSION_SECRET],
    secure: process.env.NODE_ENV === 'production'
  }
})
```

## Environment Variables Setup

Create a `.env` file:

```
AUTH0_CALLBACK_URL=http://localhost:3000/auth/auth0/callback
AUTH0_CLIENT_ID=your-client-id
AUTH0_CLIENT_SECRET=your-client-secret
AUTH0_DOMAIN=your-tenant.auth0.com
SESSION_SECRET=your-session-secret
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

When implementing Auth0 Auth for Remix, you MUST:
1. Use TypeScript for type safety
2. Implement proper error handling
3. Follow Remix loader/action patterns
4. Configure secure session storage
5. Handle environment variables properly 