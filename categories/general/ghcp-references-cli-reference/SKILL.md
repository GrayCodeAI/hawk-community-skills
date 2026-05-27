---
name: ghcp-references-cli-reference
description: 'Skill: ghcp-references-cli-reference'
license: MIT
tags:
- general
---

## .NET CLI equivalents

The `dotnet` CLI can perform some Aspire tasks:

| Aspire CLI                  | .NET CLI Equivalent              |
| --------------------------- | -------------------------------- |
| `aspire new aspire-starter` | `dotnet new aspire-starter`      |
| `aspire run`                | `dotnet run --project ./AppHost` |
| N/A                         | `dotnet build ./AppHost`         |
| N/A                         | `dotnet test ./Tests`            |

The Aspire CLI adds value with `publish`, `deploy`, `add`, `mcp`, `config`, `cache`, `do`, and `update` — commands that have no direct `dotnet` equivalent.
