---
name: ghcp-skeletons-skeleton-incremental-html
description: 'Skill: ghcp-skeletons-skeleton-incremental-html'
license: MIT
tags:
- general
---

**Fixed CSS variables (use in `<style>` block):**
```css
--red: #dc3545;    /* new vulnerability */
--green: #28a745;  /* fixed/improved */
--amber: #fd7e14;  /* previously unidentified */
--gray: #6c757d;   /* still present */
--accent: #2171b5; /* modified/info */
```

**Fixed rules:**
- ALL CSS in inline `<style>` block — no external stylesheets
- Include `@media print` styles
- Heatmap MUST have T1/T2/T3 columns after divider
- Metrics bar MUST include Trust Boundaries
- Status data in cards ONLY — not duplicated in metrics bar
- HTML threat/finding totals MUST match markdown STRIDE summary totals
