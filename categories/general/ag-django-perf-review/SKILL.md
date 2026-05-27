---
name: ag-django-perf-review
description: Django performance code review. Use when asked to "review Django performance",
  "find N+1 queries", "optimize Django", "check queryset performance", "database performance",
  "Django ORM issues", or a...
license: LICENSE
tags:
- general
allowed-tools: Read, Grep, Glob, Bash, Task
risk: unknown
source: community
---

## What NOT to Report

- Test files
- Admin-only views
- Management commands
- Migration files
- One-time scripts
- Code behind disabled feature flags
- Tables with <1000 rows that won't grow
- Patterns in cold paths (rarely executed code)
- Micro-optimizations (exists vs count, only/defer without evidence)

### False Positives to Avoid

**Queryset variable assignment is not an issue:**
```python
# This is FINE - no performance difference
projects_qs = Project.objects.filter(org=org)
projects = list(projects_qs)

# vs this - identical performance
projects = list(Project.objects.filter(org=org))
```
Querysets are lazy. Assigning to a variable doesn't execute anything.

**Single query patterns are not N+1:**
```python
# This is ONE query, not N+1
projects = list(Project.objects.filter(org=org))
```
N+1 requires a loop that triggers additional queries. A single `list()` call is fine.

**Missing select_related on single object fetch is not N+1:**
```python
# This is 2 queries, not N+1 - report as LOW at most
state = AutofixState.objects.filter(pr_id=pr_id).first()
project_id = state.request.project_id  # second query
```
N+1 requires a loop. A single object doing 2 queries instead of 1 can be reported as LOW if relevant, but never as CRITICAL/HIGH.

**Style preferences are not performance issues:**
If your only suggestion is "combine these two lines" or "rename this variable" - that's style, not performance. Don't report it.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
