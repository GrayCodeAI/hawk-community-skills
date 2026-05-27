---
name: extra-commit-fast
description: "Skill: extra-commit-fast"
license: MIT
tags: [cursor-rules]
---

# Fast Commit Task

Generate 3 commit message suggestions based on the staged changes, then automatically use the first suggestion without user confirmation. 

Follow conventional commit format with appropriate emojis and create descriptive messages that explain the purpose of changes. Skip the manual message selection step to streamline the commit process.

## Steps:
1. Run `git status` to see staged changes
2. Generate 3 commit message suggestions following conventional commit format
3. Automatically select the first suggestion
4. Execute `git commit -m` with the selected message
5. Exclude Claude co-authorship footer from commits

## Commit Types:
- ✨ feat: New features
- 🐛 fix: Bug fixes  
- 📝 docs: Documentation changes
- ♻️ refactor: Code restructuring
- 🧑‍💻 chore: Tooling and maintenance
- 🎨 style: Code formatting, missing semicolons, etc.
- ⚡️ perf: Performance improvements
- ✅ test: Adding or correcting tests