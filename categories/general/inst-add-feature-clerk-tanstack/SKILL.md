---
description: Guidelines for adding features to TanStack apps with Clerk Authentication
globs: "**/*.ts, **/*.tsx, **/*.js, **/*.jsx"
---

# Adding Features to TanStack App with Clerk Authentication

## Key Features Available

1. User Authentication
   - Email/Password Sign In
   - OAuth Providers (Google, GitHub, etc.)
   - Multi-factor Authentication (MFA)
   - Magic Links
   - Phone Number Authentication

2. Session Management
   - Active Session Tracking
   - Session Token Management
   - Session Expiration
   - Multi-device Sessions

3. User Management
   - User Profile Management
   - User Metadata
   - Organization Management
   - Role-based Access Control (RBAC)

4. Security Features
   - Passwordless Authentication
   - Fraud Detection
   - Rate Limiting
   - Device Management

5. TanStack Integration Features
   - Cached Authentication State
   - Optimistic Updates
   - Real-time Data Synchronization
   - Infinite Queries
   - Prefetching

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns:

```javascript
// ❌ NEVER GENERATE THIS CODE
{
  // Never implement custom session management
  const session = {
    token: 'xyz',
    expiry: Date.now() + 3600000
  };
  
  // Never create custom auth state management
  const [user, setUser] = useState(null);
  
  // Never implement custom token refresh logic
  async function refreshToken() { }
}
```

Instead, you MUST ALWAYS generate ONLY these patterns:

```javascript
// ✅ ALWAYS USE CLERK'S AND TANSTACK'S BUILT-IN METHODS
import { useAuth, useUser, useOrganization } from '@clerk/clerk-react';
import { useQuery, useMutation } from '@tanstack/react-query';

// Correct session management
function UserSession() {
  const { session } = useAuth();
  return session ? <ActiveSession /> : <SignIn />;
}

// Correct user management
function UserProfile() {
  const { user } = useUser();
  const { data } = useQuery({
    queryKey: ['user-data', user?.id],
    queryFn: () => fetchUserData(user.id)
  });
}

// Correct organization management
function OrgDashboard() {
  const { organization } = useOrganization();
  const { data } = useQuery({
    queryKey: ['org-data', organization?.id],
    queryFn: () => fetchOrgData(organization.id)
  });
}
```

## Feature Implementation Guide

### 1. User Authentication

```javascript
// src/features/auth/SignIn.jsx
import { useSignIn } from '@clerk/clerk-react';
import { useMutation } from '@tanstack/react-query';

export function SignIn() {
  const { signIn, isLoaded } = useSignIn();
  
  const signInMutation = useMutation({
    mutationFn: async ({ email, password }) => {
      if (!isLoaded) throw new Error('Auth not loaded');
      
      try {
        const result = await signIn.create({
          identifier: email,
          password
        });
        
        return result;
      } catch (err) {
        throw new Error('Sign in failed: ' + err.message);
      }
    }
  });
  
  return (
    <form onSubmit={handleSubmit}>
      {/* Form implementation */}
    </form>
  );
}
```

### 2. Session Management

```javascript
// src/features/session/SessionManager.jsx
import { useAuth, useSession } from '@clerk/clerk-react';
import { useQuery } from '@tanstack/react-query';

export function SessionManager() {
  const { session } = useSession();
  const { getToken } = useAuth();
  
  const { data: activeDevices } = useQuery({
    queryKey: ['active-devices', session?.id],
    queryFn: async () => {
      const token = await getToken();
      return fetchActiveDevices(token);
    },
    enabled: !!session
  });
  
  return (
    <div>
      <h2>Active Sessions</h2>
      {/* Display active devices */}
    </div>
  );
}
```

### 3. User Management

```javascript
// src/features/user/UserSettings.jsx
import { useUser } from '@clerk/clerk-react';
import { useMutation, useQueryClient } from '@tanstack/react-query';

export function UserSettings() {
  const { user } = useUser();
  const queryClient = useQueryClient();
  
  const updateProfileMutation = useMutation({
    mutationFn: async (newData) => {
      await user.update(newData);
    },
    onSuccess: () => {
      queryClient.invalidateQueries(['user-profile']);
    }
  });
  
  return (
    <form onSubmit={handleSubmit}>
      {/* Profile update form */}
    </form>
  );
}
```

### 4. Organization Management

```javascript
// src/features/org/OrgManagement.jsx
import { useOrganization, useOrganizationList } from '@clerk/clerk-react';
import { useQuery, useMutation } from '@tanstack/react-query';

export function OrgManagement() {
  const { organization } = useOrganization();
  const { organizationList, createOrganization } = useOrganizationList();
  
  const { data: orgMembers } = useQuery({
    queryKey: ['org-members', organization?.id],
    queryFn: async () => {
      const members = await organization.getMembershipList();
      return members;
    },
    enabled: !!organization
  });
  
  const createOrgMutation = useMutation({
    mutationFn: async ({ name }) => {
      await createOrganization({ name });
    }
  });
  
  return (
    <div>
      {/* Organization management UI */}
    </div>
  );
}
```

### 5. TanStack Integration Features

```javascript
// src/features/data/useInfiniteUsers.js
import { useAuth } from '@clerk/clerk-react';
import { useInfiniteQuery } from '@tanstack/react-query';

export function useInfiniteUsers() {
  const { getToken } = useAuth();
  
  return useInfiniteQuery({
    queryKey: ['users'],
    queryFn: async ({ pageParam = 0 }) => {
      const token = await getToken();
      const response = await fetch(`/api/users?page=${pageParam}`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      return response.json();
    },
    getNextPageParam: (lastPage) => lastPage.nextCursor
  });
}

// src/features/data/useOptimisticUpdate.js
import { useMutation, useQueryClient } from '@tanstack/react-query';

export function useOptimisticUpdate() {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: async (newData) => {
      // API call to update data
    },
    onMutate: async (newData) => {
      // Cancel outgoing refetches
      await queryClient.cancelQueries(['data']);
      
      // Snapshot previous value
      const previousData = queryClient.getQueryData(['data']);
      
      // Optimistically update
      queryClient.setQueryData(['data'], newData);
      
      return { previousData };
    },
    onError: (err, newData, context) => {
      // Rollback on error
      queryClient.setQueryData(['data'], context.previousData);
    }
  });
}
```

## Best Practices for Feature Implementation

1. Always use Clerk's built-in hooks for authentication and user management
2. Leverage TanStack Query for efficient data fetching and caching
3. Implement optimistic updates for better UX
4. Use proper error boundaries and error handling
5. Implement proper loading states
6. Use TypeScript for better type safety
7. Follow React best practices for component composition
8. Implement proper cleanup in useEffect hooks
9. Use proper data validation
10. Implement proper security measures

## Feature Testing Guidelines

1. Test authentication flows
2. Test session management
3. Test user management features
4. Test organization features
5. Test data fetching and caching
6. Test error handling
7. Test loading states
8. Test optimistic updates
9. Test form validation
10. Test security measures

## Performance Considerations

1. Use proper caching strategies
2. Implement proper data prefetching
3. Use optimistic updates where appropriate
4. Implement proper error retry strategies
5. Use proper query invalidation strategies
6. Implement proper loading states
7. Use proper data pagination
8. Implement proper data filtering
9. Use proper data sorting
10. Implement proper data search 