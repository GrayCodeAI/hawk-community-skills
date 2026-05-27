---
name: ghcp-references-service-gotchas
description: 'Skill: ghcp-references-service-gotchas'
license: MIT
tags:
- general
---

## 4. Service Relationship Decision Rules

Described as **default selection rules** rather than absolute determinations.

### Foundry vs Azure OpenAI vs AI Hub

```
Default rules:
├─ AI/RAG workloads → Use Microsoft Foundry (kind: 'AIServices')
│   ├─ Create Foundry resource + Foundry Project as a set
│   └─ Model deployment is performed at the Foundry resource level (accounts/deployments)
│
├─ ML/open-source model training needed → Consider AI Hub (MachineLearningServices)
│   └─ Only when the user explicitly requests it or features not supported in Foundry are needed
│
└─ Standalone Azure OpenAI resource →
    Consider only when the user explicitly requests it or
    official documentation requires a separate resource
```

> These rules are a **default selection guide** reflecting current MS recommendations.
> Azure product relationships can change, so check MS Docs when uncertain.

### Monitoring

```
Default rules:
├─ Foundry (AIServices) → Application Insights not required
└─ AI Hub (MachineLearningServices) → Application Insights + Log Analytics required
```
