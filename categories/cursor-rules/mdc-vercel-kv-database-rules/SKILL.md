---
name: mdc-vercel-kv-database-rules
description: "Defines how to interact with Vercel's KV database for storing and retrieving session and application data."
license: MIT
tags: [cursor-rules]
---

- Use Vercel's KV database to store and retrieve session data.
- Utilize `kv.set`, `kv.get`, and `kv.delete` to manage data.
- Ensure the database operations are asynchronous to avoid blocking server-side rendering (SSR).