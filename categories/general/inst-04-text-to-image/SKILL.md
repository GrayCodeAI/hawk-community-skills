---
description: Guidelines for building text-to-image generation in Next.js 15
globs: **/*.ts, **/*.tsx, **/*.js, **/*.jsx
---

# Implement Text-to-Image Generation Page

## Overview

1. Provide a user interface to input a text prompt.
2. Call Fal.ai (through the proxy) to generate an image.
3. Display the generated image on the page.

## CRITICAL INSTRUCTIONS
- Only call fal.subscribe from client-side code or server actions that remain private.
- Show a loading state or message if generation takes time.
- Ensure the Fal.ai key is never directly in client code.

## Key Steps

1. Create a Dashboard Page (app/dashboard/page.tsx):
   ```tsx
   "use client"
   import { useState } from "react"
   import { fal } from "@fal-ai/client"

   export default function DashboardPage() {
     const [prompt, setPrompt] = useState("")
     const [imageUrl, setImageUrl] = useState("")
     const [loading, setLoading] = useState(false)

     async function handleGenerate() {
       try {
         setLoading(true)
         const result = await fal.subscribe("fal-ai/flux/dev", {
           input: { prompt, image_size: "square_hd" },
         })
         setImageUrl(result.images[0]?.url || "")
       } catch (error) {
         console.error("Fal.ai error:", error)
       } finally {
         setLoading(false)
       }
     }

     return (
       <div>
         <input
           value={prompt}
           onChange={(e) => setPrompt(e.target.value)}
           placeholder="Enter your prompt..."
         />
         <button onClick={handleGenerate} disabled={loading}>
           {loading ? "Generating..." : "Generate"}
         </button>
         {imageUrl && <img src={imageUrl} alt="AI Generated" />}
       </div>
     )
   }
   ```
2. Verification:
   - Try inputting a prompt like "A futuristic city skyline at night."
   - Confirm an image appears if the Fal.ai call succeeds.

## Verification Checklist
- Is the Fal.ai request going to the proxy ("/api/fal/proxy")?
- Do you handle errors and logging gracefully?
- Does the UI update once the image is generated?

## AI MODEL RESPONSE TEMPLATE
When asked about text-to-image generation in Next.js:
1. Provide a minimal input + button + img flow.
2. Highlight the fal.subscribe call with proxyUrl set.
3. Show how to manage loading and the returned image.