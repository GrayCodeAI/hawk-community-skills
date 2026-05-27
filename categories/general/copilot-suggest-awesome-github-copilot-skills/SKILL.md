---
name: copilot-suggest-awesome-github-copilot-skills
description: Suggest relevant GitHub Copilot skills from the awesome-copilot repository
  based on current repository context and chat history, avoiding duplicates with existing
  skills in this repository, and ide...
license: MIT
tags:
- general
---

```

## Requirements

- Use `fetch` tool to get content from awesome-copilot repository skills documentation
- Use `githubRepo` tool to get individual skill content for download
- Scan local file system for existing skills in `.github/skills/` directory
- Read YAML front matter from local `SKILL.md` files to extract names and descriptions
- Compare local skills with remote versions to detect outdated skills
- Compare against existing skills in this repository to avoid duplicates
- Focus on gaps in current skill library coverage
- Validate that suggested skills align with repository's purpose and technology stack
- Provide clear rationale for each suggestion
- Include links to both awesome-copilot skills and similar local skills
- Clearly identify outdated skills with specific differences noted
- Consider bundled asset requirements and compatibility
- Don't provide any additional information or context beyond the table and the analysis

## Icons Reference

- ✅ Already installed and up-to-date
- ⚠️ Installed but outdated (update available)
- ❌ Not installed in repo

## Update Handling

When outdated skills are identified:
1. Include them in the output table with ⚠️ status
2. Document specific differences in the "Suggestion Rationale" column
3. Provide recommendation to update with key changes noted
4. When user requests update, replace entire local skill folder with remote version
5. Preserve folder location in `.github/skills/` directory
6. Ensure all bundled assets are downloaded alongside the updated `SKILL.md`
