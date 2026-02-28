# V8 Perfector 索引

## 📚 按主题分类

### 🚀 编译 & JIT
| 文档 | 标签 | 说明 |
|------|------|------|
| turbofan-jit | jit, compiler | TurboFan JIT 编译器 |
| maglev | jit, compiler | Maglev 编译器 |
| sparkplug | jit, compiler | Sparkplug 编译器 |
| ignition-interpreter | interpreter | Ignition 解释器 |
| leaving-the-sea-of-nodes | compiler, IR | Sea of Nodes IR |
| slack-tracking | compiler, optimization | 优化技术 |
| csa | compiler, asm | 代码生成 |
| background-compilation | compiler, async | 后台编译 |
| short-builtin-calls | compiler, performance | 内联优化 |
| jitless | runtime, security | 无JIT模式 |

### 🗑️ 垃圾回收
| 文档 | 标签 | 说明 |
|------|------|------|
| orinoco | gc, parallel | 并行GC |
| orinoco-parallel-scavenger | gc, scavenger | 扫描回收 |
| free-garbage-collection | gc | 自由GC |
| lazy-unlinking | gc, optimization | 延迟解链 |

### 💾 内存管理
| 文档 | 标签 | 说明 |
|------|------|------|
| optimizing-v8-memory | memory, optimization | 内存优化 |
| heap-size-limit | memory, limit | 堆大小限制 |
| static-roots | memory, roots | 静态根 |
| trash-talk | gc, humor | GC 详解 |
| optimizing-v8-memory | memory | 内存优化 |
| sandbox | security, memory | 沙箱 |

### 🕸️ WebAssembly
| 文档 | 标签 | 说明 |
|------|------|------|
| wasm-gc-porting | wasm, gc | WASM GC |
| wasm-speculative-optimizations | wasm, optimization | 投机优化 |
| wasm-code-caching | wasm, cache | 代码缓存 |
| wasm-tail-call | wasm, tail-call | 尾调用 |
| liftoff | wasm, compiler | Liftoff编译器 |
| emscripten-llvm-wasm | wasm, emscripten | Emscripten集成 |
| emscripten-standalone-wasm | wasm, standalone | 独立WASM |
| 4gb-wasm-memory | wasm, memory | 4GB内存 |

### ⚡ JavaScript 特性
| 文档 | 标签 | 说明 |
|------|------|------|
| array-sort | array, sort | 数组排序 |
| elements-kinds | array, elements | 元素类型 |
| spread-elements | array, spread | 展开运算符 |
| fast-for-in | object, iteration | for-in优化 |
| fast-properties | object, optimization | 属性访问 |
| fast-super | object, class | super优化 |
| fast-async | async, promise | async/await |
| jspi | async, promise | Promise集成 |
| jspi-newapi | async, api | 新API |
| bigint | type, number | 大整数 |
| dataview | type, buffer | 数据视图 |
| non-backtracking-regexp | regex, performance | 正则优化 |
| regexp-tier-up | regex, optimization | 分层优化 |
| faster-class-features | class, es6 | 类特性 |
| modern-javascript | js, modern | 现代JS |
| json-stringify | json, serialization | JSON序列化 |
| hash-code | hash, object | 哈希码 |
| math-random | math, random | 随机数 |

### 📊 性能 & 基准
| 文档 | 标签 | 说明 |
|------|------|------|
| cost-of-javascript-2019 | performance, analysis | JS成本分析 |
| real-world-performance | performance, metrics | 真实性能 |
| speedometer-2 | benchmark, testing | 基准测试 |
| jank-busters | performance, ui | 流畅度 |
| retiring-octane | benchmark, history | 旧基准 |
| code-caching-for-devs | cache, developer | 代码缓存 |
| javascript-code-coverage | coverage, testing | 代码覆盖 |

### 🔒 安全
| 文档 | 标签 | 说明 |
|------|------|------|
| spectre | security, vulnerability | 幽灵漏洞 |
| control-flow-integrity | security, cfi | 控制流完整性 |
| sandbox | security, isolation | 沙箱 |

### 📝 发布说明
| 文档 | 标签 | 说明 |
|------|------|------|
| v8-release-45~99 | release, history | 各版本发布 |
| faster-releases | release, cadence | 发布周期 |
| holiday-season-2023 | release, update | 节日更新 |

---

## 🔍 按标签搜索

### 核心概念
```
gc, memory, jit, compiler, interpreter, wasm, runtime
```

### 性能优化
```
optimization, performance, benchmark, cache
```

### 安全
```
security, sandbox, vulnerability
```

### JavaScript
```
array, object, async, promise, regex, type, modern-js
```

---

## 🎯 快速入口

| 需求 | 推荐 |
|------|------|
| 了解V8架构 | v8_DeepWiki, pointer-compression |
| 性能调优 | cost-of-javascript-2019, real-world-performance |
| GC问题 | orinoco, optimizing-v8-memory |
| WASM优化 | wasm-speculative-optimizations, liftoff |
| Async优化 | fast-async, jspi |
| 版本变化 | v8-releases |
