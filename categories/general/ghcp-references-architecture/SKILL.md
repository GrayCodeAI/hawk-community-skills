---
name: ghcp-references-architecture
description: 'Skill: ghcp-references-architecture'
license: MIT
tags:
- general
---

## Configuration

### Parameters

```csharp
// Plain parameter
var apiKey = builder.AddParameter("api-key");

// Secret parameter (prompted at run, not logged)
var dbPassword = builder.AddParameter("db-password", secret: true);

// Use in resources
var api = builder.AddProject<Projects.Api>("api")
    .WithEnvironment("API_KEY", apiKey);

var db = builder.AddPostgres("db", password: dbPassword);
```

### Configuration sources

Parameters are resolved from (in priority order):
1. Command-line arguments
2. Environment variables
3. User secrets (`dotnet user-secrets`)
4. `appsettings.json` / `appsettings.{Environment}.json`
5. Interactive prompt (for secrets during `aspire run`)
