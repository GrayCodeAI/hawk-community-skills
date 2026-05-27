---
name: ghcp-references-componentwillreceiveprops
description: 'Skill: ghcp-references-componentwillreceiveprops'
license: MIT
tags:
- general
---

## getDerivedStateFromProps - Traps and Warnings

### Trap 1: It fires on EVERY render, not just prop changes

Unlike `componentWillReceiveProps`, `getDerivedStateFromProps` is called before every render - including `setState` calls. Always compare against previous values stored in state.

```jsx
// WRONG - fires on every render, including setState triggers
static getDerivedStateFromProps(props, state) {
  return { sortedItems: sort(props.items) }; // re-sorts on every setState!
}

// CORRECT - only updates when items reference changes
static getDerivedStateFromProps(props, state) {
  if (props.items !== state.prevItems) {
    return { sortedItems: sort(props.items), prevItems: props.items };
  }
  return null;
}
```

### Trap 2: It cannot access `this`

`getDerivedStateFromProps` is a static method. No `this.props`, no `this.state`, no instance methods.

```jsx
// WRONG - no this in static method
static getDerivedStateFromProps(props, state) {
  return { value: this.computeValue(props) }; // ReferenceError
}

// CORRECT - pure function of props + state
static getDerivedStateFromProps(props, state) {
  return { value: computeValue(props) }; // standalone function
}
```

### Trap 3: Don't use it for side effects

If you need to fetch when a prop changes - use `componentDidUpdate`. `getDerivedStateFromProps` must be pure.

### When getDerivedStateFromProps is actually the wrong tool

If you find yourself doing complex logic in `getDerivedStateFromProps`, consider whether the consuming component should receive pre-processed data as a prop instead. The pattern exists for narrow use cases, not general prop-to-state syncing.
