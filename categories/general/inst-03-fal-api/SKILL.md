---
description: Guidelines for installing and configuring Fal.ai
globs: **/*.ts, **/*.tsx, **/*.js, **/*.jsx
---

# Install & Configure Fal.ai for Text-to-Image

## Overview

1. Install Fal.ai client (@fal-ai/client) and server proxy (@fal-ai/server-proxy).
2. Create a Next.js API route that forwards requests to Fal.ai, hiding your API key.
3. Store the Fal.ai key in environment variables.

## CRITICAL INSTRUCTIONS
- Never expose the FAL_KEY in client code.
- Use the @fal-ai/server-proxy/nextjs route to protect the key.
- Confirm your .env.local (and Vercel env) hold FAL_KEY.

## Key Steps

1. Install:
   ```bash
   npm install @fal-ai/client @fal-ai/server-proxy
   ```
2. Environment (.env.local):
   ```bash
   FAL_KEY="your-secret-fal-ai-key"
   ```
3. Create Proxy Route (app/api/fal/proxy/route.ts):
   ```ts
   import { route } from "@fal-ai/server-proxy/nextjs"

   export const { GET, POST } = route
   ```
4. Client Configuration:
   ```tsx
   // app/providers.tsx or similar
   "use client"

   import { fal } from "@fal-ai/client"

   fal.config({ proxyUrl: "/api/fal/proxy" })
   ```
   This ensures client requests go to /api/fal/proxy, which injects your secret key server-side.

## Verification Checklist
- Is FAL_KEY only in the server environment?
- Did you create /api/fal/proxy using @fal-ai/server-proxy/nextjs?
- Is the client configured with fal.config({ proxyUrl })?

## AI MODEL RESPONSE TEMPLATE
When asked about Fal.ai setup:
1. Show the npm install commands for @fal-ai/client and @fal-ai/server-proxy.
2. Provide code for the Next.js proxy route (export const { GET, POST }).
3. Emphasize storing FAL_KEY in .env.local (never exposing it on the client).