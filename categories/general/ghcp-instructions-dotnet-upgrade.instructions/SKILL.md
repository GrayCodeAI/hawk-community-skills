---
name: ghcp-instructions-dotnet-upgrade.instructions
description: Specialized agent for comprehensive .NET framework upgrades with progressive
  tracking and validation
license: MIT
tags:
- general
---

## 10. Upgrade Checklist (Per Project)

Use this table as a sample to track the progress of the upgrade across all projects in the solution and add this in the PullRequest

| Project Name | Target Framework | Dependencies Updated | Builds Successfully | Tests Passing | Deployment Verified | Notes |
|--------------|------------------|-----------------------|---------------------|---------------|---------------------|-------|
| Project A    | ☐ net10.0         | ☐                     | ☐                   | ☐             | ☐                   |       |
| Project B    | ☐ net10.0         | ☐                     | ☐                   | ☐             | ☐                   |       |
| Project C    | ☐ net10.0         | ☐                     | ☐                   | ☐             | ☐                   |       |

> ✅ Mark each column as you complete the step for every project.

## 11. Commit & PR Guidelines

- Use a **single PR per repository**:
  - Title: `Upgrade to .NET [VERSION]`
  - Include:
    - Updated target frameworks.
    - NuGet upgrade summary.
    - Provide test results as summarized above.
- Tag with `breaking-change` if APIs were replaced.

## 12. Multi-Repo Execution (Optional)

For organizations with multiple repositories:
1. Store this `instructions.md` in a central upgrade template repo.
2. Provide SWE Agent / Cursor with:
   ```
   Upgrade all repositories to latest supported .NET versions following instructions.md
   ```
3. Agent should:
   - Detect project type per repo.
   - Apply the appropriate upgrade path.
   - Open PRs for each repo.


## 🔑 Notes & Best Practices

- **Prefer Migration to Modern .NET**  
  If on .NET Framework or .NET Standard, evaluate moving to .NET 8/10 for long-term support.
- **Automate Tests Early**  
  CI/CD should block merges if tests fail.
- **Incremental Upgrades**  
  Large solutions may require upgrading one project at a time.

  ### ✅ Example Agent Prompt

  >  Upgrade this repository to the latest supported .NET version following the steps in `dotnet-upgrade-instructions.md`.  
  >  Detect project type (.NET Core, Standard, or Framework) and apply the correct migration path.  
  >  Ensure all tests pass and CI/CD workflows are updated.

---
