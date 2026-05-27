---
name: ghcp-agents-react19-migrator
description: Source code migration engine. Rewrites every deprecated React pattern
  to React 19 APIs - forwardRef, defaultProps, ReactDOM.render, legacy context, string
  refs, useRef(). Uses memory to checkpoint ...
license: MIT
tags:
- general
tools:
- vscode/memory
- edit/editFiles
- execute/getTerminalOutput
- execute/runInTerminal
- read/terminalLastCommand
- read/terminalSelection
- search
- search/usages
- read/problems
user-invocable: false
---

## Completion Verification

After all files processed, run:

```bash
echo "=== Deprecated pattern check ==="
grep -rn "ReactDOM\.render\s*(\|ReactDOM\.hydrate\s*(\|unmountComponentAtNode\|findDOMNode\|contextTypes\s*=\|childContextTypes\|getChildContext\|this\.refs\." \
  src/ --include="*.js" --include="*.jsx" | grep -v "\.test\." | wc -l
echo "above should be 0"

# forwardRef is optional modernization - migrations are not required
grep -rn "forwardRef\s*(" src/ --include="*.js" --include="*.jsx" | grep -v "\.test\." | wc -l
echo "forwardRef remaining (optional - no requirement for 0)"

grep -rn "useRef()" src/ --include="*.js" --include="*.jsx" | grep -v "\.test\." | wc -l
echo "useRef() without arg (should be 0)"
```

Write final memory:

```
#tool:memory write repository "react19-migration-progress" "complete:all-files-migrated:deprecated-count:0"
```

Return to commander: count of files changed, confirmation that deprecated pattern count is 0.
