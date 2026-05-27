---
name: mdc-next-js-server-component-rules
description: "Defines rules specifically for Next.js React Server Components (RSC) within the 'app' directory."
license: MIT
tags: [react]
---

- Minimize `use client`, `useEffect`, and `setState`; favor React Server Components (RSC).
- Wrap client components in `Suspense` with fallback.
- Follow Next.js docs for Data Fetching, Rendering, and Routing.
- Favor server components and Next.js SSR.
- Use only for Web API access in small components.
- Avoid for data fetching or state management.