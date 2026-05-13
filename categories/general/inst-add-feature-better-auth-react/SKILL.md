---
description: Guidelines for adding new features with Better Auth in React
globs: **/*.tsx, **/*.ts, **/*.jsx, **/*.js
---

You are a senior React developer with expertise in implementing Better Auth authentication features.

# Core Authentication Features

## User Authentication
- Implement sign in functionality using the useAuth hook. Example:
```typescript
const { signIn } = useAuth()
const handleSignIn = async () => {
  await signIn({ email, password })
}
```

- Add sign out functionality. Example:
```typescript
const { signOut } = useAuth()
const handleSignOut = async () => {
  await signOut()
  navigate('/')
}
```

- Access user data securely. Example:
```typescript
const { user, isLoading } = useAuth()
if (isLoading) return <LoadingSpinner />
return user ? <UserProfile user={user} /> : <SignInPrompt />
```

## Protected Routes
- Implement route protection with ProtectedRoute component. Example:
```typescript
import { ProtectedRoute } from 'better-auth-react'

function AppRoutes() {
  return (
    <Routes>
      <Route path="/dashboard" element={
        <ProtectedRoute>
          <DashboardPage />
        </ProtectedRoute>
      } />
    </Routes>
  )
}
```

## Two-Factor Authentication
- Enable 2FA for enhanced security. Example:
```typescript
const { enable2FA, verify2FA } = useAuth()

const setupTwoFactor = async () => {
  const { qrCode } = await enable2FA()
  setQRCodeImage(qrCode)
}

const verifyTwoFactor = async (code: string) => {
  await verify2FA(code)
}
```

# Organization Features

## Multi-tenant Support
- Implement organization management. Example:
```typescript
const { createOrganization, joinOrganization } = useAuth()

const handleCreateOrg = async () => {
  await createOrganization({
    name: orgName,
    settings: { allowedDomains: ['company.com'] }
  })
}
```

- Handle organization switching. Example:
```typescript
const { switchOrganization, currentOrganization } = useAuth()

const handleOrgSwitch = async (orgId: string) => {
  await switchOrganization(orgId)
  refetchOrgData()
}
```

# Session Management

## Token Handling
- Implement token refresh logic. Example:
```typescript
const { getToken, refreshToken } = useAuth()

const apiClient = axios.create({
  baseURL: '/api',
  headers: {
    Authorization: `Bearer ${getToken()}`
  }
})

apiClient.interceptors.response.use(
  response => response,
  async error => {
    if (error.response.status === 401) {
      await refreshToken()
      error.config.headers.Authorization = `Bearer ${getToken()}`
      return apiClient(error.config)
    }
    return Promise.reject(error)
  }
)
```

## Session State
- Handle session persistence. Example:
```typescript
const { initializeAuth } = useAuth()

useEffect(() => {
  initializeAuth({
    persistSession: true,
    storageType: 'localStorage'
  })
}, [])
```

# Error Handling

## Authentication Errors
- Implement proper error handling. Example:
```typescript
const { signIn } = useAuth()

try {
  await signIn(credentials)
} catch (error) {
  if (error.code === 'auth/invalid-credentials') {
    setError('Invalid email or password')
  } else if (error.code === 'auth/too-many-requests') {
    setError('Too many attempts. Try again later')
  }
}
```

## Network Error Handling
- Handle offline scenarios. Example:
```typescript
const { signIn } = useAuth()

const handleSignIn = async () => {
  if (!navigator.onLine) {
    setError('No internet connection')
    return
  }
  try {
    await signIn(credentials)
  } catch (error) {
    handleAuthError(error)
  }
}
```

# Security Features

## CSRF Protection
- Implement CSRF token handling. Example:
```typescript
const { getCsrfToken } = useAuth()

const apiClient = axios.create({
  headers: {
    'X-CSRF-Token': getCsrfToken()
  }
})
```

## Rate Limiting
- Add rate limiting for auth attempts. Example:
```typescript
const { signIn } = useAuth()
let attempts = 0

const handleSignIn = async () => {
  if (attempts >= 5) {
    setError('Too many attempts. Try again in 15 minutes')
    return
  }
  try {
    await signIn(credentials)
    attempts = 0
  } catch {
    attempts++
    setError('Invalid credentials')
  }
}
```

# Testing Features

## Mock Authentication
- Implement test utilities. Example:
```typescript
import { MockAuthProvider } from 'better-auth-react/testing'

const mockUser = {
  id: '123',
  email: 'test@example.com'
}

function TestWrapper({ children }) {
  return (
    <MockAuthProvider initialUser={mockUser}>
      {children}
    </MockAuthProvider>
  )
}
```

## Integration Testing
- Test authentication flows. Example:
```typescript
import { render, screen, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'

test('user can sign in', async () => {
  render(<SignInForm />, { wrapper: TestWrapper })
  
  await userEvent.type(screen.getByLabelText(/email/i), 'user@example.com')
  await userEvent.type(screen.getByLabelText(/password/i), 'password123')
  await userEvent.click(screen.getByRole('button', { name: /sign in/i }))
  
  await waitFor(() => {
    expect(screen.getByText(/welcome/i)).toBeInTheDocument()
  })
}) 