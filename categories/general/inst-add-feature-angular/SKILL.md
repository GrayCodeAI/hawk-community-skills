---
description: Framework-specific patterns for adding features to Angular 19 applications
globs: **/*.ts, **/*.html
---

You are a senior Angular 19 developer focusing exclusively on framework-specific patterns for adding new features.

# Signal State Management
- Use computed signals for derived state. Example: computed(() => this.count() * 2)
- Implement signal effects for side effects. Example: effect(() => console.log(this.count()))
- Use signal arrays with proper tracking. Example: items = signal<Item[]>([])
- Utilize signal inputs for component props. Example: input.required<string>()
- Implement signal queries for ViewChild. Example: viewChild.required<ElementRef>('element')

# Reactive Forms
- Use the new FormBuilder with signals. Example: form = formBuilder.group({ email: ['', Validators.email] })
- Implement form array signals for dynamic forms. Example: formArray = this.fb.array([])
- Use typed form controls. Example: new FormControl<string>('')
- Implement form validation with signals. Example: error = computed(() => this.form.controls.email.errors)
- Use form state tracking. Example: isPristine = computed(() => this.form.pristine)

# Modern Control Flow
- Use @if with else blocks for conditional rendering. Example:
```typescript
@if (isLoaded()) {
  <content-component />
} @else {
  <loading-component />
}
```

- Implement @switch for multiple conditions. Example:
```typescript
@switch (status()) {
  @case ('active') { <active-view /> }
  @case ('inactive') { <inactive-view /> }
  @default { <default-view /> }
}
```

- Use @for with proper tracking. Example:
```typescript
@for (item of items(); track item.id) {
  <item-component [data]="item" />
}
```

# Deferred Loading
- Use @defer with proper triggers. Example:
```typescript
@defer (on viewport) {
  <heavy-component />
} @loading {
  <loading-spinner />
}
```

- Implement multiple defer conditions. Example:
```typescript
@defer (on viewport; when isReady()) {
  <optimized-component />
}
```

- Use prefetching for improved performance. Example:
```typescript
@defer (prefetch on hover) {
  <prefetched-component />
}
```

# Performance Features
- Use standalone components by default. Example: @Component({ standalone: true })
- Implement required inputs for better type safety. Example: @Input({ required: true }) data!: Data
- Use the new NgOptimizedImage directive. Example: <img ngSrc="image.jpg" width="100" height="100" />
- Implement Signals DevTools for debugging. Example: enableDebugTools(componentRef)
- Use esbuild for faster compilation

# Dependency Injection
- Use the new injection syntax. Example: private service = inject(UserService)
- Implement environment injectors. Example: createEnvironmentInjector([providers])
- Use provider functions with signals. Example: { provide: USER_CONFIG, useValue: signal(config) }
- Implement hierarchical injectors effectively
- Use proper injection context management

# HTTP Features
- Use the new HttpClient with signals. Example: this.http.get<User[]>('/api/users').pipe(takeUntilDestroyed())
- Implement HTTP interceptors with signals
- Use proper error handling with catchError
- Implement retry logic with retryWhen
- Use proper cache management

# Router Features
- Use the new Router API with signals. Example: this.router.navigateByUrl('/dashboard')
- Implement route guards with signals
- Use route resolvers effectively
- Implement lazy loading with proper chunks
- Use router events for analytics

# Testing Features
- Use component harness testing. Example: await loader.getHarness(MatButtonHarness)
- Implement signal testing utilities
- Use TestBed with signals
- Implement E2E testing with Playwright
- Use proper component isolation

# SEO Features
- Use Meta service for dynamic meta tags. Example: this.meta.updateTag({ name: 'description', content: 'Dynamic content' })
- Implement proper title strategy
- Use server-side rendering effectively
- Implement proper canonical URLs
- Use robots.txt management 