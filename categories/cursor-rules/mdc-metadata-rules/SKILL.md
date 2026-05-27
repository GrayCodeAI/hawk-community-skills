---
name: mdc-metadata-rules
description: "Rules for defining metadata in Next.js 14 components for SEO optimization."
license: MIT
tags: [cursor-rules]
---

- For metadata (in .tsx files):
  tsx
  import type { Metadata } from 'next'
  export const metadata: Metadata = {
    title: 'Page Title',
    description: 'Page description',
  }