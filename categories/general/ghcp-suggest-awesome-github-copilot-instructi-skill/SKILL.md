---
name: ghcp-suggest-awesome-github-copilot-instructi-skill
description: Suggest relevant GitHub Copilot instruction files from the awesome-copilot
  repository based on current repository context and chat history, avoiding duplicates
  with existing instructions in this re...
license: MIT
tags:
- general
---

```

## Requirements

- Use `githubRepo` tool to get content from awesome-copilot repository instructions folder
- Scan local file system for existing instructions in `.github/instructions/` directory
- Read YAML front matter from local instruction files to extract descriptions and `applyTo` patterns
- Compare local instructions with remote versions to detect outdated instructions
- Compare against existing instructions in this repository to avoid duplicates
- Focus on gaps in current instruction library coverage
- Validate that suggested instructions align with repository's purpose and standards
- Provide clear rationale for each suggestion
- Include links to both awesome-copilot instructions and similar local instructions
- Clearly identify outdated instructions with specific differences noted
- Consider technology stack compatibility and project-specific needs
- Don't provide any additional information or context beyond the table and the analysis

## Icons Reference

- ✅ Already installed and up-to-date
- ⚠️ Installed but outdated (update available)
- ❌ Not installed in repo

## Update Handling

When outdated instructions are identified:
1. Include them in the output table with ⚠️ status
2. Document specific differences in the "Suggestion Rationale" column
3. Provide recommendation to update with key changes noted
4. When user requests update, replace entire local file with remote version
5. Preserve file location in `.github/instructions/` directory
