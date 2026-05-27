---
name: rb-gui_architect_and_spec
description: 'Skill: rb-gui_architect_and_spec'
license: MIT
tags:
- general
---

### 9.6 Component Relationship Map

The table and diagram below clarify **how each module depends on, or calls, the others** at runtime.

| Caller →                              | Called ↴                                                    | Purpose                                                         | Sync/Async                              |
| ------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------- |
| `sidebarProvider.ts` (TreeItem click) | VS Code `commands.executeCommand`                           | Dispatches the command ID linked to the clicked item.           | **Sync** – immediate return             |
| `extension.ts` (command handler)      | `utils.getRuleSets`                                         | Retrieve rule names when needed.                                | **Sync** – uses `spawnSync`             |
| `extension.ts`                        | VS Code window APIs – `showQuickPick`, `showWarningMessage` | Gathers user input / confirmations.                             | **Async** (Promise)                     |
| `extension.ts`                        | `utils.openTerminalAndRun`                                  | Spawns terminal & sends Python command.                         | **Sync** (fire‑and‑forget)              |
| `utils.openTerminalAndRun`            | VS Code `window.createTerminal`                             | Creates & shows terminal.                                       | **Sync**                                |
| Integrated Terminal                   | `manage_rules.py` (Python)                                  | Executes business logic; interacts with user for extra prompts. | **Runtime** – outside extension process |
| `manage_rules.py`                     | Filesystem under workspace root                             | Reads/writes rule folders, memory, tools.                       | OS‑level sync                           |
