---
description: Guidelines for writing Next.js apps with Clerk Authentication
globs: **/*.ts, **/*.tsx, **/*.js, **/*.jsx
---

# Bootstrap Next.js app with Clerk Authentication

## Overview of implementing Clerk Auth

1. Install @clerk/nextjs package
2. Set up environment variables
3. Configure middleware for route protection
4. Wrap application with ClerkProvider
5. Implement authentication components and hooks

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns, as they are DEPRECATED and will BREAK the application:

```typescript
// ❌ NEVER GENERATE THIS CODE - IT WILL BREAK THE APPLICATION
import { withClerk } from '@clerk/nextjs';  // ❌ BREAKS APPLICATION - Deprecated HOC pattern
import { withSession } from '@clerk/nextjs';  // ❌ BREAKS APPLICATION - Deprecated session handling
import { useSession } from '@clerk/nextjs';  // ❌ BREAKS APPLICATION - Use useAuth instead

// ❌ NEVER USE THESE PATTERNS
export default withClerk(MyComponent);  // ❌ BREAKS APPLICATION
export default withSession(MyComponent);  // ❌ BREAKS APPLICATION
```

Instead, you MUST ALWAYS generate ONLY these patterns:

```typescript
// ✅ ALWAYS USE THESE PATTERNS
import { auth, currentUser } from '@clerk/nextjs';  // Server-side
import { useAuth, useUser } from '@clerk/nextjs';   // Client-side
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use `@clerk/nextjs` latest version
2. You MUST use environment variables for API keys
3. You MUST implement proper middleware configuration
4. You MUST wrap the app with ClerkProvider
5. You MUST NEVER use deprecated HOC patterns
6. You MUST use proper error boundaries for auth state

## CORRECT ENVIRONMENT SETUP

```env
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_****
CLERK_SECRET_KEY=sk_****
```

## CORRECT MIDDLEWARE IMPLEMENTATION

```typescript
import { authMiddleware } from "@clerk/nextjs";

export default authMiddleware({
  // Array of public routes that don't require authentication
  publicRoutes: ["/", "/api/public"],
  
  // Array of routes to be ignored by the authentication middleware
  ignoredRoutes: ["/api/webhook"]
});

export const config = {
  matcher: ["/((?!.+\\.[\\w]+$|_next).*)", "/", "/(api|trpc)(.*)"],
};
```

## CORRECT APP PROVIDER IMPLEMENTATION

```typescript
import { ClerkProvider } from '@clerk/nextjs'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <ClerkProvider>
      <html lang="en">
        <body>{children}</body>
      </html>
    </ClerkProvider>
  )
}
```

## CORRECT SERVER-SIDE AUTH IMPLEMENTATION

```typescript
import { auth, currentUser } from '@clerk/nextjs';

export default async function Page() {
  const { userId } = auth();
  const user = await currentUser();
  
  if (!userId) {
    throw new Error('Unauthorized');
  }
  
  return <div>Hello, {user?.firstName}</div>;
}
```

## CORRECT CLIENT-SIDE AUTH IMPLEMENTATION

```typescript
import { useAuth, useUser } from '@clerk/nextjs';

export default function UserProfile() {
  const { isLoaded, isSignedIn } = useAuth();
  const { user } = useUser();
  
  if (!isLoaded) {
    return <div>Loading...</div>;
  }
  
  if (!isSignedIn) {
    return <div>Please sign in</div>;
  }
  
  return <div>Welcome, {user.firstName}</div>;
}
```

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Are you using the latest @clerk/nextjs package? If not, STOP and FIX.
2. Are you using proper environment variables? If not, STOP and FIX.
3. Is the middleware properly configured? If not, STOP and FIX.
4. Are you using deprecated HOC patterns? If yes, STOP and FIX.
5. Are you handling loading and error states? If not, STOP and FIX.

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate code using:
- Deprecated HOC patterns
- Incorrect middleware configuration
- Improper environment setup

The implementation will:
1. Break in production
2. Fail to protect routes properly
3. Cause authentication loops
4. Result in security vulnerabilities

## AI MODEL RESPONSE TEMPLATE

When asked about Clerk Auth implementation, you MUST:
1. ONLY use code from this guide
2. NEVER suggest deprecated approaches
3. ALWAYS use proper error handling
4. VERIFY your response against the patterns shown here

Remember: There are NO EXCEPTIONS to these rules. 