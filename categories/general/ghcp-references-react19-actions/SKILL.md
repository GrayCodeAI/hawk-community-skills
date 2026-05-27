---
name: ghcp-references-react19-actions
description: 'Skill: ghcp-references-react19-actions'
license: MIT
tags:
- general
title: React 19 Actions Pattern Reference
---

## Comparison Table

| Feature | React 18 | React 19 |
|---|---|---|
| Form handling | `onSubmit` + useReducer | `action` + useActionState |
| Loading state | Manual dispatch | Automatic `isPending` |
| Child component pending state | Prop drilling | `useFormStatus` hook |
| Optimistic updates | Manual state dance | `useOptimistic` hook |
| Error handling | Manual in dispatch | Return from action |
| Complexity | More boilerplate | Less boilerplate |
