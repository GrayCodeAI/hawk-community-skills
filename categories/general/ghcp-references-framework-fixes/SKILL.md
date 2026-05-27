---
name: ghcp-references-framework-fixes
description: 'Skill: ghcp-references-framework-fixes'
license: MIT
tags:
- general
---

## Debugging Techniques

### Visualizing Element Boundaries

```css
/* Use only during development */
* {
  outline: 1px solid red !important;
}
```

### Detecting Overflow

```javascript
// Run in console to detect overflow elements
document.querySelectorAll('*').forEach(el => {
  if (el.scrollWidth > el.clientWidth) {
    console.log('Horizontal overflow:', el);
  }
  if (el.scrollHeight > el.clientHeight) {
    console.log('Vertical overflow:', el);
  }
});
```

### Checking Contrast Ratio

```javascript
// Use Chrome DevTools Lighthouse or axe DevTools
// Or check at the following site:
// https://webaim.org/resources/contrastchecker/
```
