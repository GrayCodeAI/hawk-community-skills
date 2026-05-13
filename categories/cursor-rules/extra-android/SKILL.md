---
description: Android 原生开发约定和最佳实践，包括 Kotlin、Jetpack Compose、架构模式等
globs: **/*.kt,**/*.java,**/*.xml
alwaysApply: false
---

# Android 开发规范

## 项目结构和模块化

- 使用标准的 Android 项目结构
- 按功能模块组织代码，实现模块化架构
- 使用 Gradle Version Catalogs 管理依赖版本
- 合理划分 `app`、`feature`、`core`、`data` 模块
- 遵循包命名约定：`com.company.app.feature.domain`
- 分离 `presentation`、`domain`、`data` 层

## 编程语言和代码规范

- **强制使用 Kotlin**，避免 Java（除非维护遗留代码）
- 遵循 [Kotlin 编码规范](mdc:languages/kotlin.mdc)
- 优先使用数据类、密封类和内联类
- 合理使用扩展函数增强现有 API
- 使用协程和 Flow 进行异步编程
- 避免使用 `!!` 操作符，优先使用安全调用

## UI 开发

### Jetpack Compose（推荐）
- **优先使用 Jetpack Compose** 构建现代声明式 UI
- 遵循 Composition over inheritance 原则
- 使用 `@Composable` 函数构建可重用组件
- 正确使用 `remember`、`LaunchedEffect`、`derivedStateOf`
- 实现 `CompositionLocal` 进行依赖传递
- 使用 `Modifier` 进行样式和行为定制

### 传统 View 系统
- 使用 View Binding 替代 `findViewById`
- 避免使用 Data Binding（除非必要）
- 正确使用 `ConstraintLayout` 和 `RecyclerView`
- 实现自定义 View 时遵循测量、布局、绘制流程

### 设计规范
- 遵循 **Material Design 3** 设计规范
- 实现动态颜色主题（Material You）
- 支持深色主题和高对比度模式
- 实现响应式布局适配不同屏幕尺寸
- 使用 `WindowInsets` 处理状态栏和导航栏

## 架构模式

### 推荐架构
- 使用 **MVVM** 或 **MVI** 架构模式
- 遵循 **Clean Architecture** 原则
- 实现 **Repository 模式** 进行数据抽象
- 使用 **UseCase/Interactor** 封装业务逻辑
- 采用 **单向数据流** 设计

### ViewModel 最佳实践
- 使用 `ViewModel` 管理 UI 相关数据
- 通过 `StateFlow`/`LiveData` 暴露状态
- 在 `ViewModel` 中处理业务逻辑
- 正确使用 `viewModelScope` 管理协程
- 避免在 `ViewModel` 中持有 Context 引用

## 依赖注入

- **强制使用 Dagger Hilt** 进行依赖注入
- 正确配置 `@Module`、`@InstallIn`、作用域注解
- 使用 `@Qualifier` 区分相同类型的不同实现
- 避免循环依赖，合理设计依赖关系
- 使用 `@Provides` 和 `@Binds` 提供依赖
- 在测试中使用 `@TestInstallIn` 替换模块

## 数据层实现

### 本地存储
- 使用 **Room** 数据库进行复杂数据存储
- 使用 **DataStore** 替代 SharedPreferences
- 正确实现数据库迁移策略
- 使用 `@TypeConverter` 处理复杂数据类型
- 实现数据访问对象（DAO）模式

### 缓存策略
- 实现 **Repository** 模式统一数据访问
- 使用 `@Query` 和 `Flow` 实现响应式数据
- 实现离线优先（Offline-first）策略
- 正确处理缓存失效和数据同步

## 网络层

- 使用 **Retrofit** 进行 REST API 调用
- 使用 **OkHttp** 拦截器处理认证、日志、缓存
- 实现适当的错误处理和重试机制
- 使用 **Moshi** 或 **Kotlinx Serialization** 进行 JSON 解析
- 正确处理网络连接状态变化
- 实现请求去重和防抖动

## 异步编程和响应式

- **强制使用 Kotlin Coroutines** 进行异步编程
- 正确使用 `suspend` 函数和协程作用域
- 使用 **Flow** 进行响应式数据流编程
- 正确使用 `collectAsState()`、`collectAsStateWithLifecycle()`
- 避免使用 `GlobalScope`，使用结构化并发
- 正确处理协程取消和异常

## 生命周期管理

- 正确处理 Activity 和 Fragment 生命周期
- 使用 **Lifecycle-aware** 组件（`LifecycleObserver`）
- 在 Compose 中使用 `DisposableEffect` 管理资源
- 使用 `viewLifecycleOwner` 在 Fragment 中观察数据
- 避免在组件销毁后执行异步操作

## 导航和路由

- 使用 **Navigation Component** 进行页面导航
- 在 Compose 中使用 **Compose Navigation**
- 正确处理深度链接（Deep Links）
- 使用 Safe Args 进行类型安全的参数传递
- 实现单一 Activity 多 Fragment 架构

## 性能优化

### 渲染性能
- 使用 **Baseline Profiles** 优化应用启动
- 避免过度绘制和布局嵌套
- 正确使用 `RecyclerView` 的 `ViewHolder` 模式
- 在 Compose 中合理使用 `key()` 和 `remember()`

### 内存管理
- 避免内存泄漏，正确管理对象生命周期
- 使用 **LeakCanary** 检测内存泄漏
- 合理使用图片加载库（Glide、Coil）
- 实现懒加载和分页加载

### 启动优化
- 使用 **App Startup** 优化初始化流程
- 实现启动画面（Splash Screen API）
- 避免在 Application 中执行耗时操作

## 测试策略

### 单元测试
- 为业务逻辑编写单元测试，目标覆盖率 ≥80%
- 使用 **MockK** 进行 Kotlin 友好的模拟测试
- 使用 **Truth** 断言库提高测试可读性
- 测试 Repository、UseCase、ViewModel 层

### UI 测试
- 使用 **Compose Test** 测试 Compose UI
- 使用 **Espresso** 测试传统 View 系统
- 实现端到端测试覆盖关键用户流程
- 使用 **Hilt Testing** 进行依赖注入测试

## 安全实践

- 正确实现运行时权限请求
- 使用 **Android Keystore** 存储敏感数据
- 实现网络安全配置（Network Security Config）
- 使用 **Certificate Pinning** 防止中间人攻击
- 避免在日志中输出敏感信息
- 实现代码混淆和反调试措施

## 国际化和无障碍

- 实现多语言支持（i18n）
- 使用 **TalkBack** 测试无障碍功能
- 为 UI 元素添加 `contentDescription`
- 支持从右到左（RTL）布局
- 实现动态字体大小适配

## 构建和发布

### 构建配置
- 使用 **Gradle Kotlin DSL** 编写构建脚本
- 配置多变体构建（Debug/Release/Staging）
- 使用 **R8** 进行代码收缩和混淆
- 实现自动化版本管理

### 发布流程
- 使用 **Android App Bundle（AAB）** 进行发布
- 配置应用签名和密钥管理
- 实现渐进式发布和 A/B 测试
- 使用 **Play Console** 进行应用分析

## 代码质量保证

- 使用 **Detekt** 进行静态代码分析
- 配置 **Lint** 检查规则
- 使用 **ktfmt** 或 **ktlint** 进行代码格式化
- 实现 CI/CD 流水线进行自动化检查
- 定期进行代码审查（Code Review）