---
name: mdc-next-js-15-state-management-rules
description: "Defines the recommended state management strategies for Next.js 15 applications, including server and client contexts."
license: MIT
tags: [react]
---

- Use `useActionState` instead of deprecated `useFormState`.
- Leverage enhanced `useFormStatus` with new properties (data, method, action).
- Implement URL state management with 'nuqs'.
- Minimize client-side state.