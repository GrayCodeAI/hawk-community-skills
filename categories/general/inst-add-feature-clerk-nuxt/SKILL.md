---
description: Guidelines for adding new features with Clerk in Nuxt.js
globs: **/*.vue, **/*.ts, **/*.js
---

You are a senior Nuxt.js developer with expertise in implementing Clerk authentication features.

# Authentication Features

## Protected Pages
- Use auth middleware for route protection. Example:
```typescript
// middleware/auth.ts
export default defineNuxtRouteMiddleware((to) => {
  const { isSignedIn } = useAuth()
  
  if (!isSignedIn && !to.path.startsWith('/auth')) {
    return navigateTo('/sign-in')
  }
})
```

## User Profile Features
- Implement user profile components with Clerk composables. Example:
```vue
<template>
  <div v-if="isLoaded">
    <h1>Profile</h1>
    <div v-if="user">
      <img :src="user.imageUrl" :alt="user.fullName" />
      <h2>{{ user.fullName }}</h2>
      <p>{{ user.primaryEmailAddress }}</p>
      
      <button @click="updateProfile">Update Profile</button>
    </div>
  </div>
</template>

<script setup>
const { user, isLoaded } = useUser()

const updateProfile = async () => {
  await user.update({
    firstName: 'New Name',
    // other updatable fields
  })
}
</script>
```

## Authentication Flow Components
- Create sign-in page with Clerk components. Example:
```vue
<template>
  <div class="auth-container">
    <SignIn routing="path" path="/sign-in" />
  </div>
</template>

<style scoped>
.auth-container {
  max-width: 400px;
  margin: 2rem auto;
  padding: 1rem;
}
</style>
```

- Implement sign-up page with verification. Example:
```vue
<template>
  <div class="auth-container">
    <SignUp routing="path" path="/sign-up" />
  </div>
</template>
```

## Protected API Routes
- Implement protected API endpoints. Example:
```typescript
// server/api/protected/user-data.ts
export default defineEventHandler(async (event) => {
  const { getToken } = useClerkAuth()
  const token = await getToken(event)
  
  if (!token) {
    throw createError({
      statusCode: 401,
      message: 'Unauthorized'
    })
  }
  
  // Your protected API logic here
  return {
    data: 'Protected data'
  }
})
```

## Session Management
- Create session handling composable. Example:
```typescript
// composables/useAuthSession.ts
export const useAuthSession = () => {
  const { isSignedIn, isLoaded } = useAuth()
  const { user } = useUser()
  
  const checkAuth = () => {
    if (!isLoaded) return false
    return isSignedIn
  }
  
  const getUserData = () => {
    if (!checkAuth()) return null
    return {
      id: user.id,
      email: user.primaryEmailAddress,
      name: user.fullName,
      metadata: user.publicMetadata
    }
  }
  
  return {
    checkAuth,
    getUserData,
    isLoaded
  }
}
```

## Role-Based Access Control
- Implement role-based middleware. Example:
```typescript
// middleware/requireRole.ts
export default defineNuxtRouteMiddleware((to) => {
  const { user, isLoaded } = useUser()
  const requiredRole = to.meta.requiredRole
  
  if (!isLoaded) return
  
  if (!user || !user.publicMetadata?.role) {
    throw createError({
      statusCode: 403,
      message: 'Insufficient permissions'
    })
  }
  
  if (user.publicMetadata.role !== requiredRole) {
    return navigateTo('/unauthorized')
  }
})
```

## OAuth Integration
- Set up OAuth providers. Example:
```typescript
// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@clerk/nuxt'],
  clerk: {
    appearance: {
      layout: {
        socialButtonsPlacement: 'bottom'
      }
    }
  }
})
```

## Multi-Factor Authentication
- Implement MFA enrollment component. Example:
```vue
<template>
  <div v-if="isLoaded">
    <h2>Two-Factor Authentication</h2>
    <div v-if="user">
      <button @click="enrollMFA" :disabled="hasMFA">
        {{ hasMFA ? 'MFA Enabled' : 'Enable MFA' }}
      </button>
    </div>
  </div>
</template>

<script setup>
const { user, isLoaded } = useUser()
const hasMFA = computed(() => user.value?.twoFactorEnabled)

const enrollMFA = async () => {
  try {
    await user.value?.createTOTP()
  } catch (error) {
    console.error('Failed to enable MFA:', error)
  }
}
</script>
```

## Error Handling
- Implement auth error handling. Example:
```typescript
// plugins/clerk-error-handler.ts
export default defineNuxtPlugin(() => {
  const { signOut } = useClerk()
  
  return {
    provide: {
      handleAuthError: async (error: any) => {
        if (error.status === 401) {
          await signOut()
          return navigateTo('/sign-in')
        }
        
        throw createError({
          statusCode: error.status || 500,
          message: error.message || 'Authentication error'
        })
      }
    }
  }
})
```

## User Management
- Create user management composable. Example:
```typescript
// composables/useUserManagement.ts
export const useUserManagement = () => {
  const { user } = useUser()
  
  const updateUserMetadata = async (metadata: Record<string, any>) => {
    try {
      await user.value?.update({
        publicMetadata: {
          ...user.value.publicMetadata,
          ...metadata
        }
      })
    } catch (error) {
      console.error('Failed to update user metadata:', error)
      throw error
    }
  }
  
  const updateEmail = async (newEmail: string) => {
    try {
      const emailAddress = await user.value?.createEmailAddress({
        email: newEmail
      })
      await emailAddress?.prepareVerification()
    } catch (error) {
      console.error('Failed to update email:', error)
      throw error
    }
  }
  
  return {
    updateUserMetadata,
    updateEmail
  }
}
```

Remember:
1. Always use auto-imported composables from Clerk
2. Implement proper error handling
3. Use type-safe implementations
4. Follow Nuxt.js best practices for routing and middleware
5. Maintain proper security measures 