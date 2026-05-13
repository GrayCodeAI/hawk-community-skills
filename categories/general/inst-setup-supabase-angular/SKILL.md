---
description: Guidelines for writing Angular apps with Supabase Auth
globs: **/*.ts, **/*.html
---

# Bootstrap Angular app with Supabase Auth

## Overview of implementing Supabase Auth

1. Install @supabase/supabase-js package
2. Configure Supabase client
3. Create authentication service
4. Implement authentication components
5. Add route protection

## Critical Instructions for AI Language Models

As an AI language model, you MUST follow these guidelines when implementing Supabase with Angular:

1. Always use the latest @supabase/supabase-js package
2. Implement proper TypeScript types for type safety
3. Handle environment variables securely
4. Follow Angular best practices and patterns
5. Implement proper error handling

## Correct Client Setup

```typescript
// lib/supabase.ts
import { createClient } from '@supabase/supabase-js'
import { environment } from '../environments/environment'
import type { Database } from '../types/supabase'

export const supabase = createClient<Database>(
  environment.supabase.url,
  environment.supabase.anonKey,
  {
    auth: {
      autoRefreshToken: true,
      persistSession: true
    }
  }
)
```

## Correct Authentication Service

```typescript
// services/auth.service.ts
import { Injectable, inject } from '@angular/core'
import { Router } from '@angular/router'
import { BehaviorSubject, Observable } from 'rxjs'
import { supabase } from '../lib/supabase'
import type { User, Session } from '@supabase/supabase-js'

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private router = inject(Router)
  private userSubject = new BehaviorSubject<User | null>(null)
  private sessionSubject = new BehaviorSubject<Session | null>(null)

  user$ = this.userSubject.asObservable()
  session$ = this.sessionSubject.asObservable()
  isAuthenticated$ = new Observable<boolean>(observer => 
    this.session$.subscribe(session => observer.next(!!session))
  )

  constructor() {
    this.initializeAuth()
  }

  private async initializeAuth() {
    const { data: { session } } = await supabase.auth.getSession()
    this.sessionSubject.next(session)
    this.userSubject.next(session?.user ?? null)

    supabase.auth.onAuthStateChange((_, session) => {
      this.sessionSubject.next(session)
      this.userSubject.next(session?.user ?? null)
    })
  }

  async signIn(email: string, password: string) {
    try {
      const { error } = await supabase.auth.signInWithPassword({
        email,
        password
      })
      if (error) throw error
    } catch (error) {
      console.error('Error signing in:', error)
      throw error
    }
  }

  async signOut() {
    try {
      const { error } = await supabase.auth.signOut()
      if (error) throw error
      this.router.navigate(['/login'])
    } catch (error) {
      console.error('Error signing out:', error)
      throw error
    }
  }
}
```

## Correct Authentication Component

```typescript
// components/auth.component.ts
import { Component, inject } from '@angular/core'
import { FormBuilder, Validators } from '@angular/forms'
import { AuthService } from '../services/auth.service'

@Component({
  selector: 'app-auth',
  template: `
    <ng-container *ngIf="auth.isAuthenticated$ | async; else loginForm">
      <div *ngIf="auth.user$ | async as user">
        <p>Welcome, {{ user.email }}</p>
        <button (click)="signOut()">Sign Out</button>
      </div>
    </ng-container>
    <ng-template #loginForm>
      <form [formGroup]="form" (ngSubmit)="signIn()">
        <input formControlName="email" type="email" placeholder="Email" />
        <input formControlName="password" type="password" placeholder="Password" />
        <button type="submit" [disabled]="form.invalid">Sign In</button>
      </form>
    </ng-template>
  `
})
export class AuthComponent {
  private auth = inject(AuthService)
  private fb = inject(FormBuilder)

  form = this.fb.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(8)]]
  })

  async signIn() {
    if (this.form.valid) {
      try {
        const { email, password } = this.form.value
        await this.auth.signIn(email!, password!)
      } catch (error) {
        console.error('Authentication failed:', error)
      }
    }
  }

  async signOut() {
    try {
      await this.auth.signOut()
    } catch (error) {
      console.error('Sign out failed:', error)
    }
  }
}
```

## Route Protection Implementation

```typescript
// guards/auth.guard.ts
import { Injectable } from '@angular/core'
import { Router } from '@angular/router'
import { AuthService } from '../services/auth.service'
import { map, tap } from 'rxjs/operators'

@Injectable({
  providedIn: 'root'
})
export class AuthGuard {
  constructor(private auth: AuthService, private router: Router) {}

  canActivate() {
    return this.auth.isAuthenticated$.pipe(
      tap(isAuthenticated => {
        if (!isAuthenticated) {
          this.router.navigate(['/login'])
        }
      })
    )
  }
}

// app.routes.ts
import { Routes } from '@angular/router'
import { AuthGuard } from './guards/auth.guard'

export const routes: Routes = [
  {
    path: 'dashboard',
    component: DashboardComponent,
    canActivate: [AuthGuard]
  }
]
```

## Environment Variables Setup

Create an `environment.ts` file:

```typescript
export const environment = {
  production: false,
  supabase: {
    url: 'your-project-url',
    anonKey: 'your-anon-key'
  }
}
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

When implementing Supabase Auth for Angular, you MUST:
1. Use TypeScript for type safety
2. Implement proper error handling
3. Follow Angular dependency injection patterns
4. Configure secure route protection
5. Handle environment variables properly 