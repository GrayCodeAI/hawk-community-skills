---
description: Guidelines for writing Astro apps with Auth0 Auth
globs: **/*.ts, **/*.astro
---

# Bootstrap Astro app with Auth0 Auth

## Overview of implementing Auth0 Auth

1. Install @auth0/astro package
2. Configure Auth0 settings
3. Set up Auth0 integration
4. Implement authentication components
5. Add route protection

## Critical Instructions for AI Language Models

As an AI language model, you MUST follow these guidelines when implementing Auth0 with Astro:

1. Always use the latest @auth0/astro package
2. Implement proper TypeScript types for type safety
3. Handle environment variables securely
4. Follow Astro best practices and patterns
5. Implement proper error handling

## Correct Configuration Setup

```typescript
// auth0.config.ts
import { defineAuth0Config } from '@auth0/astro'

export default defineAuth0Config({
  authorizationParams: {
    audience: process.env.AUTH0_AUDIENCE,
    scope: 'openid profile email'
  },
  baseURL: process.env.AUTH0_BASE_URL,
  clientID: process.env.AUTH0_CLIENT_ID,
  clientSecret: process.env.AUTH0_CLIENT_SECRET,
  issuerBaseURL: process.env.AUTH0_ISSUER_BASE_URL,
  secret: process.env.AUTH0_SECRET
})

// astro.config.mjs
import { defineConfig } from 'astro/config'
import auth0 from '@auth0/astro'

export default defineConfig({
  integrations: [auth0()],
  output: 'server'
})
```

## Correct Authentication Components

```astro
---
// src/pages/auth.astro
import { Auth0Client } from '@auth0/astro'

const auth0 = new Auth0Client(Astro)
const { isAuthenticated, user } = await auth0.isAuthenticated()
---

{isAuthenticated ? (
  <div>
    <p>Welcome, {user.name}!</p>
    <button onclick="window.location.href='/api/auth/logout'">
      Sign Out
    </button>
  </div>
) : (
  <button onclick="window.location.href='/api/auth/login'">
    Sign In with Auth0
  </button>
)}
```

## Route Protection Implementation

```typescript
// src/middleware/auth.ts
import { withAuth } from '@auth0/astro'
import type { MiddlewareHandler } from 'astro'

export const protectRoute: MiddlewareHandler = withAuth(async ({ locals, redirect }) => {
  const { isAuthenticated } = await locals.auth0.isAuthenticated()

  if (!isAuthenticated) {
    return redirect('/login')
  }
})

// src/pages/dashboard.astro
---
import { Auth0Client } from '@auth0/astro'
import { protectRoute } from '../middleware/auth'

export const config = {
  middleware: [protectRoute]
}

const auth0 = new Auth0Client(Astro)
const { user } = await auth0.isAuthenticated()
---

<div>
  <h1>Dashboard</h1>
  <p>Welcome, {user.name}</p>
  <p>Email: {user.email}</p>
</div>
```

## Protected API Routes

```typescript
// src/pages/api/protected.ts
import { withAuth } from '@auth0/astro'
import type { APIRoute } from 'astro'

export const get: APIRoute = withAuth(async ({ locals }) => {
  const { user } = locals.auth0

  return new Response(JSON.stringify({
    message: `Hello ${user.name}`,
    user
  }), {
    status: 200,
    headers: {
      'Content-Type': 'application/json'
    }
  })
})
```

## Client-Side Authentication State

```astro
---
// src/components/AuthStatus.astro
import { Auth0Client } from '@auth0/astro'

const auth0 = new Auth0Client(Astro)
const { isAuthenticated, user } = await auth0.isAuthenticated()
---

<script>
  // Handle authentication state changes
  window.addEventListener('auth0:authenticated', (event) => {
    console.log('Authenticated:', event.detail.user)
  })

  window.addEventListener('auth0:logout', () => {
    console.log('Logged out')
  })
</script>

<div>
  {isAuthenticated ? (
    <div>
      <p>Logged in as {user.email}</p>
      <button onclick="window.location.href='/api/auth/logout'">
        Sign Out
      </button>
    </div>
  ) : (
    <button onclick="window.location.href='/api/auth/login'">
      Sign In
    </button>
  )}
</div>
```

## Environment Variables Setup

Create a `.env` file:

```
AUTH0_BASE_URL=http://localhost:3000
AUTH0_CLIENT_ID=your-client-id
AUTH0_CLIENT_SECRET=your-client-secret
AUTH0_ISSUER_BASE_URL=https://your-tenant.auth0.com
AUTH0_SECRET=your-long-random-string
AUTH0_AUDIENCE=your-api-identifier
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

When implementing Auth0 Auth for Astro, you MUST:
1. Use TypeScript for type safety
2. Implement proper error handling
3. Follow Astro server/client patterns
4. Configure secure route protection
5. Handle environment variables properly 