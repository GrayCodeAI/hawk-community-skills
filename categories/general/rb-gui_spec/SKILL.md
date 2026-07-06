---
name: rb-gui_spec
description: "Generate and maintain GUI specifications for desktop and web applications."
license: MIT
tags: [general]
---

## Overview

Create and maintain GUI specifications that define the structure, components, and interactions of user interfaces. Use this skill when:
- Designing a new UI component or screen
- Creating documentation for a UI library
- Standardizing UI patterns across a project

## Specification Format

### Component Specification

```markdown
## Component: TaskList

**Type:** Interactive list component

**Props:**
| Prop | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `tasks` | `Task[]` | Yes | - | List of tasks to display |
| `onComplete` | `(id: string) => void` | No | `() => {}` | Callback when task completed |

**State:**
- `expanded` (boolean): Whether the task detail panel is visible
- `selected` (string | null): Currently selected task ID

**Events:**
- `task:complete` — Emitted when a task is completed
- `task:select` — Emitted when a task is selected
```

## Guidelines

- Define props with types and defaults
- Document state management approach
- List events and their payloads
- Include accessibility annotations (ARIA labels, keyboard navigation)

## Verification

- [ ] All props are typed and documented
- [ ] State changes are listed with triggers
- [ ] Events include payload descriptions
- [ ] Accessibility annotations present where applicable

