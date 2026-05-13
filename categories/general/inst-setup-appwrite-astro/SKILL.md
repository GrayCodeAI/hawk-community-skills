---
description: Guidelines for writing Astro apps with Appwrite
globs: src/**/*.ts, src/**/*.astro
---

# Appwrite + Astro Integration Setup Guide

## Prerequisites
- Node.js and npm installed
- Astro project initialized
- Appwrite account and project created

## Installation

Install required dependencies:
```bash
npm install appwrite node-appwrite
npm install @astrojs/node
```

Add Node adapter to Astro:
```bash
npx astro add node
```

## Core Configuration

Create Appwrite client configuration (src/lib/appwrite.ts):
```typescript
import { Client, Account, Databases, Storage } from 'appwrite';

const client = new Client()
  .setEndpoint(import.meta.env.PUBLIC_APPWRITE_ENDPOINT || 'https://cloud.appwrite.io/v1')
  .setProject(import.meta.env.PUBLIC_APPWRITE_PROJECT_ID || '');

export const account = new Account(client);
export const databases = new Databases(client);
export const storage = new Storage(client);
export default client;
```

## Authentication Implementation

Create middleware for session handling (src/middleware.ts):
```typescript
import { defineMiddleware } from 'astro:middleware';
import { account } from './lib/appwrite';

export const onRequest = defineMiddleware(async ({ locals, cookies }, next) => {
  const sessionId = cookies.get('sessionId')?.value;
  
  if (sessionId) {
    try {
      const user = await account.get();
      locals.user = user;
    } catch (error) {
      cookies.delete('sessionId');
      locals.user = null;
    }
  }
  
  return next();
});
```

## Route Implementation Examples

Login Page (src/pages/login.astro):
```astro
---
import Layout from '../layouts/Layout.astro';
import { account } from '../lib/appwrite';

let error = null;

if (Astro.request.method === 'POST') {
  try {
    const data = await Astro.request.formData();
    const email = data.get('email')?.toString();
    const password = data.get('password')?.toString();

    if (email && password) {
      const session = await account.createEmailSession(email, password);
      Astro.cookies.set('sessionId', session.$id, {
        httpOnly: true,
        secure: import.meta.env.PROD,
        sameSite: 'lax',
        path: '/'
      });
      return Astro.redirect('/dashboard');
    }
  } catch (e) {
    error = 'Invalid credentials';
  }
}
---

<Layout title="Login">
  <main>
    <form method="POST">
      <div>
        <label for="email">Email</label>
        <input type="email" id="email" name="email" required />
      </div>
      <div>
        <label for="password">Password</label>
        <input type="password" id="password" name="password" required />
      </div>
      {error && <div class="error">{error}</div>}
      <button type="submit">Login</button>
    </form>
  </main>
</Layout>
```

Protected Dashboard Page (src/pages/dashboard.astro):
```astro
---
import Layout from '../layouts/Layout.astro';
import { databases } from '../lib/appwrite';

if (!Astro.locals.user) {
  return Astro.redirect('/login');
}

let documents = [];
try {
  const response = await databases.listDocuments(
    'DATABASE_ID',
    'COLLECTION_ID',
    []
  );
  documents = response.documents;
} catch (error) {
  console.error('Failed to fetch documents:', error);
}
---

<Layout title="Dashboard">
  <main>
    <h1>Welcome, {Astro.locals.user.name}</h1>
    <div class="documents">
      {documents.map(doc => (
        <div class="document" key={doc.$id}>
          <h2>{doc.title}</h2>
          <p>{doc.content}</p>
        </div>
      ))}
    </div>
  </main>
</Layout>
```

## Security Guidelines

1. Store sensitive configuration in environment variables
2. Implement proper session management using secure cookies
3. Set appropriate collection permissions in Appwrite Console
4. Use API keys with minimal required scopes
5. Enable HTTPS for production deployments

## Implementation Guidelines

1. Use server-side authentication with secure cookies
2. Implement proper error handling and validation
3. Create type definitions for Appwrite responses
4. Keep Appwrite client configuration in server-only files
5. Handle loading and error states consistently
6. Use Astro's built-in form handling

## Error Handling Example

Create an error component (src/components/ErrorBoundary.astro):
```astro
---
const { error } = Astro.props;
---

<div class="error-boundary">
  <h1>Error</h1>
  <p>{error.message}</p>
  <a href="/">Return Home</a>
</div>

<style>
  .error-boundary {
    padding: 2rem;
    text-align: center;
  }
</style>
``` 