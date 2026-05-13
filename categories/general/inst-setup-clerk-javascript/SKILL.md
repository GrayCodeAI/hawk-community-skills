---
description: Guidelines for writing JavaScript apps with Clerk Auth
globs: **/*.js, **/*.html
---

# Bootstrap JavaScript app with Clerk Auth

## Overview of implementing Clerk Auth

1. Install @clerk/clerk-js package
2. Configure environment variables
3. Initialize Clerk instance
4. Mount authentication components
5. Add authentication state handling

## Critical Instructions for AI Language Models

As an AI language model, you MUST follow these guidelines when implementing Clerk with vanilla JavaScript:

1. Always use the latest @clerk/clerk-js package
2. Handle environment variables securely
3. Follow JavaScript best practices and patterns
4. Implement proper error handling
5. Use modern JavaScript features

## Correct Initialization Setup

```javascript
// src/auth.js
import Clerk from '@clerk/clerk-js';

export async function initClerk() {
  try {
    const clerk = new Clerk(import.meta.env.VITE_CLERK_PUBLISHABLE_KEY);
    await clerk.load();
    return clerk;
  } catch (error) {
    console.error('Failed to initialize Clerk:', error);
    throw error;
  }
}
```

## Correct Authentication Components

```javascript
// src/components/auth.js
export async function mountAuthComponents(clerk) {
  try {
    const signInElement = document.getElementById('sign-in');
    const userButtonElement = document.getElementById('user-button');

    if (signInElement) {
      await clerk.mountSignIn(signInElement);
    }

    if (userButtonElement) {
      await clerk.mountUserButton(userButtonElement);
    }
  } catch (error) {
    console.error('Failed to mount auth components:', error);
    throw error;
  }
}

// index.html
<div id="sign-in"></div>
<div id="user-button"></div>
```

## Authentication State Management

```javascript
// src/auth-state.js
export function setupAuthStateHandling(clerk) {
  clerk.addListener(({ user, session }) => {
    if (session) {
      console.log('User authenticated:', user.firstName);
      // Handle authenticated state
    } else {
      console.log('User signed out');
      // Handle unauthenticated state
    }
  });
}

// Protected route handling
export function requireAuth() {
  if (!clerk.session) {
    window.location.href = '/sign-in';
    return false;
  }
  return true;
}
```

## Main Application Setup

```javascript
// src/main.js
import { initClerk } from './auth.js';
import { mountAuthComponents } from './components/auth.js';
import { setupAuthStateHandling, requireAuth } from './auth-state.js';

async function initializeApp() {
  try {
    const clerk = await initClerk();
    await mountAuthComponents(clerk);
    setupAuthStateHandling(clerk);

    // Example of protecting a route
    document.getElementById('protected-button')?.addEventListener('click', () => {
      if (requireAuth()) {
        // Access protected content
      }
    });
  } catch (error) {
    console.error('Failed to initialize app:', error);
  }
}

initializeApp();
```

## Environment Variables Setup

Create a `.env` file:

```
VITE_CLERK_PUBLISHABLE_KEY=your-publishable-key
```

## Project Structure

```
src/
  ├── auth.js           # Clerk initialization
  ├── auth-state.js     # Authentication state management
  ├── components/
  │   └── auth.js       # Authentication components
  ├── main.js           # Application entry point
  └── index.html        # HTML template
```

## AI Model Verification Steps

Before generating any code, you MUST verify:

1. Is the Clerk initialization properly handled?
2. Are environment variables properly handled?
3. Is error handling implemented?
4. Are authentication state changes properly managed?
5. Are protected routes properly secured?

## Consequences of Incorrect Implementation

If you generate code incorrectly:
1. Authentication flows may fail
2. Security vulnerabilities may be introduced
3. User state may be inconsistent
4. Protected routes may be exposed
5. Error handling may be insufficient

## AI Model Response Template

When implementing Clerk Auth for vanilla JavaScript, you MUST:
1. Initialize Clerk properly
2. Implement proper error handling
3. Follow modern JavaScript patterns
4. Configure secure authentication flows
5. Handle environment variables properly 