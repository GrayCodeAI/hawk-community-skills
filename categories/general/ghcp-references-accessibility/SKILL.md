---
name: ghcp-references-accessibility
description: 'Skill: ghcp-references-accessibility'
license: MIT
tags:
- general
---

## ARIA Quick Reference

### Roles

| Role | Purpose |
| ---- | ------- |
| `button` | Clickable button |
| `link` | Navigation link |
| `dialog` | Modal dialog |
| `alert` | Important message |
| `navigation` | Navigation region |
| `main` | Main content |
| `search` | Search functionality |
| `tab/tablist/tabpanel` | Tab interface |

### Properties

| Property | Purpose |
| -------- | ------- |
| `aria-label` | Accessible name |
| `aria-labelledby` | Reference to labeling element |
| `aria-describedby` | Reference to description |
| `aria-hidden` | Hide from assistive tech |
| `aria-expanded` | Expandable state |
| `aria-selected` | Selection state |
| `aria-disabled` | Disabled state |
| `aria-required` | Required field |
| `aria-invalid` | Invalid input |

### Golden Rule

**First rule of ARIA:** Don't use ARIA if native HTML works.

```text
✗ <div role="button" tabindex="0">Click</div>
✓ <button>Click</button>

```
