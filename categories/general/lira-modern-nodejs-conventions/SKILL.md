---
name: lira-modern-nodejs-conventions
description: 'Skill: lira-modern-nodejs-conventions'
license: MIT
tags:
- general
---

# Use Node’s Built-in Performance Monitoring

**Why:**
Built-in performance APIs allow agents to instrument slow operations without pulling in heavy APM tools. This is especially helpful for diagnosing bottlenecks or monitoring expensive operations.

```js
import { PerformanceObserver, performance } from 'node:perf_hooks';

const obs = new PerformanceObserver(entries => {
  for (const entry of entries.getEntries()) {
    if (entry.duration > 100) {
      console.log(`Slow operation: ${entry.name} (${entry.duration}ms)`);
    }
  }
});

obs.observe({ entryTypes: ['function', 'measure'] });

async function processLargeDataset(data) {
  performance.mark('start-process');

  const result = await heavyProcessing(data);

  performance.mark('end-process');
  performance.measure('dataset-processing', 'start-process', 'end-process');

  return result;
}
```
