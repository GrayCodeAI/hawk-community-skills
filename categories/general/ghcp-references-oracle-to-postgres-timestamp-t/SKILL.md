---
name: ghcp-references-oracle-to-postgres-timestamp-t
description: 'Skill: ghcp-references-oracle-to-postgres-timestamp-t'
license: MIT
tags:
- general
---

## Checklist

- [ ] `AppContext.SetSwitch("Npgsql.EnableLegacyTimestampBehavior", false)` applied at application startup.
- [ ] All `DateTime.Now` usages in data-access code replaced with `DateTime.UtcNow`.
- [ ] Connection string or connection-open hook sets `Timezone=UTC` / `SET TimeZone = 'UTC'`.
- [ ] Stored procedures that use `CURRENT_TIMESTAMP` or `NOW()` reviewed; `timestamp without time zone` columns explicitly cast or replaced with `timestamptz`.
- [ ] Integration tests assert `DateTime.Kind == Utc` on retrieved timestamp values.
- [ ] Tests cover date-range queries to confirm row counts match Oracle baseline.
