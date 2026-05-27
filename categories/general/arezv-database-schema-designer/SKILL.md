---
name: arezv-database-schema-designer
description: Use when the user asks to create ERD diagrams, normalize database schemas,
  design table relationships, or plan schema migrations.
license: MIT
tags:
- general
---

## Best Practices

1. **Timestamps everywhere** — `created_at`, `updated_at` on every table
2. **Soft deletes for auditable data** — `deleted_at` instead of DELETE
3. **Audit log for compliance** — log before/after JSON for regulated domains
4. **UUIDs or CUIDs as PKs** — avoid sequential integer leakage
5. **Index foreign keys** — every FK column should have an index
6. **Partial indexes** — use `WHERE deleted_at IS NULL` for active-only queries
7. **RLS over application-level filtering** — database enforces tenancy, not just app code
