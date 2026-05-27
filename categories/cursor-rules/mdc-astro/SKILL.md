---
name: mdc-astro
description: This guide provides opinionated, actionable best practices for building
  high-performance Astro applications, focusing on zero-JavaScript by default, island
  architecture, and type safety.
license: MIT
tags:
- cursor-rules
---

<Layout title="My Page">
  <header>
    <UserProfile client:load user={user} /> {/* Pass server data as props */}
  </header>
  <main>
    <!-- ... other static content and localized islands -->
  </main>
</Layout>
```

## 6. Accessibility

Build accessible experiences from the ground up.

### 6.1 Semantic HTML

Always use appropriate HTML5 semantic elements.

❌ BAD
```html
<div onclick="doSomething()">Click me</div>
```

✅ GOOD
```html
<button type="button" onclick="doSomething()">Click me</button>
```

### 6.2 ARIA Attributes

Apply ARIA attributes when native HTML semantics are insufficient, especially for complex interactive widgets within islands.

```jsx
// src/components/react/AccessibleAccordion.tsx
<div role="region" aria-labelledby="accordion-header">
  <h3 id="accordion-header">
    <button aria-expanded={isOpen} aria-controls="accordion-panel" onClick={toggle}>
      Section Title
    </button>
  </h3>
  {isOpen && <div id="accordion-panel" role="region">...</div>}
</div>
```

### 6.3 Image Alt Text

All `<img>` tags must have descriptive `alt` attributes.

❌ BAD
```html
<img src="/image.jpg" alt="">
```

✅ GOOD
```html
<img src="/image.jpg" alt="A detailed description of the image content.">
```

## 7. Testing Approaches

Implement a robust testing strategy that covers both static content and interactive islands.

### 7.1 Type Checking

Run `astro check` as part of your CI pipeline to catch TypeScript errors early.

```bash
# In your CI script
npm run astro check
```

### 7.2 Linting

Enforce code style and catch common errors with ESLint, including `eslint-plugin-astro`.

**`.eslintrc.cjs`**
```javascript
module.exports = {
  extends: [
    'eslint:recommended',
    'plugin:astro/recommended',
    'plugin:react/recommended', // If using React
    'plugin:@typescript-eslint/recommended' // If using TypeScript
  ],
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
    project: './tsconfig.json',
    extraFileExtensions: ['.astro']
  },
  rules: {
    // Custom rules
  },
  overrides: [
    {
      files: ['*.astro'],
      parser: 'astro-eslint-parser',
      parserOptions: {
        parser: '@typescript-eslint/parser',
        extraFileExtensions: ['.astro']
      }
    }
  ],
  settings: {
    react: {
      version: 'detect'
    }
  }
};
```

### 7.3 Unit Testing Islands

Test interactive UI framework components (islands) using their native testing libraries (e.g., React Testing Library, Vue Test Utils).

```tsx
// src/components/react/MyReactCounter.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import MyReactCounter from './MyReactCounter';

test('increments count on button click', () => {
  render(<MyReactCounter />);
  const button = screen.getByRole('button', { name: /increment/i });
  const countDisplay = screen.getByText(/count: 0/i);

  expect(countDisplay).toBeInTheDocument();
  fireEvent.click(button);
  expect(screen.getByText(/count: 1/i)).toBeInTheDocument();
});
```

### 7.4 End-to-End (E2E) Testing

Use Playwright or Cypress for E2E tests to verify page rendering, navigation, and island hydration in a real browser environment.

```javascript
// tests/example.spec.ts (Playwright)
import { test, expect } from '@playwright/test';

test('basic page loads and counter works', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('h1')).toHaveText('Hello, Astro!');

  // Interact with the React island
  const counterButton = page.getByRole('button', { name: 'Increment' });
  await expect(page.getByText('Count: 0')).toBeVisible();
  await counterButton.click();
  await expect(page.getByText('Count: 1')).toBeVisible();
});
```
