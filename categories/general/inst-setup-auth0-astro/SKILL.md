---
name: inst-setup-auth0-astro
description: Guidelines for writing Astro apps with Auth0 Auth
license: MIT
tags:
- general
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
