---
name: ghcp-references-ci-publishing
description: 'Skill: ghcp-references-ci-publishing'
license: MIT
tags:
- general
---

## 8. Semver Change-Type Guide

| Change | Version bump | Example |
|---|---|---|
| Breaking API change (remove/rename public symbol) | MAJOR | `1.2.3 → 2.0.0` |
| New feature, fully backward-compatible | MINOR | `1.2.3 → 1.3.0` |
| Bug fix, no API change | PATCH | `1.2.3 → 1.2.4` |
| Pre-release | suffix | `2.0.0a1 → 2.0.0rc1 → 2.0.0` |
| Packaging-only fix (no code change) | post-release | `1.2.3 → 1.2.3.post1` |
