---
name: ghcp-references-api-reference
description: 'Skill: ghcp-references-api-reference'
license: MIT
tags:
- general
---

## Text Detection

> **Beta feature** — requires the `detect_beta_user` role or a billing plan that includes the `dfd_text` product.

### `POST /text_detect`

Add `Prefer: wait` for synchronous response. Otherwise poll or use callback.

| Parameter      | Type    | Required | Description                                              |
|----------------|---------|----------|----------------------------------------------------------|
| `text`         | string  | Yes      | Text to analyze (max 100,000 characters)                 |
| `thinking`     | string  | No       | Always use `"low"` (default)                             |
| `threshold`    | float   | No       | Decision threshold 0.0–1.0 (default: 0.5)                |
| `callback_url` | string  | No       | Webhook URL for async completion notification            |
| `privacy_mode` | boolean | No       | If true, text content is not stored after analysis       |

**Response:**
```json
{
  "success": true,
  "item": {
    "uuid": "abc-123",
    "status": "completed",
    "prediction": "ai",
    "confidence": 0.91,
    "text_content": "This is some text to analyze.",
    "privacy_mode": false,
    "created_at": "...",
    "updated_at": "..."
  }
}
```

- `prediction`: `"ai"` or `"human"` — the verdict
- `confidence`: 0.0–1.0, higher = more confident
- `status`: `"processing"`, `"completed"`, or `"failed"`

### `GET /text_detect/{uuid}` — Poll

Poll until `status` is `"completed"` or `"failed"`.

### `GET /text_detect` — List

Returns paginated text detections for the team.

### Callback

If `callback_url` was provided, a `POST` is sent on completion:
```json
{ "success": true, "item": { ... } }
```
On failure:
```json
{ "success": false, "item": { ... }, "error": "Error message here" }
```
