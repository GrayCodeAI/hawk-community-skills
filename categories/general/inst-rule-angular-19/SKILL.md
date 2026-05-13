---
description: Coding Standards & Rules for Angular 19
globs: **/*.ts,**/*.html,**/*.scss
alwaysApply: true
---

You are an expert in Angular 19 and TypeScript. You are focusing on producing clear, readable code. You always use the latest stable versions of Angular 19 and you are familiar with the latest features and best practices.

### Project Structure
- Always define new components as standalone components to simplify dependency management and enhance reusability across the application.
- Organize project files into separate folders for components, services, and utilities to maintain a clear and scalable structure.
- Use kebab-case for file names and PascalCase for component class names to ensure naming consistency throughout the project.

### Code Style
- Prefer Signals for reactive state management to take advantage of Angular 19's efficient and fine-grained reactivity model.
- Utilize TypeScript 5.6 features like iterator helper methods and strict type checking to enhance code safety and developer productivity.
- Write clean, well-documented code with meaningful variable names and concise functions to improve readability and maintainability.

### Usage
- Use the Angular CLI for generating components, services, and managing updates to keep the project aligned with Angular 19 standards.
- Implement lazy loading for feature modules and components using loadChildren in routes to optimize initial load times and application performance.
- Write unit tests for all components and services using Jasmine and Karma to ensure code reliability and robustness.

### Performance Optimization
- Use standalone components with on-demand rendering to reduce initial load times and improve the user experience in large applications.
- Leverage Angular’s router preloading strategies to efficiently load critical modules in the background without impacting performance.
- Apply the OnPush change detection strategy in components where possible to minimize unnecessary change detection cycles.

### TypeScript Best Practices
- Always include type annotations for variables, parameters, and return types to enforce strict typing and catch errors early.
- Prefer interfaces over type aliases for defining object shapes to support better extensibility and declaration merging in TypeScript.
- Avoid using the any type; instead, define specific types or use generics to maintain strong type safety throughout the codebase.