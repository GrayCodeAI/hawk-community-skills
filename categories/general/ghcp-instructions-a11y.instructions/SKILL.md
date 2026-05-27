---
name: ghcp-instructions-a11y.instructions
description: 'Skill: ghcp-instructions-a11y.instructions'
license: MIT
tags:
- general
---

## Accessibility Checklist (POUR)

### Perceivable
- [ ] All images have appropriate alt text (descriptive or empty for decorative)
- [ ] Videos have synchronized captions
- [ ] Page uses semantic landmarks: `<header>`, `<nav>`, `<main>`, `<footer>`
- [ ] Headings follow logical hierarchy (h1 > h2 > h3, no gaps)
- [ ] Text contrast meets 4.5:1 (normal) / 3:1 (large)
- [ ] UI component contrast meets 3:1
- [ ] Information not conveyed by color alone
- [ ] Content reflows at 320px without horizontal scroll
- [ ] `<html lang="...">` is set correctly
- [ ] Text resizable to 200% without loss of content

### Operable
- [ ] All functionality accessible via keyboard
- [ ] No keyboard traps (Escape closes overlays)
- [ ] Skip link provided as first focusable element
- [ ] Focus indicator visible on all interactive elements
- [ ] Focus order matches visual order
- [ ] Focus not obscured by sticky headers/footers
- [ ] Focus returned to trigger after modal close
- [ ] Touch targets at least 24x24 CSS px
- [ ] Animations respect `prefers-reduced-motion`
- [ ] No content flashes more than 3 times per second

### Understandable
- [ ] All form inputs have associated `<label>` or `aria-label`
- [ ] Error messages linked to inputs via `aria-describedby`
- [ ] Required fields indicated with `required` or `aria-required`
- [ ] Error summary or focus-on-first-error on submit failure
- [ ] No unexpected context changes on focus or input

### Robust
- [ ] All interactive elements have accessible name, role, and state
- [ ] ARIA roles have required properties
- [ ] No `aria-hidden="true"` on focusable elements
- [ ] Dynamic content announced via live regions
- [ ] SPA route changes announced to screen readers
- [ ] No redundant ARIA on native HTML elements
