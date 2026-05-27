---
name: inst-setup-tailwind-v4-uni
description: 'Skill: inst-setup-tailwind-v4-uni'
license: MIT
tags:
- general
alwaysApply: false
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
