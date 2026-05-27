---
name: ghcp-references-action-patterns-data
description: 'Skill: ghcp-references-action-patterns-data'
license: MIT
tags:
- general
---

### ConvertTimeZone (Built-in, No Connector)

Converts a timestamp between timezones with no API call or connector licence cost.
Format string `"g"` produces short locale date+time (`M/d/yyyy h:mm tt`).

```json
"Convert_to_Local_Time": {
  "type": "Expression",
  "kind": "ConvertTimeZone",
  "runAfter": {},
  "inputs": {
    "baseTime": "@{outputs('UTC_Timestamp')}",
    "sourceTimeZone": "UTC",
    "destinationTimeZone": "Taipei Standard Time",
    "formatString": "g"
  }
}
```

Result reference: `@body('Convert_to_Local_Time')` — **not** `outputs()`, unlike most actions.

Common `formatString` values: `"g"` (short), `"f"` (full), `"yyyy-MM-dd"`, `"HH:mm"`

Common timezone strings: `"UTC"`, `"AUS Eastern Standard Time"`, `"Taipei Standard Time"`,
`"Singapore Standard Time"`, `"GMT Standard Time"`

> This is `type: Expression, kind: ConvertTimeZone` — a built-in Logic Apps action,
> not a connector. No connection reference needed. Reference the output via
> `body()` (not `outputs()`), otherwise the expression returns null.
