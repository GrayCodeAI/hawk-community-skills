---
name: agc-react-integration
description: 'Skill: agc-react-integration'
license: MIT
tags:
- general
---

## React StrictMode

In development, React StrictMode double-invokes effects. The keyboard handler effect returns a cleanup function (removes the listener), so double-invocation is handled. The `startDemo` function should guard against double-start with `if (isActiveRef.current) return`.
