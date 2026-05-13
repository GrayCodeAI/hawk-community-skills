---
description: Guidelines for adding features to vanilla JavaScript apps with Clerk Authentication
globs: "**/*.html, **/*.js"
---

# Adding Features to Vanilla JavaScript App with Clerk Authentication

## Overview of Clerk Features in JavaScript

1. User Authentication
2. Session Management
3. User Profile Management
4. Multi-Factor Authentication (MFA)
5. Social Login Providers
6. Organization Management
7. Webhooks Integration

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
// ✅ ALWAYS USE CLERK'S BUILT-IN METHODS
// User authentication
clerk.signIn.create({
  identifier: email,
  password: password
});

// Social login
clerk.authenticate('oauth_google');

// MFA
clerk.signIn.authenticateWithFactor({
  strategy: 'phone_code',
  code: '123456'
});

// User profile
clerk.user.update({
  firstName: 'John',
  lastName: 'Doe'
});

// Organization management
clerk.organization.create({
  name: 'My Organization'
});
```

## FEATURE IMPLEMENTATION GUIDE

### 1. User Authentication

```javascript
// Sign in with email/password
async function signInWithEmailPassword(email, password) {
  try {
    const signIn = await clerk.signIn.create({
      identifier: email,
      password: password
    });
    
    await signIn.createdSessionId;
  } catch (error) {
    handleClerkError(error);
  }
}

// Sign up new user
async function signUpNewUser(email, password, firstName, lastName) {
  try {
    const signUp = await clerk.signUp.create({
      emailAddress: email,
      password: password,
      firstName: firstName,
      lastName: lastName
    });
    
    await signUp.createdSessionId;
  } catch (error) {
    handleClerkError(error);
  }
}
```

### 2. Social Login Integration

```javascript
// Initialize social login buttons
function initializeSocialLogin() {
  const googleButton = document.getElementById('google-login');
  const githubButton = document.getElementById('github-login');
  
  googleButton?.addEventListener('click', () => {
    clerk.authenticate('oauth_google');
  });
  
  githubButton?.addEventListener('click', () => {
    clerk.authenticate('oauth_github');
  });
}
```

### 3. Multi-Factor Authentication

```javascript
// Enable MFA for user
async function enableMFA() {
  try {
    // Start MFA enrollment
    const factor = await clerk.user.createFactor({
      strategy: 'phone_code',
      phoneNumber: '+1234567890'
    });
    
    // Verify the factor
    await factor.verify({
      code: '123456'
    });
  } catch (error) {
    handleClerkError(error);
  }
}

// Authenticate with MFA
async function authenticateWithMFA(code) {
  try {
    await clerk.signIn.authenticateWithFactor({
      strategy: 'phone_code',
      code: code
    });
  } catch (error) {
    handleClerkError(error);
  }
}
```

### 4. User Profile Management

```javascript
// Update user profile
async function updateUserProfile(data) {
  try {
    await clerk.user.update(data);
  } catch (error) {
    handleClerkError(error);
  }
}

// Upload profile image
async function uploadProfileImage(file) {
  try {
    await clerk.user.setProfileImage({
      file: file
    });
  } catch (error) {
    handleClerkError(error);
  }
}
```

### 5. Organization Management

```javascript
// Create organization
async function createOrganization(name) {
  try {
    const organization = await clerk.organization.create({
      name: name
    });
    return organization;
  } catch (error) {
    handleClerkError(error);
  }
}

// Invite members
async function inviteMember(organizationId, email, role) {
  try {
    await clerk.organization.inviteMember({
      organizationId: organizationId,
      emailAddress: email,
      role: role
    });
  } catch (error) {
    handleClerkError(error);
  }
}
```

### 6. Session Management

```javascript
// Handle session changes
function initializeSessionHandling() {
  clerk.addListener(({ session }) => {
    if (session) {
      // Session is active
      console.log('Active session:', session.id);
    } else {
      // No active session
      console.log('No active session');
    }
  });
}

// Get session token
async function getSessionToken() {
  try {
    const token = await clerk.session.getToken();
    return token;
  } catch (error) {
    handleClerkError(error);
  }
}
```

### 7. Webhook Integration

```javascript
// Backend endpoint to handle Clerk webhooks
async function handleWebhook(request) {
  const WEBHOOK_SECRET = process.env.CLERK_WEBHOOK_SECRET;
  
  try {
    const payload = await verifyWebhookSignature(
      request,
      WEBHOOK_SECRET
    );
    
    switch (payload.type) {
      case 'user.created':
        // Handle user creation
        break;
      case 'user.updated':
        // Handle user update
        break;
      case 'session.created':
        // Handle new session
        break;
      // Handle other webhook events
    }
  } catch (error) {
    console.error('Webhook error:', error);
  }
}
```

## BEST PRACTICES

1. Always use Clerk's built-in methods for authentication operations
2. Implement proper error handling for all feature operations
3. Use async/await for cleaner asynchronous code
4. Handle loading states during async operations
5. Implement proper session token management
6. Use Clerk's webhook system for backend synchronization
7. Implement proper role-based access control
8. Keep the Clerk SDK updated for new features and security patches
9. Use environment variables for sensitive configuration
10. Implement proper error messages and user feedback
11. Test all authentication flows thoroughly
12. Implement proper logout handling
13. Use Clerk's built-in UI components when possible
14. Implement proper redirect handling after authentication
15. Use proper security headers in your application 