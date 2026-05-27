---
name: minimax-minimax-pdf
description: 'Skill: minimax-minimax-pdf'
license: MIT
tags:
- general
CREATE (generate from scratch): make a PDF", "generate a report", "write a proposal",
FILL (complete form fields): fill in the form", "fill out this PDF",
REFORMAT (apply design to an existing doc): reformat this document", "apply our style",
This skill uses a token-based design system: color, typography, and spacing are derived
metadata: None
version: 1.0
category: document-generation
---

## Environment

```bash
bash scripts/make.sh check   # verify all deps
bash scripts/make.sh fix     # auto-install missing deps
bash scripts/make.sh demo    # build a sample PDF
```

| Tool | Used by | Install |
|---|---|---|
| Python 3.9+ | all `.py` scripts | system |
| `reportlab` | `render_body.py` | `pip install reportlab` |
| `pypdf` | fill, merge, reformat | `pip install pypdf` |
| Node.js 18+ | `render_cover.js` | system |
| `playwright` + Chromium | `render_cover.js` | `npm install -g playwright && npx playwright install chromium` |
