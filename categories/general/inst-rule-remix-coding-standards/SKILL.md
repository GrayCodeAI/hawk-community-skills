---
description: Coding Standards & Rules for Remix 2
globs: **/*.tsx, **/*.ts, **/*.jsx, **/*.js
---

You are a Remix 2 expert with deep knowledge of TypeScript and Remix-specific patterns. Follow these framework-specific standards when working with Remix applications.

# Routing and File Structure
- Use flat-file routing in `app/routes` following Remix conventions. Example: `routes/posts.$postId.tsx` for dynamic routes
- Implement nested routing using dot notation and folder structure. Example: `routes/dashboard.overview.tsx` or `routes/dashboard/overview.tsx`
- Use `$` for dynamic segments and `_` for layout routes. Example: `routes/posts/$.tsx` for catch-all routes
- Place route-specific components in `app/routes/__components` to avoid them being treated as routes
- Use `app/root.tsx` for global providers, meta tags, and error boundaries

# Data Flow
- Use loaders for data fetching with proper types. Example: 
  `export const loader = async ({ params }: LoaderFunctionArgs) => { return json({ data }) }`
- Implement actions for form mutations. Example:
  `export const action = async ({ request }: ActionFunctionArgs) => { const formData = await request.formData() }`
- Use `defer()` for non-critical data loading. Example:
  `return defer({ critical: await getCriticalData(), nonCritical: getNonCriticalData() })`
- Implement parallel data loading for nested routes using `Promise.all` in parent loaders
- Use useMatches hook for sharing loader data between routes
- Return proper Response objects with status codes from loaders and actions

# Forms and Mutations
- Use Remix Form component for enhanced form handling with optimistic updates
- Implement progressive enhancement starting with native HTML forms
- Use useNavigation hook for loading states in forms
- Use useActionData for handling form submission results
- Implement optimistic UI updates using useFetcher

# Server-Side Features
- Use resource routes for API endpoints (routes that return non-HTML responses)
- Implement server-side sessions using createCookieSessionStorage
- Use headers export for custom caching and security headers
- Implement server timing headers for performance monitoring
- Use server-side redirects with redirect() helper

# Meta and SEO
- Export meta functions as arrays for dynamic SEO. Example:
  `export const meta: MetaFunction = () => [{ title: "Page Title" }]`
- Use V2 Meta API with nested meta data
- Implement handle export for breadcrumbs and nested metadata
- Use links export for preloading assets and stylesheets

# Error Handling
- Use route-specific ErrorBoundary components
- Implement isRouteErrorResponse for type-safe error handling
- Use root ErrorBoundary for global error handling
- Throw Response objects for HTTP errors in loaders/actions

# Performance
- Use prefetch prop on Link components for route preloading
- Implement route-based code splitting automatically via route modules
- Use headers export for proper cache control
- Implement streaming with defer() for improved loading states

# TypeScript Integration
- Use Remix-specific types: LoaderFunctionArgs, ActionFunctionArgs, MetaFunction
- Implement SerializeFrom utility type for loader data
- Use TypedResponse for typed loader/action returns
- Type route params using Params utility type