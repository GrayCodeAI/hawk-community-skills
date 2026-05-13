---
description: Coding Standards & Rules for Angular 19
globs: **/*.ts,**/*.html,**/*.scss
alwaysApply: true
---

You are an Angular 19 and TypeScript expert, focusing on clear, readable code with the latest stable version and best practices.

### Project Structure
- Use standalone components by default for simplicity and reusability.
- Organize files into components, services, and utilities folders for scalability.
- Apply kebab-case for files, PascalCase for components.

### Code Style
- Use Signals for reactive state management.
- Leverage TypeScript 5.6 features like iterator helpers and strict checks.
- Write concise, documented code with clear names.

### Usage
- Use Angular CLI for generation and updates.
- Lazy-load modules with loadChildren for performance.
- Test components and services with Jasmine/Karma.

### Performance Optimization
- Render standalone components on demand.
- Preload critical modules with router strategies.
- Use OnPush change detection where possible.

### TypeScript Best Practices
- Annotate all types for strictness.
- Prefer interfaces over type aliases for extensibility.
- Avoid any; use specific types or generics.

### General Angular 19 Coding Standards
- Inject dependencies in services for modularity.
- Use reactive forms for complex form handling.
- Handle errors with try-catch and ErrorHandler.

### Component Design
- Keep components small, extract logic to directives/pipes.
- Use typed @Input/@Output for clear data flow.
- Avoid DOM manipulation; use templates.

### State Management
- Combine Signals with RxJS for local vs. async state.
- Centralize app state in services or NgRx when needed.
- Update state immutably for predictability.

### Routing and Navigation
- Secure routes with guards (CanActivate, CanDeactivate).
- Prefetch data with resolvers.
- Track navigation with router events.

### Template Best Practices
- Optimize ngIf/ngFor with trackBy.
- Use async pipe for observables.
- Keep templates declarative, logic in components.

### Interoperability and Integration
- Create web components with custom elements.
- Use Angular Universal for SSR and SEO.
- Integrate Angular Material for UI consistency.