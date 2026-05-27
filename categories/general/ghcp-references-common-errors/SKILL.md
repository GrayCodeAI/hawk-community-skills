---
name: ghcp-references-common-errors
description: 'Skill: ghcp-references-common-errors'
license: MIT
tags:
- general
---

### Null Cascade in Filter Array / Query

**Symptom**: A lookup/filter step returns the wrong record or a later expression
fails on null even though the filter action itself succeeded.

**Root cause**: The lookup key is null or empty. A condition such as
`equals(item()?['Email'], outputs('Lookup_Email'))` can accidentally match rows
where both sides are null, or can pass an empty array downstream.

**Diagnosis**: Inspect the action that creates the lookup key and the filter
output length. Confirm the key is non-empty before trusting the filter result.

**Fix**: Add a non-empty guard before the filter, normalize comparison values
with `trim()`/`toLower()`, and branch explicitly when no match is found.
