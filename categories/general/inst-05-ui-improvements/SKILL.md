---
description: UI improvements for the text-to-image generation app
globs: **/*.ts, **/*.tsx, **/*.js, **/*.jsx
---

# Enhance the User Interface with ShadCN and Tailwind

## Overview

1. Provide a more polished and user-friendly interface.
2. Use ShadCN components for inputs, buttons, and layout.
3. Employ Tailwind CSS classes for better spacing, typography, and responsive design.

## CRITICAL INSTRUCTIONS
- Keep consistent styling with your existing ShadCN setup.
- Ensure important elements (prompt input, generate button, output image) stand out.
- Avoid cluttering the interface; maintain a simple, intuitive layout.

## Key Steps

1. Use ShadCN Form and Button components
   ```tsx
   // app/dashboard/page.tsx
   "use client"
   import { useState } from "react"
   import { fal } from "@fal-ai/client"
   import { Input } from "@/components/ui/input" // Example ShadCN Input component
   import { Button } from "@/components/ui/button" // Example ShadCN Button component

   export default function DashboardPage() {
     const [prompt, setPrompt] = useState("")
     const [imageUrl, setImageUrl] = useState("")
     const [loading, setLoading] = useState(false)

     async function handleGenerate() {
       setLoading(true)
       try {
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
       <div className="max-w-xl mx-auto mt-10 space-y-4">
         <h1 className="text-2xl font-bold">AI Image Generation</h1>
         <Input
           placeholder="Enter your prompt..."
           value={prompt}
           onChange={(e) => setPrompt(e.target.value)}
           className="w-full"
         />
         <Button onClick={handleGenerate} disabled={loading}>
           {loading ? "Generating..." : "Generate Image"}
         </Button>
         {imageUrl && (
           <div className="mt-4">
             <img
               src={imageUrl}
               alt="Generated Image"
               className="rounded-md shadow-md"
             />
           </div>
         )}
       </div>
     )
   }
   ```
2. Incorporate Tailwind Utilities:
   - Use utility classes like p-4, m-4, rounded-md, shadow-md, etc.
   - Set max-width for a cleaner layout (e.g., max-w-xl).

3. Add Loading & Error States:
   - Optionally use a ShadCN alert or spinner.
   - Display a small text or icon during generation.

4. Make it Responsive:
   - Use responsive classes like `sm:`, `md:`, `lg:` to fine-tune spacing or font sizes.
   - Ensure images shrink or wrap properly on smaller screens.

## Verification Checklist
- Did you wrap form elements in ShadCN components (Input, Button, Form, etc.)?
- Does the layout stay clear and responsive across devices?
- Are you displaying prompts, buttons, and outputs cleanly with Tailwind?

## AI MODEL RESPONSE TEMPLATE
When asked about UI improvements:
1. Show how to leverage ShadCN components (e.g., Input, Button) instead of plain HTML tags.
2. Provide Tailwind utility classes for spacing, alignment, and responsiveness.
3. Emphasize a neat, user-friendly design with minimal clutter.