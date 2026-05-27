---
name: lira-module-resolution
description: 'Skill: lira-module-resolution'
license: MIT
tags:
- general
---

## Antipatterns (Avoid)

* **Deep relative paths** (`../../../utils`) that break on refactors — replace with `#utils/...`.
* **Stringly-typed, scattered paths** — don’t hardcode file locations in many places; alias once.
* **Dynamic import without fallback** — leaves features broken silently; always handle `catch`.
* **Over-granular aliases** (`#utils/math/add.js`) — alias directories or stable entry points instead.
* **Mixing internal/external semantics** — don’t alias third-party packages under `#...`; keep them explicit.
