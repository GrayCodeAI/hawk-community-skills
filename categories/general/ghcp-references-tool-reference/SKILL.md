---
name: ghcp-references-tool-reference
description: 'Skill: ghcp-references-tool-reference'
license: MIT
tags:
- general
---

## Behavioral Notes

Non-obvious behaviors discovered through real API usage. These are things
tool schemas cannot tell you.

### `get_live_flow_run_action_outputs`
- **`actionName` is optional**: omit to get top-level actions, provide to get one
  action. For actions inside foreach loops, a named action may return multiple
  repetitions; use `iterationIndex` to pin to one iteration.
- Outputs can be 50 MB+ for bulk-data actions --- always use 120s+ timeout.

### `update_live_flow`
- Required fields can vary by server version; confirm with `tool_search`
  (`select:update_live_flow`) before create/update. If `description` is required,
  preserve the existing description when patching.
- `error` key is **always present** in response --- `null` means success.
  Do NOT check `if "error" in result`; check `result.get("error") is not None`.
- On create, `created` = new flow GUID (string). On update, `created` = `false`.
- **Cannot change flow state.** Only updates displayName, definition, and
  connectionReferences. Use `set_live_flow_state` to start/stop a flow.

### `trigger_live_flow`
- **Only works for HTTP Request triggers.** Returns error for Recurrence, connector,
  and other trigger types.
- AAD-authenticated triggers are handled automatically (impersonated Bearer token).

### `get_live_flow_runs`
- `top` defaults to **30** with automatic pagination for higher values.
- Run ID field is `name`, not `runName`. Use this value as `runName` in other tools.
- Runs are returned newest-first.

### Teams `PostMessageToConversation` (via `update_live_flow`)
- **"Chat with Flow bot"**: `body/recipient` = `"user@domain.com;"` (string with trailing semicolon).
- **"Channel"**: `body/recipient` = `{"groupId": "...", "channelId": "..."}` (object).
- `poster`: `"Flow bot"` for Workflows bot identity, `"User"` for user identity.

### `list_live_connections`
- For build workflows, pass `environmentName`; omitting it inventories
  connections across environments.
- Use `search=<connector/account>` to get smaller output and paste-ready
  `connectionReferenceTemplate` / `hostTemplate` values.
- `id` is the value you need for `connectionName` in `connectionReferences`.
- `connectorName` maps to apiId: `"/providers/Microsoft.PowerApps/apis/" + connectorName`.
