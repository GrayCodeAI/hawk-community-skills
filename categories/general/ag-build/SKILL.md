---
name: ag-build
description: build
license: MIT
tags:
- general
risk: unknown
source: community
---

## Important Guidelines

### Use AskUserQuestion Liberally

Throughout all phases, use AskUserQuestion whenever:
- There's ambiguity in requirements
- Multiple approaches are possible
- You need to validate an assumption
- A decision will significantly impact the implementation
- You're unsure about scope or priority

### Deep Research Expectations

"Deep research" means:
- Multiple web searches on different aspects
- Thorough codebase exploration
- Reading relevant documentation
- Considering multiple approaches
- Understanding trade-offs

Don't rush through research - it's the foundation for good implementation.

### Progress Tracking

Keep PROGRESS.md updated in real-time during phase work:
- Don't wait until the end to update
- Record decisions as they're made
- Note blockers immediately
- This creates valuable context for future sessions

### Scope Management

A key purpose of this workflow is preventing scope creep:
- Each phase should have clear boundaries
- If new requirements emerge, note them for future phases
- Don't expand the current phase's scope mid-implementation
- Use AskUserQuestion to validate if something is in/out of scope

### Always Works Philosophy

When implementing phases:
- Test changes as you make them
- Don't assume code works - verify it
- If something doesn't work, fix it before moving on
- The goal is working software, not just written code

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
