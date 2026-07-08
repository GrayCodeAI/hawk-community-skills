---
name: mdc-apiresponse-class
description: "Structure of ApiResponse class."
license: MIT
tags: [cursor-rules]
---

## Overview

Define the structure of API response classes following Cursor Modular Design Coding conventions. Use this skill when:
- Creating a new API client or response wrapper
- Standardizing response handling across services
- Documenting response schema patterns

## ApiResponse Class Structure

### TypeScript Example

```typescript
interface ApiResponse<T> {
  /** Whether the request was successful */
  ok: boolean;
  
  /** HTTP status code */
  status: number;
  
  /** Response body data */
  data: T | null;
  
  /** Error details if ok is false */
  error: {
    code: string;
    message: string;
    details?: unknown;
  } | null;
  
  /** Raw response for debugging */
  raw: Response;
}

class ApiClient {
  async get<T>(url: string): Promise<ApiResponse<T>> {
    const response = await fetch(url);
    const data = await response.json();
    
    if (!response.ok) {
      return {
        ok: false,
        status: response.status,
        data: null,
        error: { code: 'HTTP_ERROR', message: data.message },
        raw: response,
      };
    }
    
    return { ok: true, status: response.status, data, error: null, raw: response };
  }
}
```

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `ok` | `boolean` | Whether the request succeeded |
| `status` | `number` | HTTP status code |
| `data` | `T \| null` | Response payload or null on error |
| `error` | `object \| null` | Error details with code and message |
| `raw` | `Response` | The raw Response object for debugging |

## Error Handling Patterns

- Map HTTP 4xx/5xx to structured error objects
- Include the original response for debugging context
- Never throw raw HTTP errors — always return structured ApiResponse

## Verification

- [ ] All fields typed correctly
- [ ] Error case properly handled
- [ ] Raw response preserved for debugging
- [ ] Generic type `T` used correctly

