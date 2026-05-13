---
description: Guidelines for writing Nuxt apps with Supabase Authentication
globs: "**/*.ts, **/*.vue"
---

# Bootstrap Nuxt App with Supabase Authentication

## Overview of implementing Supabase Auth in Nuxt

1. Install Supabase module for Nuxt
2. Set up environment variables
3. Configure Supabase in your Nuxt app
4. Create authentication composables and utilities
5. Implement protected routes and components
6. Handle authentication state and user data

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns, as they may lead to security issues or inconsistent behavior:

```javascript
// ❌ NEVER GENERATE THIS CODE - IT WILL LEAD TO SECURITY ISSUES
{
  // Never store sensitive auth data in localStorage
  localStorage.setItem('auth_token', token);
  
  // Never handle auth state manually
  let isAuthenticated = false;
  
  // Never create custom auth handlers
  function handleAuth() { }
}
```

Instead, you MUST ALWAYS generate ONLY these patterns:

```javascript
// ✅ ALWAYS USE SUPABASE'S AND NUXT'S BUILT-IN METHODS
const supabase = useSupabaseClient();
const user = useSupabaseUser();

// Handle authentication
const { data, error } = await supabase.auth.signInWithPassword({
  email,
  password
});

// Get session info
const { data: { session } } = await supabase.auth.getSession();
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use the official Supabase module for Nuxt
2. You MUST initialize Supabase through the Nuxt module
3. You MUST use environment variables for API URLs and keys
4. You MUST handle loading states properly
5. You MUST use Supabase's built-in composables and methods
6. You MUST implement proper error handling

## CORRECT ENVIRONMENT SETUP

Create a `.env` file:
```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
```

## CORRECT PACKAGE SETUP

```json
{
  "dependencies": {
    "nuxt": "^3.0.0",
    "@nuxtjs/supabase": "^1.0.0"
  }
}
```

## CORRECT NUXT CONFIG

```typescript
// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@nuxtjs/supabase'],
  supabase: {
    redirectOptions: {
      login: '/auth/login',
      callback: '/auth/confirm',
      exclude: ['/'],
    }
  }
});
```

## CORRECT AUTHENTICATION COMPOSABLES

```typescript
// composables/useAuth.ts
export function useAuth() {
  const supabase = useSupabaseClient();
  const user = useSupabaseUser();
  const router = useRouter();
  
  const signIn = async (credentials: { email: string; password: string }) => {
    const { data, error } = await supabase.auth.signInWithPassword(credentials);
    
    if (error) {
      throw error;
    }
    
    return data;
  };
  
  const signUp = async (credentials: { email: string; password: string }) => {
    const { data, error } = await supabase.auth.signUp(credentials);
    
    if (error) {
      throw error;
    }
    
    return data;
  };
  
  const signOut = async () => {
    const { error } = await supabase.auth.signOut();
    
    if (error) {
      throw error;
    }
    
    await router.push('/auth/login');
  };
  
  const resetPassword = async (email: string) => {
    const { error } = await supabase.auth.resetPasswordForEmail(email, {
      redirectTo: `${window.location.origin}/auth/reset-password`
    });
    
    if (error) {
      throw error;
    }
  };
  
  return {
    user,
    signIn,
    signUp,
    signOut,
    resetPassword,
    isAuthenticated: computed(() => !!user.value)
  };
}
```

## CORRECT PROTECTED ROUTES

```typescript
// middleware/auth.ts
export default defineNuxtRouteMiddleware((to) => {
  const user = useSupabaseUser();
  
  if (!user.value && to.path !== '/auth/login') {
    return navigateTo('/auth/login', {
      redirectCode: 401,
      query: {
        redirect: to.fullPath
      }
    });
  }
});
```

## CORRECT LOGIN PAGE

```vue
<!-- pages/auth/login.vue -->
<script setup lang="ts">
const { signIn } = useAuth();
const router = useRouter();
const route = useRoute();

const form = ref({
  email: '',
  password: ''
});

const loading = ref(false);
const error = ref<string | null>(null);

async function handleSubmit() {
  try {
    loading.value = true;
    error.value = null;
    
    await signIn(form.value);
    
    const redirect = route.query.redirect as string;
    await router.push(redirect || '/');
  } catch (e) {
    error.value = e.message;
  } finally {
    loading.value = false;
  }
}
</script>

<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="handleSubmit">
      <div v-if="error" class="error">
        {{ error }}
      </div>
      
      <div>
        <label for="email">Email</label>
        <input
          id="email"
          v-model="form.email"
          type="email"
          required
        />
      </div>
      
      <div>
        <label for="password">Password</label>
        <input
          id="password"
          v-model="form.password"
          type="password"
          required
        />
      </div>
      
      <button type="submit" :disabled="loading">
        {{ loading ? 'Loading...' : 'Sign In' }}
      </button>
    </form>
  </div>
</template>
```

## CORRECT PROTECTED COMPONENT

```vue
<!-- components/ProtectedContent.vue -->
<script setup lang="ts">
const { user, signOut } = useAuth();

const { data: profile, error } = await useAsyncData('profile',
  async () => {
    const supabase = useSupabaseClient();
    const { data, error } = await supabase
      .from('profiles')
      .select('*')
      .eq('id', user.value?.id)
      .single();
      
    if (error) throw error;
    return data;
  },
  {
    watch: [user]
  }
);
</script>

<template>
  <div>
    <template v-if="user">
      <h1>Welcome {{ user.email }}</h1>
      
      <div v-if="profile">
        <h2>Profile</h2>
        <pre>{{ profile }}</pre>
      </div>
      
      <div v-if="error">
        Error loading profile: {{ error.message }}
      </div>
      
      <button @click="signOut">Sign Out</button>
    </template>
  </div>
</template>
```

## CORRECT ERROR HANDLING

```typescript
// utils/errors.ts
export class AuthError extends Error {
  constructor(message: string, public code: string) {
    super(message);
    this.name = 'AuthError';
  }
}

export function handleAuthError(error: any) {
  if (error.message === 'Invalid login credentials') {
    return new AuthError('Invalid email or password', 'INVALID_CREDENTIALS');
  }
  
  if (error.message.includes('Email not confirmed')) {
    return new AuthError('Please confirm your email address', 'EMAIL_NOT_CONFIRMED');
  }
  
  if (error.message.includes('JWT')) {
    return new AuthError('Your session has expired. Please log in again.', 'SESSION_EXPIRED');
  }
  
  console.error('Auth error:', error);
  return new AuthError('An authentication error occurred', 'AUTH_ERROR');
}
``` 