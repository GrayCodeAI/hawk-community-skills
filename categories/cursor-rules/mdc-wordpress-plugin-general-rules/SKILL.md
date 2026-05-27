---
name: mdc-wordpress-plugin-general-rules
description: "Applies general rules for WordPress plugin development, including coding standards, type hinting, and language preferences."
license: MIT
tags: [cursor-rules]
---

- You are operating in a WordPress plugin context, that has a Guzzle-based HTTP client, WP REST endpoint addition(s), and new Gutenberg editor blocks.
- Always use WordPress coding standards when writing PHP, JavaScript, and TypeScript.
- Always type hint PHP code.
- Prefer writing TypeScript over JavaScript.
- Favor functional paradigms over object-oriented ones, favor composition over inheritance, but be consistent with WordPress ecosystem best practices.
- Optimize for readability.