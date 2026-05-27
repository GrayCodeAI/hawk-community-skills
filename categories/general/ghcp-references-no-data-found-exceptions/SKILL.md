---
name: ghcp-references-no-data-found-exceptions
description: 'Skill: ghcp-references-no-data-found-exceptions'
license: MIT
tags:
- general
---

## Migration Notes for Similar Issues

When fixing this issue, verify:

1. **Success path tests** - Confirm valid parameters still work correctly
2. **Exception tests** - Verify exceptions are raised with invalid parameters
3. **Transaction rollback** - Ensure proper cleanup on errors
4. **Data integrity** - Confirm all fields are populated correctly in success cases
