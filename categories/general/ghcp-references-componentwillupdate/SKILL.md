---
name: ghcp-references-componentwillupdate
description: 'Skill: ghcp-references-componentwillupdate'
license: MIT
tags:
- general
---

## Both Cases in One Component

If a component had both DOM-reading AND side effects in `componentWillUpdate`:

```jsx
// Before: does both
componentWillUpdate(nextProps) {
  // DOM read
  if (isExpanding(nextProps)) {
    this.savedHeight = this.ref.current.offsetHeight;
  }
  // Side effect
  if (nextProps.query !== this.props.query) {
    this.request?.cancel();
  }
}
```

After: split into both patterns:

```jsx
// DOM read → getSnapshotBeforeUpdate
getSnapshotBeforeUpdate(prevProps, prevState) {
  if (isExpanding(this.props)) {
    return { height: this.ref.current.offsetHeight };
  }
  return null;
}

// Side effect → componentDidUpdate
componentDidUpdate(prevProps, prevState, snapshot) {
  // Handle snapshot if present
  if (snapshot !== null) { /* ... */ }

  // Handle side effect
  if (prevProps.query !== this.props.query) {
    this.request?.cancel();
    this.startNewRequest();
  }
}
```
