---
name: inst-rule-better-auth-javascript-coding-stand
description: "Coding standards and best practices for vanilla JavaScript apps with Better Auth Authentication"
license: MIT
tags: [general]
---

# Coding Standards for Vanilla JavaScript with Better Auth Authentication

## Overview

This document outlines the coding standards and best practices for implementing Better Auth authentication in vanilla JavaScript applications. Following these standards ensures secure, maintainable, and efficient authentication implementation.

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
│   │   ├── client.js       # Better Auth initialization and core auth functions
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
// client.js - Core authentication setup
import { createAuthClient } from 'better-auth/vanilla';

export async function initializeAuth(config) {
  if (!config.baseUrl) {
    throw new Error('Base URL is required');
  }
  
  return createAuthClient(config);
}

// handlers.js - Event handlers
export async function handleAuthStateChange(auth) {
  const user = await auth.getUser();
  if (user) {
    // Handle authenticated state
  } else {
    // Handle unauthenticated state
  }
}

// ui.js - UI components
export function updateAuthUI(isAuthenticated, user) {
  const loginForm = document.getElementById('login-form');
  const logoutBtn = document.getElementById('logout');
  const profile = document.getElementById('profile');
  
  loginForm.style.display = isAuthenticated ? 'none' : 'block';
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
async function initializeAuthClient() { }
async function handleAuthStateChange() { }
async function updateAuthenticationUI() { }

// ❌ INCORRECT
function init() { }  // Too vague
function auth() { }  // Too vague
function doAuth() { } // Unclear purpose
```

### 2. Variables

```javascript
// ✅ CORRECT
const authClient = await initializeAuthClient();
const currentUser = await authClient.getUser();
const isAuthenticated = Boolean(currentUser);

// ❌ INCORRECT
const client = await initializeAuthClient();  // Too vague
const auth = await authClient.getUser();  // Too vague
const flag = Boolean(currentUser);  // Unclear purpose
```

### 3. Event Handlers

```javascript
// ✅ CORRECT
function handleSignInSubmit() { }
function handleSignOutClick() { }
function handleAuthStateChange() { }

// ❌ INCORRECT
function submit() { }  // Too vague
function click() { }  // Too vague
function change() { }  // Too vague
```

## Error Handling

### 1. Standard Error Handling Pattern

```javascript
// ✅ CORRECT
async function handleAuthentication() {
  try {
    const auth = await createAuthClient({
      baseUrl: process.env.AUTH_API_URL
    });
    
    const user = await auth.getUser();
    if (user) {
      await handleAuthStateChange(user);
    }
    
    return auth;
  } catch (error) {
    if (error.code === 'invalid_credentials') {
      throw new AuthError('Invalid credentials', 'invalid_credentials');
    }
    throw error;
  }
}

// ❌ INCORRECT
async function handleAuthentication() {
  const auth = await createAuthClient({  // Missing error handling
    baseUrl: process.env.AUTH_API_URL
  });
  return auth;
}
```

### 2. Custom Error Classes

```javascript
// ✅ CORRECT
class AuthError extends Error {
  constructor(message, code) {
    super(message);
    this.name = 'AuthError';
    this.code = code;
  }
}

// Usage
try {
  await handleAuthentication();
} catch (error) {
  if (error instanceof AuthError) {
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
    const auth = await createAuthClient(config);
    const user = await auth.getUser();
    if (user) {
      await handleAuthStateChange(user);
      updateUI(true, user);
    } else {
      updateUI(false);
    }
    return auth;
  } catch (error) {
    handleAuthError(error);
    throw error;
  }
}

// ❌ INCORRECT
function initializeAuthentication() {
  createAuthClient(config)
    .then(auth => {
      auth.getUser()  // Missing error handling
        .then(user => {
          if (user) {
            handleAuthStateChange(user);  // Missing await
            updateUI(true, user);
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
  baseUrl: process.env.AUTH_API_URL,
  publicKey: process.env.AUTH_PUBLIC_KEY
};

// ❌ INCORRECT
const config = {
  baseUrl: 'http://api.example.com/auth',  // Hardcoded URL
  publicKey: 'public-key-123'  // Hardcoded key
};
```

### 2. Token Handling

```javascript
// ✅ CORRECT
async function getAccessToken() {
  try {
    return await auth.getToken();
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
 * Initializes the Better Auth client with the provided configuration.
 * @param {Object} config - The auth configuration object
 * @param {string} config.baseUrl - The base URL for auth API
 * @param {string} config.publicKey - The public key for auth
 * @returns {Promise<AuthClient>} The initialized auth client
 * @throws {AuthError} If initialization fails
 */
async function initializeAuthClient(config) {
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
describe('Better Auth Authentication', () => {
  it('should initialize auth client', async () => {
    const auth = await initializeAuthClient(config);
    expect(auth).toBeDefined();
  });
  
  it('should handle authentication errors', async () => {
    try {
      await initializeAuthClient({});
      fail('Should have thrown an error');
    } catch (error) {
      expect(error).toBeInstanceOf(AuthError);
    }
  });
});
```

## Performance Standards

### 1. Lazy Loading

```javascript
// ✅ CORRECT
async function loadAuth() {
  if (!window.BetterAuth) {
    await import('better-auth/vanilla');
  }
  return initializeAuthClient(config);
}
```

### 2. Event Handler Cleanup

```javascript
// ✅ CORRECT
function setupAuthListeners(auth) {
  const loginForm = document.getElementById('login-form');
  const handleSubmit = async (e) => {
    e.preventDefault();
    // Handle login
  };
  
  loginForm.addEventListener('submit', handleSubmit);
  
  // Clean up on page unload
  window.addEventListener('unload', () => {
    loginForm.removeEventListener('submit', handleSubmit);
  });
}
```

## Best Practices Summary

1. Always use the latest version of Better Auth
2. Implement proper error handling with specific error types
3. Use consistent naming conventions
4. Document all functions and types
5. Implement proper cleanup for event listeners
6. Use environment variables for configuration
7. Never store sensitive information in client-side storage
8. Always handle authentication state changes properly
9. Use proper security measures (HTTPS, secure headers)
10. Follow proper async/await patterns
11. Implement proper loading states
12. Use proper type checking and validation
13. Follow proper file organization
14. Implement proper error messages and user feedback
15. Keep the codebase maintainable and well-documented