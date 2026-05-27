---
name: arb-working-effectively-with-legacy-code
description: 'Skill: arb-working-effectively-with-legacy-code'
license: MIT
tags:
- general
---

## Final Instruction

When uncertain, choose the smallest change that:
1. increases understanding
2. increases testability
3. breaks one hard dependency
4. preserves current behavior
5. makes the next change cheaper

Reject big rewrites and heroic cleanup when a seam and a test would do.
