---
description: Guidelines for adding new features in Nuxt 3 applications
globs: **/*.vue, **/*.ts, **/*.js
---

You are a senior Nuxt 3 developer with expertise in building scalable applications.

# Page Features
- Use Nuxt's file-based routing in pages directory. Example: pages/products/[id].vue
- Implement hybrid rendering modes. Example: definePageMeta({ ssr: true, swr: 3600 })
- Use route middleware for navigation guards. Example: definePageMeta({ middleware: ['auth'] })
- Implement layout system effectively. Example: definePageMeta({ layout: 'custom' })
- Use route validation with validate helper. Example: definePageMeta({ validate: route => /^\d+$/.test(route.params.id) })

# Data Fetching
- Use useAsyncData for complex data operations. Example:
```typescript
const { data, pending } = await useAsyncData('products', 
  () => $fetch('/api/products', { 
    query: { category: 'electronics' }
  })
)
```

- Implement useFetch for simple API calls. Example:
```typescript
const { data: product } = await useFetch(`/api/products/${id}`, {
  key: `product-${id}`,
  pick: ['id', 'title', 'price']
})
```

- Use useLazyFetch for deferred loading. Example:
```typescript
const { pending, data: comments } = useLazyFetch(`/api/products/${id}/comments`, {
  watch: [id]
})
```

# State Management
- Use useState for shared state. Example: const counter = useState('counter', () => 0)
- Implement Pinia stores with auto-imports. Example:
```typescript
export const useProductStore = defineStore('products', {
  state: () => ({ items: [] as Product[] }),
  actions: {
    async fetch() {
      this.items = await $fetch('/api/products')
    }
  }
})
```

# Component Architecture
- Use component slots for flexible layouts. Example:
```vue
<BaseCard>
  <template #header>
    <h2>{{ title }}</h2>
  </template>
  <template #default>
    <p>{{ content }}</p>
  </template>
</BaseCard>
```

- Implement composables for reusable logic. Example:
```typescript
export const useCart = () => {
  const items = useState<CartItem[]>('cart-items', () => [])
  const add = (product: Product) => items.value.push({ ...product, quantity: 1 })
  return { items, add }
}
```

# Server Features
- Use Nitro API routes with typed handlers. Example:
```typescript
export default defineEventHandler(async (event) => {
  const { id } = getRouterParams(event)
  const body = await readBody(event)
  return await prisma.product.update({ 
    where: { id }, 
    data: body 
  })
})
```

- Implement server middleware. Example:
```typescript
export default defineEventHandler((event) => {
  event.context.auth = { user: getUser(event) }
})
```

# Performance Features
- Use component lazy loading. Example: const Modal = defineAsyncComponent(() => import('./Modal.vue'))
- Implement image optimization with Nuxt Image. Example: <NuxtImg src="/product.jpg" width="300" format="webp" />
- Use route level code splitting. Example: definePageMeta({ keepalive: true, key: route => route.fullPath })
- Implement proper chunk naming. Example: defineNuxtConfig({ vite: { build: { rollupOptions: { output: { manualChunks: { vendor: ['vue'] } } } } } })
- Use proper cache headers. Example: useHead({ cacheControl: 'max-age=3600' })

# Composables
- Create type-safe composables. Example:
```typescript
export const useSearch = <T extends { id: string }>(url: string) => {
  const query = ref('')
  const results = ref<T[]>([])
  
  watch(query, async (value) => {
    results.value = await $fetch(url, { 
      query: { search: value } 
    })
  })
  
  return { query, results }
}
```

# Error Handling
- Use error boundaries with onErrorCaptured. Example: const error = useError()
- Implement custom error pages. Example: error.vue with proper error props
- Use proper API error handling. Example: createError({ statusCode: 404, message: 'Not found' })
- Implement toast notifications for errors
- Use proper validation error handling

# SEO Features
- Use useHead for dynamic meta tags. Example:
```typescript
useHead({
  title: computed(() => product.value?.title),
  meta: [
    { name: 'description', content: computed(() => product.value?.description) }
  ]
})
```
- Implement canonical URLs dynamically
- Use proper OpenGraph tags
- Implement JSON-LD structured data
- Use proper sitemap generation 