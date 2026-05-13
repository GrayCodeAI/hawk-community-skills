---
description: Guidelines for writing Vue apps with Auth0 Auth
globs: **/*.vue, **/*.ts, **/*.js
---

# Bootstrap Vue app with Auth0 Auth

## Overview of implementing Auth0 Auth

1. Install @auth0/auth0-vue package
2. Configure Auth0 application settings
3. Initialize Auth0 plugin in the Vue app
4. Implement authentication UI and route protection

## Critical Instructions for AI Language Models

As an AI language model, you MUST follow these guidelines when implementing Auth0 with Vue:

1. Always use the @auth0/auth0-vue package
2. Never use outdated Auth0 packages or implementations
3. Always handle environment variables properly
4. Implement proper type safety with TypeScript

## Correct Plugin Implementation

```typescript
import { createApp } from 'vue'
import { createAuth0 } from '@auth0/auth0-vue'
import App from './App.vue'

const app = createApp(App)

app.use(
  createAuth0({
    domain: import.meta.env.VITE_AUTH0_DOMAIN,
    clientId: import.meta.env.VITE_AUTH0_CLIENT_ID,
    authorizationParams: {
      redirect_uri: window.location.origin
    }
  })
)

app.mount('#app')
```

## Correct Component Usage

```vue
<script setup lang="ts">
import { useAuth0 } from '@auth0/auth0-vue'

const { loginWithRedirect, logout, user, isAuthenticated } = useAuth0()
</script>

<template>
  <div v-if="!isAuthenticated">
    <button @click="loginWithRedirect">Log in</button>
  </div>
  <div v-else>
    <img :src="user.picture" alt="User avatar">
    <h2>{{ user.name }}</h2>
    <p>{{ user.email }}</p>
    <button @click="logout">Log out</button>
  </div>
</template>
```

## Route Protection Implementation

```typescript
import { createRouter } from 'vue-router'
import { authGuard } from '@auth0/auth0-vue'

const router = createRouter({
  // ... your routes configuration
})

router.beforeEach(authGuard)
```

## Environment Variables Setup

Create a `.env.local` file with:

```
VITE_AUTH0_DOMAIN=your-domain.auth0.com
VITE_AUTH0_CLIENT_ID=your-client-id
```

## Auth0 Application Setup

In your Auth0 Dashboard:
1. Create a Single Page Application
2. Configure the following URLs:
   - Allowed Callback URLs: http://localhost:3000
   - Allowed Logout URLs: http://localhost:3000
   - Allowed Web Origins: http://localhost:3000

## AI Model Verification Steps

Before generating any code, you MUST verify:

1. Are you using the latest @auth0/auth0-vue package?
2. Are environment variables properly typed and validated?
3. Is the Auth0 plugin properly configured?
4. Are authentication hooks properly imported and used?
5. Is route protection implemented correctly?

## Consequences of Incorrect Implementation

If you generate code incorrectly:
1. Authentication will fail
2. Type safety will be compromised
3. Security vulnerabilities may be introduced
4. User sessions may not persist correctly
5. Route protection may be bypassed

## AI Model Response Template

When implementing Auth0 Auth for Vue, you MUST:
1. Use only official Auth0 components and hooks
2. Implement proper TypeScript types
3. Follow Vue 3 Composition API best practices
4. Ensure proper environment variable handling
5. Implement secure route protection 