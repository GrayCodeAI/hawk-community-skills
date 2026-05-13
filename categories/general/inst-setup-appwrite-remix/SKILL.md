---
description: Guidelines for writing Remix apps with Appwrite
globs: app/**/*.ts, app/**/*.tsx
---

# Appwrite + Remix Integration Setup Guide

## Prerequisites
- Node.js and npm installed
- Remix project initialized
- Appwrite account and project created

## Installation

Install the Appwrite SDK:
```bash
npm install appwrite
```

## Core Configuration

Create Appwrite client configuration (app/lib/appwrite.server.ts):
```typescript
import { Client, Account, Databases, Storage } from 'appwrite';

const client = new Client();

client
  .setEndpoint(process.env.APPWRITE_ENDPOINT || 'https://cloud.appwrite.io/v1')
  .setProject(process.env.APPWRITE_PROJECT_ID || '');

export const account = new Account(client);
export const databases = new Databases(client);
export const storage = new Storage(client);
export default client;
```

## Authentication Implementation

Create an auth utility (app/utils/auth.server.ts):
```typescript
import { account } from '~/lib/appwrite.server';
import { createCookieSessionStorage, redirect } from '@remix-run/node';

const sessionStorage = createCookieSessionStorage({
  cookie: {
    name: 'appwrite_session',
    secure: process.env.NODE_ENV === 'production',
    secrets: [process.env.SESSION_SECRET || 'default-secret'],
    sameSite: 'lax',
    path: '/',
    maxAge: 60 * 60 * 24 * 30,
    httpOnly: true,
  },
});

export async function createUserSession(sessionData: any, redirectTo: string) {
  const session = await sessionStorage.getSession();
  session.set('user', sessionData);
  
  return redirect(redirectTo, {
    headers: {
      'Set-Cookie': await sessionStorage.commitSession(session),
    },
  });
}

export async function getUserSession(request: Request) {
  const session = await sessionStorage.getSession(request.headers.get('Cookie'));
  return session.get('user');
}

export async function requireUser(request: Request) {
  const user = await getUserSession(request);
  if (!user) {
    throw redirect('/login');
  }
  return user;
}

export async function logout(request: Request) {
  const session = await sessionStorage.getSession(request.headers.get('Cookie'));
  return redirect('/login', {
    headers: {
      'Set-Cookie': await sessionStorage.destroySession(session),
    },
  });
}
```

## Route Implementation Examples

Login Route (app/routes/login.tsx):
```typescript
import { json, redirect } from '@remix-run/node';
import { useActionData, Form } from '@remix-run/react';
import { account } from '~/lib/appwrite.server';
import { createUserSession } from '~/utils/auth.server';

export async function action({ request }) {
  const formData = await request.formData();
  const email = formData.get('email');
  const password = formData.get('password');

  try {
    const session = await account.createEmailSession(email, password);
    const user = await account.get();
    return createUserSession(user, '/dashboard');
  } catch (error) {
    return json({ error: 'Invalid credentials' }, { status: 400 });
  }
}

export default function Login() {
  const actionData = useActionData();

  return (
    <div>
      <Form method="post">
        <div>
          <label>Email</label>
          <input type="email" name="email" required />
        </div>
        <div>
          <label>Password</label>
          <input type="password" name="password" required />
        </div>
        {actionData?.error && <div>{actionData.error}</div>}
        <button type="submit">Login</button>
      </Form>
    </div>
  );
}
```

Protected Route Example (app/routes/dashboard.tsx):
```typescript
import { json } from '@remix-run/node';
import { useLoaderData } from '@remix-run/react';
import { requireUser } from '~/utils/auth.server';
import { databases } from '~/lib/appwrite.server';

export async function loader({ request }) {
  const user = await requireUser(request);
  
  try {
    const data = await databases.listDocuments(
      'DATABASE_ID',
      'COLLECTION_ID',
      []
    );
    
    return json({ user, data: data.documents });
  } catch (error) {
    throw new Error('Failed to load data');
  }
}

export default function Dashboard() {
  const { user, data } = useLoaderData();
  
  return (
    <div>
      <h1>Welcome, {user.name}</h1>
      <div>
        {data.map(item => (
          <div key={item.$id}>{item.title}</div>
        ))}
      </div>
    </div>
  );
}
```

## Security Guidelines

1. Store sensitive configuration in environment variables
2. Implement proper session management using Remix session storage
3. Set appropriate collection permissions in Appwrite Console
4. Use API keys with minimal required scopes
5. Enable HTTPS for production deployments

## Implementation Guidelines

1. Use server-side authentication with session cookies
2. Implement proper error boundaries for error handling
3. Create type definitions for Appwrite responses
4. Separate Appwrite client configuration into server-only files
5. Handle loading and error states consistently
6. Use Remix Form component for better progressive enhancement

## Error Handling Example

Create an error boundary (app/root.tsx):
```typescript
import { ErrorBoundary } from '@remix-run/react';

export function ErrorBoundary({ error }) {
  return (
    <div>
      <h1>Error</h1>
      <p>{error.message}</p>
    </div>
  );
}
``` 