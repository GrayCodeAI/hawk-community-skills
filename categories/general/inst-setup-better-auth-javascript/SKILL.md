---
description: Guidelines for writing vanilla JavaScript apps with Better Auth Authentication
globs: "**/*.html, **/*.js"
---

# Bootstrap Vanilla JavaScript App with Better Auth Authentication

## Overview of implementing Better Auth in JavaScript

1. Install Better Auth client
2. Set up environment variables
3. Initialize Better Auth in your application
4. Implement authentication UI and protected content
5. Handle authentication state and user data

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns, as they may lead to security issues or inconsistent behavior:

```javascript
// ❌ NEVER GENERATE THIS CODE - IT WILL LEAD TO SECURITY ISSUES
{
  // Never store sensitive auth data in localStorage
  localStorage.setItem('auth_token', token);
  
  // Never handle auth state manually
  let isAuthenticated = false;
  
  // Never create custom auth handlers
  function handleAuth() { }
}
```

Instead, you MUST ALWAYS generate ONLY these patterns:

```javascript
// ✅ ALWAYS USE BETTER AUTH'S BUILT-IN METHODS
import { createAuthClient } from 'better-auth';

const auth = createAuthClient({
  baseUrl: process.env.AUTH_API_URL
});

// Handle authentication
await auth.signIn({ email, password });
await auth.signOut();

// Get session info
const session = await auth.getSession();
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use the official Better Auth client
2. You MUST initialize Better Auth before accessing any of its features
3. You MUST use environment variables for API URLs and keys
4. You MUST handle loading states properly
5. You MUST use Better Auth's built-in methods for auth
6. You MUST implement proper error handling

## CORRECT ENVIRONMENT SETUP

Create a `.env` file:
```env
AUTH_API_URL=http://your-api-url/auth
AUTH_PUBLIC_KEY=your_public_key
```

## CORRECT HTML SETUP

```html
<!DOCTYPE html>
<html>
<head>
  <title>Better Auth Authentication</title>
  <script type="module">
    import { createAuthClient } from 'better-auth';
  </script>
</head>
<body>
  <div id="auth-container">
    <form id="login-form" style="display: none;">
      <input type="email" id="email" placeholder="Email" required>
      <input type="password" id="password" placeholder="Password" required>
      <button type="submit">Log In</button>
    </form>
    <button id="logout" style="display: none;">Log Out</button>
  </div>
  <div id="profile" style="display: none;">
    <pre></pre>
  </div>

  <script type="module">
    import { createAuthClient } from 'better-auth';
    
    let auth = null;
    
    // Initialize the Better Auth client
    async function initializeAuth() {
      auth = createAuthClient({
        baseUrl: process.env.AUTH_API_URL
      });
      
      // Check for existing session
      const session = await auth.getSession();
      if (session) {
        await updateUI(true, session.user);
      } else {
        await updateUI(false);
      }
    }
    
    // Update UI based on authentication state
    async function updateUI(isAuthenticated, user = null) {
      const loginForm = document.getElementById('login-form');
      const logoutBtn = document.getElementById('logout');
      const profileDiv = document.getElementById('profile');
      
      if (isAuthenticated && user) {
        loginForm.style.display = 'none';
        logoutBtn.style.display = 'block';
        profileDiv.style.display = 'block';
        profileDiv.querySelector('pre').textContent = JSON.stringify(user, null, 2);
      } else {
        loginForm.style.display = 'block';
        logoutBtn.style.display = 'none';
        profileDiv.style.display = 'none';
      }
    }
    
    // Handle form submission
    document.getElementById('login-form').addEventListener('submit', async (e) => {
      e.preventDefault();
      
      try {
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        
        const { user } = await auth.signIn({ email, password });
        await updateUI(true, user);
      } catch (error) {
        console.error('Login error:', error);
        alert('Login failed: ' + error.message);
      }
    });
    
    // Handle logout
    document.getElementById('logout').addEventListener('click', async () => {
      try {
        await auth.signOut();
        await updateUI(false);
      } catch (error) {
        console.error('Logout error:', error);
        alert('Logout failed: ' + error.message);
      }
    });
    
    // Initialize when the page loads
    window.addEventListener('load', initializeAuth);
  </script>
</body>
</html>
```

## CORRECT JAVASCRIPT IMPLEMENTATION

```javascript
// auth.js
class BetterAuthHandler {
  constructor(config) {
    this.config = config;
    this.auth = null;
  }
  
  async initialize() {
    try {
      const { createAuthClient } = await import('better-auth');
      this.auth = createAuthClient(this.config);
      return this.auth;
    } catch (error) {
      console.error('Error initializing Better Auth:', error);
      throw error;
    }
  }
  
  async signIn(credentials) {
    try {
      const { user } = await this.auth.signIn(credentials);
      return user;
    } catch (error) {
      console.error('Sign in error:', error);
      throw error;
    }
  }
  
  async signOut() {
    try {
      await this.auth.signOut();
    } catch (error) {
      console.error('Sign out error:', error);
      throw error;
    }
  }
  
  async getSession() {
    try {
      const session = await this.auth.getSession();
      return session;
    } catch (error) {
      console.error('Get session error:', error);
      throw error;
    }
  }
  
  async getUser() {
    try {
      const session = await this.getSession();
      return session?.user || null;
    } catch (error) {
      console.error('Get user error:', error);
      throw error;
    }
  }
  
  async fetchWithAuth(url, options = {}) {
    try {
      const response = await this.auth.fetch(url, options);
      return response;
    } catch (error) {
      console.error('Fetch error:', error);
      throw error;
    }
  }
}

// Usage
const authHandler = new BetterAuthHandler({
  baseUrl: process.env.AUTH_API_URL
});

// Initialize Better Auth
authHandler.initialize()
  .then(() => {
    console.log('Better Auth initialized');
  })
  .catch(error => {
    console.error('Error initializing Better Auth:', error);
  });
```

## CORRECT ERROR HANDLING

```javascript
// error-handling.js
class AuthError extends Error {
  constructor(message, code) {
    super(message);
    this.name = 'AuthError';
    this.code = code;
  }
}

function handleAuthError(error) {
  if (error.code === 'invalid_credentials') {
    console.error('Invalid credentials');
    // Handle invalid credentials
  } else if (error.code === 'session_expired') {
    console.error('Session expired');
    // Handle expired session
  } else {
    console.error('Unexpected error:', error);
    // Handle other errors
  }
}

// Usage with async/await
async function initAuth() {
  try {
    const { createAuthClient } = await import('better-auth');
    const auth = createAuthClient({
      baseUrl: process.env.AUTH_API_URL
    });
    
    return auth;
  } catch (error) {
    handleAuthError(error);
    throw error;
  }
}
```

## BEST PRACTICES

1. Always initialize Better Auth before accessing any of its features
2. Use async/await or Promises to handle Better Auth initialization properly
3. Implement proper error handling for all auth operations
4. Use Better Auth's built-in methods instead of creating custom ones
5. Handle loading states to prevent flashing of incorrect content
6. Protect sensitive routes and content based on authentication state
7. Use environment variables for configuration
8. Never store sensitive auth data in localStorage or cookies
9. Always handle auth state changes using Better Auth's methods
10. Keep the Better Auth client up to date for security patches and new features 