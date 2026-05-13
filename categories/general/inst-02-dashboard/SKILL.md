---
description: Guidelines for creating a ShadCN-based dashboard in Next.js
globs: **/*.ts, **/*.tsx, **/*.js, **/*.jsx
---

# Create a Dashboard & Frontend Layout with ShadCN

## Overview

1. Build a dashboard page using the ShadCN sidebar component.
2. Place the sidebar in a fixed left column with the main content on the right.
3. Use Next.js 15's App Router structure (for example, app/dashboard/layout.tsx).

## CRITICAL INSTRUCTIONS
- Render the ShadCN Sidebar in a layout component.
- Keep the overall layout flexible, such as className="flex min-h-screen".
- Use AppSidebar in your custom layout.

## Key Steps

1. Create Dashboard Layout (app/dashboard/layout.tsx):
   ```tsx
   // app/dashboard/layout.tsx
   import { AppSidebar } from "@/components/ui/sidebar"

   export default function DashboardLayout({ children }: { children: React.ReactNode }) {
     return (
       <div className="flex min-h-screen">
         <AppSidebar />
         <main className="flex-1 p-4">
           {children}
         </main>
       </div>
     )
   }
   ```
2. Customize the Sidebar Component:
   ```tsx
   // components/ui/sidebar.tsx
   // Example usage of ShadCN's sidebar
   import { Sidebar, SidebarContent, SidebarGroup, SidebarMenu, SidebarMenuItem } from "@/components/ui/sidebar"

   export function AppSidebar() {
     return (
       <Sidebar>
         <SidebarContent>
           <SidebarGroup>
             <SidebarMenu>
               <SidebarMenuItem>
                 {/* Menu items */}
               </SidebarMenuItem>
             </SidebarMenu>
           </SidebarGroup>
         </SidebarContent>
       </Sidebar>
     )
   }
   ```
3. Add Routes and Pages
   - Implement app/dashboard/page.tsx for the default dashboard view.
   - Optionally add app/settings/page.tsx if you want a settings section.

## Verification Checklist
- Does the sidebar persist on every dashboard sub-route?
- Is the layout using ShadCN components (for example, Sidebar, SidebarContent)?
- Are you following Next.js 15 App Router conventions?

## AI MODEL RESPONSE TEMPLATE
When asked about creating a dashboard:
1. Provide layout code with AppSidebar on the left and main content on the right.
2. Reference ShadCN's official sidebar usage.
3. Avoid any deprecated or unverified code patterns.