---
name: v8-advanced
description: V8 Advanced Features - Pointer compression, memory optimization, security, and other advanced topics. Load this when needing deep V8 internals knowledge.
---

# V8 Advanced Features

Reference documents in `../reference/`:

## 🔧 指针压缩 (Pointer Compression)
| 文档 | 说明 |
|------|------|
| pointer-compression.md | 指针压缩技术 |
| oilpan-pointer-compression.md | Oilpan 指针压缩 |

## 💾 内存管理 (Memory)
| 文档 | 说明 |
|------|------|
| optimizing-v8-memory.md | V8 内存优化 |
| heap-size-limit.md | 堆大小限制 |
| static-roots.md | 静态根 |
| sandbox.md | V8 沙箱 |
| trash-talk.md | GC 深入解析 |

## 🔒 安全 (Security)
| 文档 | 说明 |
|------|------|
| spectre.md | 幽灵漏洞 |
| control-flow-integrity.md | 控制流完整性 |
| sandbox.md | 沙箱技术 |

## ⚡ 性能优化 (Performance)
| 文档 | 说明 |
|------|------|
| cost-of-javascript-2019.md | JS 成本分析 |
| real-world-performance.md | 真实性能 |
| code-caching-for-devs.md | 代码缓存 |
| slack-tracking.md | Slack 追踪 |

## 🔬 编译器 (Compiler)
| 文档 | 说明 |
|------|------|
| leaving-the-sea-of-nodes.md | Sea of Nodes IR |
| embedded-builtins.md | 内置代码嵌入 |
| short-builtin-calls.md | 短内置调用 |
| explicit-compile-hints.md | 显式编译提示 |

## 🚀 启动优化 (Startup)
| 文档 | 说明 |
|------|------|
| custom-startup-snapshots.md | 自定义启动快照 |
| lazy-deserialization.md | 延迟反序列化 |

## 📊 调试 & 分析 (Debug & Analysis)
| 文档 | 说明 |
|------|------|
| system-analyzer.md | 系统分析器 |
| speeding-up-v8-heap-snapshots.md | 堆快照优化 |
| javascript-code-coverage.md | 代码覆盖 |

## 🔬 内部实现 (Internals)
| 文档 | 说明 |
|------|------|
| preparser.md | 预解析器 |
| scanner.md | 词法扫描器 |
| mutable-heap-number.md | 可变堆数字 |

## 🔄 兼容性 (Compatibility)
| 文档 | 说明 |
|------|------|
| disabling-escape-analysis.md | 转义分析禁用 |
| high-performance-cpp-gc.md | 高性能 C++ GC |
| optimizing-proxies.md | Proxy 优化 |

## 🎯 核心概念

需要理解 V8 核心概念时加载这些：
- `pointer-compression.md` - 指针压缩基础
- `sandbox.md` - 内存安全
- `leaving-the-sea-of-nodes.md` - 编译器 IR
