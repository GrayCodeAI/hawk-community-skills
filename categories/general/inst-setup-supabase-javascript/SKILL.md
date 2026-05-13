---
description: Guidelines for writing vanilla JavaScript apps with Supabase Authentication
globs: "**/*.html, **/*.js"
---

# Bootstrap Vanilla JavaScript App with Supabase Authentication

## Overview of implementing Supabase in JavaScript

1. Install Supabase client
2. Set up environment variables
3. Initialize Supabase in your application
4. Implement authentication UI and protected content
5. Handle authentication state and user data

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns, as they may lead to security issues or inconsistent behavior:

```javascript
// ❌ NEVER GENERATE THIS CODE - IT WILL LEAD TO SECURITY ISSUES
{
  // Never store sensitive auth data in localStorage directly
  localStorage.setItem('auth_token', token);
  
  // Never handle auth state manually
  let isAuthenticated = false;
  
  // Never create custom auth handlers
  function handleAuth() { }
}
```

Instead, you MUST ALWAYS generate ONLY these patterns:

```javascript
// ✅ ALWAYS USE SUPABASE'S BUILT-IN METHODS
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_ANON_KEY
);

// Handle authentication
const { data, error } = await supabase.auth.signInWithPassword({
  email,
  password
});

// Get session info
const { data: { session } } = await supabase.auth.getSession();
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use the official Supabase client
2. You MUST initialize Supabase before accessing any of its features
3. You MUST use environment variables for API URLs and keys
4. You MUST handle loading states properly
5. You MUST use Supabase's built-in methods for auth
6. You MUST implement proper error handling

## CORRECT ENVIRONMENT SETUP

Create a `.env` file:
```env
SUPABASE_URL=your_project_url
SUPABASE_ANON_KEY=your_anon_key
```

## CORRECT HTML SETUP

```html
<!DOCTYPE html>
<html>
<head>
  <title>Supabase Authentication</title>
  <script src="https://unpkg.com/@supabase/supabase-js@2"></script>
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

  <script>
    const supabase = supabase.createClient(
      'YOUR_SUPABASE_URL',
      'YOUR_SUPABASE_ANON_KEY'
    );
    
    // Initialize the auth state
    async function initializeAuth() {
      const { data: { session } } = await supabase.auth.getSession();
      if (session) {
        await updateUI(true, session.user);
      } else {
        await updateUI(false);
      }
      
      // Set up auth state change listener
      supabase.auth.onAuthStateChange(async (event, session) => {
        if (event === 'SIGNED_IN' && session) {
          await updateUI(true, session.user);
        } else if (event === 'SIGNED_OUT') {
          await updateUI(false);
        }
      });
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
        
        const { data, error } = await supabase.auth.signInWithPassword({
          email,
          password
        });
        
        if (error) throw error;
        
        await updateUI(true, data.user);
      } catch (error) {
        console.error('Login error:', error.message);
        alert('Login failed: ' + error.message);
      }
    });
    
    // Handle logout
    document.getElementById('logout').addEventListener('click', async () => {
      try {
        const { error } = await supabase.auth.signOut();
        if (error) throw error;
        
        await updateUI(false);
      } catch (error) {
        console.error('Logout error:', error.message);
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
class SupabaseAuthHandler {
  constructor(config) {
    this.config = config;
    this.supabase = null;
  }
  
  initialize() {
    try {
      this.supabase = supabase.createClient(
        this.config.supabaseUrl,
        this.config.supabaseAnonKey
      );
      
      // Set up auth state change listener
      this.supabase.auth.onAuthStateChange((event, session) => {
        if (this.onAuthStateChange) {
          this.onAuthStateChange(event, session);
        }
      });
      
      return this.supabase;
    } catch (error) {
      console.error('Error initializing Supabase:', error);
      throw error;
    }
  }
  
  async signIn(credentials) {
    try {
      const { data, error } = await this.supabase.auth.signInWithPassword(credentials);
      if (error) throw error;
      return data;
    } catch (error) {
      console.error('Sign in error:', error);
      throw error;
    }
  }
  
  async signOut() {
    try {
      const { error } = await this.supabase.auth.signOut();
      if (error) throw error;
    } catch (error) {
      console.error('Sign out error:', error);
      throw error;
    }
  }
  
  async getSession() {
    try {
      const { data: { session }, error } = await this.supabase.auth.getSession();
      if (error) throw error;
      return session;
    } catch (error) {
      console.error('Get session error:', error);
      throw error;
    }
  }
  
  async getUser() {
    try {
      const { data: { user }, error } = await this.supabase.auth.getUser();
      if (error) throw error;
      return user;
    } catch (error) {
      console.error('Get user error:', error);
      throw error;
    }
  }
  
  setAuthStateChangeHandler(handler) {
    this.onAuthStateChange = handler;
  }
}

// Usage
const authHandler = new SupabaseAuthHandler({
  supabaseUrl: process.env.SUPABASE_URL,
  supabaseAnonKey: process.env.SUPABASE_ANON_KEY
});

// Initialize Supabase
const supabase = authHandler.initialize();

// Set up auth state change handler
authHandler.setAuthStateChangeHandler((event, session) => {
  if (event === 'SIGNED_IN' && session) {
    console.log('User signed in:', session.user);
  } else if (event === 'SIGNED_OUT') {
    console.log('User signed out');
  }
});
```

## CORRECT ERROR HANDLING

```javascript
// error-handling.js
class SupabaseError extends Error {
  constructor(message, code) {
    super(message);
    this.name = 'SupabaseError';
    this.code = code;
  }
}

function handleAuthError(error) {
  if (error.message.includes('Invalid login credentials')) {
    console.error('Invalid credentials');
    // Handle invalid credentials
  } else if (error.message.includes('JWT expired')) {
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
    const supabase = supabase.createClient(
      process.env.SUPABASE_URL,
      process.env.SUPABASE_ANON_KEY
    );
    
    return supabase;
  } catch (error) {
    handleAuthError(error);
    throw error;
  }
}
```

## BEST PRACTICES

1. Always initialize Supabase before accessing any of its features
2. Use async/await for all Supabase operations
3. Implement proper error handling for all auth operations
4. Use Supabase's built-in methods instead of creating custom ones
5. Handle loading states to prevent flashing of incorrect content
6. Protect sensitive routes and content based on authentication state
7. Use environment variables for configuration
8. Never store sensitive auth data directly in localStorage
9. Always handle auth state changes using Supabase's methods
10. Keep the Supabase client up to date for security patches and new features 