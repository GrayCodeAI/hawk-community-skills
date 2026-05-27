---
name: arb-designing-data-intensive-applications
description: 'Skill: arb-designing-data-intensive-applications'
license: MIT
tags:
- general
---

## Final Instruction

When uncertain, prefer the design that:
1. makes data ownership explicit
2. makes consistency semantics explicit
3. survives retries, duplicates, and replay
4. supports evolution without silent breakage
5. treats distributed systems trade-offs honestly

Do not hide distributed complexity behind local-looking code.
