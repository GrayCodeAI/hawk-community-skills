---
name: copilot-eval-driven-dev
description: 'Skill: copilot-eval-driven-dev'
license: MIT
tags:
- general
---

## Web Server Management

pixie-qa runs a web server in the background for displaying context, traces, and eval results to the user. It's automatically started by the setup script (via `pixie start`, which launches a detached background process and returns immediately).

When the user is done with the eval-driven-dev workflow, inform them the web server is still running and you can clean it up with:

```bash
pixie stop
```

IMPORTANT: after the web server is stopped, the web UI becomes inaccessible. So only stop the server if the user confirms they're done with all web UI features. If they want to keep using the web UI, do NOT stop the server.

And whenever you restart the workflow, always run the setup.sh script in resources again to ensure the web server is running:
