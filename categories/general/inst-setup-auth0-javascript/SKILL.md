---
description: Guidelines for writing vanilla JavaScript apps with Auth0 Authentication
globs: "**/*.html, **/*.js"
---

# Bootstrap Vanilla JavaScript App with Auth0 Authentication

## Overview of implementing Auth0 Auth in JavaScript

1. Install Auth0 SPA SDK
2. Set up environment variables
3. Initialize Auth0 in your HTML
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
// ✅ ALWAYS USE AUTH0'S BUILT-IN METHODS
const auth0Client = await createAuth0Client({
  domain: 'YOUR_AUTH0_DOMAIN',
  clientId: 'YOUR_CLIENT_ID'
});

// Handle authentication
await auth0Client.loginWithRedirect();
await auth0Client.handleRedirectCallback();

// Get user info
const user = await auth0Client.getUser();
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use the official Auth0 SPA SDK
2. You MUST load Auth0 before accessing any of its features
3. You MUST use environment variables for Auth0 keys
4. You MUST handle loading states properly
5. You MUST use Auth0's built-in methods for auth
6. You MUST implement proper error handling

## CORRECT ENVIRONMENT SETUP

Create a `.env` file:
```env
AUTH0_DOMAIN=your-tenant.auth0.com
AUTH0_CLIENT_ID=your_client_id
```

## CORRECT HTML SETUP

```html
<!DOCTYPE html>
<html>
<head>
  <title>Auth0 Authentication</title>
  <script src="https://cdn.auth0.com/js/auth0-spa-js/2.0/auth0-spa-js.production.js"></script>
</head>
<body>
  <div id="login-container">
    <button id="login" style="display: none;">Log In</button>
    <button id="logout" style="display: none;">Log Out</button>
  </div>
  <div id="profile" style="display: none;">
    <pre></pre>
  </div>

  <script>
    let auth0Client = null;
    
    // Initialize the Auth0 client
    async function initializeAuth0() {
      auth0Client = await createAuth0Client({
        domain: 'YOUR_AUTH0_DOMAIN',
        clientId: 'YOUR_CLIENT_ID',
        authorizationParams: {
          redirect_uri: window.location.origin
        }
      });
      
      // Handle redirect callback
      if (window.location.search.includes("code=")) {
        try {
          await auth0Client.handleRedirectCallback();
          window.history.replaceState({}, document.title, window.location.pathname);
        } catch (error) {
          console.error('Error handling redirect:', error);
        }
      }
      
      updateUI();
    }
    
    // Update UI based on authentication state
    async function updateUI() {
      const isAuthenticated = await auth0Client.isAuthenticated();
      const loginBtn = document.getElementById('login');
      const logoutBtn = document.getElementById('logout');
      const profileDiv = document.getElementById('profile');
      
      if (isAuthenticated) {
        const user = await auth0Client.getUser();
        profileDiv.style.display = 'block';
        profileDiv.querySelector('pre').textContent = JSON.stringify(user, null, 2);
        loginBtn.style.display = 'none';
        logoutBtn.style.display = 'inline-block';
      } else {
        profileDiv.style.display = 'none';
        loginBtn.style.display = 'inline-block';
        logoutBtn.style.display = 'none';
      }
    }
    
    // Initialize when the page loads
    window.addEventListener('load', initializeAuth0);
    
    // Set up event listeners
    document.getElementById('login').addEventListener('click', async () => {
      await auth0Client.loginWithRedirect();
    });
    
    document.getElementById('logout').addEventListener('click', async () => {
      await auth0Client.logout({
        logoutParams: {
          returnTo: window.location.origin
        }
      });
    });
  </script>
</body>
</html>
```

## CORRECT JAVASCRIPT IMPLEMENTATION

```javascript
// auth.js
class Auth0Handler {
  constructor(domain, clientId) {
    this.domain = domain;
    this.clientId = clientId;
    this.client = null;
  }
  
  async initialize() {
    try {
      this.client = await createAuth0Client({
        domain: this.domain,
        clientId: this.clientId,
        authorizationParams: {
          redirect_uri: window.location.origin
        }
      });
      
      // Handle redirect callback
      if (window.location.search.includes("code=")) {
        await this.handleCallback();
      }
      
      return this.client;
    } catch (error) {
      console.error('Error initializing Auth0:', error);
      throw error;
    }
  }
  
  async handleCallback() {
    try {
      await this.client.handleRedirectCallback();
      window.history.replaceState({}, document.title, window.location.pathname);
    } catch (error) {
      console.error('Error handling callback:', error);
      throw error;
    }
  }
  
  async login() {
    await this.client.loginWithRedirect();
  }
  
  async logout() {
    await this.client.logout({
      logoutParams: {
        returnTo: window.location.origin
      }
    });
  }
  
  async getUser() {
    try {
      const user = await this.client.getUser();
      return user;
    } catch (error) {
      console.error('Error getting user:', error);
      throw error;
    }
  }
  
  async isAuthenticated() {
    try {
      return await this.client.isAuthenticated();
    } catch (error) {
      console.error('Error checking authentication:', error);
      throw error;
    }
  }
  
  async getToken() {
    try {
      const token = await this.client.getTokenSilently();
      return token;
    } catch (error) {
      console.error('Error getting token:', error);
      throw error;
    }
  }
}

// Usage
const auth0Handler = new Auth0Handler(
  'YOUR_AUTH0_DOMAIN',
  'YOUR_CLIENT_ID'
);

// Initialize Auth0
auth0Handler.initialize()
  .then(() => {
    console.log('Auth0 initialized');
  })
  .catch(error => {
    console.error('Error initializing Auth0:', error);
  });
```

## CORRECT ERROR HANDLING

```javascript
// error-handling.js
class Auth0Error extends Error {
  constructor(message, code) {
    super(message);
    this.name = 'Auth0Error';
    this.code = code;
  }
}

function handleAuth0Error(error) {
  if (error.error === 'login_required') {
    console.error('User needs to log in');
    // Redirect to login
  } else if (error.error === 'consent_required') {
    console.error('Consent required');
    // Handle consent requirement
  } else {
    console.error('Unexpected error:', error);
    // Handle other errors
  }
}

// Usage with async/await
async function initAuth() {
  try {
    const auth0Client = await createAuth0Client({
      domain: 'YOUR_AUTH0_DOMAIN',
      clientId: 'YOUR_CLIENT_ID'
    });
    
    return auth0Client;
  } catch (error) {
    handleAuth0Error(error);
    throw error;
  }
}
```

## BEST PRACTICES

1. Always initialize Auth0 before accessing any of its features
2. Use async/await or Promises to handle Auth0 initialization properly
3. Implement proper error handling for all Auth0 operations
4. Use Auth0's built-in methods instead of creating custom ones
5. Handle loading states to prevent flashing of incorrect content
6. Protect sensitive routes and content based on authentication state
7. Use environment variables for Auth0 configuration
8. Never store sensitive auth data in localStorage or cookies
9. Always handle auth state changes using Auth0's methods
10. Keep the Auth0 SDK up to date for security patches and new features 