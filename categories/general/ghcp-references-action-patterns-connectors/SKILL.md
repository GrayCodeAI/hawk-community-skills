---
name: ghcp-references-action-patterns-connectors
description: 'Skill: ghcp-references-action-patterns-connectors'
license: MIT
tags:
- general
---

## Approvals

### Split Approval (Create → Wait)

The standard "Start and wait for an approval" is a single blocking action.
For more control (e.g., posting the approval link in Teams, or adding a timeout
scope), split it into two actions: `CreateAnApproval` (fire-and-forget) then
`WaitForAnApproval` (webhook pause).

```json
"Create_Approval": {
  "type": "OpenApiConnection",
  "runAfter": {},
  "inputs": {
    "host": {
      "apiId": "/providers/Microsoft.PowerApps/apis/shared_approvals",
      "connectionName": "<connectionName>",
      "operationId": "CreateAnApproval"
    },
    "parameters": {
      "approvalType": "CustomResponse/Result",
      "ApprovalCreationInput/title": "Review: @{variables('ItemTitle')}",
      "ApprovalCreationInput/assignedTo": "approver@contoso.com",
      "ApprovalCreationInput/details": "Please review and select an option.",
      "ApprovalCreationInput/responseOptions": ["Approve", "Reject", "Defer"],
      "ApprovalCreationInput/enableNotifications": true,
      "ApprovalCreationInput/enableReassignment": true
    }
  }
},
"Wait_For_Approval": {
  "type": "OpenApiConnectionWebhook",
  "runAfter": { "Create_Approval": ["Succeeded"] },
  "inputs": {
    "host": {
      "apiId": "/providers/Microsoft.PowerApps/apis/shared_approvals",
      "connectionName": "<connectionName>",
      "operationId": "WaitForAnApproval"
    },
    "parameters": {
      "approvalName": "@body('Create_Approval')?['name']"
    }
  }
}
```

> **`approvalType` options:**
> - `"Approve/Reject - First to respond"` — binary, first responder wins
> - `"Approve/Reject - Everyone must approve"` — requires all assignees
> - `"CustomResponse/Result"` — define your own response buttons
>
> After `Wait_For_Approval`, read the outcome:
> ```
> @body('Wait_For_Approval')?['outcome']          → "Approve", "Reject", or custom
> @body('Wait_For_Approval')?['responses'][0]?['responder']?['displayName']
> @body('Wait_For_Approval')?['responses'][0]?['comments']
> ```
>
> The split pattern lets you insert actions between create and wait — e.g.,
> posting the approval link to Teams, starting a timeout scope, or logging
> the pending approval to a tracking list.
