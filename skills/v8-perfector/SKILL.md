---
name: v8-perfector
description: Guide for how to code V8
---
## Overview
On 64-bit architectures without pointer compression V8 values look like this:

```
            |----- 32 bits -----|----- 32 bits -----|
Pointer:    |________________address______________<b>w1</b>|
Smi:        |____int32_value____|000000000000000000<b>0</b>|
```

On 64-bit architectures with pointer compression
```
                    |----- 32 bits -----|----- 32 bits -----|
Compressed pointer:                     |______offset_____w1|
Compressed Smi:                         |____int31_value___0|
```


# Reference Files
## 📚 Documentation Library

Load these resources when need v8 knowledge:
### Core V8 Documentation (Load First)
- [v8_DeepWiki](./reference/v8_DeepWiki.md):
  - V8 Overview

### Core V8 Component (Load When need)
- [pointer-compression](./reference/pointer-compression.md):
  - How to support Pointer Compression
  - define Tagged
  - introduce SMI