---
name: ghcp-references-tmt-element-taxonomy
description: 'Skill: ghcp-references-tmt-element-taxonomy'
license: MIT
tags:
- general
---

## 6. Output Files

Generate **TWO files** for maximum flexibility:

### File 1: Pure Mermaid (`.mmd`)
- Raw Mermaid code only, no markdown wrapper
- Used for: CLI tools, editors, CI/CD, direct rendering

### File 2: Markdown (`.md`)
- Mermaid in ` ```mermaid ` code fence
- Include element, flow, and boundary summary tables
- Used for: GitHub, VS Code, documentation

### Format Comparison

| Format | Extension | Contents | Best For |
|--------|-----------|----------|----------|
| Pure Mermaid | `.mmd` | Raw diagram code | CLI, editors, tools |
| Markdown | `.md` | Diagram + tables | GitHub, docs, viewing |
