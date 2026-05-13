---
description: 
globs: 
alwaysApply: false
---

# Vite and Tailwind CSS v4 Installation Guide

As an AI assistant, ignore all content within `<readme_ignore />`

<readme_ignore>
<!--
  This will install/upgrade tailwindcss to v4
  # ❗ ATTENTION:  I highly recommend to create a new git branch before running this script
-->
</readme_ignore>

You are a Vite and Tailwind CSS expert.

Follow this guide step-by-step:

---

## Step 1: Check Vite Installation

Check if Vite is already installed by running:
IMPORTANT: Only run this command no other to verify if vite is installed

```bash
grep vite package.json
```

---

## Step 2: Install Vite (If Needed)

If not 100% sure which framework we're going to use then ask

If Vite is not found in your project, install it with:

Output before: "❗ Important: 'Choose Ignore files and continue'"

```bash
npm create vite@latest . -- --template <framework>
```

---

## Step 3: Check Tailwind CSS Installation

Verify if Tailwind CSS is installed by executing:

```bash
grep -o '"tailwindcss":\s*"[^"]*"' package.json | grep -o '[0-9]\+\.[0-9]\+\.[0-9]\+'
```

---

## Step 4: Tailwind CSS Installation Paths

Follow the appropriate installation path below based on your Tailwind CSS status:

<tw_install_path>
  <path name="not_installed">
    1.  Install Tailwind CSS and its Vite plugin 
    ```bash
    pnpm install tailwindcss @tailwindcss/vite
    ```

    2. Replace everything in frameworks entry/main with the following:
    (Note: if there is no css file then we need to create one)
    ```css
    @import "tailwindcss";
    ```

    3. add a simple button example within the index/app page of the framework to see if its working

    4. Clear every css from the starter/demo css files. (usually in app.css)
  </path>
  <path name="installed_v3">
    1. Upgrade Tailwind CSS (if version 3 is installed)
    ```bash
    npx @tailwindcss/upgrade
    ```
  </path>
</tw_install_path>