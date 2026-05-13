---
description: 该规则解释了 Flutter 小部件模式和跨平台移动开发的最佳实践。
globs: **/*.dart
alwaysApply: false
---

# Flutter 规则

- 对于没有内部状态的 UI 组件使用 StatelessWidget。
- 对于需要维护状态的组件使用 StatefulWidget：

```dart
class Counter extends StatefulWidget {
  @override
  _CounterState createState() => _CounterState();
}

class _CounterState extends State<Counter> {
  int _count = 0;

  void _increment() {
    setState(() { _count++; });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text('Count: $_count'),
        ElevatedButton(onPressed: _increment, child: Text('Increment')),
      ],
    );
  }
}
```

- 对于复杂应用使用状态管理解决方案（Provider、Bloc、Riverpod）。
- 使用适当的文件夹结构组织代码（models、screens、widgets、services）。
- 使用命名路由和 Navigator.pushNamed() 进行导航。
- 使用 async/await 处理异步操作，并进行适当的错误处理。
- 使用主题（themes）在整个应用中保持一致的样式。