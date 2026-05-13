---
description: Automate ShadCN installation and create a simple dashboard with a sidebar and widgets.
globs: "**/*.ts, **/*.tsx, **/*.js, **/*.jsx"
---

# Automated ShadCN Installation & Dashboard with Widgets

## Overview

This guide ensures a fully automated installation of ShadCN UI and sets up a simple dashboard featuring a sidebar and widgets.

1. **Initialize ShadCN UI** → Run `shadcn init` with predefined options.
2. **Add UI components** → Install necessary building blocks.
3. **Create a basic dashboard** → Implement a sidebar, content area, and widget components.

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any interactive installation commands that require manual input. Instead, you MUST generate ONLY fully automated commands using:

```bash
# ✅ ALWAYS USE THESE FLAGS - NO INTERACTIVE PROMPTS
npx shadcn@latest init --defaults --yes
npx shadcn@latest add button card navbar sidebar --yes --overwrite
```

(Adjust your component list based on which widgets you want to install, for example: `widget1`, `widget2`, etc.)

You MUST NEVER generate any commands that:
1. Require user confirmation.
2. Prompt the user to select a style or color.
3. Stop execution due to missing responses.

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use the `--defaults` and `--yes` flags in `shadcn init`.
2. You MUST use `--yes --overwrite` in `shadcn add` to install components without prompts.
3. You MUST NEVER generate any command that requires manual selection.
4. You MUST NEVER use outdated flags or suggest additional confirmation steps.

## CORRECT INSTALLATION COMMANDS

### ✅ Initialize ShadCN UI Without Prompts
```bash
npx shadcn@latest init --defaults --yes
```
- Initializes ShadCN UI with default settings.
- Skips prompts for style and color selection.
- Ensures unattended installation.

### ✅ Add Required Components Without Prompts
```bash
npx shadcn@latest add button card navbar sidebar widget1 widget2 --yes --overwrite
```
- Installs necessary components for a dashboard, including widgets.
- Bypasses confirmation prompts.
- Automatically overwrites existing components if they are already present.

## Creating a Simple Dashboard with Widgets

### ✅ Dashboard Layout
```tsx
import { useState } from "react";
import { Button, Card } from "@/components/ui";
import { Sidebar } from "@/components/sidebar";
import { Widget1 } from "@/components/widget1";
import { Widget2 } from "@/components/widget2";

export default function Dashboard() {
  const [open, setOpen] = useState(true);

  return (
    <div className="flex h-screen">
      <Sidebar open={open} setOpen={setOpen} />
      <div className="flex-1 p-4 space-y-4">
        <Card className="p-4">
          <h1 className="text-xl font-bold">Dashboard</h1>
          <Button onClick={() => alert("Clicked!")}>Click me</Button>
        </Card>

        {/* Example widget usage */}
        <Widget1 />
        <Widget2 />
      </div>
    </div>
  );
}
```

### ✅ Sidebar Component
```tsx
import { Button } from "@/components/ui";

export function Sidebar({ open, setOpen }) {
  return (
    <div className={`w-64 bg-gray-900 text-white p-4 ${open ? "block" : "hidden"}`}>
      <h2 className="text-lg font-semibold">Sidebar</h2>
      <Button onClick={() => setOpen(!open)}>Toggle Sidebar</Button>
    </div>
  );
}
```

### ✅ Sample Widget Components

**Widget1**
```tsx
import { Card } from "@/components/ui";

export function Widget1() {
  return (
    <Card className="p-4">
      <h2 className="text-lg font-semibold">Widget 1</h2>
      <p>Content for widget 1 goes here.</p>
    </Card>
  );
}
```

**Widget2**
```tsx
import { Card } from "@/components/ui";

export function Widget2() {
  return (
    <Card className="p-4">
      <h2 className="text-lg font-semibold">Widget 2</h2>
      <p>Content for widget 2 goes here.</p>
    </Card>
  );
}
```

## AI MODEL VERIFICATION STEPS

Before generating any installation commands or code, you MUST verify:

1. **Are you using `--defaults --yes` for `shadcn init`?** If not, STOP and FIX.
2. **Are you using `--yes --overwrite` for `shadcn add`?** If not, STOP and FIX.
3. **Does the dashboard include `Sidebar` and `Widget` components?** If not, STOP and FIX.
4. **Are you ensuring fully automated installation?** If not, STOP and FIX.

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate commands or code that:
- Require user input.
- Fail to automate installation.
- Do not follow the correct UI structure.

The setup will:
1. Stall in CI/CD pipelines.
2. Require manual intervention.
3. Break automation workflows.

## AI MODEL RESPONSE TEMPLATE

When asked how to install ShadCN UI and create a dashboard with widgets, you MUST:
1. ONLY generate commands from this guide.
2. NEVER suggest commands that require manual confirmation.
3. ALWAYS use the exact automation flags shown above.
4. VERIFY your response against the patterns in this guide.

Remember: There are NO EXCEPTIONS to these rules.

