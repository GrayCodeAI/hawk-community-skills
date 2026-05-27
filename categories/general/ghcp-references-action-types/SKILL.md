---
name: ghcp-references-action-types
description: 'Skill: ghcp-references-action-types'
license: MIT
tags:
- general
---

## Common Expressions (Reading Cheat Sheet)

| Expression | Meaning |
|---|---|
| `@outputs('X')?['body/value']` | Array result from connector action X |
| `@body('X')` | Direct body of action X (Query, Select, ParseJson) |
| `@item()?['Field']` | Current loop item's field |
| `@triggerBody()?['Field']` | Trigger payload field |
| `@variables('name')` | Variable value |
| `@coalesce(a, b)` | First non-null of a, b |
| `@first(array)` | First element (null if empty) |
| `@length(array)` | Array count |
| `@empty(value)` | True if null/empty string/empty array |
| `@union(a, b)` | Merge arrays — **first wins** on duplicates |
| `@result('Scope')` | Array of action outcomes inside a Scope |
