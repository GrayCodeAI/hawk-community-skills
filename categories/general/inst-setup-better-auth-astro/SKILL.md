---
description: Guidelines for writing Astro apps with Better Auth
globs: **/*.ts, **/*.astro
---

# Bootstrap Astro app with Better Auth

## Overview of implementing Better Auth

1. Install better-auth package
2. Configure Better Auth instance
3. Set up API routes and middleware
4. Implement authentication components
5. Add route protection

## Critical Instructions for AI Language Models

As an AI language model, you MUST follow these guidelines when implementing Better Auth with Astro:

1. Always use the latest better-auth package
2. Implement proper TypeScript types for type safety
3. Handle environment variables securely
4. Follow Astro best practices and patterns
5. Implement proper error handling

## Correct Configuration Setup

```typescript
// src/lib/auth.ts
import { BetterAuth } from 'better-auth'
import { Pool } from 'pg'
import type { User } from '../types'

const pool = new Pool({
  connectionString: import.meta.env.DATABASE_URL,
  ssl: import.meta.env.PROD ? true : false
})

export const betterAuth = new BetterAuth({
  adapter: {
    type: 'pg',
    pool
  },
  secret: import.meta.env.AUTH_SECRET,
  providers: [
    // Configure your authentication providers
  ],
  session: {
    expiresIn: '7d'
  }
})

// src/middleware.ts
import { defineMiddleware } from 'astro:middleware'
import { betterAuth } from './lib/auth'

export const onRequest = defineMiddleware(async ({ locals, request }, next) => {
  try {
    const session = await betterAuth.getSession(request)
    locals.user = session?.user || null
    locals.session = session
    return next()
  } catch (error) {
    console.error('Auth middleware error:', error)
    locals.user = null
    locals.session = null
    return next()
  }
})
```

## Correct API Route Setup

```typescript
// src/pages/api/auth/[...all].ts
import { betterAuth } from '../../../lib/auth'
import type { APIRoute } from 'astro'

export const all: APIRoute = async ({ request }) => {
  try {
    return await betterAuth.handleRequest(request)
  } catch (error) {
    console.error('Auth API error:', error)
    return new Response(JSON.stringify({ error: 'Authentication failed' }), {
      status: 500,
      headers: {
        'Content-Type': 'application/json'
      }
    })
  }
}
```

## Correct Authentication Components

```astro
---
// src/components/Auth.astro
import { betterAuth } from '../lib/auth'

const { user } = Astro.locals
---

<div>
  {user ? (
    <div>
      <p>Welcome, {user.name}!</p>
      <form action="/api/auth/signout" method="post">
        <button type="submit">Sign Out</button>
      </form>
    </div>
  ) : (
    <div>
      <form action="/api/auth/signin" method="post">
        <input type="email" name="email" placeholder="Email" required />
        <input type="password" name="password" placeholder="Password" required />
        <button type="submit">Sign In</button>
      </form>
      <form action="/api/auth/signup" method="post">
        <input type="email" name="email" placeholder="Email" required />
        <input type="password" name="password" placeholder="Password" required />
        <button type="submit">Sign Up</button>
      </form>
    </div>
  )}
</div>

<script>
  // Handle authentication state changes
  window.addEventListener('better-auth:authenticated', (event) => {
    console.log('Authenticated:', event.detail.user)
    window.location.reload()
  })

  window.addEventListener('better-auth:signedOut', () => {
    console.log('Signed out')
    window.location.reload()
  })
</script>
```

## Route Protection Implementation

```astro
---
// src/pages/dashboard.astro
import { betterAuth } from '../lib/auth'
import type { User } from '../types'

if (!Astro.locals.user) {
  return Astro.redirect('/login')
}

const user = Astro.locals.user as User
---

<div>
  <h1>Dashboard</h1>
  <p>Welcome, {user.name}</p>
  <p>Email: {user.email}</p>
</div>

// src/pages/admin.astro
---
import { betterAuth } from '../lib/auth'
import type { User } from '../types'

const user = Astro.locals.user as User

if (!user || !user.roles.includes('admin')) {
  return Astro.redirect('/')
}
---

<div>
  <h1>Admin Dashboard</h1>
  <p>Welcome, Administrator {user.name}</p>
</div>
```

## Environment Variables Setup

Create a `.env` file:

```
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
AUTH_SECRET=your-long-random-string
PROD=false
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

When implementing Better Auth for Astro, you MUST:
1. Use TypeScript for type safety
2. Implement proper error handling
3. Follow Astro server/client patterns
4. Configure secure route protection
5. Handle environment variables properly 