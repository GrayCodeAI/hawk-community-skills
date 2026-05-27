---
name: ghcp-references-batching-categories
description: 'Skill: ghcp-references-batching-categories'
license: MIT
tags:
- general
---

## Test Patterns That Break Due to Batching

```jsx
// Before (React 17 - intermediate state was synchronously visible):
it('shows saving indicator', () => {
  render(<AutoSaveForm />);
  fireEvent.change(input, { target: { value: 'new text' } });
  expect(screen.getByText('Saving...')).toBeInTheDocument(); // ← sync check
});

// After (React 18 - use waitFor for intermediate states):
it('shows saving indicator', async () => {
  render(<AutoSaveForm />);
  fireEvent.change(input, { target: { value: 'new text' } });
  await waitFor(() => expect(screen.getByText('Saving...')).toBeInTheDocument());
  await waitFor(() => expect(screen.getByText('Saved')).toBeInTheDocument());
});
```
