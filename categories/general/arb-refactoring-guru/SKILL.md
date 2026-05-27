---
name: arb-refactoring-guru
description: 'Skill: arb-refactoring-guru'
license: MIT
tags:
- general
---

## Review Checklist

- Is the change a refactoring, a feature, or a bug fix, and is that boundary clear?
- Did the code become cleaner in the touched area?
- Is there a named smell that justified the transformation?
- Was the smallest suitable technique used?
- Did all relevant tests pass?
- Did any public interface change receive compatibility handling?
- Did the change reduce duplication, bloat, coupling, or unclear control flow?
- Did it avoid speculative abstractions?
- Did it avoid needless polymorphism, inheritance, or bidirectional associations?
- Is any remaining smell explicitly deferred rather than hidden?
