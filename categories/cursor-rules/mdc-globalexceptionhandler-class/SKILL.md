---
name: mdc-globalexceptionhandler-class
description: "Structure of GlobalExceptionHandler class."
license: MIT
tags: [cursor-rules]
---

## Overview

Define a GlobalExceptionHandler class that centralizes error handling across an application. Use this skill when:
- Implementing centralized error logging and reporting
- Creating error boundaries for React applications
- Standardizing error handling across services

## GlobalExceptionHandler Class Structure

### TypeScript Example

```typescript
class GlobalExceptionHandler {
  private handlers: Map<string, (error: unknown) => void> = new Map();
  
  register(category: string, handler: (error: unknown) => void): void {
    this.handlers.set(category, handler);
  }
  
  handle(error: unknown, context?: Record<string, unknown>): void {
    const category = this.classify(error);
    const handler = this.handlers.get(category);
    
    console.error(`[GlobalExceptionHandler] ${category}:`, error);
    
    if (handler) {
      handler(error);
    } else {
      this.defaultHandler(error);
    }
  }
  
  private classify(error: unknown): string {
    if (error instanceof NetworkError) return 'network';
    if (error instanceof ValidationError) return 'validation';
    if (error instanceof DatabaseError) return 'database';
    return 'unknown';
  }
  
  private defaultHandler(error: unknown): void {
    console.error('Unhandled error:', error);
    // Report to error tracking service
    // Send alert to team
  }
}

const globalHandler = new GlobalExceptionHandler();
globalHandler.register('network', (err) => {
  // Refresh token, retry request
});
```

### Required Methods

| Method | Description |
|--------|-------------|
| `handle(error, context?)` | Route error to appropriate handler based on classification |
| `register(category, handler)` | Add a handler for a specific error category |
| `classify(error)` | Determine the category of an error |

### Error Categories

| Category | Source | Recovery Action |
|----------|--------|----------------|
| `network` | API/network failures | Retry with backoff, refresh token |
| `validation` | Input validation failures | Return user-facing error message |
| `database` | DB query/connection failures | Rollback transaction, fail gracefully |
| `auth` | Authentication/authorization failures | Redirect to login, clear session |
| `unknown` | Unhandled errors | Log, alert, fail safely |

## Integration Points

- React: wrap app with error boundary that uses GlobalExceptionHandler
- Express: add middleware that catches errors and routes to handler
- CLI: register handlers for command failures and tool errors

## Verification

- [ ] All error categories have handlers
- [ ] Default handler catches unclassified errors
- [ ] Context passed to handlers includes relevant request info
- [ ] Recovery actions are defined per category

