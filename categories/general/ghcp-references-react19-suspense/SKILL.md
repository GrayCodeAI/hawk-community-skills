---
name: ghcp-references-react19-suspense
description: 'Skill: ghcp-references-react19-suspense'
license: MIT
tags:
- general
title: React 19 Suspense for Data Fetching Pattern Reference
---

## Important Warnings

1. **Still Preview**  Suspense for data is marked experimental, behavior may change
2. **Performance**  promises are recreated on every render without memoization; use `useMemo`
3. **Cache**  `use()` doesn't cache; use React Query or similar for production apps
4. **SSR**  Suspense SSR support is limited; check Next.js version requirements
