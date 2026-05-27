---
name: inst-setup-better-auth-astro
description: Guidelines for writing Astro apps with Better Auth
license: MIT
tags:
- general
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
