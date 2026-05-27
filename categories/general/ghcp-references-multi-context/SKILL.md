---
name: ghcp-references-multi-context
description: 'Skill: ghcp-references-multi-context'
license: MIT
tags:
- general
---

## Verification After All Contexts Migrated

```bash
# Should return zero hits for legacy context patterns
echo "=== childContextTypes ==="
grep -rn "childContextTypes" src/ --include="*.js" --include="*.jsx" | grep -v "\.test\." | wc -l

echo "=== contextTypes (legacy) ==="
grep -rn "^\s*static contextTypes\s*=\|contextTypes\.propTypes" src/ --include="*.js" | grep -v "\.test\." | wc -l

echo "=== getChildContext ==="
grep -rn "getChildContext" src/ --include="*.js" --include="*.jsx" | grep -v "\.test\." | wc -l

echo "All three should be 0"
```

Note: `static contextType` (singular) is the MODERN API - that's correct. Only `contextTypes` (plural) is legacy.
