---
name: vercel-deploy-to-vercel
description: Deploy applications and websites to Vercel. Use when the user requests
  deployment actions like "deploy my app", "deploy and give me the link", "push this
  live", or "create a preview deployment".
license: MIT
tags:
- general
metadata: None
author: vercel
version: 3.0.0
---

## Troubleshooting

### Network Egress Error (claude.ai)

If deployment fails due to network restrictions on claude.ai, tell the user:

```
Deployment failed due to network restrictions. To fix this:

1. Go to https://claude.ai/settings/capabilities
2. Add *.vercel.com to the allowed domains
3. Try deploying again
```

### Escalated Network Access (Codex / sandboxed environments)

If deployment fails due to network issues (timeouts, DNS errors, connection resets) in a sandboxed environment, rerun with escalated permissions (`sandbox_permissions=require_escalated`). Do not escalate the initial CLI availability check — only escalate the actual deploy command.

Example guidance to the user:
```
The deploy needs escalated network access to deploy to Vercel. I can rerun
the command with escalated permissions — want me to proceed?
```

### CLI Auth Failure

If `vercel login` or `vercel deploy` fails with authentication errors, fall back to the no-auth deploy script (claude.ai or Codex variant, depending on the environment).
