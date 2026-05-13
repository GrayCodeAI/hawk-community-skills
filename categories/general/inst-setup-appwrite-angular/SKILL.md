---
description: Guidelines for writing Angular apps with Appwrite
globs: src/**/*.ts, src/**/*.html
---

# Appwrite + Angular Integration Setup Guide

## Prerequisites
- Node.js and npm installed
- Angular project initialized
- Appwrite account and project created

## Installation

Install the Appwrite SDK:
```bash
npm install appwrite
```

## Core Configuration

Create environment configuration (src/environments/environment.ts):
```typescript
export const environment = {
  production: false,
  appwrite: {
    endpoint: 'https://cloud.appwrite.io/v1',
    projectId: 'your-project-id'
  }
};
```

Create the Appwrite service (src/app/services/appwrite.service.ts):
```typescript
import { Injectable } from '@angular/core';
import { Client, Account, Databases, Storage } from 'appwrite';
import { environment } from '../../environments/environment';
import { from, Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AppwriteService {
  private client: Client;
  public account: Account;
  public databases: Databases;
  public storage: Storage;

  constructor() {
    this.client = new Client();
    this.client
      .setEndpoint(environment.appwrite.endpoint)
      .setProject(environment.appwrite.projectId);

    this.account = new Account(this.client);
    this.databases = new Databases(this.client);
    this.storage = new Storage(this.client);
  }

  login(email: string, password: string): Observable<any> {
    return from(this.account.createEmailSession(email, password)).pipe(
      catchError(error => {
        console.error('Login error:', error);
        return throwError(() => error);
      })
    );
  }

  getCurrentUser(): Observable<any> {
    return from(this.account.get()).pipe(
      catchError(error => {
        console.error('Get user error:', error);
        return throwError(() => error);
      })
    );
  }

  logout(): Observable<any> {
    return from(this.account.deleteSession('current')).pipe(
      catchError(error => {
        console.error('Logout error:', error);
        return throwError(() => error);
      })
    );
  }
}
```

## Authentication Component Example

Create an authentication component (src/app/components/auth/auth.component.ts):
```typescript
import { Component } from '@angular/core';
import { AppwriteService } from '../../services/appwrite.service';

@Component({
  selector: 'app-auth',
  template: `
    <div class="auth-container">
      <form (ngSubmit)="login()" #loginForm="ngForm">
        <div class="form-group">
          <input [(ngModel)]="email" name="email" type="email" required>
        </div>
        <div class="form-group">
          <input [(ngModel)]="password" name="password" type="password" required>
        </div>
        <button type="submit" [disabled]="!loginForm.form.valid || loading">
          {{ loading ? 'Loading...' : 'Login' }}
        </button>
      </form>
    </div>
  `
})
export class AuthComponent {
  email = '';
  password = '';
  loading = false;

  constructor(private appwrite: AppwriteService) {}

  login() {
    this.loading = true;
    this.appwrite.login(this.email, this.password).subscribe({
      next: () => {
        this.loading = false;
        // Handle successful login
      },
      error: () => {
        this.loading = false;
        // Handle login error
      }
    });
  }
}
```

## Database Operations Example

Create a data service (src/app/services/data.service.ts):
```typescript
import { Injectable } from '@angular/core';
import { AppwriteService } from './appwrite.service';
import { Query } from 'appwrite';
import { from, Observable } from 'rxjs';
import { catchError, map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  constructor(private appwrite: AppwriteService) {}

  getDocuments(databaseId: string, collectionId: string): Observable<any> {
    return from(this.appwrite.databases.listDocuments(
      databaseId,
      collectionId,
      [
        Query.limit(20),
        Query.orderDesc('$createdAt')
      ]
    )).pipe(
      map(response => response.documents),
      catchError(error => {
        console.error('Fetch documents error:', error);
        return throwError(() => error);
      })
    );
  }
}
```

## Security Guidelines

1. Store sensitive configuration in environment files
2. Implement proper session management and token handling
3. Set appropriate collection permissions in Appwrite Console
4. Use API keys with minimal required scopes
5. Enable HTTPS for production deployments

## Implementation Guidelines

1. Use RxJS Observables for Appwrite operations
2. Implement loading states for async operations
3. Create separate services for different Appwrite features
4. Use TypeScript interfaces for API responses
5. Handle errors consistently across the application
6. Use Angular's async pipe in templates

## Usage Examples

### Authentication Component
```typescript
import { Component } from '@angular/core';
import { AppwriteService } from '../services/appwrite.service';

@Component({
  selector: 'app-auth',
  template: `
    <form (ngSubmit)="login()">
      <input [(ngModel)]="email" name="email" type="email" placeholder="Email">
      <input [(ngModel)]="password" name="password" type="password" placeholder="Password">
      <button type="submit">Login</button>
    </form>
  `
})
export class AuthComponent {
  email: string = '';
  password: string = '';

  constructor(private appwrite: AppwriteService) {}

  async login() {
    try {
      await this.appwrite.createSession(this.email, this.password);
      const user = await this.appwrite.getCurrentUser();
      console.log('Logged in user:', user);
    } catch (error) {
      console.error('Login failed:', error);
    }
  }
}
```

### SSR Support
For server-side rendering support:
```typescript
const session = await this.account.createEmailSession(email, password);
this.client.setSession(session.secret);
```

### Two-Factor Authentication
```typescript
async setup2FA() {
  try {
    const challenge = await this.account.createChallenge('email');
    await this.account.updateChallenge(challenge.$id, 'oneTimeCode');
  } catch (error) {
    console.error('2FA setup failed:', error);
  }
}
```

### Database Operations
```typescript
import { Query } from 'appwrite';

async getDocuments() {
  try {
    const documents = await this.databases.listDocuments(
      'DATABASE_ID',
      'COLLECTION_ID',
      [
        Query.contains('content', ['happy', 'love']),
        Query.or([
          Query.contains('name', 'ivy'),
          Query.greaterThan('age', 30)
        ])
      ]
    );
    return documents;
  } catch (error) {
    console.error('Failed to fetch documents:', error);
    throw error;
  }
}
```

## Security Considerations
1. Never expose your project ID in client-side code without proper security measures
2. Implement proper session management
3. Use environment variables for sensitive configuration
4. Set up appropriate database security rules

## Best Practices
1. Use dependency injection for the Appwrite service
2. Implement proper error handling for all Appwrite operations
3. Use TypeScript interfaces for better type safety
4. Create separate services for different Appwrite features (auth, database, storage)
5. Implement proper loading states for asynchronous operations
6. Use Angular's async pipe for handling observables

## Troubleshooting
1. Ensure your project ID and endpoint are correct
2. Check network requests in browser developer tools
3. Verify proper CORS configuration in Appwrite console
4. Monitor Appwrite logs for potential issues

## Additional Resources
- [Appwrite Documentation](https://appwrite.io/docs)
- [Angular Documentation](https://angular.io/docs)
- [Appwrite Discord Community](https://discord.gg/appwrite) 