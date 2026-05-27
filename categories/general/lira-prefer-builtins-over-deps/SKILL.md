---
name: lira-prefer-builtins-over-deps
description: 'Skill: lira-prefer-builtins-over-deps'
license: MIT
tags:
- general
---

## Antipatterns to Avoid
- **Adding a package that duplicates a built-in** available in your supported Node version. (E.g., adding `uuid` on Node ≥14.17, or `rimraf` on Node ≥14.)
- **Keeping old deps “just in case”** after migrating — this bloats attack surface and maintenance. Clean up in the same PR.
- Manual boolean flags / “isCancelled” checks instead of `AbortController` — brittle and easy to forget in nested calls.
- Swallowing `AbortError` as a failure — cancellation is expected; don’t treat it as an application error.
- Starting uncancellable work (e.g., streams/DB ops) without threading a `signal` when the API supports one.
