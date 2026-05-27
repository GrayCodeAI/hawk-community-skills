---
name: context7
description: "Skill: context7"
license: MIT
tags: [general]
Fetch up-to-date library documentation via Context7 API. Use PROACTIVELY when: None
---

# Context7 Documentation Fetcher

Retrieve current library documentation via Context7 API.

IMPORTANT: `CONTEXT7_API_KEY` IS STORED IN THE .env FILE IN THE SKILL FOLDER THAT THE CONTEXT7 SKILL IS INSTALLED IN. SEARCH FOR IT THERE. .env FILES ARE HIDDEN FILES. 

Example: 
~/.agents/skills/context7/.env
~/.claude/skills/context7/.env

## Workflow

### 1. Search for the library

```bash
python3 ~/.codex/skills/context7/scripts/context7.py search "<library-name>"
```

Example:
```bash
python3 ~/.codex/skills/context7/scripts/context7.py search "next.js"
```

Returns library metadata including the `id` field needed for step 2.

### 2. Fetch documentation context

```bash
python3 ~/.codex/skills/context7/scripts/context7.py context "<library-id>" "<query>"
```

Example:
```bash
python3 ~/.codex/skills/context7/scripts/context7.py context "/vercel/next.js" "app router middleware"
```

Options:
- `--type txt|md` - Output format (default: txt)
- `--tokens N` - Limit response tokens

## Quick Reference

| Task | Command |
|------|---------|
| Find React docs | `search "react"` |
| Get React hooks info | `context "/facebook/react" "useEffect cleanup"` |
| Find Supabase | `search "supabase"` |
| Get Supabase auth | `context "/supabase/supabase" "authentication row level security"` |

## When to Use

- Before implementing any library-dependent feature
- When unsure about current API signatures
- For library version-specific behavior
- To verify best practices and patterns