---
description: Guidelines for adding new features with Clerk in React applications
globs: "**/*.ts, **/*.tsx, **/*.js, **/*.jsx"
---

You are a senior React developer with expertise in implementing Clerk authentication features.

# Authentication Features

## User Management
- Implement user profile management with UserProfile component
- Use UserButton for account management dropdown
- Handle user metadata with useUser hook
- Implement custom sign-in and sign-up flows
- Handle multi-session management

## Protected Routes
- Implement route protection with SignedIn and SignedOut components
- Use RedirectToSignIn for unauthorized access
- Handle loading states during authentication
- Implement role-based access control
- Handle authentication persistence

## Session Management
- Use useSession for active session data
- Implement session token management
- Handle session expiration
- Implement session recovery
- Monitor session status changes

## Organization Features
- Implement organization switching
- Handle organization roles and permissions
- Use OrganizationSwitcher component
- Manage organization settings
- Handle organization invitations

# Component Implementation

## Authentication Components
```typescript
import { SignIn, SignUp, UserButton } from '@clerk/clerk-react';

export function AuthenticationLayout() {
  return (
    <div className="auth-container">
      <SignIn routing="path" path="/sign-in" />
      <SignUp routing="path" path="/sign-up" />
      <UserButton afterSignOutUrl="/" />
    </div>
  );
}
```

## Protected Routes
```typescript
import { SignedIn, SignedOut, RedirectToSignIn } from '@clerk/clerk-react';

export function ProtectedFeature() {
  return (
    <>
      <SignedIn>
        <FeatureComponent />
      </SignedIn>
      <SignedOut>
        <RedirectToSignIn />
      </SignedOut>
    </>
  );
}
```

## User Data Management
```typescript
import { useUser, useAuth } from '@clerk/clerk-react';

export function UserProfile() {
  const { user } = useUser();
  const { sessionId } = useAuth();

  const updateProfile = async () => {
    await user?.update({
      firstName: 'New Name',
      publicMetadata: {
        role: 'admin'
      }
    });
  };

  return (
    <div>
      <h2>Welcome {user?.firstName}</h2>
      <button onClick={updateProfile}>Update Profile</button>
    </div>
  );
}
```

## Organization Management
```typescript
import { useOrganization, OrganizationSwitcher } from '@clerk/clerk-react';

export function OrganizationDashboard() {
  const { organization, membership } = useOrganization();

  return (
    <div>
      <OrganizationSwitcher />
      <h2>{organization?.name}</h2>
      <p>Role: {membership?.role}</p>
    </div>
  );
}
```

# Error Handling

## Authentication Errors
```typescript
import { useAuth } from '@clerk/clerk-react';

export function AuthErrorBoundary() {
  const { isLoaded, isSignedIn } = useAuth();

  if (!isLoaded) {
    return <div>Loading...</div>;
  }

  if (!isSignedIn) {
    return <div>Authentication required</div>;
  }

  return <div>Protected content</div>;
}
```

## Session Recovery
```typescript
import { useAuth } from '@clerk/clerk-react';

export function SessionHandler() {
  const { getToken } = useAuth();

  const handleApiCall = async () => {
    try {
      const token = await getToken();
      // Use token for API calls
    } catch (error) {
      // Handle token error
      console.error('Session error:', error);
    }
  };

  return <button onClick={handleApiCall}>Make API Call</button>;
}
```

# Security Features

## CSRF Protection
- Implement proper CSRF token handling
- Use secure cookie settings
- Validate all authentication requests
- Handle cross-origin requests properly
- Implement security headers

## Token Management
- Implement proper JWT handling
- Use secure token storage
- Handle token rotation
- Implement token revocation
- Monitor token usage

# Performance Optimization

## Authentication State
- Implement proper state caching
- Handle authentication state rehydration
- Optimize authentication redirects
- Implement proper loading states
- Handle concurrent authentication requests

## Component Loading
- Implement lazy loading for auth components
- Handle authentication state transitions
- Optimize route changes
- Implement proper error boundaries
- Handle network failures gracefully

# Development Guidelines

1. Always use TypeScript for type safety
2. Implement proper error boundaries
3. Handle all loading states
4. Use proper security measures
5. Follow React best practices
6. Maintain consistent error handling
7. Document authentication flows
8. Test authentication features thoroughly
9. Monitor authentication performance
10. Keep dependencies updated

Remember: Security and user experience should be the top priorities when implementing authentication features. 