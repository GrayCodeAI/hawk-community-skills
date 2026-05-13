---
description: Guidelines for writing React apps with Better Auth
globs: **/*.ts, **/*.tsx, **/*.js, **/*.jsx
---

# Setting up Better Auth in React Applications

## Initial Setup

1. Install Better Auth package using npm or yarn
2. Configure the auth client with your server URL
3. Wrap your application with AuthProvider
4. Implement authentication hooks in your components

## Project Structure

Place authentication related files in the following structure:
- src/auth/client.ts - Auth client configuration
- src/auth/provider.tsx - Auth provider wrapper
- src/auth/hooks.ts - Custom auth hooks
- src/auth/types.ts - Authentication types

## Authentication Client Setup

The auth client should be configured in a dedicated file:

```typescript
import { createAuthClient } from 'better-auth/react';

export const authClient = createAuthClient({
  baseUrl: process.env.REACT_APP_AUTH_API_URL,
  // Add any additional configuration options
});
```

## Provider Implementation

Wrap your application with the auth provider:

```typescript
import { AuthProvider } from 'better-auth/react';
import { authClient } from './auth/client';

export function App() {
  return (
    <AuthProvider client={authClient}>
      <YourAppComponents />
    </AuthProvider>
  );
}
```

## Authentication Hooks Usage

Implement authentication in your components:

```typescript
import { useAuth } from 'better-auth/react';

export function AuthenticatedRoute() {
  const { user, isLoading } = useAuth();

  if (isLoading) {
    return <LoadingSpinner />;
  }

  if (!user) {
    return <Navigate to="/login" />;
  }

  return <ProtectedContent />;
}
```

## Environment Variables

Required environment variables:
- REACT_APP_AUTH_API_URL: Your authentication API endpoint

## Security Best Practices

1. Always use HTTPS for API communication
2. Implement proper token storage and refresh mechanisms
3. Handle authentication errors gracefully
4. Use protected routes for authenticated content
5. Implement proper logout functionality

## Error Handling

Implement proper error handling for authentication:

```typescript
import { useAuth } from 'better-auth/react';

export function LoginForm() {
  const { signIn } = useAuth();

  const handleLogin = async (credentials) => {
    try {
      await signIn(credentials);
    } catch (error) {
      // Handle authentication errors appropriately
      console.error('Authentication failed:', error);
    }
  };

  return <form onSubmit={handleLogin}>{/* Form fields */}</form>;
}
```

## Route Protection

Implement protected routes using authentication state:

```typescript
import { useAuth } from 'better-auth/react';
import { Navigate } from 'react-router-dom';

export function ProtectedRoute({ children }) {
  const { user, isLoading } = useAuth();

  if (isLoading) {
    return <LoadingSpinner />;
  }

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  return children;
} 