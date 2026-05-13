---
description: Implement a simple token or quota system for free image generations
globs: **/*.ts, **/*.tsx, **/*.js, **/*.jsx
---

# Add a Basic Token or Quota System (No Authentication)

## Overview

1. Limit each user to a small number of free generations (e.g., 2).
2. Track usage in client-side storage or via IP checks on the server.
3. Prevent unlimited calls to the Fal.ai proxy route.

## CRITICAL INSTRUCTIONS
- No user authentication is used, so rely on localStorage or a minimal IP-based rate limit.
- Keep the logic straightforward: if free quota is reached, disable generation or prompt an upgrade (even if you have no Stripe flow).
- Implement basic server-side checks in the Fal proxy route if you want IP-based limiting.

## Key Steps

1. Client-Side Quota Tracking (LocalStorage)
   ```tsx
   "use client"
   import { useState, useEffect } from "react"
   import { fal } from "@fal-ai/client"

   export default function DashboardPage() {
     const [prompt, setPrompt] = useState("")
     const [imageUrl, setImageUrl] = useState("")
     const [loading, setLoading] = useState(false)
     const [freeRemaining, setFreeRemaining] = useState(2) // default 2 free
     
     useEffect(() => {
       // Load from localStorage on mount
       const stored = localStorage.getItem("freeRemaining")
       if (stored) {
         setFreeRemaining(parseInt(stored, 10))
       }
     }, [])

     async function handleGenerate() {
       if (freeRemaining <= 0) {
         alert("Free quota reached. Please consider upgrading.")
         return
       }

       try {
         setLoading(true)
         const result = await fal.subscribe("fal-ai/flux/dev", {
           input: { prompt, image_size: "square_hd" },
         })
         setImageUrl(result.images[0]?.url || "")
         // Decrement free usage
         const newCount = freeRemaining - 1
         setFreeRemaining(newCount)
         localStorage.setItem("freeRemaining", newCount.toString())
       } catch (error) {
         console.error("Fal.ai error:", error)
       } finally {
         setLoading(false)
       }
     }

     return (
       <div>
         <h1>Free Generations Left: {freeRemaining}</h1>
         <input
           value={prompt}
           onChange={(e) => setPrompt(e.target.value)}
           placeholder="Enter prompt..."
         />
         <button onClick={handleGenerate} disabled={loading}>
           {loading ? "Generating..." : "Generate"}
         </button>
         {imageUrl && <img src={imageUrl} alt="Generated" />}
       </div>
     )
   }
   ```

2. Optional Server-Side IP Rate Limiting (Fal Proxy)
   ```ts
   // app/api/fal/proxy/route.ts
   import { NextRequest, NextResponse } from "next/server"
   import { route } from "@fal-ai/server-proxy/nextjs"

   // Simple in-memory map to track usage per IP:
   const ipUsage: Record<string, number> = {}

   export const { GET, POST } = route({
     preHandler: (req: NextRequest) => {
       const ip = req.headers.get("x-real-ip") || req.ip || "unknown-ip"
       if (!ipUsage[ip]) {
         ipUsage[ip] = 0
       }
       if (ipUsage[ip] >= 2) {
         return new NextResponse("Free quota exceeded for this IP.", { status: 429 })
       }
       ipUsage[ip] += 1
     },
   })
   ```
   - This simple approach denies requests after 2 generations per IP. 
   - Because it’s in-memory, it resets on server restart (for production, use a more robust store).

## Verification Checklist
- Does localStorage properly persist the user's freeRemaining count?
- Is the IP-based limit (if used) rejecting requests after the free quota?
- Are error messages or alerts shown when the user can’t generate more images?

## AI MODEL RESPONSE TEMPLATE
When asked about a simple free quota system without authentication:
1. Provide a localStorage-based example for the client side.
2. Suggest a minimal IP-based approach on the server to prevent abuse.
3. Emphasize that this is a basic placeholder solution—users can potentially bypass it unless additional checks are implemented.