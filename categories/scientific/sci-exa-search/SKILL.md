---
name: sci-exa-search
description: 'Web toolkit powered by Exa, tuned for scientific and technical content.
  Use this skill when the user needs to search the web or fetch/extract URL content.
  Covers: web search (semantic lookups, rese...'
license: MIT
tags:
- scientific
compatibility: Requires exa-py Python SDK, an EXA_API_KEY, and internet access.
metadata: None
skill-author: Exa
website: https://exa.ai
docs: https://exa.ai/docs
---

## Files in this skill

- `SKILL.md` — this file (routing and setup)
- `references/web-search.md` — detailed web search reference with academic strategy
- `references/web-extract.md` — URL content extraction reference
- `scripts/exa_search.py` — CLI wrapper around `client.search_and_contents`
- `scripts/exa_extract.py` — CLI wrapper around `client.get_contents`
