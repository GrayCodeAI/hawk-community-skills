---
name: ghcp-references-example-configs
description: 'Skill: ghcp-references-example-configs'
license: MIT
tags:
- general
---

## 12. Target Non-Default Branch

Test updates on a development branch before production:

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    target-branch: "develop"
    labels:
      - "dependencies"
      - "staging"

  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    target-branch: "develop"
```

Note: Security updates always target the default branch regardless of `target-branch`.
