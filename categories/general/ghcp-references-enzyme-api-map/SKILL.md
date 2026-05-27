---
name: ghcp-references-enzyme-api-map
description: 'Skill: ghcp-references-enzyme-api-map'
license: MIT
tags:
- general
---

## Before/After: Complete Component Test

```jsx
// Enzyme version:
import { shallow } from 'enzyme';

describe('LoginForm', () => {
  it('submits with credentials', () => {
    const mockSubmit = jest.fn();
    const wrapper = shallow(<LoginForm onSubmit={mockSubmit} />);

    wrapper.find('input[name="email"]').simulate('change', {
      target: { value: 'user@example.com' }
    });
    wrapper.find('input[name="password"]').simulate('change', {
      target: { value: 'password123' }
    });
    wrapper.find('button[type="submit"]').simulate('click');

    expect(wrapper.state('loading')).toBe(true);
    expect(mockSubmit).toHaveBeenCalledWith({
      email: 'user@example.com',
      password: 'password123'
    });
  });
});
```

```jsx
// RTL version:
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

describe('LoginForm', () => {
  it('submits with credentials', async () => {
    const mockSubmit = jest.fn();
    const user = userEvent.setup();
    render(<LoginForm onSubmit={mockSubmit} />);

    await user.type(screen.getByLabelText(/email/i), 'user@example.com');
    await user.type(screen.getByLabelText(/password/i), 'password123');
    await user.click(screen.getByRole('button', { name: /submit/i }));

    // Assert on visible output - not on state
    expect(screen.getByRole('button', { name: /submit/i })).toBeDisabled(); // loading state
    expect(mockSubmit).toHaveBeenCalledWith({
      email: 'user@example.com',
      password: 'password123'
    });
  });
});
```
