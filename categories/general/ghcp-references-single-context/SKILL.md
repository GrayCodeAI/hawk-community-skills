---
name: ghcp-references-single-context
description: 'Skill: ghcp-references-single-context'
license: MIT
tags:
- general
---

### Verification Checklist

After migrating one context:

```bash
# Provider - no legacy context exports remain
grep -n "childContextTypes\|getChildContext" src/ThemeProvider.js

# Consumers - no legacy context consumption remains
grep -rn "contextTypes\s*=" src/ --include="*.js" --include="*.jsx" | grep -v "ThemeContext\|\.test\."

# this.context usage - confirm it reads from contextType not legacy
grep -rn "this\.context\." src/ --include="*.js" | grep -v "\.test\."
```

Each should return zero hits for the migrated context.
