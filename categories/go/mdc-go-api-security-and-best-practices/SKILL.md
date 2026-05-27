---
name: mdc-go-api-security-and-best-practices
description: "This rule emphasizes security, scalability, and maintainability best practices in Go API development."
license: MIT
tags: [go]
---

- Implement input validation for API endpoints.
- Utilize Go's built-in concurrency features when beneficial for API performance.
- Follow RESTful API design principles and best practices.
- Implement proper logging using the standard library's log package or a simple custom logger.
- Consider implementing middleware for cross-cutting concerns (e.g., logging, authentication).
- Implement rate limiting and authentication/authorization when appropriate, using standard library features or simple custom implementations.
- Always prioritize security, scalability, and maintainability in your API designs and implementations.