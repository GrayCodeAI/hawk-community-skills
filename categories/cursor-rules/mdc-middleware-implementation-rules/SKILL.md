---
name: mdc-middleware-implementation-rules
description: "Applies specifically to the `middleware.ts` file to manage requests and"
license: MIT
tags: [cursor-rules]
---

- Use Vercel middleware to handle incoming requests.
- Use middleware to parse user input and manage sessions with the KV database.
- Use Vercel's KV database for managing stateful data.