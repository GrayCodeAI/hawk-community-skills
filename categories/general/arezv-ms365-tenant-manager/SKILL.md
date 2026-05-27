---
name: arezv-ms365-tenant-manager
description: Microsoft 365 tenant administration for Global Administrators. Automate
  M365 tenant setup, Office 365 admin tasks, Azure AD user management, Exchange Online
  configuration, Teams administration, and...
license: MIT
tags:
- general
---

## Limitations

| Constraint | Impact |
|------------|--------|
| Global Admin required | Full tenant setup needs highest privilege |
| API rate limits | Bulk operations may be throttled |
| License dependencies | E3/E5 required for advanced features |
| Hybrid scenarios | On-premises AD needs additional configuration |
| PowerShell prerequisites | Microsoft.Graph module required |

### Required PowerShell Modules

```powershell
Install-Module Microsoft.Graph -Scope CurrentUser
Install-Module ExchangeOnlineManagement -Scope CurrentUser
Install-Module MicrosoftTeams -Scope CurrentUser
```

### Required Permissions

- **Global Administrator** — Full tenant setup
- **User Administrator** — User management
- **Security Administrator** — Security policies
- **Exchange Administrator** — Mailbox management
