---
description: Guidelines for writing TanStack apps with Auth0 Authentication
globs: "**/*.ts, **/*.tsx, **/*.js, **/*.jsx"
---

# Bootstrap TanStack App with Auth0 Authentication

## Overview of implementing Auth0 Auth in TanStack

1. Install Auth0 and TanStack dependencies
2. Set up environment variables
3. Initialize Auth0 in your application
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
// ✅ ALWAYS USE AUTH0'S AND TANSTACK'S BUILT-IN METHODS
import { Auth0Provider, useAuth0 } from '@auth0/auth0-react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const queryClient = new QueryClient();

function App() {
  return (
    <Auth0Provider
      domain={process.env.REACT_APP_AUTH0_DOMAIN}
      clientId={process.env.REACT_APP_AUTH0_CLIENT_ID}
      redirectUri={window.location.origin}
    >
      <QueryClientProvider client={queryClient}>
        {/* Your app content */}
      </QueryClientProvider>
    </Auth0Provider>
  );
}
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use the official Auth0 and TanStack packages
2. You MUST initialize both Auth0 and TanStack before using their features
3. You MUST use environment variables for API keys
4. You MUST handle loading states properly
5. You MUST use Auth0's built-in hooks and components
6. You MUST implement proper error handling

## CORRECT ENVIRONMENT SETUP

Create a `.env` file:
```env
REACT_APP_AUTH0_DOMAIN=your_auth0_domain
REACT_APP_AUTH0_CLIENT_ID=your_client_id
```

## CORRECT PACKAGE SETUP

```json
{
  "dependencies": {
    "@auth0/auth0-react": "^2.0.0",
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
import { Auth0Provider } from '@auth0/auth0-react';
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

const router = createRouter({
  routeTree,
  context: {
    auth: undefined!,
  }
});

function InnerApp() {
  const auth = useAuth0();
  return <RouterProvider router={router} context={{ auth }} />;
}

function App() {
  return (
    <Auth0Provider
      domain={process.env.REACT_APP_AUTH0_DOMAIN}
      clientId={process.env.REACT_APP_AUTH0_CLIENT_ID}
      redirectUri={window.location.origin}
    >
      <QueryClientProvider client={queryClient}>
        <InnerApp />
        <ReactQueryDevtools initialIsOpen={false} />
      </QueryClientProvider>
    </Auth0Provider>
  );
}

export default App;
```

## CORRECT AUTHENTICATION HOOKS

```javascript
// src/hooks/useAuthQuery.js
import { useAuth0 } from '@auth0/auth0-react';
import { useQuery } from '@tanstack/react-query';

export function useAuthQuery(queryKey, queryFn, options = {}) {
  const { getAccessTokenSilently, isAuthenticated } = useAuth0();
  
  return useQuery({
    queryKey,
    queryFn: async () => {
      if (!isAuthenticated) {
        throw new Error('Not authenticated');
      }
      
      const token = await getAccessTokenSilently();
      return queryFn(token);
    },
    ...options,
    enabled: isAuthenticated && (options.enabled !== false)
  });
}

// src/hooks/useAuthMutation.js
import { useAuth0 } from '@auth0/auth0-react';
import { useMutation, useQueryClient } from '@tanstack/react-query';

export function useAuthMutation(mutationFn, options = {}) {
  const { getAccessTokenSilently, isAuthenticated } = useAuth0();
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: async (variables) => {
      if (!isAuthenticated) {
        throw new Error('Not authenticated');
      }
      
      const token = await getAccessTokenSilently();
      return mutationFn(variables, token);
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
```

## CORRECT PROTECTED ROUTES

```javascript
// src/routes/protected.jsx
import { createFileRoute, redirect } from '@tanstack/react-router';

export const Route = createFileRoute('/protected')({
  beforeLoad: ({ context }) => {
    if (!context.auth.isAuthenticated) {
      throw redirect({
        to: '/login',
        search: {
          redirect: '/protected'
        }
      });
    }
  },
  component: ProtectedComponent
});

function ProtectedComponent() {
  const { user } = useAuth0();
  
  return (
    <div>
      <h1>Protected Route</h1>
      <p>Welcome {user.name}!</p>
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
  
  if (error.message.includes('access token')) {
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
import { Auth0ContextInterface } from '@auth0/auth0-react';

interface RouterContext {
  auth: Auth0ContextInterface;
}

export const Route = createRootRouteWithContext<RouterContext>()({
  component: RootComponent
});

function RootComponent() {
  const { isLoading } = useAuth0();
  
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
  const { isAuthenticated, loginWithRedirect, logout, user } = useAuth0();
  
  return (
    <div>
      <h1>Home</h1>
      {isAuthenticated ? (
        <>
          <p>Welcome {user.name}</p>
          <button onClick={() => logout()}>Log Out</button>
        </>
      ) : (
        <button onClick={() => loginWithRedirect()}>Log In</button>
      )}
    </div>
  );
}
``` 