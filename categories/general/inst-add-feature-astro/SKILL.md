---
description: Framework-specific patterns for adding features to Astro 4 applications
globs: **/*.astro, **/*.ts, **/*.js
---

You are a senior Astro 4 developer focusing exclusively on framework-specific patterns for adding new features. These guidelines focus only on Astro-specific approaches, assuming general web development best practices are already understood.

# Content Collections
- Use typed collections with Zod schemas. Example:
```typescript
const posts = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    pubDate: z.date(),
    featured: z.boolean().default(false)
  })
})
```

- Implement collection queries effectively. Example:
```astro
---
const featuredPosts = await getCollection('posts', ({ data }) => {
  return data.featured && data.pubDate < new Date()
})
---
```

# View Transitions
- Use persistent elements across pages. Example:
```astro
<header transition:persist>
  <Navigation />
</header>
```

- Implement custom transitions. Example:
```astro
<div transition:animate="slide">
  <ProductCard transition:name="product-card">
    <h2 transition:name="product-title">{product.title}</h2>
  </ProductCard>
</div>
```

# Island Architecture
- Use client directives effectively. Example:
```astro
<InteractiveChart client:visible />
<ShoppingCart client:only="react" />
<UserProfile client:media="(max-width: 768px)" />
```

- Implement hydration control. Example:
```astro
<script>
  // Hydrates immediately
  const criticalFeature = document.querySelector('.critical')
  criticalFeature.initialize()
</script>

<script defer>
  // Hydrates after page load
  import { initializeFeature } from './feature'
</script>
```

# Server Endpoints
- Create type-safe API routes. Example:
```typescript
export async function GET({ params, request }) {
  const products = await db.products.findMany({
    where: { category: params.category }
  })
  
  return new Response(JSON.stringify(products), {
    status: 200,
    headers: {
      'Content-Type': 'application/json'
    }
  })
}
```

# Middleware Features
- Use middleware for request handling. Example:
```typescript
export function onRequest({ request, locals }, next) {
  locals.user = await auth.getUser(request)
  const response = await next()
  response.headers.set('X-Custom-Header', 'value')
  return response
}
```

# Performance Features
- Use image optimization. Example:
```astro
<Image 
  src={product.image} 
  width={300} 
  height={200} 
  format="webp" 
  loading="lazy" 
/>
```

- Implement partial hydration. Example:
```astro
<Component client:idle>
  <SubComponent client:visible />
</Component>
```

# State Management
- Use Nano Stores effectively. Example:
```typescript
export const cartStore = atom({
  items: [],
  total: 0
})

export function addToCart(product) {
  cartStore.set({
    items: [...cartStore.get().items, product],
    total: cartStore.get().total + product.price
  })
}
```

# Integration Features
- Use framework components properly. Example:
```astro
---
import { Counter } from './Counter.jsx'
import { Timer } from './Timer.svelte'
---

<Counter client:load />
<Timer client:visible />
```

# Error Handling
- Implement error boundaries. Example:
```astro
---
let error = null
try {
  const data = await fetchData()
} catch (e) {
  error = e
}
---

{error ? <ErrorComponent error={error} /> : <DataDisplay data={data} />}
```

# SEO Features
- Use metadata effectively. Example:
```astro
---
const { frontmatter } = Astro.props
---
<head>
  <title>{frontmatter.title}</title>
  <meta name="description" content={frontmatter.description} />
  <meta property="og:image" content={frontmatter.image} />
  <link rel="canonical" href={new URL(Astro.url.pathname, Astro.site)} />
</head>
```

# Dos
- Use Content Collections for feature data
- Implement View Transitions properly
- Use Islands Architecture effectively
- Configure SSR appropriately
- Handle server integration properly

# Donts
- Don't skip schema validation
- Avoid unnecessary client hydration
- Don't bypass transition system
- Don't ignore SSR capabilities
- Don't misuse server features 