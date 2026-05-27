---
name: ghcp-microsoft-docs-skill
description: Query official Microsoft documentation to find concepts, tutorials, and
  code examples across Azure, .NET, Agent Framework, Aspire, VS Code, GitHub, and
  more. Uses Microsoft Learn MCP as the default...
license: MIT
tags:
- general
---

## Writing Effective Queries

Be specific — include version, intent, and language:

```
# ❌ Too broad
"Azure Functions"
"agent framework"

# ✅ Specific
"Azure Functions Python v2 programming model"
"Cosmos DB partition key design best practices"
"GitHub Actions workflow_dispatch inputs matrix strategy"
"Aspire AddUvicornApp Python FastAPI integration"
"DevUI serve agents tracing OpenTelemetry directory discovery"
"Agent Framework workflow conditional edges branching handoff"
```

Include context:
- **Version** when relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Task intent** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Language** for polyglot docs (`Python`, `TypeScript`, `C#`)
