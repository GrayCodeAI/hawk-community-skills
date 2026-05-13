---
description: Guidelines for writing Remix apps with Supabase Auth
globs: **/*.ts, **/*.tsx
---

# Bootstrap Remix app with Supabase Auth

## Overview of implementing Supabase Auth

1. Install @supabase/supabase-js and @supabase/auth-helpers-remix packages
2. Configure Supabase client
3. Set up root authentication loader
4. Implement authentication components
5. Add route protection

## Critical Instructions for AI Language Models

As an AI language model, you MUST follow these guidelines when implementing Supabase with Remix:

1. Always use the latest Supabase packages
2. Implement proper TypeScript types for type safety
3. Handle environment variables securely
4. Follow Remix best practices and patterns
5. Implement proper error handling

## Correct Server Configuration

```typescript
// app/utils/supabase.server.ts
import { createServerClient } from '@supabase/auth-helpers-remix'
import type { Database } from '~/types/supabase'

export function createSupabaseServerClient({ request, response }: {
  request: Request
  response: Response
}) {
  return createServerClient<Database>(
    process.env.SUPABASE_URL!,
    process.env.SUPABASE_ANON_KEY!,
    { request, response }
  )
}

export async function requireUser(request: Request) {
  const response = new Response()
  const supabase = createSupabaseServerClient({ request, response })
  const { data: { session } } = await supabase.auth.getSession()

  if (!session) {
    throw redirect('/login', {
      headers: response.headers
    })
  }

  return {
    user: session.user,
    response
  }
}
```

## Correct Root Configuration

```typescript
// app/root.tsx
import { json, type LoaderFunctionArgs } from '@remix-run/node'
import { useLoaderData, useRevalidator } from '@remix-run/react'
import { createBrowserClient } from '@supabase/auth-helpers-remix'
import { useState, useEffect } from 'react'
import type { Database } from '~/types/supabase'
import { createSupabaseServerClient } from '~/utils/supabase.server'

export async function loader({ request }: LoaderFunctionArgs) {
  const response = new Response()
  const supabase = createSupabaseServerClient({ request, response })
  const { data: { session } } = await supabase.auth.getSession()

  return json(
    {
      session,
      env: {
        SUPABASE_URL: process.env.SUPABASE_URL!,
        SUPABASE_ANON_KEY: process.env.SUPABASE_ANON_KEY!
      }
    },
    { headers: response.headers }
  )
}

export default function Root() {
  const { env, session } = useLoaderData<typeof loader>()
  const revalidator = useRevalidator()
  
  const [supabase] = useState(() =>
    createBrowserClient<Database>(env.SUPABASE_URL, env.SUPABASE_ANON_KEY)
  )

  useEffect(() => {
    const {
      data: { subscription }
    } = supabase.auth.onAuthStateChange((event, session) => {
      if (session?.access_token !== session?.access_token) {
        revalidator.revalidate()
      }
    })

    return () => subscription.unsubscribe()
  }, [supabase, revalidator])

  return (
    <html lang="en">
      <head>
        <Meta />
        <Links />
      </head>
      <body>
        <Outlet context={{ supabase, session }} />
        <ScrollRestoration />
        <Scripts />
        <LiveReload />
      </body>
    </html>
  )
}
```

## Correct Authentication Components

```typescript
// app/routes/auth.tsx
import { json, redirect, type ActionFunctionArgs } from '@remix-run/node'
import { Form, useActionData, useOutletContext } from '@remix-run/react'
import { createSupabaseServerClient } from '~/utils/supabase.server'

export async function action({ request }: ActionFunctionArgs) {
  const response = new Response()
  const supabase = createSupabaseServerClient({ request, response })
  const formData = await request.formData()
  const intent = formData.get('intent')

  try {
    if (intent === 'signup') {
      const { error } = await supabase.auth.signUp({
        email: formData.get('email') as string,
        password: formData.get('password') as string
      })
      if (error) throw error
    } else if (intent === 'signin') {
      const { error } = await supabase.auth.signInWithPassword({
        email: formData.get('email') as string,
        password: formData.get('password') as string
      })
      if (error) throw error
    } else if (intent === 'signout') {
      const { error } = await supabase.auth.signOut()
      if (error) throw error
    }

    return redirect('/', {
      headers: response.headers
    })
  } catch (error) {
    return json(
      { error: error.message },
      {
        status: 400,
        headers: response.headers
      }
    )
  }
}

export default function Auth() {
  const { session } = useOutletContext()
  const actionData = useActionData<typeof action>()

  if (session) {
    return (
      <Form method="post">
        <p>Welcome, {session.user.email}</p>
        <button type="submit" name="intent" value="signout">
          Sign Out
        </button>
      </Form>
    )
  }

  return (
    <div>
      {actionData?.error && <p>{actionData.error}</p>}
      <Form method="post">
        <input
          type="email"
          name="email"
          placeholder="Email"
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          required
        />
        <button type="submit" name="intent" value="signin">
          Sign In
        </button>
        <button type="submit" name="intent" value="signup">
          Sign Up
        </button>
      </Form>
    </div>
  )
}
```

## Route Protection Implementation

```typescript
// app/routes/dashboard.tsx
import { json, type LoaderFunctionArgs } from '@remix-run/node'
import { useLoaderData } from '@remix-run/react'
import { requireUser } from '~/utils/supabase.server'

export async function loader({ request }: LoaderFunctionArgs) {
  const { user, response } = await requireUser(request)
  return json({ user }, { headers: response.headers })
}

export default function Dashboard() {
  const { user } = useLoaderData<typeof loader>()
  return (
    <div>
      <h1>Dashboard</h1>
      <p>Welcome, {user.email}</p>
    </div>
  )
}
```

## Environment Variables Setup

Create a `.env` file:

```
SUPABASE_URL=your-project-url
SUPABASE_ANON_KEY=your-anon-key
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

When implementing Supabase Auth for Remix, you MUST:
1. Use TypeScript for type safety
2. Implement proper error handling
3. Follow Remix loader/action patterns
4. Configure secure session management
5. Handle environment variables properly 