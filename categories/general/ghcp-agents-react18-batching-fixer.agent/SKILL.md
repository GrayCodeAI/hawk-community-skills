---
name: ghcp-agents-react18-batching-fixer.agent
description: Automatic batching regression specialist. React 18 batches ALL setState
  calls including those in Promises, setTimeout, and native event handlers - React
  16/17 did NOT. Class components with async s...
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

## Completion Report

```bash
echo "=== Checking for this.state reads after await ==="
grep -rn -A 30 "async\s" src/ --include="*.js" --include="*.jsx" | grep -B5 "this\.state\." | grep "await" | grep -v "\.test\." | wc -l
echo "potential batching reads remaining (aim for 0)"
```

Write to audit file:

```bash
cat >> .github/react18-audit.md << 'EOF'

## Automatic Batching Fix Status
- Async methods reviewed: [N]
- flushSync insertions: [N]
- Refactored (no flushSync needed): [N]
- Test patterns flagged for test-guardian: [N]
EOF
```

Write final memory:

```
#tool:memory write repository "react18-batching-progress" "complete:flushSync-insertions:[N]"
```

Return to commander: count of fixes applied, flushSync insertions, any remaining concerns.
