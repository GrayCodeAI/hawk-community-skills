---
description: Coding standards and best practices for vanilla JavaScript apps with Supabase Authentication
globs: "**/*.html, **/*.js"
---

# Coding Standards for Vanilla JavaScript with Supabase Authentication

## Overview

This document outlines the coding standards and best practices for implementing Supabase authentication in vanilla JavaScript applications. Following these standards ensures secure, maintainable, and efficient authentication implementation.

## 🚨 CRITICAL RULES 🚨

1. NEVER store authentication tokens in localStorage directly
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
│   │   ├── client.js       # Supabase initialization and core auth functions
│   │   ├── handlers.js     # Auth event handlers
│   │   └── ui.js          # UI-related auth functions
│   ├── db/
│   │   ├── service.js      # Database service class
│   │   └── queries.js      # Database queries
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
// client.js - Core Supabase setup
import { createClient } from '@supabase/supabase-js';

export function initializeSupabase(config) {
  if (!config.supabaseUrl || !config.supabaseAnonKey) {
    throw new Error('Supabase URL and Anon Key are required');
  }
  
  return createClient(config.supabaseUrl, config.supabaseAnonKey);
}

// handlers.js - Event handlers
export function setupAuthStateHandler(supabase, callback) {
  return supabase.auth.onAuthStateChange((event, session) => {
    callback(event, session);
  });
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
async function initializeSupabaseClient() { }
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
const supabaseClient = initializeSupabaseClient();
const currentUser = await supabaseClient.auth.getUser();
const isAuthenticated = Boolean(currentUser);

// ❌ INCORRECT
const client = initializeSupabaseClient();  // Too vague
const auth = await supabaseClient.auth.getUser();  // Too vague
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
    const { data, error } = await supabase.auth.signInWithPassword({
      email,
      password
    });
    
    if (error) throw error;
    
    return data;
  } catch (error) {
    if (error.message.includes('Invalid login credentials')) {
      throw new SupabaseError('Invalid credentials', 'auth/invalid-credentials');
    }
    throw error;
  }
}

// ❌ INCORRECT
async function handleAuthentication() {
  const { data, error } = await supabase.auth.signInWithPassword({  // Missing error handling
    email,
    password
  });
  return data;
}
```

### 2. Custom Error Classes

```javascript
// ✅ CORRECT
class SupabaseError extends Error {
  constructor(message, code) {
    super(message);
    this.name = 'SupabaseError';
    this.code = code;
  }
}

// Usage
try {
  await handleAuthentication();
} catch (error) {
  if (error instanceof SupabaseError) {
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
    const { data: { session }, error } = await supabase.auth.getSession();
    if (error) throw error;
    
    if (session) {
      await handleAuthStateChange(session);
      updateUI(true, session.user);
    } else {
      updateUI(false);
    }
    
    return session;
  } catch (error) {
    handleAuthError(error);
    throw error;
  }
}

// ❌ INCORRECT
function initializeAuthentication() {
  supabase.auth.getSession()
    .then(({ data: { session } }) => {
      if (session) {
        handleAuthStateChange(session);  // Missing error handling
        updateUI(true, session.user);
      }
    });
}
```

## Security Standards

### 1. Environment Variables

```javascript
// ✅ CORRECT
const supabaseConfig = {
  supabaseUrl: process.env.SUPABASE_URL,
  supabaseAnonKey: process.env.SUPABASE_ANON_KEY
};

// ❌ INCORRECT
const supabaseConfig = {
  supabaseUrl: 'https://your-project.supabase.co',  // Hardcoded URL
  supabaseAnonKey: 'your-anon-key'  // Hardcoded key
};
```

### 2. Token Handling

```javascript
// ✅ CORRECT
async function getAccessToken() {
  try {
    const { data: { session }, error } = await supabase.auth.getSession();
    if (error) throw error;
    return session?.access_token;
  } catch (error) {
    handleTokenError(error);
    throw error;
  }
}

// ❌ INCORRECT
function getAccessToken() {
  const token = localStorage.getItem('supabase.access_token');  // Never access tokens directly
  return token;
}
```

## Documentation Standards

### 1. Function Documentation

```javascript
// ✅ CORRECT
/**
 * Initializes the Supabase client with the provided configuration.
 * @param {Object} config - The Supabase configuration object
 * @param {string} config.supabaseUrl - The Supabase project URL
 * @param {string} config.supabaseAnonKey - The Supabase anonymous key
 * @returns {SupabaseClient} The initialized Supabase client
 * @throws {SupabaseError} If initialization fails
 */
function initializeSupabaseClient(config) {
  // Implementation
}

// ❌ INCORRECT
// Initializes Supabase
function initSupabase(config) {
  // Implementation
}
```

## Testing Standards

### 1. Authentication Tests

```javascript
// ✅ CORRECT
describe('Supabase Authentication', () => {
  it('should initialize Supabase client', async () => {
    const supabase = initializeSupabaseClient(config);
    expect(supabase).toBeDefined();
  });
  
  it('should handle authentication errors', async () => {
    try {
      await initializeSupabaseClient({});
      fail('Should have thrown an error');
    } catch (error) {
      expect(error).toBeInstanceOf(SupabaseError);
    }
  });
});
```

## Performance Standards

### 1. Lazy Loading

```javascript
// ✅ CORRECT
async function loadSupabase() {
  if (!window.supabase) {
    const { createClient } = await import('@supabase/supabase-js');
    window.supabase = createClient(
      process.env.SUPABASE_URL,
      process.env.SUPABASE_ANON_KEY
    );
  }
  return window.supabase;
}
```

### 2. Event Handler Cleanup

```javascript
// ✅ CORRECT
function setupAuthListeners(supabase) {
  const loginForm = document.getElementById('login-form');
  const handleSubmit = async (e) => {
    e.preventDefault();
    // Handle login
  };
  
  const { data: { subscription } } = supabase.auth.onAuthStateChange((event, session) => {
    // Handle auth state change
  });
  
  loginForm.addEventListener('submit', handleSubmit);
  
  // Clean up on page unload
  window.addEventListener('unload', () => {
    subscription.unsubscribe();
    loginForm.removeEventListener('submit', handleSubmit);
  });
}
```

## Best Practices Summary

1. Always use the latest version of Supabase
2. Implement proper error handling with specific error types
3. Use consistent naming conventions
4. Document all functions and types
5. Implement proper cleanup for event listeners and subscriptions
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