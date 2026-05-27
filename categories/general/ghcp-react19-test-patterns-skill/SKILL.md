---
name: ghcp-react19-test-patterns-skill
description: Provides before/after patterns for migrating test files to React 19 compatibility,
  including act() imports, Simulate removal, and StrictMode call count changes.
license: MIT
tags:
- general
---

## 4. StrictMode Call Count Fixes

React 19 StrictMode no longer double-invokes `useEffect` in development. Spy assertions counting effect calls must be updated.

**Strategy  always measure, never guess:**
```bash
# Run the failing test, read the actual count from the error:
npm test -- --watchAll=false --testPathPattern="[filename]" --forceExit 2>&1 | grep -E "Expected|Received"
```

```jsx
// Before (React 18 StrictMode  effects ran twice):
expect(mockFn).toHaveBeenCalledTimes(2);  // 1 call × 2 (strict double-invoke)

// After (React 19 StrictMode  effects run once):
expect(mockFn).toHaveBeenCalledTimes(1);
```

```jsx
// Render-phase calls (component body)  still double-invoked in React 19 StrictMode:
expect(renderSpy).toHaveBeenCalledTimes(2);  // stays at 2 for render body calls
