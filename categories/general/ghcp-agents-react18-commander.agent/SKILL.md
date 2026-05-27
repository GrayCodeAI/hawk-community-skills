---
name: ghcp-agents-react18-commander.agent
description: Master orchestrator for React 16/17 → 18.3.1 migration. Designed for
  class-component-heavy codebases. Coordinates audit, dependency upgrade, class component
  surgery, automatic batching fixes, and t...
license: MIT
tags:
- general
tools:
- agent
- vscode/memory
- edit/editFiles
- execute/getTerminalOutput
- execute/runInTerminal
- read/terminalLastCommand
- read/terminalSelection
- search
- search/usages
- read/problems
agents:
- react18-auditor
- react18-dep-surgeon
- react18-class-surgeon
- react18-batching-fixer
- react18-test-guardian
argument-hint: Just activate to start the React 18 migration.
---

## Migration Checklist

- [ ] Audit report generated (.github/react18-audit.md)
- [ ] react@18.3.1 + react-dom@18.3.1 installed
- [ ] @testing-library/react@14+ installed
- [ ] All peer deps resolved (npm ls: 0 errors)
- [ ] componentWillMount → componentDidMount / constructor
- [ ] componentWillReceiveProps → getDerivedStateFromProps / componentDidUpdate
- [ ] componentWillUpdate → getSnapshotBeforeUpdate / componentDidUpdate
- [ ] Legacy context → createContext
- [ ] String refs → React.createRef()
- [ ] findDOMNode → direct refs
- [ ] ReactDOM.render → createRoot
- [ ] ReactDOM.hydrate → hydrateRoot
- [ ] Automatic batching regressions identified and fixed (flushSync where needed)
- [ ] Event delegation assumptions audited
- [ ] All tests passing (0 failures)
- [ ] Build succeeds
- [ ] Zero React 18.3.1 deprecation warnings
