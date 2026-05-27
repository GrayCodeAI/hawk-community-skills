---
name: ghcp-references-trigger-types
description: 'Skill: ghcp-references-trigger-types'
license: MIT
tags:
- general
---

## Child Flow (Called by Another Flow)

```json
"manual": {
  "type": "Request",
  "kind": "Button",
  "inputs": {
    "schema": {
      "type": "object",
      "properties": {
        "items": {
          "type": "array",
          "items": { "type": "object" }
        }
      }
    }
  }
}
```

Access parent-supplied data: `@triggerBody()?['items']`

To return data to the parent, add a `Response` action:
```json
"Respond_to_Parent": {
  "type": "Response",
  "runAfter": { "Compose_Result": ["Succeeded"] },
  "inputs": {
    "statusCode": 200,
    "body": "@outputs('Compose_Result')"
  }
}
```
