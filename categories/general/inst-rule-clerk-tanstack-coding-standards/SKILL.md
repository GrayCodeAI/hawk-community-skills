---
description: Coding standards and best practices for implementing Clerk authentication in TanStack applications
globs: "**/*.ts, **/*.tsx, **/*.js, **/*.jsx"
---

# Coding Standards for TanStack Apps with Clerk Authentication

## 🚨 CRITICAL RULES 🚨

1. NEVER store authentication tokens in localStorage or cookies
2. NEVER implement custom authentication flows
3. NEVER bypass Clerk's built-in security features
4. ALWAYS use environment variables for sensitive data
5. ALWAYS use HTTPS in production
6. ALWAYS implement proper error handling
7. ALWAYS use TypeScript for better type safety
8. ALWAYS follow React Query best practices
9. ALWAYS use proper loading states
10. ALWAYS implement proper cleanup

## File Structure

```
src/
├── auth/
│   ├── client.ts         # Clerk client configuration
│   ├── hooks/            # Custom auth hooks
│   │   ├── useAuthQuery.ts
│   │   └── useAuthMutation.ts
│   └── components/       # Auth-related components
│       ├── SignIn.tsx
│       └── SignUp.tsx
├── features/
│   ├── user/            # User-related features
│   │   ├── Profile.tsx
│   │   └── Settings.tsx
│   └── org/            # Organization-related features
│       ├── Dashboard.tsx
│       └── Members.tsx
├── hooks/              # Shared hooks
│   ├── useQueryConfig.ts
│   └── useMutationConfig.ts
└── utils/
    ├── errors.ts      # Error handling utilities
    └── validation.ts  # Validation utilities
```

## Code Organization Standards

### 1. Client Initialization

```typescript
// src/auth/client.ts
import { ClerkProvider } from '@clerk/clerk-react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 60 * 1000,
      retry: 1,
      refetchOnWindowFocus: false
    }
  }
});

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <ClerkProvider publishableKey={process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY}>
      <QueryClientProvider client={queryClient}>
        {children}
        <ReactQueryDevtools />
      </QueryClientProvider>
    </ClerkProvider>
  );
}
```

### 2. Custom Hooks

```typescript
// src/auth/hooks/useAuthQuery.ts
import { useAuth } from '@clerk/clerk-react';
import { UseQueryOptions, useQuery } from '@tanstack/react-query';
import { AuthError } from '@/utils/errors';

interface AuthQueryOptions<TData> extends Omit<UseQueryOptions<TData>, 'queryFn'> {
  requireAuth?: boolean;
}

export function useAuthQuery<TData>({
  queryKey,
  queryFn,
  requireAuth = true,
  ...options
}: AuthQueryOptions<TData>) {
  const { getToken, isSignedIn } = useAuth();
  
  return useQuery({
    queryKey,
    queryFn: async () => {
      if (requireAuth && !isSignedIn) {
        throw new AuthError('Authentication required');
      }
      
      const token = await getToken();
      return queryFn(token);
    },
    ...options,
    enabled: (!requireAuth || isSignedIn) && options.enabled
  });
}
```

## Naming Conventions

### 1. Functions and Variables

```typescript
// ✅ CORRECT
const useUserProfile = () => { /* ... */ };
const handleSignIn = async () => { /* ... */ };
const isAuthenticated = true;

// ❌ INCORRECT
const UserProfile = () => { /* ... */ };  // Looks like a component
const signin = async () => { /* ... */ }; // Inconsistent casing
const authenticated = true;               // Unclear boolean naming
```

### 2. Components

```typescript
// ✅ CORRECT
export function SignInForm() { /* ... */ }
export function UserProfileCard() { /* ... */ }
export function OrganizationList() { /* ... */ }

// ❌ INCORRECT
export function signInForm() { /* ... */ }   // Wrong casing
export function Profile() { /* ... */ }      // Too generic
export function OrgList() { /* ... */ }      // Unclear abbreviation
```

### 3. Event Handlers

```typescript
// ✅ CORRECT
const handleSubmit = (event: FormEvent) => { /* ... */ };
const handleSignInClick = () => { /* ... */ };
const handleProfileUpdate = async () => { /* ... */ };

// ❌ INCORRECT
const submit = (event: FormEvent) => { /* ... */ };     // Too generic
const clickSignIn = () => { /* ... */ };               // Wrong order
const profileUpdateHandler = async () => { /* ... */ }; // Inconsistent naming
```

## Error Handling

```typescript
// src/utils/errors.ts
export class AuthError extends Error {
  constructor(
    message: string,
    public code: string = 'UNAUTHORIZED',
    public status: number = 401
  ) {
    super(message);
    this.name = 'AuthError';
  }
}

export function handleAuthError(error: unknown): AuthError {
  if (error instanceof AuthError) {
    return error;
  }
  
  if (error instanceof Error) {
    return new AuthError(error.message);
  }
  
  return new AuthError('An unknown error occurred');
}

// Usage in components
function UserProfile() {
  const { data, error } = useAuthQuery({
    queryKey: ['profile'],
    queryFn: async (token) => {
      try {
        const response = await fetch('/api/profile', {
          headers: { Authorization: `Bearer ${token}` }
        });
        
        if (!response.ok) {
          throw new AuthError('Failed to fetch profile', 'FETCH_ERROR', response.status);
        }
        
        return response.json();
      } catch (error) {
        throw handleAuthError(error);
      }
    },
    onError: (error) => {
      if (error instanceof AuthError) {
        // Handle specific error types
        switch (error.code) {
          case 'UNAUTHORIZED':
            // Redirect to sign in
            break;
          case 'FETCH_ERROR':
            // Show retry button
            break;
          default:
            // Show general error message
        }
      }
    }
  });
}
```

## Async/Await Usage

```typescript
// ✅ CORRECT
async function fetchUserData(token: string) {
  try {
    const response = await fetch('/api/user', {
      headers: { Authorization: `Bearer ${token}` }
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return response.json();
  } catch (error) {
    throw handleAuthError(error);
  }
}

// ❌ INCORRECT
function fetchUserData(token: string) {
  return fetch('/api/user', {
    headers: { Authorization: `Bearer ${token}` }
  })
    .then(response => response.json())
    .catch(error => console.error(error)); // Don't swallow errors
}
```

## Security Standards

```typescript
// ✅ CORRECT
const useSecureProfile = () => {
  const { getToken } = useAuth();
  
  return useQuery({
    queryKey: ['secure-profile'],
    queryFn: async () => {
      const token = await getToken();
      return fetch('/api/profile', {
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json'
        }
      });
    }
  });
};

// ❌ INCORRECT
const useInsecureProfile = () => {
  const token = localStorage.getItem('token'); // Never store tokens in localStorage
  
  return useQuery({
    queryKey: ['insecure-profile'],
    queryFn: () => fetch('/api/profile', {
      headers: { token } // Don't use custom token headers
    })
  });
};
```

## Documentation Standards

```typescript
/**
 * Custom hook for authenticated queries using Clerk and TanStack Query.
 * 
 * @param queryKey - The key for the query cache
 * @param queryFn - The function to fetch data (receives auth token)
 * @param options - Additional TanStack Query options
 * @returns Query result with authenticated data
 * 
 * @example
 * ```tsx
 * const { data, isLoading } = useAuthQuery({
 *   queryKey: ['profile'],
 *   queryFn: (token) => fetchProfile(token)
 * });
 * ```
 */
export function useAuthQuery<TData>({ /* ... */ }) {
  // Implementation
}
```

## Testing Standards

```typescript
// src/__tests__/auth/hooks/useAuthQuery.test.ts
import { renderHook, waitFor } from '@testing-library/react';
import { useAuthQuery } from '@/auth/hooks/useAuthQuery';

describe('useAuthQuery', () => {
  it('should fetch data when authenticated', async () => {
    const { result } = renderHook(() => useAuthQuery({
      queryKey: ['test'],
      queryFn: async (token) => ({ data: 'test' })
    }));
    
    await waitFor(() => {
      expect(result.current.data).toEqual({ data: 'test' });
    });
  });
  
  it('should throw error when not authenticated', async () => {
    const { result } = renderHook(() => useAuthQuery({
      queryKey: ['test'],
      queryFn: async (token) => ({ data: 'test' }),
      requireAuth: true
    }));
    
    await waitFor(() => {
      expect(result.current.error).toBeInstanceOf(AuthError);
    });
  });
});
```

## Performance Standards

```typescript
// ✅ CORRECT
const useOptimizedQuery = () => {
  return useQuery({
    queryKey: ['data'],
    queryFn: fetchData,
    staleTime: 60 * 1000, // 1 minute
    cacheTime: 15 * 60 * 1000, // 15 minutes
    retry: 1,
    refetchOnWindowFocus: false
  });
};

// ❌ INCORRECT
const useUnoptimizedQuery = () => {
  return useQuery({
    queryKey: ['data'],
    queryFn: fetchData,
    // Missing optimization options
    // Will refetch too often
  });
};
```

## Best Practices Summary

1. Use TypeScript for better type safety and developer experience
2. Follow proper file and folder structure
3. Use consistent naming conventions
4. Implement proper error handling
5. Use async/await with proper error handling
6. Follow security best practices
7. Document code properly
8. Write comprehensive tests
9. Optimize for performance
10. Keep dependencies up to date 