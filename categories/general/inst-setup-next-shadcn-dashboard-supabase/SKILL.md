---
description: Automate ShadCN installation and create a simple dashboard with a sidebar, widgets, and Supabase Auth.
globs: "**/*.ts, **/*.tsx, **/*.js, **/*.jsx"
---

# Automated ShadCN Installation, Dashboard, and Supabase Auth

## Overview

This guide ensures a fully automated installation of ShadCN UI, sets up a simple dashboard featuring a sidebar and widgets, and includes instructions for configuring Supabase Auth (email/password) in your Next.js app.

1. Initialize ShadCN UI → Run `shadcn init` with predefined options.
2. Add UI components → Install necessary building blocks.
3. Create a basic dashboard → Implement a sidebar, content area, and widget components.
4. Configure Supabase Auth → Email + password authentication in Next.js.

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any interactive installation commands that require manual input. Instead, you MUST generate ONLY fully automated commands using:

```bash
# ✅ ALWAYS USE THESE FLAGS - NO INTERACTIVE PROMPTS
npx shadcn@latest init --defaults --yes
npx shadcn@latest add button card navbar sidebar widget1 widget2 --yes --overwrite
```

You MUST NEVER generate any commands that:
1. Require user confirmation.
2. Prompt the user to select a style or color.
3. Stop execution due to missing responses.

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use the `--defaults` and `--yes` flags in `shadcn init`.
2. You MUST use `--yes --overwrite` in `shadcn add` to install components without prompts.
3. You MUST NEVER generate any command that requires manual selection.
4. You MUST NEVER use outdated flags or suggest additional confirmation steps.

## CORRECT INSTALLATION COMMANDS

### ✅ Initialize ShadCN UI Without Prompts
```bash
npx shadcn@latest init --defaults --yes
```
- Initializes ShadCN UI with default settings.
- Skips prompts for style and color selection.
- Ensures unattended installation.

### ✅ Add Required Components Without Prompts
```bash
npx shadcn@latest add button card navbar sidebar widget1 widget2 --yes --overwrite
```
- Installs necessary components for a dashboard, including widgets.
- Bypasses confirmation prompts.
- Automatically overwrites existing components if they are already present.

## Creating a Simple Dashboard with Widgets

### ✅ Dashboard Layout
```tsx
import { useState } from "react";
import { Button, Card } from "@/components/ui";
import { Sidebar } from "@/components/sidebar";
import { Widget1 } from "@/components/widget1";
import { Widget2 } from "@/components/widget2";

export default function Dashboard() {
  const [open, setOpen] = useState(true);

  return (
    <div className="flex h-screen">
      <Sidebar open={open} setOpen={setOpen} />
      <div className="flex-1 p-4 space-y-4">
        <Card className="p-4">
          <h1 className="text-xl font-bold">Dashboard</h1>
          <Button onClick={() => alert("Clicked!")}>Click me</Button>
        </Card>

        {/* Example widget usage */}
        <Widget1 />
        <Widget2 />
      </div>
    </div>
  );
}
```

### ✅ Sidebar Component
```tsx
import { Button } from "@/components/ui";

export function Sidebar({ open, setOpen }) {
  return (
    <div className={`w-64 bg-gray-900 text-white p-4 ${open ? "block" : "hidden"}`}>
      <h2 className="text-lg font-semibold">Sidebar</h2>
      <Button onClick={() => setOpen(!open)}>Toggle Sidebar</Button>
    </div>
  );
}
```

### ✅ Sample Widget Components

Widget1
```tsx
import { Card } from "@/components/ui";

export function Widget1() {
  return (
    <Card className="p-4">
      <h2 className="text-lg font-semibold">Widget 1</h2>
      <p>Content for widget 1 goes here.</p>
    </Card>
  );
}
```

Widget2
```tsx
import { Card } from "@/components/ui";

export function Widget2() {
  return (
    <Card className="p-4">
      <h2 className="text-lg font-semibold">Widget 2</h2>
      <p>Content for widget 2 goes here.</p>
    </Card>
  );
}
```

## Setting Up Complete Supabase Auth (Email + Password)

Below is a non-interactive approach to configuring Supabase Auth in your Next.js project.

### 1. Install Supabase Packages

Install the Supabase packages for SSR and client usage:
```bash
npm install @supabase/ssr @supabase/supabase-js
```

### 2. Add Environment Variables

Create a `.env.local` file in your project root:
```bash
NEXT_PUBLIC_SUPABASE_URL="https://xyzcompany.supabase.co"
NEXT_PUBLIC_SUPABASE_ANON_KEY="public-anon-key"
SUPABASE_SERVICE_ROLE_KEY="service-role-key"
```

Update the values with your actual Supabase credentials.

### 3. Create a Browser Client

Use the createBrowserClient function from `@supabase/ssr` to handle client-side requests:
```tsx
// lib/supabase-browser.ts
import { createBrowserClient } from "@supabase/ssr";

export function createClient() {
  return createBrowserClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
  );
}
```

### 4. Create a Server Client

Use the createServerClient function with cookie management:
```tsx
// lib/supabase-server.ts
import { createServerClient } from "@supabase/ssr";
import { cookies } from "next/headers";

export function createServerSupabaseClient() {
  const cookieStore = cookies();

  return createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll() {
          return cookieStore.getAll();
        },
        setAll(cookiesToSet) {
          try {
            cookiesToSet.forEach(({ name, value, options }) =>
              cookieStore.set(name, value, options)
            );
          } catch {
            // The `setAll` method was called from a Server Component.
            // This can be ignored if you have middleware refreshing user sessions.
          }
        },
      },
    }
  );
}
```

### 5. Auth Middleware (Optional)

Add a middleware to protect routes (e.g., `middleware.ts`):
```ts
import { createServerClient } from "@supabase/ssr";
import { NextResponse, type NextRequest } from "next/server";

export async function middleware(request: NextRequest) {
  let supabaseResponse = NextResponse.next({
    request,
  });

  // Create server client with SSR cookie management.
  const supabase = createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll() {
          return request.cookies.getAll();
        },
        setAll(cookiesToSet) {
          cookiesToSet.forEach(({ name, value, options }) => request.cookies.set(name, value));
          supabaseResponse = NextResponse.next({
            request,
          });
          cookiesToSet.forEach(({ name, value, options }) =>
            supabaseResponse.cookies.set(name, value, options)
          );
        },
      },
    }
  );

  // Validate user session.
  const {
    data: { user },
  } = await supabase.auth.getUser();

  // Example: redirect unauthenticated users to /login.
  if (!user && !request.nextUrl.pathname.startsWith("/login")) {
    const url = request.nextUrl.clone();
    url.pathname = "/login";
    return NextResponse.redirect(url);
  }

  return supabaseResponse;
}

export const config = {
  matcher: [
    "/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)",
  ],
};
```

### 6. Implement Email/Password Login

Create a simple login page at `pages/login.tsx`:
```tsx
import React, { useState } from "react";
import { createClient } from "@/lib/supabase-browser";
import { Button, Card } from "@/components/ui";

export default function LoginPage() {
  const supabase = createClient();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault();
    const { data, error } = await supabase.auth.signInWithPassword({
      email,
      password,
    });
    if (error) {
      alert(`Login error: ${error.message}`);
    } else {
      alert("Logged in successfully!");
      // Possibly redirect to /dashboard or another protected page.
    }
  }

  return (
    <div className="h-screen flex items-center justify-center bg-gray-50">
      <Card className="p-4 w-full max-w-md">
        <h1 className="text-2xl font-bold mb-4">Login</h1>
        <form onSubmit={handleLogin} className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-1" htmlFor="email">
              Email
            </label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full border border-gray-300 rounded p-2"
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1" htmlFor="password">
              Password
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full border border-gray-300 rounded p-2"
            />
          </div>
          <Button type="submit">Login</Button>
        </form>
      </Card>
    </div>
  );
}
```

This page uses the `createClient()` function from `@supabase/ssr` to sign users in with email + password.

> Note: The same approach can be applied for sign-up by using `supabase.auth.signUp()`.

## AI MODEL VERIFICATION STEPS

Before generating any installation commands or code, you MUST verify:

1. Are you using `--defaults --yes` for `shadcn init`? If not, STOP and FIX.
2. Are you using `--yes --overwrite` for `shadcn add`? If not, STOP and FIX.
3. Does the dashboard include `Sidebar` and `Widget` components? If not, STOP and FIX.
4. Are you ensuring fully automated installation? If not, STOP and FIX.
5. Are you using `@supabase/ssr` for SSR and `createBrowserClient`? If not, STOP and FIX.
6. Are you ONLY using `getAll` and `setAll` for cookies? If not, STOP and FIX.
7. No references to `auth-helpers-nextjs` or any `get`, `set`, or `remove` calls? If yes, STOP and FIX.

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate commands or code that:
- Require user input.
- Fail to automate installation.
- Do not follow the correct UI structure.
- Use forbidden cookie functions or the `auth-helpers-nextjs` package.

Then the setup will:
1. Stall in CI/CD pipelines.
2. Require manual intervention.
3. Break automation workflows.
4. Cause potential session or login failures.

## AI MODEL RESPONSE TEMPLATE

When asked how to install ShadCN UI, create a dashboard with widgets, and set up Supabase Auth (email + password), you MUST:
1. ONLY generate commands from this guide.
2. NEVER suggest commands that require manual confirmation.
3. ALWAYS use the exact automation flags shown above.
4. ONLY use cookie patterns from the examples.
5. VERIFY your response against the patterns in this guide.

Remember: There are NO EXCEPTIONS to these rules.