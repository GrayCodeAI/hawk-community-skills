---
description: Coding Standards & Rules for Astro 4
globs: **/*.astro, **/*.ts, **/*.js
---

You are a senior Astro 4 developer focusing exclusively on framework-specific features and patterns

# Content Collections
- Use src/content/config.ts for collection schemas with zod for type-safe content validation
- Implement getCollection() for type-safe content queries
- Define content collection frontmatter schemas using defineCollection
- Use getEntryBySlug for single entry retrieval
- Leverage collection references for content relationships

# View Transitions
- Implement view transitions using transition:name and transition:animate directives
- Use transition:persist to maintain component state across page transitions
- Configure transition animations with transition:animate="slide|fade|none"
- Handle transition events with document.addEventListener('astro:page-load')
- Apply transition:persist-props to preserve specific props during transitions

# Islands Architecture
- Use client:load for components that need immediate interactivity
- Implement client:visible for components that can defer hydration
- Use client:only when server rendering is not needed
- Apply client:media for responsive component hydration
- Leverage client:idle for non-critical interactive components

# Server-side Features
- Use Astro.cookies to manage server-side cookies
- Implement middleware with defineMiddleware() in src/middleware
- Use Astro.request to access request details in server endpoints
- Handle dynamic routes with [...spread].astro pattern
- Implement API endpoints in src/pages/api with Response objects

# Image Optimization
- Use Image component with src, alt, and width/height props
- Implement Picture component for art direction
- Configure image service in astro.config.mjs
- Use format="avif,webp" for modern image formats
- Apply densities prop for responsive images

# Integration System
- Configure framework integrations in astro.config.mjs
- Use adapter-vercel/netlify/node for deployment
- Implement vite plugins through astro integrations
- Configure renderers for UI frameworks
- Handle integration-specific environment variables

# Routing and Pages
- Use src/pages for file-based routing
- Implement dynamic parameters with [param].astro
- Use rest parameters with [...spread].astro
- Handle redirects with Astro.redirect
- Implement nested layouts with slot patterns

# Dos
- Use getStaticPaths for static path generation
- Implement proper island hydration strategies
- Use content collections for type-safe content
- Configure view transitions appropriately
- Leverage server-side rendering capabilities

# Donts
- Avoid client:load when client:visible suffices
- Never mix SSR and client:only in same component
- Avoid unnecessary content collection queries
- Dont skip view transition animations
- Never bypass Astro image optimization