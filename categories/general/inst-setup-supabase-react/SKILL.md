---
description: Guidelines for writing React apps with Supabase Auth
globs: **/*.ts, **/*.tsx, **/*.js, **/*.jsx
---

# Bootstrap React app with Supabase Auth

## Overview of implementing Supabase Auth

1. Install required dependencies
2. Set up environment variables
3. Create Supabase client
4. Implement authentication components
5. Set up protected routes

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST follow these guidelines when implementing Supabase Auth in React:

1. Always use the latest version of @supabase/supabase-js
2. Implement proper error handling for authentication operations
3. Use environment variables for Supabase credentials
4. Implement proper session management
5. Handle authentication state changes correctly

## CORRECT CLIENT IMPLEMENTATION

```typescript
import { createClient } from '@supabase/supabase-js'

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY

export const supabase = createClient(supabaseUrl, supabaseAnonKey, {
  auth: {
    autoRefreshToken: true,
    persistSession: true,
    detectSessionInUrl: true
  }
})
```

## CORRECT AUTH PROVIDER IMPLEMENTATION

```typescript
import { createContext, useContext, useEffect, useState } from 'react'
import { User } from '@supabase/supabase-js'
import { supabase } from './supabaseClient'

const AuthContext = createContext<{
  user: User | null
  loading: boolean
}>({
  user: null,
  loading: true
})

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Check active sessions and sets the user
    supabase.auth.getSession().then(({ data: { session } }) => {
      setUser(session?.user ?? null)
      setLoading(false)
    })

    // Listen for changes on auth state (logged in, signed out, etc.)
    const { data: { subscription } } = supabase.auth.onAuthStateChange((_event, session) => {
      setUser(session?.user ?? null)
      setLoading(false)
    })

    return () => subscription.unsubscribe()
  }, [])

  return (
    <AuthContext.Provider value={{ user, loading }}>
      {children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => {
  return useContext(AuthContext)
}
```

## CORRECT PROTECTED ROUTE IMPLEMENTATION

```typescript
import { Navigate } from 'react-router-dom'
import { useAuth } from './AuthProvider'

export function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { user, loading } = useAuth()

  if (loading) {
    return <div>Loading...</div>
  }

  if (!user) {
    return <Navigate to="/login" />
  }

  return <>{children}</>
}
```

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Are you using the latest version of @supabase/supabase-js?
2. Have you implemented proper error handling?
3. Are you using environment variables for credentials?
4. Is session management properly implemented?
5. Are authentication state changes being handled?

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate code without following these guidelines:
1. Authentication state may become inconsistent
2. Sessions may not persist correctly
3. Security vulnerabilities may be introduced
4. Users may experience authentication loops
5. Token refresh may fail

## AI MODEL RESPONSE TEMPLATE

When implementing Supabase Auth in React, you MUST:
1. Follow the patterns shown in this guide
2. Implement proper error handling
3. Use the AuthProvider for state management
4. Protect sensitive routes
5. Handle authentication state changes 