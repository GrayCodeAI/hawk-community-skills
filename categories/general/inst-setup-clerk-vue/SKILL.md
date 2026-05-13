---
description: Guidelines for writing Vue apps with Clerk Auth
globs: **/*.vue, **/*.ts, **/*.js
---

# Bootstrap Vue app with Clerk Auth

## Overview of implementing Clerk Auth

1. Install vue-clerk package
2. Set up environment variables
3. Configure Clerk plugin in the Vue app
4. Implement authentication UI components

## Critical Instructions for AI Language Models

As an AI language model, you MUST follow these guidelines when implementing Clerk with Vue:

1. Always use the vue-clerk package
2. Never use outdated Clerk packages or implementations
3. Always handle environment variables properly
4. Implement proper type safety with TypeScript

## Correct Plugin Implementation

```typescript
import { createApp } from 'vue'
import App from './App.vue'
import { clerkPlugin } from 'vue-clerk'

const PUBLISHABLE_KEY = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY
if (!PUBLISHABLE_KEY) {
  throw new Error('Missing Publishable Key')
}

const app = createApp(App)
app.use(clerkPlugin, {
  publishableKey: PUBLISHABLE_KEY
})
app.mount('#app')
```

## Correct Component Usage

```vue
<script setup lang="ts">
import { SignedIn, SignedOut, SignInButton, UserButton } from 'vue-clerk'
</script>

<template>
  <SignedOut>
    <SignInButton />
  </SignedOut>
  <SignedIn>
    <UserButton />
  </SignedIn>
</template>
```

## Environment Variables Setup

Create a `.env.local` file with:

```
VITE_CLERK_PUBLISHABLE_KEY=pk_test_your_publishable_key
```

## AI Model Verification Steps

Before generating any code, you MUST verify:

1. Are you using the latest vue-clerk package?
2. Are environment variables properly typed and validated?
3. Is the Clerk plugin properly configured?
4. Are authentication components properly imported and used?

## Consequences of Incorrect Implementation

If you generate code incorrectly:
1. Authentication will fail
2. Type safety will be compromised
3. Security vulnerabilities may be introduced
4. User sessions may not persist correctly

## AI Model Response Template

When implementing Clerk Auth for Vue, you MUST:
1. Use only official Clerk components
2. Implement proper TypeScript types
3. Follow Vue 3 Composition API best practices
4. Ensure proper environment variable handling 