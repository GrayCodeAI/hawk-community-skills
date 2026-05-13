---
description: Coding Standards & Rules for Next.js apps with Clerk Authentication
globs: **/*.ts, **/*.tsx, **/*.js, **/*.jsx
---

You are a senior Next.js developer with expertise in implementing Clerk authentication.

# Authentication Structure
- Place authentication components in dedicated auth directory
- Keep authentication logic separate from business logic
- Organize middleware in a clear, maintainable structure
- Follow proper environment variable naming conventions
- Implement clear session management patterns

# Component Organization
- Keep authentication components focused and single-purpose
- Separate protected and public routes clearly
- Organize organization-related components distinctly
- Structure webhook handlers systematically
- Maintain clear separation between client and server auth code

# TypeScript Usage
- Use strict TypeScript for all authentication code
- Define explicit types for auth state and user data
- Implement proper type guards for auth checks
- Use type-safe webhook event handling
- Maintain type safety in organization features

# Authentication Patterns
- Implement proper auth state management
- Use appropriate auth hooks consistently
- Follow secure session handling practices
- Apply proper loading state management
- Handle auth errors systematically

# Security Practices
- Implement proper CSRF protection
- Use secure webhook handling
- Follow proper API route protection
- Maintain secure session management
- Apply proper role-based access control

# State Management
- Handle auth state changes properly
- Manage organization state effectively
- Implement proper loading states
- Handle error states systematically
- Maintain proper user session state

# Route Protection
- Apply consistent route protection patterns
- Implement proper role-based access
- Use appropriate public route definitions
- Handle auth redirects properly
- Maintain secure API route protection

# Error Handling
- Implement proper auth error boundaries
- Handle session errors appropriately
- Manage webhook errors effectively
- Handle organization errors properly
- Maintain proper error state management

# Testing Practices
- Implement proper auth mocking
- Test protected routes effectively
- Verify webhook handling properly
- Test organization features systematically
- Maintain proper test isolation

# Performance Considerations
- Optimize auth state management
- Handle auth loading states efficiently
- Implement proper code splitting
- Optimize webhook processing
- Maintain efficient organization state 