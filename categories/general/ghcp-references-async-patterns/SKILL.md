---
name: ghcp-references-async-patterns
description: 'Skill: ghcp-references-async-patterns'
license: MIT
tags:
- general
---

## Common Migration Mistakes

```jsx
// WRONG - mixing async query with sync assertion:
const el = await screen.findByText('Result');
// el is already resolved here - findBy returns the element, not a promise
expect(await el).toBeInTheDocument(); // unnecessary second await

// CORRECT:
const el = await screen.findByText('Result');
expect(el).toBeInTheDocument();
// OR simply:
expect(await screen.findByText('Result')).toBeInTheDocument();
```

```jsx
// WRONG - using getBy* for elements that appear asynchronously:
fireEvent.click(button);
expect(screen.getByText('Loaded!')).toBeInTheDocument(); // throws before data loads

// CORRECT:
fireEvent.click(button);
expect(await screen.findByText('Loaded!')).toBeInTheDocument(); // waits
```
