---
name: lira-error-handling
description: 'Skill: lira-error-handling'
license: MIT
tags:
- general
---

## Advanced Diagnostics (Custom Channels)

Use **`node:diagnostics_channel`** to publish/subscribe to app-level diagnostic events without coupling your business logic to logging/monitoring.

```ts
import diagnostics_channel from "node:diagnostics_channel";

// Create custom diagnostic channels
const dbChannel = diagnostics_channel.channel("app:database");
const httpChannel = diagnostics_channel.channel("app:http");

// Subscribe to diagnostic events
dbChannel.subscribe((message) => {
  console.log("Database operation:", {
    operation: message.operation,
    duration: message.duration,
    query: message.query,
  });
});

// Publish diagnostic information
export async function queryDatabase(sql: string, params: unknown[]) {
  const start = performance.now();
  try {
    const result = await db.query(sql, params);

    dbChannel.publish({
      operation: "query",
      sql,
      params,
      duration: performance.now() - start,
      success: true,
    });

    return result;
  } catch (error) {
    dbChannel.publish({
      operation: "query",
      sql,
      params,
      duration: performance.now() - start,
      success: false,
      error: (error as Error).message,
    });
    throw error;
  }
}
```

### Diagnostics Best Practices

* **Name channels by domain** (`app:database`, `app:http`, `app:featureX`) for easy routing.
* **Keep subscribers fast & safe:** work they do happens in-process—avoid heavy/async work directly in the callback; forward to your logger/queue.
* **Emit minimal, structured payloads:** operation, duration, identifiers—no secrets/PII.
* **Pair with errors:** when publishing failures, include the related `AppError`’s `code` and a short summary (full details live in logs).
* **Sample when needed:** for very hot paths, add sampling or level control to reduce noise and overhead.
* **Test observability paths:** have tests that assert a publish happens for both success and failure branches.

### Diagnostics Antipatterns (to avoid)

* **Spamming channels with raw payloads** (big objects/rows) → log bloat, perf hit.
* **Doing blocking work in subscribers** → slows the hot path; offload.
* **Inconsistent message shapes** across publishes → hard to parse/monitor; keep a schema-like shape per channel.
