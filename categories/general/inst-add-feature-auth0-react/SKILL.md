---
description: Guidelines for adding new features with Auth0 in React applications
globs: "**/*.ts, **/*.tsx, **/*.js, **/*.jsx"
---

You are a senior React developer with expertise in implementing Auth0 authentication features.

# Authentication Features

## User Management
- Implement user profile management with useAuth0 hook
- Handle user metadata and roles
- Implement custom login and signup flows
- Handle social identity providers
- Manage user sessions

## Protected Routes
- Implement route protection with withAuthenticationRequired
- Handle unauthorized access
- Manage loading states during authentication
- Implement role-based access control
- Handle authentication persistence

## Session Management
- Use getAccessTokenSilently for token management
- Handle token expiration and renewal
- Implement session timeout handling
- Handle session recovery
- Monitor session status

## API Integration
- Implement authenticated API calls
- Handle API error states
- Manage token-based requests
- Implement API scopes
- Handle API authorization

# Component Implementation

## Authentication Components
```typescript
import { useAuth0 } from '@auth0/auth0-react';

export function AuthenticationLayout() {
  const { loginWithRedirect, logout, isAuthenticated } = useAuth0();

  return (
    <div className="auth-container">
      {!isAuthenticated ? (
        <button onClick={() => loginWithRedirect()}>Log In</button>
      ) : (
        <button onClick={() => logout({ 
          logoutParams: { 
            returnTo: window.location.origin 
          }
        })}>
          Log Out
        </button>
      )}
    </div>
  );
}
```

## Protected Routes
```typescript
import { withAuthenticationRequired } from '@auth0/auth0-react';
import { ComponentType } from 'react';

export function withAuth<P extends object>(
  Component: ComponentType<P>
) {
  return withAuthenticationRequired(Component, {
    onRedirecting: () => <div>Loading...</div>
  });
}

// Usage
const ProtectedFeature = withAuth(FeatureComponent);
```

## User Profile Management
```typescript
import { useAuth0 } from '@auth0/auth0-react';

export function UserProfile() {
  const { user, isLoading } = useAuth0();

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Profile</h2>
      <img src={user?.picture} alt={user?.name} />
      <h3>{user?.name}</h3>
      <p>{user?.email}</p>
    </div>
  );
}
```

## API Integration
```typescript
import { useAuth0 } from '@auth0/auth0-react';

export function ApiComponent() {
  const { getAccessTokenSilently } = useAuth0();

  const callApi = async () => {
    try {
      const token = await getAccessTokenSilently({
        authorizationParams: {
          audience: 'https://api.example.com',
          scope: 'read:messages'
        }
      });

      const response = await fetch('https://api.example.com/protected', {
        headers: {
          Authorization: `Bearer ${token}`
        }
      });

      const data = await response.json();
      return data;
    } catch (error) {
      console.error('API Error:', error);
      throw error;
    }
  };

  return <button onClick={callApi}>Call API</button>;
}
```

# Error Handling

## Authentication Errors
```typescript
import { useAuth0 } from '@auth0/auth0-react';

export function AuthErrorBoundary() {
  const { error, isLoading, isAuthenticated } = useAuth0();

  if (error) {
    return <div>Authentication Error: {error.message}</div>;
  }

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (!isAuthenticated) {
    return <div>Please log in</div>;
  }

  return <div>Authenticated content</div>;
}
```

## API Error Handling
```typescript
import { useAuth0 } from '@auth0/auth0-react';

export function ApiErrorHandler() {
  const { getAccessTokenSilently } = useAuth0();

  const handleApiCall = async () => {
    try {
      const token = await getAccessTokenSilently();
      // API call
    } catch (error) {
      if (error.error === 'login_required') {
        // Handle authentication errors
      } else if (error.error === 'consent_required') {
        // Handle consent errors
      } else {
        // Handle other errors
      }
    }
  };

  return <button onClick={handleApiCall}>Make API Call</button>;
}
```

# Security Features

## Token Management
- Implement secure token storage
- Handle token rotation
- Manage token scopes
- Implement token validation
- Monitor token usage

## Authorization
- Implement role-based access
- Handle permission scopes
- Manage user roles
- Implement access policies
- Handle authorization errors

# Performance Optimization

## Authentication State
- Implement proper state caching
- Handle state rehydration
- Optimize auth redirects
- Manage loading states
- Handle concurrent requests

## Component Loading
- Implement lazy loading
- Handle state transitions
- Optimize route changes
- Use error boundaries
- Handle network issues

# Development Guidelines

1. Always use TypeScript
2. Implement error boundaries
3. Handle loading states
4. Use proper security
5. Follow React practices
6. Handle errors consistently
7. Document auth flows
8. Test thoroughly
9. Monitor performance
10. Keep dependencies updated

Remember: Security and user experience are top priorities when implementing authentication features. 