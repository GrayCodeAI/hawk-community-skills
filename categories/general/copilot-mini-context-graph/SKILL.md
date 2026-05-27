---
name: copilot-mini-context-graph
description: 'Skill: copilot-mini-context-graph'
license: MIT
tags:
- general
---

## Design Philosophy

> "The wiki is a persistent, compounding artifact. The cross-references are already there. The synthesis already reflects everything you've read." — Karpathy

| Layer | What Happens | Who Owns It |
|-------|-----------|-------------|
| **LLM Reasoning** | Extraction, synthesis, writing wiki pages | Agent (.md guidance files) |
| **Wiki Persistence** | Index, log, file I/O | `wiki_store.py` |
| **Graph Persistence** | Dedup, index, BFS traverse | `graph_store.py`, `retrieval_engine.py` |
| **Raw Source Storage** | Immutable docs + chunks + provenance | `documents_store.py` |

The human curates sources and asks questions. The LLM writes the wiki, extracts the graph, and answers with citations. Python handles all bookkeeping.
