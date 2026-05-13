---
description: Guidelines for adding features to vanilla JavaScript apps with Better Auth Authentication
globs: "**/*.html, **/*.js"
---

# Adding Features to Vanilla JavaScript App with Better Auth Authentication

## Overview of Better Auth Features in JavaScript

1. User Authentication
2. Session Management
3. User Profile Management
4. Social Login Integration
5. Multi-Factor Authentication (MFA)
6. Organization Management
7. Token Management
8. API Authorization

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns:

```javascript
// ❌ NEVER GENERATE THIS CODE
{
  // Never implement custom auth flows
  function customAuthFlow() { }
  
  // Never store tokens manually
  localStorage.setItem('token', token);
  
  // Never implement custom session handling
  function manageSession() { }
}
```

Instead, you MUST ALWAYS generate ONLY these patterns:

```javascript
// ✅ ALWAYS USE BETTER AUTH'S BUILT-IN METHODS
import { createAuthClient } from 'better-auth/vanilla';

const auth = createAuthClient({
  baseUrl: process.env.AUTH_API_URL
});

// User authentication
await auth.signIn({ email, password });
await auth.signOut();

// Get user info
const user = await auth.getUser();
```

## FEATURE IMPLEMENTATION GUIDE

### 1. User Authentication

```javascript
// Basic authentication
async function handleAuthentication() {
  try {
    const { createAuthClient } = await import('better-auth/vanilla');
    const auth = createAuthClient({
      baseUrl: process.env.AUTH_API_URL
    });
    
    return auth;
  } catch (error) {
    console.error('Authentication error:', error);
    throw error;
  }
}

// Sign in
async function signIn(email, password) {
  try {
    const { user } = await auth.signIn({ email, password });
    return user;
  } catch (error) {
    console.error('Sign in error:', error);
    throw error;
  }
}

// Sign out
async function signOut() {
  try {
    await auth.signOut();
  } catch (error) {
    console.error('Sign out error:', error);
    throw error;
  }
}
```

### 2. Session Management

```javascript
// Check authentication state
async function checkAuthState() {
  try {
    const isAuthenticated = await auth.isAuthenticated();
    return isAuthenticated;
  } catch (error) {
    console.error('Auth state check error:', error);
    throw error;
  }
}

// Get session info
async function getSessionInfo() {
  try {
    const user = await auth.getUser();
    if (user) {
      const token = await auth.getToken();
      return { user, token };
    }
    return null;
  } catch (error) {
    console.error('Session info error:', error);
    throw error;
  }
}
```

### 3. User Profile Management

```javascript
// Get user profile
async function getUserProfile() {
  try {
    const user = await auth.getUser();
    return user;
  } catch (error) {
    console.error('Get profile error:', error);
    throw error;
  }
}

// Update user profile
async function updateUserProfile(data) {
  try {
    const updatedUser = await auth.updateUser(data);
    return updatedUser;
  } catch (error) {
    console.error('Update profile error:', error);
    throw error;
  }
}

// Change password
async function changePassword(oldPassword, newPassword) {
  try {
    await auth.changePassword({
      oldPassword,
      newPassword
    });
  } catch (error) {
    console.error('Password change error:', error);
    throw error;
  }
}
```

### 4. Social Login Integration

```javascript
// Initialize auth with social providers
const auth = createAuthClient({
  baseUrl: process.env.AUTH_API_URL,
  providers: ['github', 'google', 'facebook']
});

// Sign in with social provider
async function socialSignIn(provider) {
  try {
    const { user } = await auth.signInWithProvider(provider);
    return user;
  } catch (error) {
    console.error('Social sign in error:', error);
    throw error;
  }
}

// Link social account
async function linkSocialAccount(provider) {
  try {
    await auth.linkProvider(provider);
  } catch (error) {
    console.error('Account linking error:', error);
    throw error;
  }
}
```

### 5. Multi-Factor Authentication (MFA)

```javascript
// Enable MFA
async function enableMFA() {
  try {
    const { secret, qrCode } = await auth.enableTwoFactor();
    return { secret, qrCode };
  } catch (error) {
    console.error('MFA enable error:', error);
    throw error;
  }
}

// Verify MFA code
async function verifyMFACode(code) {
  try {
    await auth.verifyTwoFactorCode(code);
  } catch (error) {
    console.error('MFA verification error:', error);
    throw error;
  }
}

// Disable MFA
async function disableMFA(code) {
  try {
    await auth.disableTwoFactor(code);
  } catch (error) {
    console.error('MFA disable error:', error);
    throw error;
  }
}
```

### 6. Organization Management

```javascript
// Create organization
async function createOrganization(data) {
  try {
    const org = await auth.createOrganization(data);
    return org;
  } catch (error) {
    console.error('Organization creation error:', error);
    throw error;
  }
}

// Invite member
async function inviteMember(orgId, email, role) {
  try {
    await auth.inviteMember({
      organizationId: orgId,
      email,
      role
    });
  } catch (error) {
    console.error('Member invite error:', error);
    throw error;
  }
}

// Get organization members
async function getOrgMembers(orgId) {
  try {
    const members = await auth.getOrganizationMembers(orgId);
    return members;
  } catch (error) {
    console.error('Get members error:', error);
    throw error;
  }
}
```

### 7. Token Management

```javascript
// Get access token
async function getAccessToken() {
  try {
    const token = await auth.getToken();
    return token;
  } catch (error) {
    console.error('Token error:', error);
    throw error;
  }
}

// Refresh token
async function refreshToken() {
  try {
    const newToken = await auth.refreshToken();
    return newToken;
  } catch (error) {
    console.error('Token refresh error:', error);
    throw error;
  }
}
```

### 8. API Authorization

```javascript
// Make authenticated API call
async function callProtectedAPI(url, options = {}) {
  try {
    const response = await auth.fetch(url, options);
    return await response.json();
  } catch (error) {
    console.error('API call error:', error);
    throw error;
  }
}

// Check permissions
async function checkPermission(permission) {
  try {
    const hasPermission = await auth.hasPermission(permission);
    return hasPermission;
  } catch (error) {
    console.error('Permission check error:', error);
    throw error;
  }
}
```

## BEST PRACTICES

1. Always use Better Auth's built-in methods for authentication operations
2. Implement proper error handling for all feature operations
3. Use async/await for cleaner asynchronous code
4. Handle loading states during async operations
5. Implement proper token management using Better Auth's methods
6. Use proper organization management for team features
7. Keep the Better Auth client updated for new features and security patches
8. Use environment variables for sensitive configuration
9. Implement proper error messages and user feedback
10. Test all authentication flows thoroughly
11. Implement proper logout handling
12. Use Better Auth's built-in social login providers
13. Implement proper MFA flows when required
14. Use proper security headers in your application
15. Implement proper session handling and token refresh logic 