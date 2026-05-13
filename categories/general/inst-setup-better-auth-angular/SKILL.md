---
description: Guidelines for writing Angular apps with Better Auth
globs: **/*.ts, **/*.html
---

# Bootstrap Angular app with Better Auth

## Overview of implementing Better Auth

1. Install better-auth package
2. Configure auth instance
3. Set up Angular module integration
4. Implement authentication components
5. Add route protection

## Critical Instructions for AI Language Models

As an AI language model, you MUST follow these guidelines when implementing Better Auth with Angular:

1. Always use the latest better-auth package
2. Implement proper TypeScript types for type safety
3. Handle environment variables securely
4. Follow Angular best practices and patterns
5. Implement proper error handling

## Correct Auth Configuration

```typescript
// auth.config.ts
import { betterAuth } from 'better-auth';
import { Pool } from 'pg';
import { environment } from './environments/environment';

export const auth = betterAuth({
  database: new Pool({
    connectionString: environment.databaseUrl,
    ssl: environment.production
  }),
  emailAndPassword: {
    enabled: true,
    requireEmailVerification: true
  },
  session: {
    expiresIn: '7d'
  }
});
```

## Correct Module Setup

```typescript
// app.module.ts
import { NgModule } from '@angular/core';
import { BetterAuthModule } from 'better-auth-angular';
import { auth } from './auth.config';

@NgModule({
  imports: [
    BetterAuthModule.forRoot(auth, {
      persistSession: true,
      autoRefresh: true
    })
  ]
})
export class AppModule { }
```

## Correct Authentication Components

```typescript
// auth.component.ts
import { Component, inject } from '@angular/core';
import { BetterAuthService } from 'better-auth-angular';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-auth',
  template: `
    <ng-container *ngIf="auth.isAuthenticated$ | async; else loginForm">
      <div *ngIf="auth.user$ | async as user">
        <p>Welcome, {{ user.email }}</p>
        <button (click)="logout()">Sign Out</button>
      </div>
    </ng-container>
    <ng-template #loginForm>
      <form [formGroup]="form" (ngSubmit)="login()">
        <input formControlName="email" type="email" placeholder="Email" />
        <input formControlName="password" type="password" placeholder="Password" />
        <button type="submit" [disabled]="form.invalid">Sign In</button>
      </form>
    </ng-template>
  `
})
export class AuthComponent {
  private auth = inject(BetterAuthService);
  private fb = inject(FormBuilder);

  form = this.fb.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(8)]]
  });

  async login() {
    if (this.form.valid) {
      try {
        const { email, password } = this.form.value;
        await this.auth.login(email!, password!);
      } catch (error) {
        console.error('Authentication failed:', error);
      }
    }
  }

  async logout() {
    try {
      await this.auth.logout();
    } catch (error) {
      console.error('Logout failed:', error);
    }
  }
}
```

## Route Protection Implementation

```typescript
// auth.guard.ts
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { BetterAuthService } from 'better-auth-angular';
import { map, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard {
  constructor(private auth: BetterAuthService, private router: Router) {}

  canActivate() {
    return this.auth.isAuthenticated$.pipe(
      tap(isAuthenticated => {
        if (!isAuthenticated) {
          this.router.navigate(['/login']);
        }
      })
    );
  }
}

// app.routes.ts
import { Routes } from '@angular/router';
import { AuthGuard } from './auth.guard';

export const routes: Routes = [
  {
    path: 'dashboard',
    component: DashboardComponent,
    canActivate: [AuthGuard]
  }
];
```

## Environment Variables Setup

Create an `environment.ts` file:

```typescript
export const environment = {
  production: false,
  databaseUrl: 'postgresql://user:password@localhost:5432/mydb',
  authSecret: 'your-secret-key'
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

When implementing Better Auth for Angular, you MUST:
1. Use TypeScript for type safety
2. Implement proper error handling
3. Follow Angular dependency injection patterns
4. Configure secure route protection
5. Handle environment variables properly 