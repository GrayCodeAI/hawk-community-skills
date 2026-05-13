---
description: Guidelines for writing Next.js apps with shadcn/ui
globs: **/*.ts, **/*.tsx, **/*.js, **/*.jsx
---

# Next.js Dashboard Setup with shadcn/ui

Follow these steps in order to create a modern dashboard application:

1. Create Project
   - Run: pnpm dlx shadcn@latest init
   - For quick setup with defaults: pnpm dlx shadcn@latest init -d
   - Select New York style and Zinc color scheme when prompted
   - Enable CSS variables for theming support

2. Configure Project Structure
   - Remove app/page.tsx (default demo page)
   - Create following directory structure:
     ```
     app/
     ├── layout.tsx
     ├── page.tsx (dashboard page)
     ├── loading.tsx
     ├── error.tsx
     └── components/
         ├── ui/ (shadcn components)
         └── dashboard/
             ├── header.tsx
             ├── sidebar.tsx
             ├── main.tsx
             └── widgets/
     ```

3. Install Essential Components
   ```bash
   pnpm dlx shadcn@latest add card
   pnpm dlx shadcn@latest add button
   pnpm dlx shadcn@latest add dropdown-menu
   pnpm dlx shadcn@latest add separator
   pnpm dlx shadcn@latest add sheet
   pnpm dlx shadcn@latest add theme-toggle
   ```

4. Create Root Layout
   ```tsx
   // app/layout.tsx
   import { ThemeProvider } from '@/components/theme-provider'
   
   export default function RootLayout({
     children,
   }: {
     children: React.ReactNode
   }) {
     return (
       <html lang="en" suppressHydrationWarning>
         <body>
           <ThemeProvider
             attribute="class"
             defaultTheme="system"
             enableSystem
           >
             {children}
           </ThemeProvider>
         </body>
       </html>
     )
   }
   ```

5. Implement Dashboard Layout Components
   ```tsx
   // components/dashboard/header.tsx
   export function Header() {
     return (
       <header className="border-b">
         <div className="flex h-16 items-center px-4">
           <div className="ml-auto flex items-center space-x-4">
             <ThemeToggle />
           </div>
         </div>
       </header>
     )
   }

   // components/dashboard/sidebar.tsx
   export function Sidebar() {
     return (
       <div className="hidden border-r bg-background md:block md:w-64">
         <div className="space-y-4 py-4">
           {/* Add navigation items */}
         </div>
       </div>
     )
   }
   ```

6. Create Main Dashboard Page
   ```tsx
   // app/page.tsx
   import { Header } from '@/components/dashboard/header'
   import { Sidebar } from '@/components/dashboard/sidebar'
   
   export default function DashboardPage() {
     return (
       <div className="flex min-h-screen flex-col">
         <Header />
         <div className="flex flex-1">
           <Sidebar />
           <main className="flex-1 p-6">
             <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
               {/* Add dashboard widgets */}
             </div>
           </main>
         </div>
       </div>
     )
   }
   ```

7. Add Mobile Responsiveness
   - Add Sheet component for mobile navigation
   - Implement responsive breakpoints
   - Create mobile menu toggle button

8. Implement Loading States
   ```tsx
   // app/loading.tsx
   export default function Loading() {
     return (
       <div className="flex h-screen w-screen items-center justify-center">
         <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-primary" />
       </div>
     )
   }
   ```

9. Follow Best Practices
   - Use TypeScript for all components
   - Keep shadcn components in ui directory
   - Create wrapper components for customization
   - Use React Server Components by default
   - Add client-side interactivity only when needed
   - Implement proper error boundaries
   - Follow accessibility guidelines

10. Performance Optimization
    - Implement code splitting
    - Use dynamic imports for heavy components
    - Add Suspense boundaries
    - Monitor bundle size
    - Optimize images and assets

11. Theme Configuration
    - Maintain consistent spacing with Tailwind
    - Use CSS variables for dynamic theming
    - Follow New York style guidelines
    - Implement dark mode correctly

12. Testing Setup (Recommended)
    - Add component tests
    - Implement E2E testing
    - Test responsive behavior
    - Verify theme switching
    - Test loading states 