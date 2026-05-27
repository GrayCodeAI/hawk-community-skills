---
name: ghcp-references-patterns
description: 'Skill: ghcp-references-patterns'
license: MIT
tags:
- general
---

## Ref Passed to a Child Component {#forwarded-refs}

If a string ref was passed to a custom component (not a DOM element), the migration also requires updating the child.

```jsx
// Before:
class Parent extends React.Component {
  handleClick() {
    this.refs.myInput.focus(); // Parent accesses child's DOM node
  }
  render() {
    return (
      <div>
        <MyInput ref="myInput" />
        <button onClick={() => this.handleClick()}>Focus</button>
      </div>
    );
  }
}

// MyInput.js (child - class component):
class MyInput extends React.Component {
  render() {
    return <input className="my-input" />;
  }
}
```

```jsx
// After:
class Parent extends React.Component {
  myInputRef = React.createRef();

  handleClick() {
    this.myInputRef.current.focus();
  }

  render() {
    return (
      <div>
        {/* React 18: forwardRef needed. React 19: ref is a direct prop */}
        <MyInput ref={this.myInputRef} />
        <button onClick={() => this.handleClick()}>Focus</button>
      </div>
    );
  }
}

// MyInput.js (React 18 - use forwardRef):
import { forwardRef } from 'react';
const MyInput = forwardRef(function MyInput(props, ref) {
  return <input ref={ref} className="my-input" />;
});

// MyInput.js (React 19 - ref as direct prop, no forwardRef):
function MyInput({ ref, ...props }) {
  return <input ref={ref} className="my-input" />;
}
```

---
