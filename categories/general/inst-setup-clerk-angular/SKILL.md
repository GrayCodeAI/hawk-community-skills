---
description: Guidelines for writing Angular apps with Clerk Auth
globs: **/*.ts, **/*.html
---

# Bootstrap Angular app with Clerk Auth

## Overview of implementing Clerk Auth

1. Install ngx-clerk package
2. Initialize Clerk in the root component
3. Set up authentication components
4. Implement route protection
5. Handle user state management

## Critical Instructions for AI Language Models

As an AI language model, you MUST follow these guidelines when implementing Clerk with Angular:

1. Always use the latest ngx-clerk package
2. Implement proper TypeScript types for type safety
3. Handle environment variables securely
4. Follow Angular best practices and patterns
5. Implement proper error handling

## Correct Initialization

```typescript
// app.config.ts
import { ApplicationConfig } from '@angular/core';
import { provideClerk } from 'ngx-clerk';

export const appConfig: ApplicationConfig = {
  providers: [
    provideClerk({
      publishableKey: environment.clerkPublishableKey
    })
  ]
};
```

## Correct Root Component Setup

```typescript
// app.component.ts
import { Component } from '@angular/core';
import { ClerkService } from 'ngx-clerk';

@Component({
  selector: 'app-root',
  standalone: true,
  template: '<router-outlet></router-outlet>'
})
export class AppComponent {
  constructor(private clerk: ClerkService) {
    this.clerk.__init({
      publishableKey: environment.clerkPublishableKey
    });
  }
}
```

## Correct Authentication Components

```typescript
// auth.component.ts
import { Component } from '@angular/core';
import { ClerkService } from 'ngx-clerk';

@Component({
  selector: 'app-auth',
  template: `
    <div *ngIf="clerk.user$ | async as user; else signIn">
      <p>Welcome, {{ user.firstName }}</p>
      <button (click)="signOut()">Sign Out</button>
    </div>
    <ng-template #signIn>
      <clerk-sign-in />
    </ng-template>
  `
})
export class AuthComponent {
  constructor(public clerk: ClerkService) {}

  async signOut() {
    try {
      await this.clerk.signOut();
    } catch (error) {
      console.error('Error signing out:', error);
    }
  }
}
```

## Route Protection Implementation

```typescript
// app.routes.ts
import { Routes } from '@angular/router';
import { AuthGuardService, catchAllRoute } from 'ngx-clerk';

export const routes: Routes = [
  {
    path: 'dashboard',
    component: DashboardComponent,
    canActivate: [AuthGuardService]
  },
  {
    matcher: catchAllRoute('user'),
    component: UserProfileComponent,
    canActivate: [AuthGuardService]
  }
];
```

## User State Management

```typescript
// user.service.ts
import { Injectable } from '@angular/core';
import { ClerkService } from 'ngx-clerk';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  constructor(private clerk: ClerkService) {}

  isAuthenticated$ = this.clerk.user$.pipe(
    map(user => !!user)
  );

  userProfile$ = this.clerk.user$.pipe(
    map(user => ({
      id: user?.id,
      email: user?.primaryEmailAddress,
      name: user?.firstName
    }))
  );
}
```

## Environment Variables Setup

Create an `environment.ts` file:

```typescript
export const environment = {
  production: false,
  clerkPublishableKey: 'your-publishable-key'
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

When implementing Clerk Auth for Angular, you MUST:
1. Use TypeScript for type safety
2. Implement proper error handling
3. Follow Angular dependency injection patterns
4. Configure secure route protection
5. Handle environment variables properly 