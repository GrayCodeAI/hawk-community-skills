---
name: ghcp-references-dep-scans
description: 'Skill: ghcp-references-dep-scans'
license: MIT
tags:
- general
---

## Lock File Consistency

```bash
# Check lockfile is in sync with package.json
npm ls --depth=0 2>&1 | head -20

# Check for duplicate react installs (can cause hooks errors)
find node_modules -name "package.json" -path "*/react/package.json" 2>/dev/null \
  | grep -v "node_modules/node_modules" \
  | xargs grep '"version"' | sort -u
```
