---
name: ghcp-references-platform-guidelines
description: 'Skill: ghcp-references-platform-guidelines'
license: MIT
tags:
- general
---

## Cross-Platform Considerations

### Shared Principles

- Consistent brand identity
- Same core user flows
- Synchronized data/state
- Familiar information architecture

### Platform-Specific Adaptations

| Aspect | iOS | Android | Web |
| ------ | --- | ------- | --- |
| Back | Left nav | Left or gesture | Browser back |
| Primary action | Right nav | FAB | Top right button |
| Lists | Swipe actions | Long press | Hover actions |
| Menus | Action sheets | Bottom sheet | Dropdown/context |
| Alerts | Centered modal | Centered modal | Various positions |

### Design Tokens Across Platforms

Create platform-agnostic tokens:

```text
// Spacing
spacing-sm: 8
spacing-md: 16
spacing-lg: 24

// These map to platform units
iOS: points (pt)
Android: density-independent pixels (dp)
Web: pixels (px) or rem

```
