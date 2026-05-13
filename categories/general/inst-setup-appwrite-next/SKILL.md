---
description: Guidelines for writing Next.js 14 apps with Appwrite
globs: src/**/*.ts, src/**/*.tsx
---

# Appwrite + Next.js 14 Integration Setup Guide

## Prerequisites
- Node.js and npm installed
- Next.js 14 project initialized
- Appwrite account and project created

## Installation

Install required dependencies:
```bash
npm install appwrite
```

## Core Configuration

Create Appwrite client configuration (src/lib/appwrite.ts):
```typescript
import { Client, Account, Databases, Storage, ID } from 'appwrite';

const client = new Client()
  .setEndpoint(process.env.NEXT_PUBLIC_APPWRITE_ENDPOINT || 'https://cloud.appwrite.io/v1')
  .setProject(process.env.NEXT_PUBLIC_APPWRITE_PROJECT_ID || '');

export const account = new Account(client);
export const databases = new Databases(client);
export const storage = new Storage(client);
export { ID };
export default client;
```

## Authentication Implementation

Create authentication service (src/services/auth.ts):
```typescript
import { account, ID } from '@/lib/appwrite';

export const AuthService = {
  async register(email: string, password: string, name: string) {
    try {
      await account.create(ID.unique(), email, password, name);
      return this.login(email, password);
    } catch (error) {
      console.error('Registration error:', error);
      throw error;
    }
  },

  async login(email: string, password: string) {
    try {
      const session = await account.createEmailSession(email, password);
      const user = await account.get();
      return { session, user };
    } catch (error) {
      console.error('Login error:', error);
      throw error;
    }
  },

  async getCurrentUser() {
    try {
      return await account.get();
    } catch (error) {
      console.error('Get user error:', error);
      return null;
    }
  },

  async logout() {
    try {
      await account.deleteSession('current');
    } catch (error) {
      console.error('Logout error:', error);
      throw error;
    }
  }
};
```

Create authentication API routes (src/app/api/auth/[...route]/route.ts):
```typescript
import { AuthService } from '@/services/auth';
import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const { email, password, name, action } = await request.json();

    switch (action) {
      case 'login':
        const loginResult = await AuthService.login(email, password);
        return NextResponse.json(loginResult);

      case 'register':
        const registerResult = await AuthService.register(email, password, name);
        return NextResponse.json(registerResult);

      case 'logout':
        await AuthService.logout();
        return NextResponse.json({ success: true });

      default:
        return NextResponse.json(
          { error: 'Invalid action' },
          { status: 400 }
        );
    }
  } catch (error: any) {
    return NextResponse.json(
      { error: error.message },
      { status: 400 }
    );
  }
}

export async function GET() {
  try {
    const user = await AuthService.getCurrentUser();
    return NextResponse.json({ user });
  } catch (error: any) {
    return NextResponse.json(
      { error: error.message },
      { status: 400 }
    );
  }
}
```

## Database Implementation

Create database service (src/services/database.ts):
```typescript
import { databases, ID } from '@/lib/appwrite';
import { Query } from 'appwrite';

export const DatabaseService = {
  async listDocuments(databaseId: string, collectionId: string, queries: any[] = []) {
    try {
      return await databases.listDocuments(
        databaseId,
        collectionId,
        [
          Query.limit(20),
          Query.orderDesc('$createdAt'),
          ...queries,
        ]
      );
    } catch (error) {
      console.error('List documents error:', error);
      throw error;
    }
  },

  async getDocument(databaseId: string, collectionId: string, documentId: string) {
    try {
      return await databases.getDocument(
        databaseId,
        collectionId,
        documentId
      );
    } catch (error) {
      console.error('Get document error:', error);
      throw error;
    }
  },

  async createDocument(databaseId: string, collectionId: string, data: any) {
    try {
      return await databases.createDocument(
        databaseId,
        collectionId,
        ID.unique(),
        data
      );
    } catch (error) {
      console.error('Create document error:', error);
      throw error;
    }
  },

  async updateDocument(databaseId: string, collectionId: string, documentId: string, data: any) {
    try {
      return await databases.updateDocument(
        databaseId,
        collectionId,
        documentId,
        data
      );
    } catch (error) {
      console.error('Update document error:', error);
      throw error;
    }
  },

  async deleteDocument(databaseId: string, collectionId: string, documentId: string) {
    try {
      await databases.deleteDocument(
        databaseId,
        collectionId,
        documentId
      );
    } catch (error) {
      console.error('Delete document error:', error);
      throw error;
    }
  }
};
```

## Usage Examples

Authentication Component (src/components/Auth.tsx):
```typescript
'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';

export default function Auth() {
  const router = useRouter();
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const [isRegistering, setIsRegistering] = useState(false);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setIsLoading(true);
    setError('');

    const formData = new FormData(e.currentTarget);
    const email = formData.get('email') as string;
    const password = formData.get('password') as string;
    const name = formData.get('name') as string;

    try {
      const response = await fetch('/api/auth/route', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email,
          password,
          name,
          action: isRegistering ? 'register' : 'login',
        }),
      });

      if (!response.ok) {
        const data = await response.json();
        throw new Error(data.error);
      }

      router.push('/dashboard');
    } catch (err: any) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="auth-container">
      <h1>{isRegistering ? 'Register' : 'Login'}</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="email">Email</label>
          <input
            id="email"
            name="email"
            type="email"
            required
          />
        </div>
        <div>
          <label htmlFor="password">Password</label>
          <input
            id="password"
            name="password"
            type="password"
            required
          />
        </div>
        {isRegistering && (
          <div>
            <label htmlFor="name">Name</label>
            <input
              id="name"
              name="name"
              type="text"
              required
            />
          </div>
        )}
        {error && <div className="error">{error}</div>}
        <button type="submit" disabled={isLoading}>
          {isLoading ? 'Loading...' : (isRegistering ? 'Register' : 'Login')}
        </button>
        <button
          type="button"
          onClick={() => setIsRegistering(!isRegistering)}
        >
          {isRegistering ? 'Switch to Login' : 'Switch to Register'}
        </button>
      </form>
    </div>
  );
}
```

Document List Component (src/components/DocumentList.tsx):
```typescript
'use client';

import { useEffect, useState } from 'react';
import { DatabaseService } from '@/services/database';

interface Document {
  $id: string;
  title: string;
  content: string;
}

export default function DocumentList({
  databaseId,
  collectionId,
}: {
  databaseId: string;
  collectionId: string;
}) {
  const [documents, setDocuments] = useState<Document[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    loadDocuments();
  }, []);

  const loadDocuments = async () => {
    try {
      const response = await DatabaseService.listDocuments(databaseId, collectionId);
      setDocuments(response.documents);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleCreate = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    const title = formData.get('title') as string;
    const content = formData.get('content') as string;

    try {
      const newDoc = await DatabaseService.createDocument(databaseId, collectionId, {
        title,
        content,
      });
      setDocuments([newDoc, ...documents]);
      (e.target as HTMLFormElement).reset();
    } catch (err: any) {
      setError(err.message);
    }
  };

  const handleDelete = async (documentId: string) => {
    try {
      await DatabaseService.deleteDocument(databaseId, collectionId, documentId);
      setDocuments(documents.filter(doc => doc.$id !== documentId));
    } catch (err: any) {
      setError(err.message);
    }
  };

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="documents-container">
      <form onSubmit={handleCreate}>
        <div>
          <label htmlFor="title">Title</label>
          <input id="title" name="title" required />
        </div>
        <div>
          <label htmlFor="content">Content</label>
          <textarea id="content" name="content" required />
        </div>
        <button type="submit">Create Document</button>
      </form>

      <div className="documents-list">
        {documents.map(doc => (
          <div key={doc.$id} className="document-item">
            <h3>{doc.title}</h3>
            <p>{doc.content}</p>
            <button onClick={() => handleDelete(doc.$id)}>Delete</button>
          </div>
        ))}
      </div>
    </div>
  );
}
```

## Security Guidelines

1. Store sensitive configuration in environment variables
2. Implement proper error handling for all operations
3. Set appropriate collection permissions in Appwrite Console
4. Use API keys with minimal required scopes
5. Enable HTTPS for production deployments

## Implementation Guidelines

1. Use server components for initial data fetching
2. Implement proper error handling and loading states
3. Use TypeScript for better type safety
4. Keep Appwrite configuration in server-only files
5. Handle loading and error states consistently
6. Use Next.js API routes for authentication

## Error Handling Example

Create error utility (src/utils/error.ts):
```typescript
export class AppwriteError extends Error {
  constructor(message: string, public originalError: any) {
    super(message);
    this.name = 'AppwriteError';
  }
}

export function handleError(error: any, customMessage = 'Operation failed') {
  console.error(customMessage, error);
  
  if (error.response) {
    throw new AppwriteError(
      `${customMessage}: ${error.response.message}`,
      error
    );
  }
  
  throw new AppwriteError(customMessage, error);
} 