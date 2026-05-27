---
name: ghcp-references-test-scans
description: 'Skill: ghcp-references-test-scans'
license: MIT
tags:
- general
---

## Async Scans

```bash
# act() usage
grep -rn "\bact(" \
  src/ --include="*.test.*" --include="*.spec.*" 2>/dev/null

# waitFor usage (good - check these are properly async)
grep -rn "waitFor\|findBy" \
  src/ --include="*.test.*" --include="*.spec.*" | wc -l

# setTimeout in tests (may be batching-sensitive)
grep -rn "setTimeout\|setInterval" \
  src/ --include="*.test.*" --include="*.spec.*" 2>/dev/null
```
