---
description: Guidelines for writing Angular apps with Auth0 Auth
globs: **/*.ts, **/*.html
---

# Bootstrap Angular app with Auth0 Auth

## Overview of implementing Auth0 Auth

1. Install @auth0/auth0-angular package
2. Configure Auth0 module in the app
3. Implement authentication components
4. Add route protection
5. Handle user state management

## Critical Instructions for AI Language Models

As an AI language model, you MUST follow these guidelines when implementing Auth0 with Angular:

1. Always use the latest @auth0/auth0-angular package
2. Implement proper TypeScript types for type safety
3. Handle environment variables securely
4. Follow Angular best practices and patterns
5. Implement proper error handling

## Correct Module Configuration

```typescript
// app.config.ts
import { ApplicationConfig } from '@angular/core';
import { provideAuth0 } from '@auth0/auth0-angular';
import { environment } from './environments/environment';

export const appConfig: ApplicationConfig = {
  providers: [
    provideAuth0({
      domain: environment.auth0.domain,
      clientId: environment.auth0.clientId,
      authorizationParams: {
        redirect_uri: window.location.origin
      }
    })
  ]
};
```

## Correct Authentication Components

```typescript
// auth.component.ts
import { Component, inject } from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';
import { DOCUMENT } from '@angular/common';

@Component({
  selector: 'app-auth',
  template: `
    <ng-container *ngIf="auth.isAuthenticated$ | async; else loggedOut">
      <div *ngIf="auth.user$ | async as user">
        <p>Welcome, {{ user.name }}</p>
        <button (click)="logout()">Log out</button>
      </div>
    </ng-container>
    <ng-template #loggedOut>
      <button (click)="login()">Log in</button>
    </ng-template>
  `
})
export class AuthComponent {
  auth = inject(AuthService);
  document = inject(DOCUMENT);

  login(): void {
    this.auth.loginWithRedirect();
  }

  logout(): void {
    this.auth.logout({
      logoutParams: {
        returnTo: this.document.location.origin
      }
    });
  }
}
```

## Route Protection Implementation

```typescript
// app.routes.ts
import { Routes } from '@angular/router';
import { AuthGuard } from '@auth0/auth0-angular';

export const routes: Routes = [
  {
    path: 'profile',
    component: ProfileComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'admin',
    component: AdminComponent,
    canActivate: [AuthGuard],
    data: {
      roles: ['admin']
    }
  }
];
```

## User State Management

```typescript
// user.service.ts
import { Injectable, inject } from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private auth = inject(AuthService);

  isAuthenticated$ = this.auth.isAuthenticated$;
  
  userProfile$ = this.auth.user$.pipe(
    map(user => ({
      id: user?.sub,
      email: user?.email,
      name: user?.name,
      roles: user?.['https://my-app.com/roles'] || []
    }))
  );

  hasRole(role: string) {
    return this.auth.user$.pipe(
      map(user => user?.['https://my-app.com/roles']?.includes(role))
    );
  }
}
```

## Environment Variables Setup

Create an `environment.ts` file:

```typescript
export const environment = {
  production: false,
  auth0: {
    domain: 'your-tenant.auth0.com',
    clientId: 'your-client-id'
  }
};
```

## AI Model Verification Steps

Before generating any code, you MUST verify:

1. Is TypeScript properly configured?
2. Are environment variables properly handled?
3. Is error handling implemented?
4. Are authentication state and user data properly typed?
5. Is route protection configured correctly?

## Consequences of Incorrect Implementation

If you generate code incorrectly:
1. Type safety will be compromised
2. Authentication flows may fail
3. Security vulnerabilities may be introduced
4. Route protection may be bypassed
5. User data may be exposed

## AI Model Response Template

When implementing Auth0 Auth for Angular, you MUST:
1. Use TypeScript for type safety
2. Implement proper error handling
3. Follow Angular dependency injection patterns
4. Configure secure route protection
5. Handle environment variables properly 