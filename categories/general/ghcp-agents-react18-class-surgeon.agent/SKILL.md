---
name: ghcp-agents-react18-class-surgeon.agent
description: Class component migration specialist for React 16/17 → 18.3.1. Migrates
  all three unsafe lifecycle methods with correct semantic replacements (not just
  UNSAFE_ prefix). Migrates legacy context to c...
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

After all files are processed:

```bash
echo "=== UNSAFE lifecycle check ==="
grep -rn "componentWillMount\b\|componentWillReceiveProps\b\|componentWillUpdate\b" \
  src/ --include="*.js" --include="*.jsx" | grep -v "UNSAFE_\|\.test\." | wc -l
echo "above should be 0"

echo "=== Legacy context check ==="
grep -rn "contextTypes\s*=\|childContextTypes\|getChildContext" \
  src/ --include="*.js" --include="*.jsx" | grep -v "\.test\." | wc -l
echo "above should be 0"

echo "=== String refs check ==="
grep -rn "this\.refs\." src/ --include="*.js" --include="*.jsx" | grep -v "\.test\." | wc -l
echo "above should be 0"

echo "=== ReactDOM.render check ==="
grep -rn "ReactDOM\.render\s*(" src/ --include="*.js" --include="*.jsx" | wc -l
echo "above should be 0"
```

Write final memory:

```
#tool:memory write repository "react18-class-surgery-progress" "complete:all-deprecated-count:0"
```

Return to commander: files changed, all deprecated counts confirmed at 0.
