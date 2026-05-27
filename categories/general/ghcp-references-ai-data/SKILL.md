---
name: ghcp-references-ai-data
description: 'Skill: ghcp-references-ai-data'
license: MIT
tags:
- general
---

## 7. Common AI/Data Architecture Combinations

### RAG Chatbot

```
Foundry (AIServices) + Project
├── <chat-model> (chat)              — Confirmed after availability check in Phase 1
├── <embedding-model> (embedding)    — Confirmed after availability check in Phase 1
├── AI Search (vector + semantic)
├── ADLS Gen2 (document store)
└── Key Vault (secrets)
+ Full VNet/PE configuration
```

### Data Platform

```
Fabric Capacity (analytics)
├── ADLS Gen2 (data lake)
├── ADF (ingestion)
└── Key Vault (secrets)
+ VNet/PE configuration
```
