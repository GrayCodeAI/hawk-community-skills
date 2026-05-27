---
name: ghcp-references-ingestion
description: 'Skill: ghcp-references-ingestion'
license: MIT
tags:
- general
---

## Example

**Input document:**
```
System crashes due to memory leaks.
Memory leaks occur when objects are not released.
```

**Expected extraction output:**
```json
{
  "entities": [
    { "name": "system crash", "type": "issue",     "supporting_text": "system crashes due to memory leaks" },
    { "name": "memory leak",  "type": "issue",     "supporting_text": "memory leaks occur when objects are not released" },
    { "name": "object",       "type": "component", "supporting_text": "objects are not released" }
  ],
  "relations": [
    {
      "source": "memory leak",
      "target": "system crash",
      "type": "causes",
      "confidence": 1.0,
      "supporting_text": "System crashes due to memory leaks."
    },
    {
      "source": "object",
      "target": "memory leak",
      "type": "contributes to",
      "confidence": 0.9,
      "supporting_text": "Memory leaks occur when objects are not released."
    }
  ]
}
```
