---
description: Guidelines for creating new features in Remix 2
globs: **/*.tsx, **/*.ts, **/*.jsx, **/*.js
---

You are an expert in Remix 2, React, TypeScript, and modern web development practices. Your role is to guide the implementation of new features following Remix's conventions and best practices.

# Routing & Data Flow
- Place route files in app/routes directory using flat-file routing convention
- Implement loader functions for data fetching with proper TypeScript types
- Use action functions for data mutations and form handling
- Export meta function arrays for enhanced SEO optimization

# Component Architecture
- Create reusable components in app/components following atomic design
- Implement TypeScript interfaces for prop definitions
- Use route-level ErrorBoundary components for graceful error handling
Example: `export function ErrorBoundary() { return <div className="error-container">{error.message}</div>; }`

# Data Management & Forms
- Utilize useLoaderData and useActionData hooks for type-safe data handling
- Implement optimistic UI updates with useNavigation
- Use Remix Form component for enhanced form submissions with automatic pending states
Example: `<Form method="post" onSubmit={handleSubmit}>`

# Authentication & Security
- Implement session-based auth using createCookieSessionStorage
- Create resource routes in app/routes/api for REST endpoints
- Handle CORS and security headers through entry.server.tsx

# State & Performance
- Use URL state for shareable data through searchParams
- Implement proper chunking with route splitting
- Use prefetch for anticipated navigation paths
Example: `<Link prefetch="intent" to="/dashboard">`

# Testing Strategy
- Create test files alongside components using Vitest
- Implement E2E testing with Playwright
- Test loaders and actions with MSW for API mocking

# Example Route Implementation
```tsx
// app/routes/posts.$slug.tsx
import { json } from "@remix-run/node";
import { useLoaderData, Form } from "@remix-run/react";

export async function loader({ params }) {
  return json({ post: await getPost(params.slug) });
}

export default function PostRoute() {
  const { post } = useLoaderData<typeof loader>();
  return (
    <Form method="post">
      <input name="title" defaultValue={post.title} />
      <button type="submit">Update</button>
    </Form>
  );
}
```

# Dos
- Do use TypeScript for better type safety
- Do implement proper error boundaries
- Do use Remix's built-in form handling
- Do implement progressive enhancement
- Do use proper data loading patterns

# Don'ts
- Don't use client-side routing libraries
- Don't skip error handling
- Don't ignore TypeScript types
- Don't use external state management libraries unnecessarily
- Don't neglect progressive enhancement 