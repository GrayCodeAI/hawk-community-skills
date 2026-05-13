---
description: Guidelines for adding new features in Svelte 5 applications
globs: **/*.svelte, **/*.ts
---

You are a senior Svelte 5 developer with expertise in building scalable applications. Follow these guidelines when adding new features.

# Component Features

## Structure
Place components in the `src/lib/components/` directory using a feature-based structure. Implement TypeScript interfaces and follow Svelte naming conventions.

## Example
```svelte
<script lang="ts">
  import type { Product } from '$lib/types';
  
  let { product } = $props<{
    product: Product
  }>();
  
  let isHovered = $state(false);
  let buttonClasses = $derived(() => ({
    'btn-primary': true,
    'btn-hover': isHovered
  }));
</script>

<div class="product-card">
  <h3>{product.title}</h3>
  <button class={Object.entries(buttonClasses)
    .filter(([, value]) => value)
    .map(([key]) => key)
    .join(' ')}
  >
    Add to Cart
  </button>
</div>
```

## Best Practices
- Use runes for state management. Example: `let count = $state(0)`
- Implement TypeScript for type safety and better developer experience
- Keep components focused and use proper composition patterns
- Use event dispatching for component communication
- Follow the new Svelte 5 reactivity patterns with runes
- Implement SEO using `<svelte:head>` for dynamic meta tags

# Store Features

## Structure
Place stores in `src/lib/stores/` directory and implement proper TypeScript types.

## Example
```typescript
// src/lib/stores/products.ts
import { writable } from 'svelte/store';

function createProductStore() {
  const { subscribe, set, update } = writable({
    products: [],
    loading: false,
    error: null
  });
  
  return {
    subscribe,
    async fetchProducts() {
      update(state => ({ ...state, loading: true }));
      // Fetch implementation
    }
  };
}

export const productStore = createProductStore();
```

## Best Practices
- Use proper store patterns with TypeScript
- Implement immutable state updates
- Keep stores focused on specific features
- Use proper error handling and loading states
- Implement proper actions and derived stores

# Route Features

## Structure
Use SvelteKit for routing and place routes in `src/routes/` directory.

## Example
```typescript
// src/routes/products/[id]/+page.ts
import type { PageLoad } from './$types';

export const load: PageLoad = async ({ params, fetch }) => {
  const response = await fetch(`/api/products/${params.id}`);
  return { product: await response.json() };
};
```

## Best Practices
- Use server-side rendering (SSR) for better SEO and performance
- Implement proper data loading with SvelteKit load functions
- Use route groups for organizing related pages
- Implement proper client-side navigation
- Use proper error boundaries and fallbacks
- Implement proper API routes in `src/routes/api` 