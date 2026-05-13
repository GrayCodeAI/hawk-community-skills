---
description: Guidelines for writing Nuxt.js apps with Clerk
globs: **/*.vue, **/*.ts, **/*.js
---

# Bootstrap Nuxt.js app with Clerk Authentication

## Overview of implementing Clerk Auth

1. Install @clerk/nuxt package
2. Set up environment variables
3. Configure Nuxt module
4. Implement authentication components and middleware
5. Use Clerk composables for auth state and user data

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns, as they are DEPRECATED or will cause issues:

```typescript
// ❌ NEVER GENERATE THIS CODE - IT WILL CAUSE ISSUES
import { useAuth } from '@clerk/clerk-js'  // ❌ Wrong import
import Clerk from '@clerk/clerk-js'        // ❌ Wrong import
new Clerk()                                // ❌ Never instantiate directly
useClerk().session                         // ❌ Avoid direct session access

// ❌ NEVER USE THESE PATTERNS
const clerk = new Clerk()                  // ❌ Wrong initialization
const session = await clerk.session        // ❌ Wrong session access
```

Instead, you MUST ALWAYS use these patterns:

```typescript
// ✅ CORRECT IMPORTS AND USAGE
import { useAuth, useUser, useClerk } from '#imports'

// ✅ CORRECT AUTH STATE ACCESS
const { isSignedIn, userId } = useAuth()
const { user } = useUser()

// ✅ CORRECT SESSION HANDLING
const { signOut } = useClerk()
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use `@clerk/nuxt` package
2. You MUST use auto-imported composables from '#imports'
3. You MUST NEVER manually instantiate Clerk
4. You MUST NEVER directly access session properties
5. You MUST use environment variables with NUXT_ prefix

## CORRECT ENVIRONMENT SETUP

```bash
# .env
NUXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_...
NUXT_CLERK_SECRET_KEY=sk_test_...
```

## CORRECT MODULE CONFIGURATION

```typescript
// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@clerk/nuxt'],
  clerk: {
    // Optional Clerk options
    appearance: {
      // Optional appearance options
    }
  }
})
```

## CORRECT MIDDLEWARE IMPLEMENTATION

```typescript
// middleware/auth.ts
export default defineNuxtRouteMiddleware((to) => {
  const { isSignedIn } = useAuth()

  if (!isSignedIn && to.path !== '/sign-in') {
    return navigateTo('/sign-in')
  }
})
```

## CORRECT COMPONENT IMPLEMENTATION

```vue
<template>
  <div>
    <SignedIn>
      <UserButton />
      <div>
        Welcome {{ user.firstName }}!
      </div>
    </SignedIn>
    <SignedOut>
      <SignInButton />
    </SignedOut>
  </div>
</template>

<script setup>
const { user } = useUser()
</script>
```

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Are you using auto-imported composables from '#imports'? If not, STOP and FIX.
2. Are you using the correct environment variable prefix (NUXT_)? If not, STOP and FIX.
3. Are you seeing any direct Clerk instantiation? If yes, STOP and FIX.
4. Are you using the correct module configuration? If not, STOP and FIX.

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate code using:
- Direct Clerk instantiation
- Wrong imports
- Incorrect environment variable names
- Manual session handling

The implementation will:
1. Break in production
2. Fail to maintain session state
3. Cause authentication loops
4. Result in security vulnerabilities

## AI MODEL RESPONSE TEMPLATE

When asked about Clerk Auth implementation in Nuxt, you MUST:
1. ONLY use code patterns from this guide
2. NEVER suggest deprecated approaches
3. ALWAYS use auto-imported composables
4. VERIFY your response against the patterns shown here

Remember: There are NO EXCEPTIONS to these rules. 