---
description: Coding Standards & Rules for Clerk in Nuxt.js
globs: **/*.vue, **/*.ts, **/*.js
---

# Clerk Authentication Coding Standards for Nuxt.js

## Import Standards
- Always use auto-imports from '#imports' for Clerk composables
- Never import directly from '@clerk/clerk-js'
- Never import from deprecated packages

## Environment Variables
- Use NUXT_ prefix for all Clerk environment variables
- Keep environment variables in .env file
- Never expose secret keys in client-side code

## Authentication State
- Use useAuth() for authentication state
- Use useUser() for user data
- Use useClerk() for Clerk instance methods
- Never access session directly
- Never store sensitive auth data in local storage

## Component Standards
- Use Clerk components with proper routing props
- Implement loading states for auth-dependent components
- Handle auth errors gracefully
- Follow proper component naming conventions

## Middleware Implementation
- Use typed route middleware
- Implement proper auth checks
- Handle redirect logic securely
- Maintain clean middleware structure

## API Route Security
- Implement proper token validation
- Use appropriate error responses
- Never expose sensitive data
- Handle rate limiting appropriately

## Session Management
- Use proper session handling methods
- Implement secure session storage
- Handle session expiration gracefully
- Never manipulate session data directly

## Error Handling
- Implement consistent error handling
- Use proper error boundaries
- Provide user-friendly error messages
- Log authentication errors appropriately

## Type Safety
- Use TypeScript for all auth-related code
- Define proper interfaces for auth data
- Use strict type checking
- Avoid any type when possible

## Security Best Practices
- Implement proper CSRF protection
- Use secure cookie settings
- Handle sensitive data securely
- Follow OAuth best practices

## Performance Considerations
- Lazy load auth components when possible
- Optimize auth state updates
- Minimize unnecessary re-renders
- Cache auth data appropriately

## Testing Standards
- Write tests for auth flows
- Mock Clerk services properly
- Test error scenarios
- Validate security measures

## Documentation
- Document auth implementation details
- Maintain clear API documentation
- Document security measures
- Keep configuration documentation updated

## Code Organization
- Maintain clear auth-related file structure
- Group auth components logically
- Separate auth logic from business logic
- Follow consistent naming patterns

## Composable Usage
- Create reusable auth composables
- Maintain single responsibility principle
- Implement proper error handling
- Use proper typing for composables

## State Management
- Handle auth state properly
- Use appropriate storage methods
- Implement proper state updates
- Maintain state consistency

## Route Protection
- Implement consistent route guards
- Handle auth redirects properly
- Protect sensitive routes
- Maintain clean routing logic

## Form Handling
- Implement proper form validation
- Handle auth form submissions securely
- Provide clear form feedback
- Maintain consistent form behavior

## UI/UX Standards
- Maintain consistent auth UI
- Provide clear user feedback
- Handle loading states properly
- Follow accessibility guidelines

## Configuration Management
- Maintain clean config structure
- Document configuration options
- Handle environment-specific configs
- Follow security best practices

## Deployment Considerations
- Handle environment variables properly
- Implement proper build process
- Maintain security in production
- Follow deployment best practices

Remember:
1. Security is the top priority
2. Maintain consistent coding patterns
3. Follow Nuxt.js best practices
4. Keep code clean and maintainable
5. Document everything properly 