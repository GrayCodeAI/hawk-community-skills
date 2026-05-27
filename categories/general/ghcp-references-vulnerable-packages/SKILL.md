---
name: ghcp-references-vulnerable-packages
description: 'Skill: ghcp-references-vulnerable-packages'
license: MIT
tags:
- general
---

## General Red Flags (Any Ecosystem)

Flag any dependency that:
1. Has not been updated in > 2 years AND has > 10 open security issues
2. Has been deprecated by its maintainer with a security advisory
3. Is a fork of a known package from an unknown publisher (typosquatting)
4. Has a name that's one character off from a popular package (e.g., `lodash` vs `1odash`)
5. Was recently transferred to a new owner (check git history / npm transfer notices)
