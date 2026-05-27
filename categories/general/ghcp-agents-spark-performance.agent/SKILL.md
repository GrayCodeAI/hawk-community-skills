---
name: ghcp-agents-spark-performance.agent
description: Diagnose PySpark performance bottlenecks, distributed execution pitfalls,
  and suggest Spark-native rewrites and safer distributed patterns (incl. mapInPandas
  guidance).
license: MIT
tags:
- general
---

## Safety / correctness boundaries
- Do not fabricate Spark UI metrics, data sizes, or cluster configs.
