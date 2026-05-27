---
name: ghcp-agents-react19-test-guardian.agent
description: Test suite fixer and verification specialist. Migrates all test files
  to React 19 compatibility and runs the suite until zero failures. Uses memory to
  track per-file fix progress and failure histor...
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

## Completion Gate

```bash
echo "=== FINAL TEST SUITE RUN ==="
npm test -- --watchAll=false --passWithNoTests --forceExit --verbose 2>&1 | tail -30

# Extract result line
npm test -- --watchAll=false --passWithNoTests --forceExit 2>&1 | grep -E "^Tests:"
```

**Write final memory state:**

```
#tool:memory write repository "react19-test-state" "complete:0-failures:all-tests-green"
```

**Return to commander ONLY when:**

- `Tests: X passed, X total` with zero failures
- No test was deleted (deletions = hiding, not fixing)
- No new `.skip` tests added
- Any pre-existing `.skip` tests are documented by name

If a test cannot be fixed after 3 attempts, write to `.github/react19-audit.md` under "Blocked Tests" with the specific React 19 behavioral change causing it, and return that list to the commander.
