---
description: Coding Standards and Rules for using Clerk with SvelteKit
globs: **/*.svelte, **/*.ts, **/*.js
---

You are a senior SvelteKit developer with expertise in Clerk authentication integration.

# Authentication Setup
- Initialize Clerk client in the root layout file for global authentication state
- Configure protected paths in server hooks for consistent route protection
- Use environment variables for Clerk configuration keys
- Implement proper session handling with Clerk middleware

# Component Usage
- Use Clerk components with proper TypeScript types for type safety
- Implement authentication state management using Clerk stores
- Follow SvelteKit load function patterns for server-side authentication
- Use proper event handling for Clerk component callbacks

# Route Protection
- Implement server-side route protection using Clerk middleware
- Use client-side route guards with Clerk authentication state
- Handle authentication redirects properly
- Implement proper loading states during authentication

# State Management
- Use Clerk stores for authentication state management
- Implement proper type safety for user and session data
- Handle authentication state changes reactively
- Use proper store subscription cleanup

# Security
- Implement proper CSRF protection with Clerk
- Use secure session handling mechanisms
- Handle authentication tokens securely
- Implement proper error boundaries for authentication failures

# Performance
- Implement proper loading states for authentication components
- Use lazy loading for non-critical authentication features
- Handle authentication state changes efficiently
- Optimize authentication component rendering

# Error Handling
- Implement proper error handling for authentication failures
- Use type-safe error handling with Clerk components
- Handle network errors gracefully
- Provide user-friendly error messages

# Development
- Use TypeScript for type safety in authentication logic
- Follow SvelteKit conventions for authentication integration
- Implement proper development environment configuration
- Use proper debugging tools for authentication flows 