---
name: ghcp-references-react18-scans
description: 'Skill: ghcp-references-react18-scans'
license: MIT
tags:
- general
---

## Full Summary Script

Run this for a quick overview before detailed scanning:

```bash
#!/bin/bash
echo "=============================="
echo "React 18 Migration Audit Summary"
echo "=============================="
echo ""
echo "LIFECYCLE METHODS:"
echo "  componentWillMount:          $(grep -rn "componentWillMount\b" src/ --include="*.js" --include="*.jsx" | grep -v "UNSAFE_\|\.test\." | wc -l | tr -d ' ') hits"
echo "  componentWillReceiveProps:   $(grep -rn "componentWillReceiveProps\b" src/ --include="*.js" --include="*.jsx" | grep -v "UNSAFE_\|\.test\." | wc -l | tr -d ' ') hits"
echo "  componentWillUpdate:         $(grep -rn "componentWillUpdate\b" src/ --include="*.js" --include="*.jsx" | grep -v "UNSAFE_\|\.test\." | wc -l | tr -d ' ') hits"
echo ""
echo "LEGACY APIS:"
echo "  Legacy context (providers):  $(grep -rn "childContextTypes" src/ --include="*.js" --include="*.jsx" | grep -v "\.test\." | wc -l | tr -d ' ') hits"
echo "  String refs (this.refs):     $(grep -rn "this\.refs\." src/ --include="*.js" --include="*.jsx" | grep -v "\.test\." | wc -l | tr -d ' ') hits"
echo "  findDOMNode:                 $(grep -rn "findDOMNode" src/ --include="*.js" --include="*.jsx" | grep -v "\.test\." | wc -l | tr -d ' ') hits"
echo "  ReactDOM.render:             $(grep -rn "ReactDOM\.render\s*(" src/ --include="*.js" --include="*.jsx" | wc -l | tr -d ' ') hits"
echo ""
echo "ENZYME (BLOCKER):"
echo "  Enzyme test files:           $(grep -rl "from 'enzyme'" src/ --include="*.test.*" 2>/dev/null | wc -l | tr -d ' ') files"
echo ""
echo "ASYNC BATCHING RISK:"
echo "  Async class methods:         $(grep -rn "^\s*async [a-zA-Z]" src/ --include="*.js" --include="*.jsx" | grep -v "\.test\." | wc -l | tr -d ' ') hits"
```
