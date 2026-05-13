---
description: Guidelines for writing Next.js apps with Supabase Authentication
globs: "**/*.ts, **/*.tsx, **/*.js, **/*.jsx"
---

# Bootstrap Next.js App with Supabase Authentication

## Overview of implementing Supabase Auth in Next.js

1. Install Supabase dependencies
2. Set up environment variables
3. Initialize Supabase in your Next.js app
4. Create authentication utilities and middleware
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
// ✅ ALWAYS USE SUPABASE'S BUILT-IN METHODS
import { createServerComponentClient } from '@supabase/auth-helpers-nextjs';
import { cookies } from 'next/headers';

const supabase = createServerComponentClient({ cookies });

// Handle authentication
const { data, error } = await supabase.auth.signInWithPassword({
  email,
  password
});

// Get session info
const { data: { session } } = await supabase.auth.getSession();
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use the official Supabase packages
2. You MUST initialize Supabase correctly for server and client components
3. You MUST use environment variables for API URLs and keys
4. You MUST handle loading states properly
5. You MUST use Supabase's built-in methods for auth
6. You MUST implement proper error handling

## CORRECT ENVIRONMENT SETUP

Create a `.env.local` file:
```env
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
```

## CORRECT PACKAGE SETUP

```json
{
  "dependencies": {
    "next": "^14.0.0",
    "@supabase/supabase-js": "^2.0.0",
    "@supabase/auth-helpers-nextjs": "^0.8.0",
    "@supabase/auth-ui-react": "^0.4.0",
    "@supabase/auth-ui-shared": "^0.1.0"
  }
}
```

## CORRECT MIDDLEWARE SETUP

```typescript
// middleware.ts
import { createMiddlewareClient } from '@supabase/auth-helpers-nextjs';
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export async function middleware(req: NextRequest) {
  const res = NextResponse.next();
  const supabase = createMiddlewareClient({ req, res });

  const {
    data: { session },
  } = await supabase.auth.getSession();

  // Protect routes that require authentication
  if (!session && req.nextUrl.pathname.startsWith('/protected')) {
    const redirectUrl = req.nextUrl.clone();
    redirectUrl.pathname = '/auth/login';
    redirectUrl.searchParams.set('redirectTo', req.nextUrl.pathname);
    return NextResponse.redirect(redirectUrl);
  }

  return res;
}

export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico (favicon file)
     * Feel free to modify this pattern to include more paths.
     */
    '/((?!_next/static|_next/image|favicon.ico).*)',
  ],
};
```

## CORRECT SERVER COMPONENT

```typescript
// app/protected/page.tsx
import { createServerComponentClient } from '@supabase/auth-helpers-nextjs';
import { cookies } from 'next/headers';
import { redirect } from 'next/navigation';

export default async function ProtectedPage() {
  const supabase = createServerComponentClient({ cookies });
  
  const {
    data: { session },
  } = await supabase.auth.getSession();

  if (!session) {
    redirect('/auth/login');
  }

  const { data: profile, error } = await supabase
    .from('profiles')
    .select('*')
    .eq('id', session.user.id)
    .single();

  if (error) {
    console.error('Error fetching profile:', error);
  }

  return (
    <div>
      <h1>Protected Page</h1>
      <p>Welcome {session.user.email}</p>
      {profile && (
        <div>
          <h2>Profile</h2>
          <pre>{JSON.stringify(profile, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
```

## CORRECT CLIENT COMPONENT

```typescript
// components/AuthForm.tsx
'use client';

import { createClientComponentClient } from '@supabase/auth-helpers-nextjs';
import { useRouter } from 'next/navigation';
import { useState } from 'react';

export default function AuthForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  
  const router = useRouter();
  const supabase = createClientComponentClient();

  const handleSignIn = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const { error } = await supabase.auth.signInWithPassword({
        email,
        password,
      });

      if (error) {
        throw error;
      }

      router.refresh();
      router.push('/protected');
    } catch (error: any) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSignIn}>
      {error && (
        <div className="error">
          {error}
        </div>
      )}
      
      <div>
        <label htmlFor="email">Email</label>
        <input
          id="email"
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
      </div>

      <div>
        <label htmlFor="password">Password</label>
        <input
          id="password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
      </div>

      <button type="submit" disabled={loading}>
        {loading ? 'Loading...' : 'Sign In'}
      </button>
    </form>
  );
}
```

## CORRECT AUTH PROVIDER

```typescript
// components/Providers.tsx
'use client';

import { createClientComponentClient } from '@supabase/auth-helpers-nextjs';
import { useRouter } from 'next/navigation';
import { useEffect } from 'react';

export default function AuthProvider({
  children,
}: {
  children: React.ReactNode;
}) {
  const router = useRouter();
  const supabase = createClientComponentClient();

  useEffect(() => {
    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange((event, session) => {
      if (event === 'SIGNED_IN') {
        router.refresh();
      }
      if (event === 'SIGNED_OUT') {
        router.refresh();
        router.push('/auth/login');
      }
    });

    return () => {
      subscription.unsubscribe();
    };
  }, [router, supabase]);

  return children;
}
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

## CORRECT ROOT LAYOUT

```typescript
// app/layout.tsx
import { createServerComponentClient } from '@supabase/auth-helpers-nextjs';
import { cookies } from 'next/headers';
import AuthProvider from '@/components/Providers';

export default async function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const supabase = createServerComponentClient({ cookies });

  const {
    data: { session },
  } = await supabase.auth.getSession();

  return (
    <html lang="en">
      <body>
        <AuthProvider>
          <header>
            {session ? (
              <nav>
                <a href="/protected">Protected</a>
                <form action="/auth/signout" method="post">
                  <button type="submit">Sign Out</button>
                </form>
              </nav>
            ) : (
              <nav>
                <a href="/auth/login">Sign In</a>
              </nav>
            )}
          </header>
          {children}
        </AuthProvider>
      </body>
    </html>
  );
}
``` 