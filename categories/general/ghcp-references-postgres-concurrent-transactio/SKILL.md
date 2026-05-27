---
name: ghcp-references-postgres-concurrent-transactio
description: 'Skill: ghcp-references-postgres-concurrent-transactio'
license: MIT
tags:
- general
---

## Best Practices

1. **Materialize early** — Call `.ToList()` or `.ToArray()` on query results before iterating and issuing further database calls. This is the simplest and most reliable fix.

2. **Audit data access patterns** — Review all repository and data access methods for deferred-execution return types (`IEnumerable`, `IQueryable`) that callers iterate while issuing additional queries.

3. **Prefer single queries** — Where feasible, combine nested lookups into JOINs or subqueries to eliminate the concurrent-command pattern entirely.

4. **Isolate connections when necessary** — If concurrent operations are genuinely required, use separate connections rather than attempting to share one.

5. **Test iterative workflows** — Integration tests should cover scenarios where code iterates result sets and performs additional database operations per row, as these are the most common failure points.

## Migration Checklist

- [ ] Identify all code paths that execute multiple commands on a single connection concurrently
- [ ] Locate `IEnumerable`-backed data access methods that defer execution with open readers
- [ ] Add `.ToList()` / `.ToArray()` materialization where deferred results are iterated alongside further queries
- [ ] Refactor nested database calls to use separate connections or combined queries where appropriate
- [ ] Verify EF Core navigation properties and lazy loading do not trigger concurrent connection usage
- [ ] Update integration tests to cover iterative data access patterns
- [ ] Load-test connection pool sizing if Solution 2 (separate connections) is used extensively

## References

- [Npgsql Documentation: Basic Usage](https://www.npgsql.org/doc/basic-usage.html)
- [PostgreSQL Documentation: Concurrency Control](https://www.postgresql.org/docs/current/mvcc.html)
- [Npgsql GitHub: Multiple Active Result Sets Discussion](https://github.com/npgsql/npgsql/issues/462)
