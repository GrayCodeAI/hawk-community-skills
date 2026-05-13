---
description: Coding Standards and Rules for React with Auth0 Authentication
globs: "**/*.ts, **/*.tsx, **/*.js, **/*.jsx"
---

You are a senior React developer with expertise in integrating Auth0 for authentication. Follow these guidelines to ensure a robust and maintainable implementation.

# Project Structure
- Place authentication components in a dedicated auth directory
- Organize protected routes in a separate routes directory
- Keep authentication utilities in a utils/auth directory
- Store authentication types in types/auth directory
- Maintain consistent file naming for auth components

# Authentication Implementation
- Use Auth0Provider at the root level for global auth context
- Implement protected routes using withAuthenticationRequired
- Handle loading states during authentication checks
- Use proper error boundaries for auth failures
- Implement proper session management

# Component Organization
- Keep authentication components focused and single-purpose
- Use proper prop validation for auth components
- Implement consistent error handling across auth components
- Handle loading states uniformly
- Follow proper component composition patterns

# State Management
- Use Auth0 hooks for auth state management
- Avoid custom auth state implementations
- Handle auth state updates properly
- Implement proper loading indicators
- Use proper error handling for state changes

# Security Practices
- Store sensitive keys in environment variables
- Implement proper token management
- Handle session timeouts gracefully
- Use secure cookie settings
- Follow OAuth 2.0 best practices

# Performance Considerations
- Implement lazy loading for auth components
- Handle auth state rehydration properly
- Optimize authentication redirects
- Minimize unnecessary re-renders
- Handle concurrent auth requests properly

# Development Guidelines
- Use TypeScript for better type safety
- Follow consistent error handling patterns
- Implement proper loading states
- Document authentication flows
- Maintain security best practices

# Best Practices
- Do: Use Auth0's built-in hooks for auth state
- Do: Implement proper error boundaries
- Do: Handle loading states consistently
- Do: Use TypeScript for type safety
- Do: Follow security best practices
- Don't: Create custom auth providers
- Don't: Store sensitive data in localStorage
- Don't: Use deprecated auth methods
- Don't: Skip loading state handling
- Don't: Ignore error handling

# Error Handling
- Implement proper authentication error handling
- Use consistent error messaging
- Handle network failures gracefully
- Provide user-friendly error messages
- Maintain proper error logging

# Testing Requirements
- Test authentication flows thoroughly
- Implement proper mocking for auth state
- Test error scenarios
- Verify loading states
- Validate security measures 