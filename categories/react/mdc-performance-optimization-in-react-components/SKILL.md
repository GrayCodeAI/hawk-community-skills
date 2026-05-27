---
name: mdc-performance-optimization-in-react-components
description: "Applies performance optimization techniques specifically to React components, focusing on minimizing client-side rendering and optimizing resource loading."
license: MIT
tags: [react]
---

- Minimize 'use client', 'useEffect', and 'setState'; favor React Server Components (RSC)
- Wrap client components in Suspense with fallback
- Use dynamic loading for non-critical components
- Optimize images: use WebP format, include size data, implement lazy loading