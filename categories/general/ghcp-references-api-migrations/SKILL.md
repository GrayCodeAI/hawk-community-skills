---
name: ghcp-references-api-migrations
description: 'Skill: ghcp-references-api-migrations'
license: MIT
tags:
- general
title: React 19 API Migrations Reference
---

## Complete Migration Checklist

```bash
# 1. Find all ReactDOM.render calls:
grep -rn "ReactDOM.render" src/ --include="*.js" --include="*.jsx"
# Should be converted to createRoot

# 2. Find all ReactDOM.hydrate calls:
grep -rn "ReactDOM.hydrate" src/ --include="*.js" --include="*.jsx"
# Should be converted to hydrateRoot

# 3. Find all forwardRef usages:
grep -rn "forwardRef" src/ --include="*.js" --include="*.jsx"
# Check each one to see if it can be removed (most can)

# 4. Find all .defaultProps assignments:
grep -rn "\.defaultProps\s*=" src/ --include="*.js" --include="*.jsx"
# Replace with ES6 default params

# 5. Find all useRef() without initial value:
grep -rn "useRef()" src/ --include="*.js" --include="*.jsx"
# Add null: useRef(null)

# 6. Find old context (contextTypes):
grep -rn "contextTypes\|childContextTypes\|getChildContext" src/ --include="*.js" --include="*.jsx"
# Migrate to createContext

# 7. Find string refs (ref="name"):
grep -rn 'ref="' src/ --include="*.js" --include="*.jsx"
# Migrate to createRef or callback ref

# 8. Find unused React imports:
grep -rn "^import React from 'react';" src/ --include="*.js" --include="*.jsx"
# Check if React is used in the file
```
