---
name: cr-netlify-official
description: Cursor rules for netlify-official
license: MIT
tags:
- cursor-rules
- tested
domain: engineering
version: 1.0
author: PatrickJS/awesome-cursorrules
---

# Creating new sites

  - do not add redirects to netlify.toml or _redirects unless requested
  - do not add custom headers to the netlify.toml or _headers unless requested

  # Initializing sites or linking them
  - determine if a site is linked by checking if `PROJECT_FOLDER/.netlify/state.json` file exists and it has a populated `siteId` value.
  - if the site is not linked, run `netlify init` to allow the user to set up the site with Netlify. If the user deploys manually, it will set up the site to use Netlify automatically. If the user decides to set up a repo, they might have to set up the repo first. If the site is already set up on netlify then run `netlify link` for the user to input the credentials to link.

</ProviderContext>
