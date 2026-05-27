---
name: arezv-senior-backend
description: Designs and implements backend systems including REST APIs, microservices,
  database architectures, authentication flows, and security hardening. Use when the
  user asks to "design REST APIs", "optim...
license: MIT
tags:
- general
---

## Common Commands

```bash
# API Development
python scripts/api_scaffolder.py openapi.yaml --framework express
python scripts/api_scaffolder.py src/routes/ --generate-spec

# Database Operations
python scripts/database_migration_tool.py --connection $DATABASE_URL --analyze
python scripts/database_migration_tool.py --connection $DATABASE_URL --migrate file.sql

# Performance Testing
python scripts/api_load_tester.py https://api.example.com/endpoint --concurrency 50
python scripts/api_load_tester.py https://api.example.com/endpoint --compare baseline.json
```
