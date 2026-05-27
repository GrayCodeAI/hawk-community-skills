---
name: mdc-next-js-page-rules
description: "Specific rules for Next.js pages, including routing, data fetching, and image optimization."
license: MIT
tags: [react]
---

- Use dynamic routes with bracket notation ([id].tsx)
- Validate and sanitize route parameters
- Prefer flat, descriptive routes
- Use getServerSideProps for dynamic data, getStaticProps/getStaticPaths for static
- Implement Incremental Static Regeneration (ISR) where appropriate
- Use next/image for optimized images
- Configure image layout, priority, sizes, and srcSet attributes