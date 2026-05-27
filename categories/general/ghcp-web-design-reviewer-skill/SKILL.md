---
name: ghcp-web-design-reviewer-skill
description: This skill enables visual inspection of websites running locally or remotely
  to identify and fix design issues. Triggers on requests like "review website design",
  "check the UI", "fix the layout", ...
license: MIT
tags:
- general
---

## Troubleshooting

### Problem: Style files not found

1. Check dependencies in `package.json`
2. Consider the possibility of CSS-in-JS
3. Consider CSS generated at build time
4. Ask user about styling method

### Problem: Fixes not reflected

1. Check if development server HMR is working
2. Clear browser cache
3. Rebuild if project requires build
4. Check CSS specificity issues

### Problem: Fixes affecting other areas

1. Rollback changes
2. Use more specific selectors
3. Consider using CSS Modules or scoped styles
4. Consult user to confirm impact scope
