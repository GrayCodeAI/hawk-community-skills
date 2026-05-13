---
description: Guidelines for adding new features with Clerk in Next.js
globs: **/*.ts, **/*.tsx, **/*.js, **/*.jsx
---

You are a senior Next.js developer with expertise in implementing Clerk authentication features.

# Authentication Components
- Use SignIn component for login pages. Example: pages/sign-in/[[...index]].tsx
- Implement SignUp component for registration. Example: pages/sign-up/[[...index]].tsx
- Use UserButton for account management. Example: components/UserButton.tsx
- Implement SignedIn and SignedOut components for conditional rendering
- Use OrganizationSwitcher for multi-org support

# Protected Routes
- Use middleware for route protection. Example:
```typescript
import { authMiddleware } from '@clerk/nextjs'

export default authMiddleware({
  publicRoutes: ['/'],
  ignoredRoutes: ['/api/public']
})
```

- Implement role-based access control. Example:
```typescript
import { clerkClient } from '@clerk/nextjs'

export async function hasRole(userId: string, role: string) {
  const user = await clerkClient.users.getUser(userId)
  return user.publicMetadata.role === role
}
```

# Server-Side Features
- Use auth() for server component authentication. Example:
```typescript
import { auth } from '@clerk/nextjs'

export default async function Page() {
  const { userId } = auth()
  if (!userId) return null
  
  const data = await fetchUserData(userId)
  return <UserProfile data={data} />
}
```

- Implement currentUser() for user data. Example:
```typescript
import { currentUser } from '@clerk/nextjs'

export default async function Dashboard() {
  const user = await currentUser()
  if (!user) return null
  
  return <div>Welcome {user.firstName}</div>
}
```

# Client-Side Features
- Use useUser hook for user data. Example:
```typescript
import { useUser } from '@clerk/nextjs'

export function ProfileButton() {
  const { user, isLoaded } = useUser()
  if (!isLoaded) return null
  
  return <button>{user?.firstName}</button>
}
```

- Implement useAuth for auth state. Example:
```typescript
import { useAuth } from '@clerk/nextjs'

export function AuthGuard({ children }) {
  const { isLoaded, isSignedIn } = useAuth()
  
  if (!isLoaded) return <Loading />
  if (!isSignedIn) return <SignIn />
  
  return children
}
```

# Organization Features
- Use useOrganization hook. Example:
```typescript
import { useOrganization } from '@clerk/nextjs'

export function OrgDashboard() {
  const { organization, isLoaded } = useOrganization()
  if (!isLoaded) return null
  
  return <div>{organization?.name}</div>
}
```

- Implement organization invitations. Example:
```typescript
import { clerkClient } from '@clerk/nextjs'

export async function inviteToOrg(email: string, role: string) {
  const invitation = await clerkClient.organizations.createOrganizationInvitation({
    organizationId: 'org_id',
    emailAddress: email,
    role: role
  })
  return invitation
}
```

# Webhook Implementation
- Set up webhook endpoints. Example:
```typescript
import { Webhook } from 'svix'
import { WebhookEvent } from '@clerk/nextjs/server'

export async function POST(req: Request) {
  const WEBHOOK_SECRET = process.env.WEBHOOK_SECRET
  
  const headerPayload = req.headers.get('svix-signature')
  const payload = await req.json()
  
  const wh = new Webhook(WEBHOOK_SECRET)
  const evt = wh.verify(JSON.stringify(payload), {
    'svix-signature': headerPayload
  }) as WebhookEvent
  
  const { id, object, type } = evt
  
  switch (type) {
    case 'user.created':
      // Handle user creation
      break
    case 'user.updated':
      // Handle user update
      break
  }
  
  return new Response('Success', { status: 200 })
}
```

# Custom OAuth
- Implement custom OAuth providers. Example:
```typescript
import { clerkClient } from '@clerk/nextjs'

export async function createOAuthConnection(userId: string, token: string) {
  const user = await clerkClient.users.updateUserMetadata(userId, {
    publicMetadata: {
      customOAuthToken: token
    }
  })
  return user
}
```

# Error Handling
- Implement auth error boundaries. Example:
```typescript
import { useAuth } from '@clerk/nextjs'

export function AuthErrorBoundary({ children }) {
  const { isLoaded, isSignedIn } = useAuth()
  
  if (!isLoaded) {
    return <div>Loading auth state...</div>
  }
  
  if (!isSignedIn) {
    return <div>Please sign in to continue</div>
  }
  
  try {
    return children
  } catch (error) {
    return <div>Authentication error occurred</div>
  }
}
```

# Session Management
- Use session token management. Example:
```typescript
import { auth } from '@clerk/nextjs'

export async function getActiveSession() {
  const { sessionId } = auth()
  if (!sessionId) {
    throw new Error('No active session')
  }
  return sessionId
}
```

# Security Features
- Implement CSRF protection. Example:
```typescript
import { headers } from 'next/headers'
import { auth } from '@clerk/nextjs'

export async function POST(req: Request) {
  const headersList = headers()
  const csrfToken = headersList.get('x-csrf-token')
  
  const { sessionId } = auth()
  if (!sessionId || !csrfToken) {
    return new Response('Unauthorized', { status: 401 })
  }
  
  // Process request
}
```

# Testing Features
- Implement auth mocking. Example:
```typescript
import { ClerkProvider } from '@clerk/nextjs'

export function MockClerkProvider({ children }) {
  const mockUser = {
    id: 'user_test',
    firstName: 'Test',
    lastName: 'User'
  }
  
  return (
    <ClerkProvider>
      {children}
    </ClerkProvider>
  )
}
``` 