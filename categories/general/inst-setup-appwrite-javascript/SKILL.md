---
description: Guidelines for writing JavaScript apps with Appwrite
globs: src/**/*.js, src/**/*.jsx
---

# Appwrite + JavaScript Integration Setup Guide

## Prerequisites
- Node.js and npm installed
- JavaScript project initialized
- Appwrite account and project created

## Installation

Install the Appwrite SDK:
```bash
npm install appwrite
```

## Core Configuration

Create Appwrite client configuration (src/lib/appwrite.js):
```javascript
import { Client, Account, Databases, Storage, ID } from 'appwrite';

const client = new Client()
  .setEndpoint(process.env.VITE_APPWRITE_ENDPOINT || 'https://cloud.appwrite.io/v1')
  .setProject(process.env.VITE_APPWRITE_PROJECT_ID || '');

export const account = new Account(client);
export const databases = new Databases(client);
export const storage = new Storage(client);
export { ID };
export default client;
```

## Authentication Implementation

Create authentication service (src/services/auth.js):
```javascript
import { account, ID } from '../lib/appwrite';

export const AuthService = {
  async register(email, password, name) {
    try {
      await account.create(ID.unique(), email, password, name);
      return this.login(email, password);
    } catch (error) {
      console.error('Registration error:', error);
      throw error;
    }
  },

  async login(email, password) {
    try {
      return await account.createEmailSession(email, password);
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

## Database Implementation

Create database service (src/services/database.js):
```javascript
import { databases, ID } from '../lib/appwrite';
import { Query } from 'appwrite';

export const DatabaseService = {
  async createDocument(databaseId, collectionId, data) {
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

  async listDocuments(databaseId, collectionId, queries = []) {
    try {
      return await databases.listDocuments(
        databaseId,
        collectionId,
        [
          Query.limit(20),
          Query.orderDesc('$createdAt'),
          ...queries
        ]
      );
    } catch (error) {
      console.error('List documents error:', error);
      throw error;
    }
  },

  async updateDocument(databaseId, collectionId, documentId, data) {
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

  async deleteDocument(databaseId, collectionId, documentId) {
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

Authentication Example:
```javascript
import { AuthService } from './services/auth';

// Registration
try {
  await AuthService.register('user@example.com', 'password123', 'John Doe');
  console.log('Registration successful');
} catch (error) {
  console.error('Registration failed:', error);
}

// Login
try {
  const session = await AuthService.login('user@example.com', 'password123');
  console.log('Login successful:', session);
} catch (error) {
  console.error('Login failed:', error);
}

// Get current user
try {
  const user = await AuthService.getCurrentUser();
  if (user) {
    console.log('Current user:', user);
  } else {
    console.log('No user logged in');
  }
} catch (error) {
  console.error('Failed to get user:', error);
}
```

Database Operations Example:
```javascript
import { DatabaseService } from './services/database';
import { Query } from 'appwrite';

// Create document
try {
  const document = await DatabaseService.createDocument(
    'DATABASE_ID',
    'COLLECTION_ID',
    {
      title: 'New Post',
      content: 'Post content here',
      author: 'John Doe'
    }
  );
  console.log('Document created:', document);
} catch (error) {
  console.error('Failed to create document:', error);
}

// List documents with filtering
try {
  const documents = await DatabaseService.listDocuments(
    'DATABASE_ID',
    'COLLECTION_ID',
    [
      Query.equal('author', 'John Doe'),
      Query.orderDesc('$createdAt')
    ]
  );
  console.log('Documents:', documents);
} catch (error) {
  console.error('Failed to list documents:', error);
}
```

## Security Guidelines

1. Store sensitive configuration in environment variables
2. Implement proper error handling for all operations
3. Set appropriate collection permissions in Appwrite Console
4. Use API keys with minimal required scopes
5. Enable HTTPS for production deployments

## Implementation Guidelines

1. Use service-based architecture for better organization
2. Implement proper error handling and validation
3. Use environment variables for configuration
4. Create reusable utility functions
5. Handle loading and error states consistently
6. Implement proper client-side caching when needed

## Error Handling Example

Create error utility (src/utils/error.js):
```javascript
export class AppwriteError extends Error {
  constructor(message, originalError) {
    super(message);
    this.name = 'AppwriteError';
    this.originalError = originalError;
  }
}

export const handleError = (error, customMessage = 'Operation failed') => {
  console.error(customMessage, error);
  
  if (error.response) {
    // Handle Appwrite error response
    throw new AppwriteError(
      `${customMessage}: ${error.response.message}`,
      error
    );
  }
  
  throw new AppwriteError(customMessage, error);
}; 