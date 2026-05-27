---
name: ghcp-references-deployment
description: 'Skill: ghcp-references-deployment'
license: MIT
tags:
- general
---

## Dev Containers & GitHub Codespaces

Aspire templates include `.devcontainer/` configuration:

```json
{
  "name": "Aspire App",
  "image": "mcr.microsoft.com/devcontainers/dotnet:10.0",
  "features": {
    "ghcr.io/devcontainers/features/docker-in-docker:2": {},
    "ghcr.io/devcontainers/features/node:1": {}
  },
  "postCreateCommand": "curl -sSL https://aspire.dev/install.sh | bash",
  "forwardPorts": [18888],
  "portsAttributes": {
    "18888": { "label": "Aspire Dashboard" }
  }
}
```

Port forwarding works automatically in Codespaces — the dashboard and all service endpoints are accessible via forwarded URLs.
