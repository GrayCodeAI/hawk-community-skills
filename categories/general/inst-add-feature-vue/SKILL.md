---
description: "Framework-specific patterns for adding features to Vue 3 applications"
globs: "**/*.vue, **/*.ts, **/*.js"
---

You are a senior Vue 3 developer focusing exclusively on framework-specific patterns for adding new features. These guidelines focus only on Vue-specific approaches, assuming general web development best practices are already understood.

# Composition API Features

## Basic Component
```vue
<script setup lang="ts">
import { ref, computed } from 'vue'

const count = ref(0)
const doubled = computed(() => count.value * 2)

function increment() {
  count.value++
}
</script>

<template>
  <div>
    <p>Count: {{ count }}</p>
    <p>Doubled: {{ doubled }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>
```

## Composable Function
```typescript
// composables/useFeature.ts
import { ref, onMounted, onUnmounted } from 'vue'

export function useFeature() {
  const isActive = ref(false)
  const data = ref(null)

  async function fetchData() {
    data.value = await fetch('/api/data')
  }

  onMounted(() => {
    isActive.value = true
    fetchData()
  })

  onUnmounted(() => {
    isActive.value = false
  })

  return {
    isActive,
    data,
    fetchData
  }
}
```

## Best Practices
- Use script setup syntax
- Implement proper composables
- Handle lifecycle hooks
- Manage reactive state
- Structure component logic

# Component Features

## Props and Events
```vue
<script setup lang="ts">
const props = defineProps<{
  title: string
  items: Array<{ id: number; name: string }>
}>()

const emit = defineEmits<{
  'update': [item: { id: number; name: string }]
  'delete': [id: number]
}>()
</script>

<template>
  <div>
    <h2>{{ title }}</h2>
    <ul>
      <li v-for="item in items" :key="item.id">
        {{ item.name }}
        <button @click="emit('delete', item.id)">Delete</button>
      </li>
    </ul>
  </div>
</template>
```

## Two-way Binding
```vue
<script setup lang="ts">
const model = defineModel<string>()
const count = defineModel<number>('count', { default: 0 })
</script>

<template>
  <input v-model="model" />
  <input type="number" v-model="count" />
</template>
```

## Best Practices
- Use defineProps properly
- Implement defineEmits
- Handle defineModel
- Manage component state
- Structure prop validation

# Async Features

## Suspense Integration
```vue
<template>
  <Suspense>
    <template #default>
      <AsyncFeature />
    </template>
    <template #fallback>
      <LoadingSpinner />
    </template>
  </Suspense>
</template>

<script setup lang="ts">
import { defineAsyncComponent } from 'vue'

const AsyncFeature = defineAsyncComponent(() =>
  import('./AsyncFeature.vue')
)
</script>
```

## Async Setup
```vue
<script setup lang="ts">
const data = await fetch('/api/data')
const result = await data.json()

// Component won't render until data is loaded
</script>

<template>
  <div>
    {{ result }}
  </div>
</template>
```

## Best Practices
- Use Suspense properly
- Handle async components
- Manage loading states
- Structure async setup
- Handle error scenarios

# State Management

## Provide/Inject Pattern
```vue
<script setup lang="ts">
import { provide, ref } from 'vue'

const feature = ref({
  enabled: true,
  config: {}
})

provide('feature', {
  state: feature,
  toggle: () => feature.value.enabled = !feature.value.enabled
})
</script>

<script setup lang="ts">
import { inject } from 'vue'

const { state, toggle } = inject('feature')
</script>
```

## Reactive Store
```typescript
// stores/featureStore.ts
import { reactive } from 'vue'

export const featureStore = reactive({
  items: [],
  async addItem(item) {
    this.items.push(item)
  },
  removeItem(id) {
    const index = this.items.findIndex(item => item.id === id)
    if (index > -1) this.items.splice(index, 1)
  }
})
```

## Best Practices
- Use provide/inject properly
- Implement reactive stores
- Handle shared state
- Manage state updates
- Structure store patterns

# Dos
- Use Composition API
- Implement script setup
- Use defineModel
- Handle async properly
- Follow reactivity rules

# Donts
- Don't use Options API
- Avoid this keyword
- Don't mix styles
- Don't ignore reactivity
- Don't skip proper setup 