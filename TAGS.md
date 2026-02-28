# V8 Perfector 标签索引

## 🏷️ 完整标签列表

### 编译 & 运行时
- **jit**: turbofan-jit, maglev, sparkplug, leaving-the-sea-of-nodes
- **compiler**: turbofan-jit, maglev, sparkplug, csa, liftoff, leaving-the-sea-of-nodes
- **interpreter**: ignition-interpreter
- **runtime**: jitless, custom-startup-snapshots
- **asm**: csa

### 垃圾回收
- **gc**: orinoco, orinoco-parallel-scavenger, free-garbage-collection, lazy-unlinking
- **scavenger**: orinoco-parallel-scavenger

### 内存
- **memory**: optimizing-v8-memory, heap-size-limit, static-roots, sandbox, 4gb-wasm-memory
- **heap**: optimizing-v8-memory, heap-size-limit
- **roots**: static-roots

### WebAssembly
- **wasm**: wasm-gc-porting, wasm-speculative-optimizations, wasm-code-caching, wasm-tail-call, liftoff, emscripten-llvm-wasm, emscripten-standalone-wasm, 4gb-wasm-memory
- **emscripten**: emscripten-llvm-wasm, emscripten-standalone-wasm

### JavaScript 特性
- **array**: array-sort, elements-kinds, spread-elements
- **object**: fast-properties, fast-for-in, fast-super, hash-code
- **async**: fast-async, jspi, jspi-newapi, jspi-ot
- **promise**: fast-async, jspi, jspi-newapi
- **regex**: non-backtracking-regexp, regexp-tier-up, regexp-lookbehind-assertions, speeding-up-regular-expressions
- **type**: bigint, dataview
- **class**: faster-class-features
- **modern-js**: modern-javascript, understanding-ecmascript-part-1~4

### 性能
- **optimization**: slack-tracking, fast-properties, fast-for-in, fast-super, wasm-speculative-optimizations
- **performance**: cost-of-javascript-2019, real-world-performance, speedometer-2, jank-busters
- **benchmark**: speedometer-2, retiring-octane
- **cache**: code-caching-for-devs, code-caching, wasm-code-caching

### 安全
- **security**: sandbox, spectre, control-flow-integrity
- **vulnerability**: spectre

### 其他
- **pointer-compression**: pointer-compression, oilpan-pointer-compression
- **startup**: custom-startup-snapshots
- **serialization**: json-stringify
- **testing**: javascript-code-coverage, test-the-future
- **intl**: intl
- **math**: math-random
- **coverage**: javascript-code-coverage
