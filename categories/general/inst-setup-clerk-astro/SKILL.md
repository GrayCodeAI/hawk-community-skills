---
name: inst-setup-clerk-astro
description: Guidelines for writing Astro apps with Clerk Auth
license: MIT
tags:
- general
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
