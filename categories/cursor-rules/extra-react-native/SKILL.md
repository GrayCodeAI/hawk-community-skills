---
description: 该规则解释了 TypeScript、React Native、Expo 和移动 UI 开发的使用方法和最佳实践。
globs: **/*.jsx,**/*.tsx
alwaysApply: false
---

# TypeScript、React Native、Expo 和移动 UI 开发规则

## 代码风格和结构
- 编写清晰、可读的代码：确保你的代码易于阅读和理解。为变量和函数使用描述性名称。
- 使用函数组件：优先使用带有钩子（useState, useEffect 等）的函数组件，而非类组件。
- 组件模块化：将组件拆分为更小、可重用的部分。保持组件专注于单一职责。
- 按功能组织文件：将相关组件、钩子和样式按功能特性分组到目录中（例如，user-profile）。

## 命名约定
- 变量和函数：使用驼峰命名法(camelCase)命名变量和函数，并具有描述性（例如，isFetchingData, handleUserInput）。
- 组件：使用帕斯卡命名法(PascalCase)命名组件（例如，UserProfile）。
- 目录：使用小写和连字符命名目录（例如，user-profile）。

## TypeScript 使用
- 所有代码使用 TypeScript；接口(interfaces)优于类型(types)
- 避免使用枚举(enums)；使用映射(maps)代替
- 使用带有 TypeScript 接口的函数组件
- 在 TypeScript 中使用严格模式以提高类型安全性

## 语法和格式
- 使用 "function" 关键字定义纯函数
- 避免在条件语句中使用不必要的花括号；简单语句使用简洁语法
- 使用声明式 JSX
- 使用 Prettier 保持代码格式一致

## UI 和样式
- 使用 Expo 内置组件实现常见 UI 模式和布局
- 使用 Flexbox 和 Expo 的 useWindowDimensions 实现响应式设计
- 使用 styled-components 或 Tailwind CSS 进行组件样式设计
- 使用 Expo 的 useColorScheme 实现深色模式支持
- 确保高可访问性(a11y)标准，使用 ARIA 角色和原生可访问性属性
- 利用 react-native-reanimated 和 react-native-gesture-handler 实现高性能动画和手势

## 安全区域管理
- 使用 react-native-safe-area-context 中的 SafeAreaProvider 全局管理安全区域
- 用 SafeAreaView 包装顶层组件，处理 iOS 和 Android 上的刘海、状态栏和其他屏幕缩进
- 使用 SafeAreaScrollView 处理可滚动内容，确保其尊重安全区域边界
- 避免为安全区域硬编码内边距或外边距；依赖 SafeAreaView 和上下文钩子

## 性能优化
- 最小化 useState 和 useEffect 的使用；优先使用 context 和 reducers 进行状态管理
- 使用 Expo 的 AppLoading 和 SplashScreen 优化应用启动体验
- 优化图像：在支持的地方使用 WebP 格式，包含尺寸数据，使用 expo-image 实现延迟加载
- 使用 React 的 Suspense 和动态导入实现代码分割和非关键组件的懒加载
- 使用 React Native 内置工具和 Expo 调试功能监控性能
- 通过适当使用组件记忆化、useMemo 和 useCallback 钩子避免不必要的重新渲染

## 导航
- 使用 react-navigation 进行路由和导航；遵循其栈导航器、标签导航器和抽屉导航器的最佳实践
- 利用深度链接和通用链接提升用户参与度和导航流程
- 使用 expo-router 的动态路由以获得更好的导航处理

## 状态管理
- 使用 React Context 和 useReducer 管理全局状态
- 利用 react-query 进行数据获取和缓存；避免过多的 API 调用
- 对于复杂的状态管理，考虑使用 Zustand 或 Redux Toolkit
- 使用 expo-linking 等库处理 URL 搜索参数

## 错误处理和验证
- 使用 Zod 进行运行时验证和错误处理
- 使用 Sentry 或类似服务实现适当的错误日志记录
- 优先处理错误和边缘情况：
  - 在函数开始时处理错误
  - 为错误条件使用提前返回，避免深度嵌套的 if 语句
  - 避免不必要的 else 语句；使用 if-return 模式
  - 实现全局错误边界以捕获和处理意外错误
- 使用 expo-error-reporter 记录和报告生产环境中的错误

## 测试
- 使用 Jest 和 React Native Testing Library 编写单元测试
- 使用 Detox 为关键用户流程实现集成测试
- 使用 Expo 的测试工具在不同环境中运行测试
- 考虑为组件使用快照测试以确保 UI 一致性

## 安全
- 清理用户输入以防止 XSS 攻击
- 使用 react-native-encrypted-storage 安全存储敏感数据
- 确保使用 HTTPS 和适当的身份验证与 API 进行安全通信
- 使用 Expo 的安全指南保护应用程序：https://docs.expo.dev/guides/security/

## 国际化 (i18n)
- 使用 react-native-i18n 或 expo-localization 进行国际化和本地化
- 支持多语言和 RTL 布局
- 确保文本缩放和字体调整以提高可访问性

## 关键约定
1. 依赖 Expo 的托管工作流程简化开发和部署
2. 优先考虑移动 Web 性能指标（加载时间、卡顿和响应性）
3. 使用 expo-constants 管理环境变量和配置
4. 使用 expo-permissions 优雅处理设备权限
5. 实现 expo-updates 进行空中(OTA)更新
6. 遵循 Expo 的应用部署和发布最佳实践：https://docs.expo.dev/distribution/introduction/
7. 通过在 iOS 和 Android 平台上进行广泛测试，确保兼容性

## API 文档
- 使用 Expo 官方文档设置和配置项目：https://docs.expo.dev/

请参考 Expo 文档获取有关 Views、Blueprints 和 Extensions 的最佳实践详细信息。
