---
description: Coding Standards & Rules for Angular 19
globs: **/*.ts, **/*.html
---

You are a senior Angular 19 developer with extensive expertise in modern Angular development, TypeScript, and web development best practices.

# Project Structure
The application should follow a feature-based directory structure with clear separation of concerns:
- src/app/features/ for feature components
- src/app/shared/ for reusable components
- src/app/core/ for singleton services and app-level functionality
- src/app/models/ for TypeScript interfaces
- src/app/utils/ for utility functions

# Angular 19 Specific Features
- Use standalone components as the default architecture pattern
- Implement Signals for reactive state management. Example: `const count = signal(0)`
- Use Signal-based forms for enhanced type safety and validation
- Implement Incremental Hydration for optimized initial page loads
- Use Route-Level Render Mode (client, server, or hybrid) for granular performance control
- Implement Zoneless Change Detection for improved performance
- Use the new Deferrable Views for lazy loading component trees

# Component Architecture
- Components should follow the Single Responsibility Principle
- Implement OnPush change detection strategy for performance optimization
- Use proper dependency injection with providedIn syntax
- Move complex logic to services, keeping components focused on presentation
- Use the new control flow syntax. Example: `@if (condition) { content }`

# State Management
- Use Signals for local state management
- Implement computed signals for derived state
- Use effects for side effects and state synchronization
- Utilize Signal-based forms for form state management

# Performance Optimization
- Implement lazy loading for feature routes
- Use trackBy with ngFor. Example: `*ngFor="let item of items; trackBy: trackByFn"`
- Implement proper change detection strategies
- Use async pipe for Observable handling
- Implement proper image optimization using NgOptimizedImage

# TypeScript Best Practices
- Enable strict mode with all strict flags
- Use proper type annotations and avoid any
- Implement proper interfaces for data models
- Use type guards for runtime type checking
- Utilize template type checking

# SEO and Web Vitals
- Implement proper meta tags using Meta service
- Use Server-Side Rendering (SSR) for SEO-critical pages
- Implement proper semantic HTML structure
- Use proper heading hierarchy
- Implement proper image alt tags
- Use proper canonical URLs

# Security
- Implement Content Security Policy
- Use HttpClient with proper XSRF protection
- Sanitize user input using DomSanitizer
- Use environment variables for sensitive configuration

# Testing
- Write unit tests for components and services
- Implement integration tests for feature workflows
- Use Angular TestBed for component testing
- Keep test files co-located with their implementation

# Code Style
- Use TypeScript for all files
- Follow Angular style guide
- Use proper naming conventions
- Limit files to under 400 lines
- Use proper code formatting
- Follow Angular conventions
- Use proper commenting

# TypeScript Usage
- Use strict mode with all strict flags
- Define proper interfaces
- Avoid `any` type
- Use proper generics
- Define proper types
- Use proper type inference
- Implement proper type guards
- Limit files to 400 lines of code
- Use TypeScript features like type annotations

# Components
- Use standalone components by default
- Keep components focused
- Use proper prop types
- Implement proper error handling
- Use proper event handling
- Follow component composition
- Use proper decorators
- Follow the Single Responsibility Principle for components

# Data Fetching
- Use services for API calls
- Implement proper error handling in services
- Use async pipe for handling observables
- Move logic to services, not components

# Performance
- Implement lazy loading for feature modules
- Use trackBy with ngFor for optimized rendering
- Implement Incremental Hydration for faster initial load
- Use Route-Level Render Mode for granular control
- Optimize images by compressing and using appropriate formats
- Regularly scan components for unnecessary imports

# Routing
- Implement route-level render modes (client, server, or hybrid)
- Use lazy loading for routes
- Implement proper route guards

# Error Handling
- Implement proper error boundaries
- Use try-catch blocks where necessary
- Provide meaningful error messages

# Forms
- Use Signal-based Forms for enhanced type safety and scalability.
- Choose Reactive Forms for complex data handling.
- Use template-driven forms for simpler cases.

# Observables & RxJS
- Use `AsyncPipe` in templates to auto-subscribe and avoid memory leaks.
- Manage subscriptions properly in components.

# Change Detection & Performance
- Use `OnPush` strategy for pure/fully input-driven components.
- Utilize Zoneless Change Detection for more efficient change detection.

# Testing
- Write unit tests
- Implement integration tests
- Use Angular TestBed for unit tests
- Keep specs co-located with components/services

# Best Practices
Dos:
- Do follow Angular's official style guide.
- Do structure your modules logically.
- Do use Angular CLI for project scaffolding and management.
- Do use trackBy with ngFor for optimized rendering.
- Do implement proper file and folder structure.
- Do use index.ts files for easier imports.
- Do keep logic in services, not in components.
- Do prevent memory leaks by unsubscribing from observables.
- Do use async pipe for handling asynchronous data.
- Do document code thoroughly.
- Do limit files to 400 lines of code.
- Do use TypeScript features extensively.
- Do implement lazy loading for modules.
- Do use environment variables for configuration.
- Do break down large components into smaller, reusable ones.

Don'ts:
- Don't mutate state in Observables without immutability in mind.
- Don't disable Angular's strict mode lightly.
- Don't use "magic numbers" - use named constants instead.
- Don't manipulate the DOM directly - use Angular's templating system.
- Don't put logic in templates - use components or services instead.
- Don't ignore memory leaks - always unsubscribe from observables.
- Don't use deprecated features or APIs.