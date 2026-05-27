---
name: ag-fp-ts-errors
description: Handle errors as values using fp-ts Either and TaskEither for cleaner,
  more predictable TypeScript code. Use when implementing error handling patterns
  with fp-ts.
license: MIT
tags:
- general
risk: safe
source: https://github.com/whatiskadudoing/fp-ts-skills
date_added: 2026-02-27
---

## Summary

1. **Return errors as values** - Use Either/TaskEither instead of throwing
2. **Chain with confidence** - `chain` stops at first error automatically
3. **Collect all errors when needed** - Use validation applicative for forms
4. **Wrap at boundaries** - Convert throwing/Promise code at the edges
5. **Match at the end** - Use `fold` to handle both cases when you're ready to act

The payoff: TypeScript tracks your errors, no more forgotten try/catch, clear control flow, and composable error handling.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
