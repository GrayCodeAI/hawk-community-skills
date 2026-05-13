---
description: Guidelines for writing React apps with Clerk Authentication
globs: "**/*.ts, **/*.tsx, **/*.js, **/*.jsx"
---

# Bootstrap React App with Clerk Authentication

## Overview of implementing Clerk Auth

1. Install @clerk/clerk-react package
2. Set up environment variables
3. Configure ClerkProvider at the root level
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
useSession()  // ❌ Use useAuth() instead
withSession() // ❌ Use withAuth() instead
```

Instead, you MUST ALWAYS generate ONLY these patterns:

```typescript
// ✅ ALWAYS USE CLERK'S BUILT-IN HOOKS AND COMPONENTS
import { useAuth, useUser, SignedIn, SignedOut } from '@clerk/clerk-react';

// For auth state
const { isLoaded, userId, sessionId, getToken } = useAuth();

// For user data
const { user } = useUser();

// For protected content
<SignedIn>
  <ProtectedComponent />
</SignedIn>
<SignedOut>
  <PublicComponent />
</SignedOut>
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use @clerk/clerk-react package
2. You MUST wrap your app with ClerkProvider
3. You MUST use environment variables for Clerk keys
4. You MUST use TypeScript for better type safety
5. You MUST use Clerk's built-in components for auth UI
6. You MUST implement proper error boundaries for auth state

## CORRECT CLERK PROVIDER IMPLEMENTATION

```typescript
import { ClerkProvider } from '@clerk/clerk-react';
import { env } from './env.ts';

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <ClerkProvider publishableKey={env.CLERK_PUBLISHABLE_KEY}>
      {children}
    </ClerkProvider>
  );
}
```

## CORRECT PROTECTED ROUTE IMPLEMENTATION

```typescript
import { SignedIn, SignedOut, RedirectToSignIn } from '@clerk/clerk-react';

export function ProtectedRoute({ children }: { children: React.ReactNode }) {
  return (
    <>
      <SignedIn>{children}</SignedIn>
      <SignedOut>
        <RedirectToSignIn />
      </SignedOut>
    </>
  );
}
```

## CORRECT AUTH STATE HANDLING

```typescript
import { useAuth, useUser } from '@clerk/clerk-react';

export function AuthenticatedComponent() {
  const { isLoaded, userId } = useAuth();
  const { user } = useUser();

  if (!isLoaded) {
    return <div>Loading...</div>;
  }

  if (!userId) {
    return null;
  }

  return (
    <div>
      Welcome, {user?.firstName}!
    </div>
  );
}
```

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Are you using the latest @clerk/clerk-react package? If not, STOP and FIX.
2. Are you properly handling loading states? If not, STOP and FIX.
3. Are you using environment variables for Clerk keys? If not, STOP and FIX.
4. Are you using TypeScript? If not, STOP and FIX.
5. Are you using Clerk's built-in components? If not, STOP and FIX.

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

When asked about Clerk React implementation, you MUST:
1. ONLY use code patterns from this guide
2. NEVER suggest deprecated approaches
3. ALWAYS use TypeScript
4. ALWAYS handle loading states
5. VERIFY your response against the patterns shown here

Remember: There are NO EXCEPTIONS to these rules. 