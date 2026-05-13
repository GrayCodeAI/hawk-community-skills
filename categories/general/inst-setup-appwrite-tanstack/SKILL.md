---
description: Guidelines for writing React apps with Appwrite and TanStack Query
globs: src/**/*.ts, src/**/*.tsx
---

# Appwrite + TanStack Query Integration Setup Guide

## Prerequisites
- Node.js and npm installed
- React project initialized
- Appwrite account and project created

## Installation

Install required dependencies:
```bash
npm install @tanstack/react-query appwrite
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

## Query Client Setup

Create query client configuration (src/lib/query-client.ts):
```typescript
import { QueryClient } from '@tanstack/react-query';

export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 60 * 5, // 5 minutes
      retry: 1,
    },
  },
});
```

## Authentication Implementation

Create authentication hooks (src/hooks/auth.ts):
```typescript
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { account, ID } from '../lib/appwrite';

export function useUser() {
  return useQuery({
    queryKey: ['user'],
    queryFn: () => account.get(),
    retry: false,
  });
}

export function useLogin() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async ({ email, password }: { email: string; password: string }) => {
      await account.createEmailSession(email, password);
      return account.get();
    },
    onSuccess: (user) => {
      queryClient.setQueryData(['user'], user);
    },
  });
}

export function useRegister() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async ({ email, password, name }: { email: string; password: string; name: string }) => {
      await account.create(ID.unique(), email, password, name);
      await account.createEmailSession(email, password);
      return account.get();
    },
    onSuccess: (user) => {
      queryClient.setQueryData(['user'], user);
    },
  });
}

export function useLogout() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: () => account.deleteSession('current'),
    onSuccess: () => {
      queryClient.setQueryData(['user'], null);
      queryClient.clear();
    },
  });
}
```

## Database Implementation

Create database hooks (src/hooks/database.ts):
```typescript
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { databases, ID } from '../lib/appwrite';
import { Query } from 'appwrite';

export function useDocuments(databaseId: string, collectionId: string) {
  return useQuery({
    queryKey: ['documents', databaseId, collectionId],
    queryFn: () => databases.listDocuments(
      databaseId,
      collectionId,
      [
        Query.limit(20),
        Query.orderDesc('$createdAt')
      ]
    ),
  });
}

export function useDocument(databaseId: string, collectionId: string, documentId: string) {
  return useQuery({
    queryKey: ['document', databaseId, collectionId, documentId],
    queryFn: () => databases.getDocument(
      databaseId,
      collectionId,
      documentId
    ),
  });
}

export function useCreateDocument(databaseId: string, collectionId: string) {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (data: any) => databases.createDocument(
      databaseId,
      collectionId,
      ID.unique(),
      data
    ),
    onSuccess: () => {
      queryClient.invalidateQueries(['documents', databaseId, collectionId]);
    },
  });
}

export function useUpdateDocument(databaseId: string, collectionId: string) {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ documentId, data }: { documentId: string; data: any }) => databases.updateDocument(
      databaseId,
      collectionId,
      documentId,
      data
    ),
    onSuccess: (_, { documentId }) => {
      queryClient.invalidateQueries(['document', databaseId, collectionId, documentId]);
      queryClient.invalidateQueries(['documents', databaseId, collectionId]);
    },
  });
}

export function useDeleteDocument(databaseId: string, collectionId: string) {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (documentId: string) => databases.deleteDocument(
      databaseId,
      collectionId,
      documentId
    ),
    onSuccess: () => {
      queryClient.invalidateQueries(['documents', databaseId, collectionId]);
    },
  });
}
```

## Usage Examples

Authentication Component:
```typescript
import { useLogin, useUser } from '../hooks/auth';

function LoginForm() {
  const login = useLogin();
  const { data: user } = useUser();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const form = e.target as HTMLFormElement;
    const email = form.email.value;
    const password = form.password.value;

    try {
      await login.mutateAsync({ email, password });
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  if (user) {
    return <div>Welcome, {user.name}!</div>;
  }

  return (
    <form onSubmit={handleSubmit}>
      <input name="email" type="email" required />
      <input name="password" type="password" required />
      <button type="submit" disabled={login.isPending}>
        {login.isPending ? 'Loading...' : 'Login'}
      </button>
    </form>
  );
}
```

Document List Component:
```typescript
import { useDocuments, useCreateDocument } from '../hooks/database';

function DocumentList() {
  const { data, isLoading } = useDocuments('DATABASE_ID', 'COLLECTION_ID');
  const createDocument = useCreateDocument('DATABASE_ID', 'COLLECTION_ID');

  const handleCreate = async (e: React.FormEvent) => {
    e.preventDefault();
    const form = e.target as HTMLFormElement;
    const title = form.title.value;

    try {
      await createDocument.mutateAsync({ title });
      form.reset();
    } catch (error) {
      console.error('Failed to create document:', error);
    }
  };

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <form onSubmit={handleCreate}>
        <input name="title" required />
        <button type="submit" disabled={createDocument.isPending}>
          Create
        </button>
      </form>

      <div>
        {data?.documents.map(doc => (
          <div key={doc.$id}>
            <h3>{doc.title}</h3>
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

1. Use TanStack Query hooks for all Appwrite operations
2. Implement proper error handling and loading states
3. Use environment variables for configuration
4. Create reusable hooks for common operations
5. Handle cache invalidation properly
6. Implement optimistic updates when appropriate

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