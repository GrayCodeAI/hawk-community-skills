---
name: agc-implementation
description: 'Skill: agc-implementation'
license: MIT
tags:
- general
---

## Print styles

```css
@media print {
  .demo-panel, .demo-interstitial { display: none !important; }
}
```

## Accessibility

```html
<div id="narrator" class="demo-narrator" role="status" aria-live="polite"></div>
```

Add `role="status"` and `aria-live="polite"` to the narrator element so screen readers announce the narration text as it changes.
