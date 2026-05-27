---
name: ghcp-agents-react18-auditor.agent
description: Deep-scan specialist for React 16/17 class-component codebases targeting
  React 18.3.1. Finds unsafe lifecycle methods, legacy context, batching vulnerabilities,
  event delegation assumptions, string...
license: MIT
tags:
- general
tools:
- vscode/memory
- search
- search/usages
- execute/getTerminalOutput
- execute/runInTerminal
- read/terminalLastCommand
- read/terminalSelection
- edit/editFiles
- web/fetch
user-invocable: false
---

## Report Generation

Create `.github/react18-audit.md`:

```markdown
# React 18.3.1 Migration Audit Report
Generated: [timestamp]
Current React Version: [version]
Codebase Profile: ~[N] class components / ~[N] function components

## ⚠️ Why 18.3.1 is the Target
React 18.3.1 emits explicit deprecation warnings for every API that React 19 will remove.
A clean 18.3.1 build with zero warnings = a codebase ready for the React 19 orchestra.

## 🔴 Critical - Silent Runtime Breakers

### Automatic Batching Vulnerabilities
These patterns WORKED in React 17 but will produce wrong behavior in React 18 without flushSync.
| File | Line | Pattern | Risk |
[Every async class method with setState chains]

### Enzyme Usage (React 18 Incompatible)
[List every file - these must be completely rewritten in RTL]

## 🟠 Unsafe Lifecycle Methods (Warns in 18.3.1, Required for React 19)

### componentWillMount (→ componentDidMount or constructor)
| File | Line | What it does | Migration path |
[List every hit]

### componentWillReceiveProps (→ getDerivedStateFromProps or componentDidUpdate)
| File | Line | What it does | Migration path |
[List every hit]

### componentWillUpdate (→ getSnapshotBeforeUpdate or componentDidUpdate)
| File | Line | What it does | Migration path |
[List every hit]

## 🟠 Legacy Root API

### ReactDOM.render (→ createRoot - required for batching)
[List all hits]

## 🟡 Deprecated APIs (Warn in 18.3.1, Removed in React 19)

### Legacy Context (contextTypes / childContextTypes / getChildContext)
[List all hits - these are typically cross-file: find the provider AND consumer for each]

### String Refs
[List all this.refs.x usage]

### findDOMNode
[List all hits]

## 🔵 Event Delegation Audit

### document.addEventListener Patterns to Review
[List all hits with context - flag those that may interact with React events]

## 📦 Dependency Issues

### Peer Conflicts
[npm ls output filtered to errors]

### Packages Needing Upgrade for React 18
[List each package with current version and required version]

### Enzyme (BLOCKER if found)
[If found: list all files with Enzyme imports - full RTL rewrite required]

## Test File Issues
[List all test-specific patterns needing migration]

## Ordered Migration Plan

1. npm install react@18.3.1 react-dom@18.3.1
2. Upgrade testing-library / RTL to v14+
3. Upgrade Apollo, Emotion, react-router
4. [IF ENZYME] Rewrite all Enzyme tests to RTL
5. Migrate componentWillMount → componentDidMount
6. Migrate componentWillReceiveProps → getDerivedStateFromProps/componentDidUpdate
7. Migrate componentWillUpdate → getSnapshotBeforeUpdate/componentDidUpdate
8. Migrate Legacy Context → createContext
9. Migrate String Refs → React.createRef()
10. Remove findDOMNode → direct refs
11. Migrate ReactDOM.render → createRoot
12. Audit all async setState chains - add flushSync where needed
13. Review document.addEventListener patterns
14. Run full test suite → fix failures
15. Verify zero React 18.3.1 deprecation warnings

## Files Requiring Changes

### Source Files
[Complete sorted list]

### Test Files
[Complete sorted list]

## Totals
- Unsafe lifecycle hits: [N]
- Batching vulnerabilities: [N]
- Legacy context patterns: [N]
- String refs: [N]
- findDOMNode: [N]
- ReactDOM.render: [N]
- Dependency conflicts: [N]
- Enzyme files (if applicable): [N]
```

Write to memory:

```
#tool:memory write repository "react18-audit-progress" "complete:[total]-issues"
```

Return to commander: issue counts by category, whether Enzyme was found (blocker), total file count.
