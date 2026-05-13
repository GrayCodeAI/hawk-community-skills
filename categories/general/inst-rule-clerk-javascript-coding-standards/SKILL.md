---
description: Coding standards and best practices for vanilla JavaScript apps with Clerk Authentication
globs: "**/*.html, **/*.js"
---

# Coding Standards for Vanilla JavaScript with Clerk Authentication

## Overview

This document outlines the coding standards and best practices for implementing Clerk authentication in vanilla JavaScript applications. Following these standards ensures secure, maintainable, and efficient authentication implementation.

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
│   │   ├── clerk.js        # Clerk initialization and core auth functions
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
// clerk.js - Core authentication setup
export function initializeClerk(publishableKey) {
  if (!publishableKey) {
    throw new Error('Publishable key is required');
  }
  
  return window.Clerk.load({
    publishableKey
  });
}

// handlers.js - Event handlers
export function setupAuthHandlers(clerk) {
  clerk.addListener(({ user }) => {
    handleAuthStateChange(user);
  });
}

// ui.js - UI components
export function mountAuthComponents(clerk) {
  mountSignIn(clerk);
  mountUserButton(clerk);
}
```

## Naming Conventions

### 1. Functions

```javascript
// ✅ CORRECT
function initializeClerk() { }
function handleAuthStateChange() { }
function mountSignInComponent() { }

// ❌ INCORRECT
function init() { }  // Too vague
function auth() { }  // Too vague
function doAuth() { } // Unclear purpose
```

### 2. Variables

```javascript
// ✅ CORRECT
const clerkInstance = await initializeClerk();
const currentUser = clerk.user;
const isAuthenticated = Boolean(clerk.user);

// ❌ INCORRECT
const ci = await initializeClerk();  // Too short
const auth = clerk.user;  // Too vague
const flag = Boolean(clerk.user);  // Unclear purpose
```

### 3. Event Handlers

```javascript
// ✅ CORRECT
function handleSignInSubmit(event) { }
function handleAuthStateChange(user) { }
function handleSessionExpired() { }

// ❌ INCORRECT
function submit() { }  // Too vague
function userChanged() { }  // Too vague
function expired() { }  // Too vague
```

## Error Handling

### 1. Standard Error Handling Pattern

```javascript
// ✅ CORRECT
async function authenticateUser(email, password) {
  try {
    const signIn = await clerk.signIn.create({
      identifier: email,
      password: password
    });
    return signIn;
  } catch (error) {
    if (error.code === 'invalid_credentials') {
      throw new AuthError('Invalid email or password');
    }
    throw error;
  }
}

// ❌ INCORRECT
async function authenticateUser(email, password) {
  const signIn = await clerk.signIn.create({  // Missing error handling
    identifier: email,
    password: password
  });
  return signIn;
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
  await authenticateUser(email, password);
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
async function initializeAuth() {
  try {
    const clerk = await initializeClerk(publishableKey);
    await setupAuthHandlers(clerk);
    await mountAuthComponents(clerk);
    return clerk;
  } catch (error) {
    handleInitializationError(error);
    throw error;
  }
}

// ❌ INCORRECT
function initializeAuth() {
  initializeClerk(publishableKey)
    .then(clerk => {
      setupAuthHandlers(clerk);  // Missing error handling
      mountAuthComponents(clerk);  // Missing await
    });
}
```

## Security Standards

### 1. Environment Variables

```javascript
// ✅ CORRECT
const publishableKey = process.env.CLERK_PUBLISHABLE_KEY;
const webhookSecret = process.env.CLERK_WEBHOOK_SECRET;

// ❌ INCORRECT
const publishableKey = 'pk_test_...';  // Hardcoded key
const webhookSecret = 'whsec_...';  // Hardcoded secret
```

### 2. HTTPS Usage

```javascript
// ✅ CORRECT
if (window.location.protocol !== 'https:' && process.env.NODE_ENV === 'production') {
  window.location.href = window.location.href.replace('http:', 'https:');
}
```

## Documentation Standards

### 1. Function Documentation

```javascript
// ✅ CORRECT
/**
 * Initializes Clerk authentication.
 * @param {string} publishableKey - The Clerk publishable key
 * @returns {Promise<Clerk>} The initialized Clerk instance
 * @throws {AuthError} If initialization fails
 */
async function initializeClerk(publishableKey) {
  // Implementation
}

// ❌ INCORRECT
// Initializes auth
function initializeClerk(key) {
  // Implementation
}
```

### 2. Type Documentation

```javascript
// ✅ CORRECT
/**
 * @typedef {Object} AuthConfig
 * @property {string} publishableKey - Clerk publishable key
 * @property {boolean} [debug] - Enable debug mode
 */

/**
 * @param {AuthConfig} config
 */
function initializeAuth(config) {
  // Implementation
}
```

## Testing Standards

### 1. Test Organization

```javascript
// ✅ CORRECT
describe('Authentication', () => {
  describe('initialization', () => {
    it('should initialize Clerk with valid key', async () => {
      // Test implementation
    });
    
    it('should throw error with invalid key', async () => {
      // Test implementation
    });
  });
});
```

### 2. Error Testing

```javascript
// ✅ CORRECT
it('should handle invalid credentials', async () => {
  try {
    await authenticateUser('invalid@email.com', 'wrongpassword');
    fail('Should have thrown an error');
  } catch (error) {
    expect(error).toBeInstanceOf(AuthError);
    expect(error.code).toBe('invalid_credentials');
  }
});
```

## Performance Standards

### 1. Lazy Loading

```javascript
// ✅ CORRECT
// Only load Clerk when needed
async function loadClerk() {
  if (!window.Clerk) {
    await import('@clerk/clerk-js');
  }
  return initializeClerk(publishableKey);
}
```

### 2. Event Handler Cleanup

```javascript
// ✅ CORRECT
function setupAuthListeners(clerk) {
  const unsubscribe = clerk.addListener(({ user }) => {
    // Handle auth state change
  });
  
  // Clean up on page unload
  window.addEventListener('unload', unsubscribe);
}
```

## Accessibility Standards

### 1. ARIA Attributes

```html
<!-- ✅ CORRECT -->
<button 
  onclick="handleSignIn()"
  aria-label="Sign in with email"
  role="button"
>
  Sign In
</button>

<!-- ❌ INCORRECT -->
<div onclick="handleSignIn()">Sign In</div>
```

### 2. Keyboard Navigation

```javascript
// ✅ CORRECT
function setupAccessibleAuth() {
  const signInButton = document.getElementById('sign-in');
  signInButton.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      handleSignIn();
    }
  });
}
```

## Best Practices Summary

1. Always initialize Clerk before using any of its features
2. Use proper error handling with specific error types
3. Follow consistent naming conventions
4. Document all functions and types
5. Implement proper cleanup for event listeners
6. Use environment variables for configuration
7. Implement proper accessibility features
8. Test all authentication flows thoroughly
9. Use proper security measures (HTTPS, secure headers)
10. Follow proper async/await patterns
11. Implement proper loading states
12. Use proper type checking and validation
13. Follow proper file organization
14. Implement proper error messages and user feedback
15. Keep the codebase maintainable and well-documented 