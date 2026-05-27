---
name: arezv-google-workspace-cli
description: Google Workspace administration via the gws CLI. Install, authenticate,
  and automate Gmail, Drive, Sheets, Calendar, Docs, Chat, and Tasks. Run security
  audits, execute 43 built-in recipes, and use...
license: MIT
tags:
- general
---

## Limitations

| Constraint | Impact |
|------------|--------|
| OAuth tokens expire after 1 hour | Re-auth needed for long-running scripts |
| API rate limits (per-user, per-service) | Bulk operations may hit 429 errors |
| Scope requirements vary by service | Must request correct scopes during auth |
| Pre-v1.0 CLI status | Breaking changes possible between releases |
| Google Cloud project required | Free, but requires setup in Cloud Console |
| Admin API needs admin privileges | Some audit checks require Workspace Admin role |

### Required Scopes by Service

```bash
# List scopes for specific services
python3 scripts/auth_setup_guide.py --scopes gmail,drive,calendar,sheets
```

| Service | Key Scopes |
|---------|-----------|
| Gmail | `gmail.modify`, `gmail.send`, `gmail.labels` |
| Drive | `drive.file`, `drive.metadata.readonly` |
| Sheets | `spreadsheets` |
| Calendar | `calendar`, `calendar.events` |
| Admin | `admin.directory.user.readonly`, `admin.directory.group` |
| Tasks | `tasks` |
