---
name: ghcp-agents-project-documenter
description: Generates professional MS Word project documentation with draw.io architecture
  diagrams and embedded PNG images. Automatically discovers any project's technology
  stack, architecture, and code struc...
license: MIT
tags:
- general
tools: None
---

## Error Recovery

| Problem | Action |
|---------|--------|
| draw.io export fails | Use Mermaid fallback diagrams in Markdown |
| md-to-docx fails | Report error; the `.md` file is still usable |
| Source file not found | Note the gap, continue with available files |
| Unrecognized tech stack | Document what you can observe, note gaps |
