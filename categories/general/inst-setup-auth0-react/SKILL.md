---
description: Guidelines for writing React apps with Auth0 Authentication
globs: "**/*.ts, **/*.tsx, **/*.js, **/*.jsx"
---

# Bootstrap React App with Auth0 Authentication

## Overview of implementing Auth0 Auth

1. Install @auth0/auth0-react package
2. Set up environment variables
3. Configure Auth0Provider at the root level
4. Implement authentication components and protected routes
5. Handle authentication state and user data

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns, as they may lead to security issues or inconsistent behavior:

```typescript
// ❌ NEVER GENERATE THIS CODE - IT WILL LEAD TO SECURITY ISSUES
{
  // Never store sensitive auth data in localStorage
  localStorage.setItem('auth_token', token);
  
  // Never handle auth state manually
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  
  // Never create custom auth providers
  const AuthContext = createContext();
}

// ❌ NEVER USE DEPRECATED METHODS
withAuth() // ❌ Use useAuth0() hook instead
auth.getUser() // ❌ Use useAuth0() hook instead
```

Instead, you MUST ALWAYS generate ONLY these patterns:

```typescript
// ✅ ALWAYS USE AUTH0'S BUILT-IN HOOKS AND COMPONENTS
import { useAuth0 } from '@auth0/auth0-react';

// For auth state and user data
const { isAuthenticated, user, isLoading, getAccessTokenSilently } = useAuth0();

// For login/logout
const { loginWithRedirect, logout } = useAuth0();

// For protected content
{isAuthenticated ? (
  <ProtectedComponent />
) : (
  <LoginComponent />
)}
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use @auth0/auth0-react package
2. You MUST wrap your app with Auth0Provider
3. You MUST use environment variables for Auth0 credentials
4. You MUST use TypeScript for better type safety
5. You MUST use Auth0's built-in hooks for auth state
6. You MUST implement proper error boundaries for auth state

## CORRECT AUTH0 PROVIDER IMPLEMENTATION

```typescript
import { Auth0Provider } from '@auth0/auth0-react';
import { env } from './env.ts';

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <Auth0Provider
      domain={env.AUTH0_DOMAIN}
      clientId={env.AUTH0_CLIENT_ID}
      authorizationParams={{
        redirect_uri: window.location.origin
      }}
    >
      {children}
    </Auth0Provider>
  );
}
```

## CORRECT PROTECTED ROUTE IMPLEMENTATION

```typescript
import { useAuth0 } from '@auth0/auth0-react';
import { Navigate } from 'react-router-dom';

export function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { isAuthenticated, isLoading } = useAuth0();

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return <>{children}</>;
}
```

## CORRECT AUTH STATE HANDLING

```typescript
import { useAuth0 } from '@auth0/auth0-react';

export function AuthenticatedComponent() {
  const { isAuthenticated, user, isLoading } = useAuth0();

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (!isAuthenticated) {
    return null;
  }

  return (
    <div>
      Welcome, {user?.name}!
    </div>
  );
}
```

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Are you using the latest @auth0/auth0-react package? If not, STOP and FIX.
2. Are you properly handling loading states? If not, STOP and FIX.
3. Are you using environment variables for Auth0 credentials? If not, STOP and FIX.
4. Are you using TypeScript? If not, STOP and FIX.
5. Are you using Auth0's built-in hooks? If not, STOP and FIX.

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate code using:
- localStorage for auth state
- Custom auth providers
- Deprecated methods
- Manual auth state management

The implementation will:
1. Create security vulnerabilities
2. Lead to inconsistent auth state
3. Break session management
4. Cause poor user experience
5. Make maintenance difficult

## AI MODEL RESPONSE TEMPLATE

When asked about Auth0 React implementation, you MUST:
1. ONLY use code patterns from this guide
2. NEVER suggest deprecated approaches
3. ALWAYS use TypeScript
4. ALWAYS handle loading states
5. VERIFY your response against the patterns shown here

Remember: There are NO EXCEPTIONS to these rules. 