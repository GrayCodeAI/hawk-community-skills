---
name: ghcp-agents-dotnet-upgrade.agent
description: Perform janitorial tasks on C#/.NET code including cleanup, modernization,
  and tech debt remediation.
license: MIT
tags:
- general
tools:
- codebase
- edit/editFiles
- search
- runCommands
- runTasks
- runTests
- problems
- changes
- usages
- findTestFiles
- testFailure
- terminalLastCommand
- terminalSelection
- web/fetch
- microsoft.docs.mcp
---

## Chatmode Prompt Library
1. "List all projects with current and recommended .NET versions."
2. "Generate a per-project upgrade plan from <currentVersion> to <targetVersion>."
3. "Suggest .csproj and pipeline edits to upgrade <ProjectName>."
4. "Summarize build/test results post-upgrade for <ProjectName>."
5. "Create PR description and checklist for the upgrade."

---
