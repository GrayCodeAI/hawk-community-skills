---
name: ghcp-references-commit-classification
description: 'Skill: ghcp-references-commit-classification'
license: MIT
tags:
- general
---

## Mapping categories to Keep a Changelog sections

| Category | Changelog section |
|---|---|
| `breaking` + new behavior | Changed |
| `breaking` + removal | Removed |
| `feat` | Added |
| `fix`, `perf` | Fixed |
| `security` | Security |
| `refactor`, `docs`, `chore`, `test` | Omit (unless user-visible) |

**User-visible refactor example:** Extracting a previously internal helper into a
new public export → treat as Added, not Refactor.
