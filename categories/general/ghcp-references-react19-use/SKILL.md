---
name: ghcp-references-react19-use
description: 'Skill: ghcp-references-react19-use'
license: MIT
tags:
- general
title: React 19 use() Hook Pattern Reference
---

## When NOT to use use()

- **Avoid during migration**  stabilize React 19 first
- **Complex dependencies**  if multiple promises or complex ordering logic, stick with `useEffect`
- **Retry logic**  `use()` doesn't handle retry; `useEffect` with state is clearer
- **Debounced updates**  `use()` refetches on every prop change; `useEffect` with cleanup is better
