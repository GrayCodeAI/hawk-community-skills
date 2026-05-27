---
name: inst-rule-auth0-javascript-coding-standards
description: "Coding standards and best practices for vanilla JavaScript apps with Auth0 Authentication"
license: MIT
tags: [general]
---

# Coding Standards for Vanilla JavaScript with Auth0 Authentication

## Overview

This document outlines the coding standards and best practices for implementing Auth0 authentication in vanilla JavaScript applications. Following these standards ensures secure, maintainable, and efficient authentication implementation.

## 🚨 CRITICAL RULES 🚨

1. NEVER store authentication tokens in localStorage or cookies
2. NEVER implement custom authentication flows
3. NEVER expose sensitive keys in client-side code
4. ALWAYS use HTTPS in production
5. ALWAYS implement proper error handling
6. ALWAYS use environment variables for configuration

## Code Organization

### 1. File Structure

```
project/
├── src/
│   ├── auth/
│   │   ├── auth0.js        # Auth0 initialization and core auth functions
│   │   ├── handlers.js     # Auth event handlers
│   │   └── ui.js          # UI-related auth functions
│   ├── components/
│   │   └── auth/          # Auth-related components
│   └── utils/
│       └── errors.js      # Error handling utilities
├── public/
│   └── index.html         # Main HTML file
└── .env                   # Environment variables
```

### 2. Code Organization Standards

```javascript
// auth0.js - Core authentication setup
export async function initializeAuth0(config) {
  if (!config.domain || !config.clientId) {
    throw new Error('Domain and clientId are required');
  }
  
  return await createAuth0Client(config);
}

// handlers.js - Event handlers
export async function handleAuthCallback(auth0Client) {
  if (location.search.includes("code=") && location.search.includes("state=")) {
    await auth0Client.handleRedirectCallback();
    window.history.replaceState({}, document.title, "/");
  }
}

// ui.js - UI components
export function updateAuthUI(isAuthenticated, user) {
  const loginBtn = document.getElementById('login');
  const logoutBtn = document.getElementById('logout');
  const profile = document.getElementById('profile');
  
  loginBtn.style.display = isAuthenticated ? 'none' : 'block';
  logoutBtn.style.display = isAuthenticated ? 'block' : 'none';
  profile.style.display = isAuthenticated ? 'block' : 'none';
  
  if (isAuthenticated && user) {
    profile.textContent = JSON.stringify(user, null, 2);
  }
}
```

## Naming Conventions

### 1. Functions

```javascript
// ✅ CORRECT
async function initializeAuth0Client() { }
async function handleAuthenticationCallback() { }
async function updateAuthenticationUI() { }

// ❌ INCORRECT
function init() { }  // Too vague
function auth() { }  // Too vague
function doAuth() { } // Unclear purpose
```

### 2. Variables

```javascript
// ✅ CORRECT
const auth0Client = await initializeAuth0Client();
const currentUser = await auth0Client.getUser();
const isAuthenticated = await auth0Client.isAuthenticated();

// ❌ INCORRECT
const client = await initializeAuth0Client();  // Too vague
const auth = await auth0Client.getUser();  // Too vague
const flag = await auth0Client.isAuthenticated();  // Unclear purpose
```

### 3. Event Handlers

```javascript
// ✅ CORRECT
function handleLoginClick() { }
function handleLogoutClick() { }
function handleAuthenticationCallback() { }

// ❌ INCORRECT
function login() { }  // Too vague
function handleAuth() { }  // Too vague
function callback() { }  // Too vague
```

## Error Handling

### 1. Standard Error Handling Pattern

```javascript
// ✅ CORRECT
async function handleAuthentication() {
  try {
    const auth0Client = await createAuth0Client({
      domain: 'YOUR_AUTH0_DOMAIN',
      clientId: 'YOUR_CLIENT_ID'
    });
    
    if (location.search.includes("code=")) {
      await auth0Client.handleRedirectCallback();
      window.history.replaceState({}, document.title, "/");
    }
    
    return auth0Client;
  } catch (error) {
    if (error.error === 'login_required') {
      throw new Auth0Error('Authentication required', 'login_required');
    }
    throw error;
  }
}

// ❌ INCORRECT
async function handleAuthentication() {
  const auth0Client = await createAuth0Client({  // Missing error handling
    domain: 'YOUR_AUTH0_DOMAIN',
    clientId: 'YOUR_CLIENT_ID'
  });
  return auth0Client;
}
```

### 2. Custom Error Classes

```javascript
// ✅ CORRECT
class Auth0Error extends Error {
  constructor(message, code) {
    super(message);
    this.name = 'Auth0Error';
    this.code = code;
  }
}

// Usage
try {
  await handleAuthentication();
} catch (error) {
  if (error instanceof Auth0Error) {
    showAuthError(error.message);
  } else {
    showGeneralError('An unexpected error occurred');
  }
}
```

## Async/Await Usage

### 1. Proper Async/Await Pattern

```javascript
// ✅ CORRECT
async function initializeAuthentication() {
  try {
    const auth0Client = await createAuth0Client(config);
    await handleAuthCallback(auth0Client);
    const isAuthenticated = await auth0Client.isAuthenticated();
    if (isAuthenticated) {
      const user = await auth0Client.getUser();
      updateUI(user);
    }
    return auth0Client;
  } catch (error) {
    handleAuthError(error);
    throw error;
  }
}

// ❌ INCORRECT
function initializeAuthentication() {
  createAuth0Client(config)
    .then(auth0Client => {
      handleAuthCallback(auth0Client);  // Missing await
      auth0Client.isAuthenticated()  // Missing error handling
        .then(isAuthenticated => {
          if (isAuthenticated) {
            auth0Client.getUser()  // Missing error handling
              .then(updateUI);
          }
        });
    });
}
```

## Security Standards

### 1. Environment Variables

```javascript
// ✅ CORRECT
const config = {
  domain: process.env.AUTH0_DOMAIN,
  clientId: process.env.AUTH0_CLIENT_ID
};

// ❌ INCORRECT
const config = {
  domain: 'your-tenant.auth0.com',  // Hardcoded domain
  clientId: 'your-client-id'  // Hardcoded client ID
};
```

### 2. Token Handling

```javascript
// ✅ CORRECT
async function getAccessToken() {
  try {
    return await auth0Client.getTokenSilently();
  } catch (error) {
    handleTokenError(error);
    throw error;
  }
}

// ❌ INCORRECT
function getAccessToken() {
  const token = localStorage.getItem('access_token');  // Never store tokens in localStorage
  return token;
}
```

## Documentation Standards

### 1. Function Documentation

```javascript
// ✅ CORRECT
/**
 * Initializes the Auth0 client with the provided configuration.
 * @param {Object} config - The Auth0 configuration object
 * @param {string} config.domain - The Auth0 domain
 * @param {string} config.clientId - The Auth0 client ID
 * @returns {Promise<Auth0Client>} The initialized Auth0 client
 * @throws {Auth0Error} If initialization fails
 */
async function initializeAuth0Client(config) {
  // Implementation
}

// ❌ INCORRECT
// Initializes auth
function initAuth(config) {
  // Implementation
}
```

## Testing Standards

### 1. Authentication Tests

```javascript
// ✅ CORRECT
describe('Auth0 Authentication', () => {
  it('should initialize Auth0 client', async () => {
    const auth0Client = await initializeAuth0Client(config);
    expect(auth0Client).toBeDefined();
  });
  
  it('should handle authentication errors', async () => {
    try {
      await initializeAuth0Client({});
      fail('Should have thrown an error');
    } catch (error) {
      expect(error).toBeInstanceOf(Auth0Error);
    }
  });
});
```

## Performance Standards

### 1. Lazy Loading

```javascript
// ✅ CORRECT
async function loadAuth0() {
  if (!window.createAuth0Client) {
    await import('@auth0/auth0-spa-js');
  }
  return initializeAuth0Client(config);
}
```

### 2. Event Handler Cleanup

```javascript
// ✅ CORRECT
function setupAuthListeners(auth0Client) {
  const loginButton = document.getElementById('login');
  const loginHandler = () => auth0Client.loginWithRedirect();
  loginButton.addEventListener('click', loginHandler);
  
  // Clean up on page unload
  window.addEventListener('unload', () => {
    loginButton.removeEventListener('click', loginHandler);
  });
}
```

## Best Practices Summary

1. Always use the latest version of the Auth0 SPA SDK
2. Implement proper error handling with specific error types
3. Use consistent naming conventions
4. Document all functions and types
5. Implement proper cleanup for event listeners
6. Use environment variables for configuration
7. Never store sensitive information in client-side storage
8. Always handle authentication callbacks properly
9. Use proper security measures (HTTPS, secure headers)
10. Follow proper async/await patterns
11. Implement proper loading states
12. Use proper type checking and validation
13. Follow proper file organization
14. Implement proper error messages and user feedback
15. Keep the codebase maintainable and well-documented