---
description: Guidelines for writing TanStack apps with Supabase Authentication
globs: "**/*.ts, **/*.tsx, **/*.js, **/*.jsx"
---

# Bootstrap TanStack App with Supabase Authentication

## Overview of implementing Supabase Auth in TanStack

1. Install Supabase and TanStack dependencies
2. Set up environment variables
3. Initialize Supabase in your application
4. Create authentication hooks and utilities
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
// ✅ ALWAYS USE SUPABASE'S AND TANSTACK'S BUILT-IN METHODS
import { createBrowserClient } from '@supabase/ssr';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const queryClient = new QueryClient();
const supabase = createBrowserClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
);

function App() {
  return (
    <SupabaseProvider client={supabase}>
      <QueryClientProvider client={queryClient}>
        {/* Your app content */}
      </QueryClientProvider>
    </SupabaseProvider>
  );
}
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use the official Supabase and TanStack packages
2. You MUST initialize both Supabase and TanStack before using their features
3. You MUST use environment variables for API URLs and keys
4. You MUST handle loading states properly
5. You MUST use Supabase's built-in hooks and components
6. You MUST implement proper error handling

## CORRECT ENVIRONMENT SETUP

Create a `.env` file:
```env
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key
```

## CORRECT PACKAGE SETUP

```json
{
  "dependencies": {
    "@supabase/supabase-js": "^2.0.0",
    "@supabase/ssr": "^2.0.0",
    "@supabase-cache-helpers/postgrest-react-query": "^1.0.0",
    "@tanstack/react-query": "^5.0.0",
    "@tanstack/react-query-devtools": "^5.0.0",
    "@tanstack/react-router": "^1.0.0",
    "react": "^18.0.0",
    "react-dom": "^18.0.0"
  }
}
```

## CORRECT PROVIDER SETUP

```javascript
// src/App.jsx
import { createBrowserClient } from '@supabase/ssr';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import { RouterProvider, createRouter } from '@tanstack/react-router';
import { routeTree } from './routeTree.gen';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 60 * 1000, // 1 minute
      retry: 1
    }
  }
});

const supabase = createBrowserClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
);

const router = createRouter({
  routeTree,
  context: {
    supabase: undefined!,
  }
});

function InnerApp() {
  return <RouterProvider router={router} context={{ supabase }} />;
}

function App() {
  return (
    <SupabaseProvider client={supabase}>
      <QueryClientProvider client={queryClient}>
        <InnerApp />
        <ReactQueryDevtools initialIsOpen={false} />
      </QueryClientProvider>
    </SupabaseProvider>
  );
}

export default App;
```

## CORRECT AUTHENTICATION HOOKS

```javascript
// src/hooks/useAuthQuery.js
import { useSupabase } from '@/providers/supabase';
import { useQuery } from '@tanstack/react-query';

export function useAuthQuery(queryKey, queryFn, options = {}) {
  const { supabase } = useSupabase();
  const { data: session } = useSessionQuery();
  
  return useQuery({
    queryKey,
    queryFn: async () => {
      if (!session) {
        throw new Error('Not authenticated');
      }
      
      return queryFn(supabase);
    },
    ...options,
    enabled: !!session && (options.enabled !== false)
  });
}

// src/hooks/useAuthMutation.js
import { useSupabase } from '@/providers/supabase';
import { useMutation, useQueryClient } from '@tanstack/react-query';

export function useAuthMutation(mutationFn, options = {}) {
  const { supabase } = useSupabase();
  const { data: session } = useSessionQuery();
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: async (variables) => {
      if (!session) {
        throw new Error('Not authenticated');
      }
      
      return mutationFn(variables, supabase);
    },
    ...options,
    onSuccess: async (...args) => {
      // Invalidate queries when mutation succeeds
      if (options.invalidateQueries) {
        await queryClient.invalidateQueries(options.invalidateQueries);
      }
      
      if (options.onSuccess) {
        await options.onSuccess(...args);
      }
    }
  });
}

// src/hooks/useSessionQuery.js
import { useSupabase } from '@/providers/supabase';
import { useQuery } from '@tanstack/react-query';

export function useSessionQuery() {
  const { supabase } = useSupabase();
  
  return useQuery({
    queryKey: ['session'],
    queryFn: async () => {
      const { data: { session }, error } = await supabase.auth.getSession();
      if (error) throw error;
      return session;
    }
  });
}
```

## CORRECT PROTECTED ROUTES

```javascript
// src/routes/protected.jsx
import { createFileRoute, redirect } from '@tanstack/react-router';

export const Route = createFileRoute('/protected')({
  beforeLoad: async ({ context }) => {
    const { data: { session }, error } = await context.supabase.auth.getSession();
    if (!session || error) {
      throw redirect({
        to: '/login',
        search: {
          redirect: '/protected'
        }
      });
    }
    return { session };
  },
  component: ProtectedComponent
});

function ProtectedComponent() {
  const { session } = Route.useLoaderData();
  
  return (
    <div>
      <h1>Protected Route</h1>
      <p>Welcome {session.user.email}!</p>
    </div>
  );
}
```

## CORRECT ERROR HANDLING

```javascript
// src/utils/errors.js
export class AuthError extends Error {
  constructor(message, code) {
    super(message);
    this.name = 'AuthError';
    this.code = code;
  }
}

export function handleAuthError(error) {
  if (error.message === 'Not authenticated') {
    // Handle unauthenticated error
    console.error('User is not authenticated');
    return new AuthError('Please log in to continue', 'UNAUTHENTICATED');
  }
  
  if (error.message.includes('JWT')) {
    // Handle token errors
    console.error('Token error:', error);
    return new AuthError('Authentication token error', 'TOKEN_ERROR');
  }
  
  // Handle other errors
  console.error('Auth error:', error);
  return new AuthError('An authentication error occurred', 'AUTH_ERROR');
}
```

## CORRECT USAGE WITH TANSTACK ROUTER

```javascript
// src/routes/root.jsx
import { createRootRouteWithContext } from '@tanstack/react-router';
import { SupabaseClient } from '@supabase/supabase-js';

interface RouterContext {
  supabase: SupabaseClient;
}

export const Route = createRootRouteWithContext<RouterContext>()({
  component: RootComponent
});

function RootComponent() {
  const { data: session, isLoading } = useSessionQuery();
  
  if (isLoading) {
    return <div>Loading...</div>;
  }
  
  return <Outlet />;
}

// src/routes/index.jsx
import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/')({
  component: HomeComponent
});

function HomeComponent() {
  const { supabase } = useSupabase();
  const { data: session } = useSessionQuery();
  
  const handleSignIn = async () => {
    await supabase.auth.signInWithOAuth({
      provider: 'github'
    });
  };
  
  const handleSignOut = async () => {
    await supabase.auth.signOut();
  };
  
  return (
    <div>
      <h1>Home</h1>
      {session ? (
        <>
          <p>Welcome {session.user.email}</p>
          <button onClick={handleSignOut}>Sign Out</button>
        </>
      ) : (
        <button onClick={handleSignIn}>Sign In with GitHub</button>
      )}
    </div>
  );
}
``` 