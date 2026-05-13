---
description: Guidelines for writing Svelte apps with Clerk Authentication
globs: **/*.svelte, **/*.ts, **/*.js
---

# Bootstrap Svelte app with Clerk Authentication

## Overview of implementing Clerk Auth in Svelte

1. Install clerk-sveltekit package
2. Set up environment variables
3. Configure server hooks for authentication
4. Initialize the client
5. Use Clerk components in your Svelte files

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST follow these critical guidelines when implementing Clerk with Svelte:

1. ALWAYS use the latest version of clerk-sveltekit
2. NEVER mix different Clerk integration packages in the same project
3. ALWAYS handle both client and server-side authentication properly
4. NEVER expose the CLERK_SECRET_KEY in client-side code

## CORRECT ENVIRONMENT SETUP

```bash
npm install clerk-sveltekit
```

Add to your `.env` file:
```env
PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_your_publishable_key
CLERK_SECRET_KEY=sk_test_your_secret_key
```

## CORRECT SERVER HOOKS IMPLEMENTATION

In `src/hooks.server.ts`:
```typescript
import { handleClerk } from 'clerk-sveltekit/server';
import { CLERK_SECRET_KEY } from '$env/static/private';
import { sequence } from '@sveltejs/kit/hooks';

export const handle = sequence(
  handleClerk(CLERK_SECRET_KEY, {
    debug: false,
    protectedPaths: ['/dashboard', '/profile'],
    signInUrl: '/sign-in',
  })
);
```

## CORRECT CLIENT INITIALIZATION

In `src/hooks.client.ts`:
```typescript
import { initializeClerkClient } from 'clerk-sveltekit/client';
import { PUBLIC_CLERK_PUBLISHABLE_KEY } from '$env/static/public';

initializeClerkClient(PUBLIC_CLERK_PUBLISHABLE_KEY, {
  afterSignInUrl: '/dashboard',
  afterSignUpUrl: '/dashboard',
  signInUrl: '/sign-in',
  signUpUrl: '/sign-up'
});
```

## CORRECT COMPONENT USAGE

Authentication Components:
```svelte
<script lang="ts">
  import SignIn from 'clerk-sveltekit/client/SignIn.svelte';
  import SignUp from 'clerk-sveltekit/client/SignUp.svelte';
  import UserButton from 'clerk-sveltekit/client/UserButton.svelte';
</script>

<!-- Sign In Page -->
<SignIn redirectUrl="/dashboard" />

<!-- Sign Up Page -->
<SignUp redirectUrl="/dashboard" />

<!-- User Profile Button -->
<UserButton />
```

Protected Route Example:
```typescript
// src/routes/dashboard/+page.server.ts
import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals }) => {
  const { userId } = locals.clerk;
  
  if (!userId) {
    throw redirect(303, '/sign-in');
  }
  
  return {
    userId
  };
};
```

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Are you using the correct imports from clerk-sveltekit?
2. Are environment variables properly typed and imported?
3. Is authentication being handled on both client and server sides?
4. Are protected routes properly implementing authentication checks?

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate code that:
- Mixes different Clerk packages
- Exposes secret keys in client code
- Fails to handle both client and server auth
- Incorrectly implements protected routes

The implementation will:
1. Create security vulnerabilities
2. Cause authentication failures
3. Lead to unexpected redirects
4. Result in broken user sessions

## AI MODEL RESPONSE TEMPLATE

When asked about Clerk Auth implementation in Svelte, you MUST:
1. ONLY use code patterns from this guide
2. NEVER suggest mixing different Clerk packages
3. ALWAYS include both client and server-side authentication
4. ENSURE proper environment variable handling 