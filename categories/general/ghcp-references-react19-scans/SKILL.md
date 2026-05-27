---
name: ghcp-references-react19-scans
description: 'Skill: ghcp-references-react19-scans'
license: MIT
tags:
- general
---

## Full Summary Script

```bash
#!/bin/bash
echo "=============================="
echo "React 19 Migration Audit Summary"
echo "=============================="
echo ""
echo "REMOVED APIs (Critical):"
echo "  ReactDOM.render:             $(grep -rn "ReactDOM\.render\s*(" src/ --include="*.js" --include="*.jsx" | wc -l | tr -d ' ') hits"
echo "  ReactDOM.hydrate:            $(grep -rn "ReactDOM\.hydrate\s*(" src/ --include="*.js" --include="*.jsx" | wc -l | tr -d ' ') hits"
echo "  unmountComponentAtNode:      $(grep -rn "unmountComponentAtNode" src/ --include="*.js" --include="*.jsx" | wc -l | tr -d ' ') hits"
echo "  findDOMNode:                 $(grep -rn "findDOMNode" src/ --include="*.js" --include="*.jsx" | wc -l | tr -d ' ') hits"
echo "  react-dom/test-utils:        $(grep -rn "from 'react-dom/test-utils'" src/ --include="*.js" --include="*.jsx" | wc -l | tr -d ' ') hits"
echo "  Legacy context:              $(grep -rn "contextTypes\|childContextTypes\|getChildContext" src/ --include="*.js" --include="*.jsx" | grep -v "\.test\." | wc -l | tr -d ' ') hits"
echo "  String refs:                 $(grep -rn "this\.refs\." src/ --include="*.js" --include="*.jsx" | grep -v "\.test\." | wc -l | tr -d ' ') hits"
echo ""
echo "DEPRECATED APIs:"
echo "  forwardRef:                  $(grep -rn "forwardRef" src/ --include="*.js" --include="*.jsx" | grep -v "\.test\." | wc -l | tr -d ' ') hits"
echo "  defaultProps (fn comps):     $(grep -rn "\.defaultProps\s*=" src/ --include="*.js" --include="*.jsx" | grep -v "\.test\." | wc -l | tr -d ' ') hits"
echo "  useRef() no arg:             $(grep -rn "useRef()" src/ --include="*.js" --include="*.jsx" | grep -v "\.test\." | wc -l | tr -d ' ') hits"
echo ""
echo "TEST FILE ISSUES:"
echo "  react-dom/test-utils:        $(grep -rn "from 'react-dom/test-utils'" src/ --include="*.test.*" --include="*.spec.*" | wc -l | tr -d ' ') hits"
echo "  Simulate usage:              $(grep -rn "Simulate\." src/ --include="*.test.*" | wc -l | tr -d ' ') hits"
```
