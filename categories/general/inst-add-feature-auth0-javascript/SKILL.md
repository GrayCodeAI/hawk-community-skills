---
description: Guidelines for adding features to vanilla JavaScript apps with Auth0 Authentication
globs: "**/*.html, **/*.js"
---

# Adding Features to Vanilla JavaScript App with Auth0 Authentication

## Overview of Auth0 Features in JavaScript

1. User Authentication
2. Session Management
3. User Profile Management
4. Social Login Integration
5. Multi-Factor Authentication (MFA)
6. Role-Based Access Control (RBAC)
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
// ✅ ALWAYS USE AUTH0'S BUILT-IN METHODS
// User authentication
await auth0Client.loginWithRedirect();

// Get user profile
const user = await auth0Client.getUser();

// Get access token
const token = await auth0Client.getTokenSilently();

// Check authentication
const isAuthenticated = await auth0Client.isAuthenticated();
```

## FEATURE IMPLEMENTATION GUIDE

### 1. User Authentication

```javascript
// Basic authentication
async function handleAuthentication() {
  try {
    // Initialize Auth0 client
    const auth0Client = await createAuth0Client({
      domain: 'YOUR_AUTH0_DOMAIN',
      clientId: 'YOUR_CLIENT_ID',
      authorizationParams: {
        redirect_uri: window.location.origin
      }
    });
    
    // Handle redirect callback
    if (window.location.search.includes("code=")) {
      await auth0Client.handleRedirectCallback();
      window.history.replaceState({}, document.title, window.location.pathname);
    }
    
    return auth0Client;
  } catch (error) {
    console.error('Authentication error:', error);
    throw error;
  }
}

// Login
async function login() {
  try {
    await auth0Client.loginWithRedirect();
  } catch (error) {
    console.error('Login error:', error);
    throw error;
  }
}

// Logout
async function logout() {
  try {
    await auth0Client.logout({
      logoutParams: {
        returnTo: window.location.origin
      }
    });
  } catch (error) {
    console.error('Logout error:', error);
    throw error;
  }
}
```

### 2. Session Management

```javascript
// Check authentication state
async function checkAuthState() {
  try {
    const isAuthenticated = await auth0Client.isAuthenticated();
    return isAuthenticated;
  } catch (error) {
    console.error('Auth state check error:', error);
    throw error;
  }
}

// Get session info
async function getSessionInfo() {
  try {
    if (await auth0Client.isAuthenticated()) {
      const user = await auth0Client.getUser();
      const token = await auth0Client.getTokenSilently();
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
    const user = await auth0Client.getUser();
    return user;
  } catch (error) {
    console.error('Get profile error:', error);
    throw error;
  }
}

// Update user metadata
async function updateUserMetadata(metadata) {
  try {
    const token = await auth0Client.getTokenSilently();
    const response = await fetch(`https://YOUR_AUTH0_DOMAIN/api/v2/users/${user.sub}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ user_metadata: metadata })
    });
    return await response.json();
  } catch (error) {
    console.error('Update metadata error:', error);
    throw error;
  }
}
```

### 4. Social Login Integration

```javascript
// Initialize Auth0 with social providers
const auth0Client = await createAuth0Client({
  domain: 'YOUR_AUTH0_DOMAIN',
  clientId: 'YOUR_CLIENT_ID',
  authorizationParams: {
    redirect_uri: window.location.origin,
    connection: 'google-oauth2' // Specify social connection
  }
});

// Login with specific social provider
async function socialLogin(provider) {
  try {
    await auth0Client.loginWithRedirect({
      authorizationParams: {
        connection: provider // 'google-oauth2', 'facebook', 'github', etc.
      }
    });
  } catch (error) {
    console.error('Social login error:', error);
    throw error;
  }
}
```

### 5. Multi-Factor Authentication (MFA)

```javascript
// Initialize Auth0 with MFA
const auth0Client = await createAuth0Client({
  domain: 'YOUR_AUTH0_DOMAIN',
  clientId: 'YOUR_CLIENT_ID',
  authorizationParams: {
    redirect_uri: window.location.origin
  }
});

// Handle MFA challenge
async function handleMFAChallenge() {
  try {
    await auth0Client.loginWithRedirect({
      authorizationParams: {
        acr_values: 'http://schemas.openid.net/pape/policies/2007/06/multi-factor'
      }
    });
  } catch (error) {
    console.error('MFA error:', error);
    throw error;
  }
}
```

### 6. Role-Based Access Control (RBAC)

```javascript
// Check user roles
async function checkUserRole(requiredRole) {
  try {
    const user = await auth0Client.getUser();
    return user?.['https://your-namespace/roles']?.includes(requiredRole);
  } catch (error) {
    console.error('Role check error:', error);
    throw error;
  }
}

// Protect content based on role
async function protectContent(element, requiredRole) {
  try {
    const hasRole = await checkUserRole(requiredRole);
    element.style.display = hasRole ? 'block' : 'none';
  } catch (error) {
    console.error('Content protection error:', error);
    throw error;
  }
}
```

### 7. Token Management

```javascript
// Get access token
async function getAccessToken() {
  try {
    const token = await auth0Client.getTokenSilently();
    return token;
  } catch (error) {
    console.error('Token error:', error);
    throw error;
  }
}

// Make authenticated API call
async function callProtectedAPI(url) {
  try {
    const token = await getAccessToken();
    const response = await fetch(url, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });
    return await response.json();
  } catch (error) {
    console.error('API call error:', error);
    throw error;
  }
}
```

### 8. API Authorization

```javascript
// Initialize Auth0 with audience
const auth0Client = await createAuth0Client({
  domain: 'YOUR_AUTH0_DOMAIN',
  clientId: 'YOUR_CLIENT_ID',
  authorizationParams: {
    redirect_uri: window.location.origin,
    audience: 'YOUR_API_IDENTIFIER'
  }
});

// Get scoped access token
async function getScopedAccessToken(scope) {
  try {
    const token = await auth0Client.getTokenSilently({
      authorizationParams: {
        audience: 'YOUR_API_IDENTIFIER',
        scope: scope
      }
    });
    return token;
  } catch (error) {
    console.error('Scoped token error:', error);
    throw error;
  }
}
```

## BEST PRACTICES

1. Always use Auth0's built-in methods for authentication operations
2. Implement proper error handling for all feature operations
3. Use async/await for cleaner asynchronous code
4. Handle loading states during async operations
5. Implement proper token management using Auth0's methods
6. Use proper RBAC for content protection
7. Keep the Auth0 SDK updated for new features and security patches
8. Use environment variables for sensitive configuration
9. Implement proper error messages and user feedback
10. Test all authentication flows thoroughly
11. Implement proper logout handling
12. Use Auth0's built-in social login providers
13. Implement proper MFA flows when required
14. Use proper security headers in your application
15. Implement proper session handling and token refresh logic 