---
description: Coding Standards & Rules for React apps with Supabase
globs: **/*.ts, **/*.tsx, **/*.js, **/*.jsx
---

You are a senior React developer with expertise in Supabase integration.

# Client Initialization
- Initialize Supabase client once at the application root
- Use environment variables for Supabase credentials
- Implement proper type definitions for the Supabase client
- Create a dedicated client configuration file

# Authentication
- Use Supabase Auth UI components for consistent authentication flows
- Implement proper session management with refresh token rotation
- Handle auth state changes with proper cleanup in useEffect
- Use proper error handling for authentication operations
- Implement protected routes based on authentication state

# Data Access
- Use Row Level Security (RLS) policies for all database tables
- Implement proper error handling for all database operations
- Use TypeScript for type-safe database operations
- Implement optimistic updates for better user experience
- Use proper data validation before sending to Supabase

# Real-time Subscriptions
- Clean up subscriptions in useEffect cleanup function
- Use proper error handling for subscription events
- Implement proper state management for real-time data
- Use TypeScript for type-safe subscription payloads
- Handle subscription reconnection properly

# Storage
- Implement proper file type validation
- Use content-type headers for file uploads
- Implement proper error handling for storage operations
- Clean up storage resources when components unmount
- Use proper file naming conventions

# Edge Functions
- Use proper error handling for function invocations
- Implement proper type definitions for function payloads
- Use proper validation for function inputs
- Handle function timeouts properly
- Implement proper error responses

# Performance
- Use connection pooling for database operations
- Implement proper caching strategies
- Use proper indexing for database queries
- Optimize real-time subscriptions
- Use proper batch operations for bulk updates

# Security
- Never expose Supabase service role key in client code
- Implement proper CORS policies
- Use proper input sanitization
- Implement proper rate limiting
- Use proper audit logging for sensitive operations 