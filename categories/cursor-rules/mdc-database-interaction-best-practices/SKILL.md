---
name: mdc-database-interaction-best-practices
description: "Best practices when interacting with databases in backend Go code."
license: MIT
tags: [cursor-rules]
---

When interacting with databases:
- Use prepared statements to prevent SQL injection.
- Handle database errors gracefully.
- Consider using an ORM for complex queries and data modeling.
- Close database connections when they are no longer needed.
- Use connection pooling to improve performance.