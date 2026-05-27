---
name: ghcp-references-componentwillmount
description: 'Skill: ghcp-references-componentwillmount'
license: MIT
tags:
- general
---

## Multiple Patterns in One Method

If a single `componentWillMount` does both state init AND side effects:

```jsx
// Mixed - state init + fetch
componentWillMount() {
  this.setState({ loading: true, items: [] });              // Case A
  fetch('/api/items').then(r => r.json())                   // Case B
    .then(items => this.setState({ items, loading: false }));
}
```

Split them:

```jsx
constructor(props) {
  super(props);
  this.state = { loading: true, items: [] }; // Case A → constructor
}

componentDidMount() {
  fetch('/api/items').then(r => r.json())    // Case B → componentDidMount
    .then(items => this.setState({ items, loading: false }));
}
```
