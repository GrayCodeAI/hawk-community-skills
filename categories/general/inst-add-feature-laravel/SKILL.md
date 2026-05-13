---
description: Guidelines for adding new features in Laravel 11 applications
globs: **/*.php
---

You are a senior Laravel 11 developer with expertise in building scalable applications.

# Controller Features
- Use invokable controllers for single actions. Example: CreateProductController
- Implement resource controllers for CRUD. Example: php artisan make:controller ProductController --resource
- Use form requests for validation. Example: php artisan make:request StoreProductRequest
- Implement API resources for responses. Example: php artisan make:resource ProductResource
- Use controller middleware effectively. Example: $this->middleware('auth')->except(['index', 'show'])

# Service Pattern
- Implement service classes for business logic. Example:
```php
class ProductService
{
    public function __construct(
        private readonly ProductRepository $repository,
        private readonly ImageService $imageService
    ) {}

    public function create(array $data): Product
    {
        return DB::transaction(function () use ($data) {
            $product = $this->repository->create($data);
            $this->imageService->attach($product, $data['image']);
            ProductCreated::dispatch($product);
            return $product;
        });
    }
}
```

# Repository Pattern
- Use repositories for data access. Example:
```php
class ProductRepository
{
    public function findByCategory(string $category): Collection
    {
        return Product::query()
            ->whereBelongsTo(Category::findBySlug($category))
            ->with(['variants', 'media'])
            ->cached()
            ->get();
    }
}
```

# Model Features
- Use Laravel's new model features. Example:
```php
class Product extends Model
{
    use HasUuid, SoftDeletes, HasFactory;
    
    protected $casts = [
        'price' => Price::class,
        'status' => ProductStatus::class,
        'settings' => AsArrayObject::class
    ];
    
    public function scopeActive($query): void
    {
        $query->where('status', ProductStatus::Active);
    }
}
```

# Event System
- Implement event listeners effectively. Example:
```php
class ProductEventSubscriber
{
    public function handleProductCreated(ProductCreated $event): void
    {
        Cache::tags(['products'])->flush();
        Notification::send($admins, new ProductCreatedNotification($event->product));
    }
    
    public function subscribe(Dispatcher $events): array
    {
        return [
            ProductCreated::class => 'handleProductCreated'
        ];
    }
}
```

# Job Queue Features
- Use job batching for complex operations. Example:
```php
$batch = Bus::batch([
    new ProcessProductImages($product),
    new UpdateSearchIndex($product),
    new NotifySubscribers($product)
])->then(function (Batch $batch) {
    Log::info('All jobs completed');
})->dispatch();
```

# Cache Features
- Implement cache tags and invalidation. Example:
```php
Cache::tags(['products', "product-{$id}"])
    ->remember("product-{$id}", 3600, fn () => 
        Product::with('category')->findOrFail($id)
    );
```

# API Features
- Use API resources with conditional attributes. Example:
```php
class ProductResource extends JsonResource
{
    public function toArray(Request $request): array
    {
        return [
            'id' => $this->id,
            'name' => $this->name,
            $this->mergeWhen($request->user()?->isAdmin(), [
                'cost' => $this->cost,
                'margin' => $this->margin
            ])
        ];
    }
}
```

# Testing Features
- Use Pest for testing with datasets. Example:
```php
test('it calculates product margins')
    ->with([
        [100, 150, 50],
        [200, 300, 100]
    ])
    ->expect(fn (int $cost, int $price, int $margin) => 
        Product::calculateMargin($cost, $price)
    )->toBe(fn (int $margin) => $margin);
```

# Performance Features
- Use lazy loading for collections. Example: Product::lazy()->each(fn ($product) => $product->process())
- Implement query builder improvements. Example: Product::whereFullText('description', $search)
- Use proper database indexing. Example: $table->fullText(['title', 'description'])
- Implement proper caching strategies. Example: Cache::tags(['products'])->remember()
- Use proper eager loading. Example: Product::with('category', 'tags')->get()

# SEO Features
- Use sitemap generation. Example: php artisan sitemap:generate
- Implement meta tags effectively. Example: <meta name="description" content="{{ $product->meta_description }}">
- Use proper canonical URLs. Example: <link rel="canonical" href="{{ $product->canonical_url }}">
- Implement schema markup. Example: @json(['@type' => 'Product', 'name' => $product->name])
- Use proper robots.txt management 