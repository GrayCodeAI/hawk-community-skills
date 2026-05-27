---
name: mdc-next-js-15-async-request-api-rules
description: "Dictates how asynchronous requests should be handled within Next.js 15, specifically concerning runtime APIs."
license: MIT
tags: [react]
---

- Always use async versions of runtime APIs:
  typescript
  const cookieStore = await cookies()
  const headersList = await headers()
  const { isEnabled } = await draftMode()
  
- Handle async params in layouts/pages:
  typescript
  const params = await props.params
  const searchParams = await props.searchParams