---
name: ghcp-agents-elasticsearch-observability.ag
description: 'Skill: ghcp-agents-elasticsearch-observability.ag'
license: MIT
tags:
- general
---

# User

## Observability & Code-Level Debugging

### Prompt
My `checkout-service` (in Java) is throwing `HTTP 503` errors. Correlate its logs, metrics (CPU, memory), and APM traces to find the root cause.

### Prompt
I'm seeing `javax.persistence.OptimisticLockException` in my Spring Boot service logs. Analyze the traces for the request `POST /api/v1/update_item` and suggest a code change (e.g., in Java) to handle this concurrency issue.

### Prompt
An 'OOMKilled' event was detected on my 'payment-processor' pod. Analyze the associated JVM metrics (heap, GC) and logs from that container, then generate a report on the potential memory leak and suggest remediation steps.

### Prompt
Generate an ES|QL query to find the P95 latency for all traces tagged with `http.method: "POST"` and `service.name: "api-gateway"` that also have an error.

## Search, Vector & Performance Optimization

### Prompt
I have a slow ES|QL query: `[...query...]`. Analyze it and suggest a rewrite or a new index mapping for my 'production-logs' index to improve its performance.

### Prompt
I am building a RAG application. Show me the best way to create an Elasticsearch index mapping for storing 768-dim embedding vectors using `HNSW` for efficient kNN search.

### Prompt
Show me the Python code to perform a hybrid search on my 'doc-index'. It should combine a BM25 full-text search for `query_text` with a kNN vector search for `query_vector`, and use RRF to combine the scores.

### Prompt
My vector search recall is low. Based on my index mapping, what `HNSW` parameters (like `m` and `ef_construction`) should I tune, and what are the trade-offs?

## Security & Remediation

### Prompt
Elastic Security generated an alert: "Anomalous Network Activity Detected" for `user_id: 'alice'`. Summarize the associated logs and endpoint data. Is this a false positive or a real threat, and what are the recommended remediation steps?
