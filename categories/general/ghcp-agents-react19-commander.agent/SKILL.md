---
name: ghcp-agents-react19-commander.agent
description: 'Skill: ghcp-agents-react19-commander.agent'
license: MIT
tags:
- general
---

## Migration Checklist (Tracked via Memory)

- [ ] Audit report generated
- [ ] <react@19.x.x> installed
- [ ] <react-dom@19.x.x> installed
- [ ] All peer dependency conflicts resolved
- [ ] @testing-library/react@16+ installed
- [ ] ReactDOM.render → createRoot
- [ ] ReactDOM.hydrate → hydrateRoot
- [ ] unmountComponentAtNode → root.unmount()
- [ ] findDOMNode removed
- [ ] forwardRef → ref as prop
- [ ] defaultProps → ES6 defaults
- [ ] Legacy Context → createContext
- [ ] String refs → createRef
- [ ] useRef() → useRef(null)
- [ ] act import fixed in all tests
- [ ] Simulate → fireEvent in all tests
- [ ] StrictMode call count assertions updated
- [ ] All tests passing (0 failures)
- [ ] Build succeeds
