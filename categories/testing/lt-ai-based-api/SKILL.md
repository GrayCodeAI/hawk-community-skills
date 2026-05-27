---
name: lt-ai-based-api
description: 'Skill: lt-ai-based-api'
license: MIT
tags:
- testing
or "convert user intent to API calls". Triggers on: tool schema", "function spec",
  "agentic API",
languages: None
category: api-testing
metadata: None
author: TestMu AI
version: 1.0
---

## API-as-Plugin (OpenAPI → GPT Plugin / Tool)

Minimal `ai-plugin.json`:
```json
{
  "schema_version": "v1",
  "name_for_human": "My API",
  "name_for_model": "my_api",
  "description_for_human": "Access my service's data and actions.",
  "description_for_model": "Use this plugin to search, create, update and delete resources in My API. Always prefer specific endpoints over generic ones. Confirm destructive actions with the user first.",
  "auth": { "type": "oauth" },
  "api": { "type": "openapi", "url": "https://api.example.com/openapi.json" }
}
```
