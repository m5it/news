# Why LLM Training Infrastructure Is Written in C++ (Not Rust)

## The Question

With all the modern hype around Rust, why is most large language model (LLM) training infrastructure still written in **C++**?

## Short Answer

Because the AI stack was built on C++ long before Rust was ready, and the cost of rewriting it now outweighs the benefits for most players.

## 1. Ecosystem Maturity and Historical Dominance

### Decades of Code

Frameworks like **PyTorch** and **TensorFlow** were started years before Rust became mainstream. They have accumulated:

- Millions of lines of optimized C++
- Deeply tuned CUDA kernels
- Battle-tested distributed training logic
- A huge community of contributors and plugins

Rewriting all of that in Rust would take enormous engineering effort with little immediate functional reward.

### The "Glue" Advantage

| Layer | Language | Role |
|-------|----------|------|
| Research & scripting | Python | Fast experimentation, readable code |
| Backend & kernels | C++ | Raw performance, hardware control |
| GPU kernels | CUDA (C/C++) | Parallel matrix math |

Python acts as the **glue** for AI researchers. C++ provides the **performance backend**. Rust would mostly replace the C++ layer, but that layer is the hardest and most entrenched part to move.

## 2. Hardware and Vendor Lock-In

### NVIDIA CUDA Ecosystem

GPU acceleration for deep learning is dominated by **NVIDIA CUDA**, which is built around:

- C and C++ toolchains
- NVIDIA drivers
- cuBLAS, cuDNN, NCCL, and other native C++ libraries

### Frictionless Interoperability

C++ interfaces directly with these low-level NVIDIA APIs. Rust would need extensive **FFI (Foreign Function Interface)** wrappers to talk to the same hardware, adding:

- Maintenance burden
- Performance overhead at boundaries
- More complex build pipelines

Until NVIDIA ships first-class Rust toolchains, C++ remains the path of least resistance.

## 3. Safety vs. Performance Trade-Offs

### Undefined Behavior for Speed

C++ compilers aggressively optimize code by leveraging **undefined behavior**. In tightly controlled high-performance code, engineers can use this to:

- Skip unnecessary bounds checks
- Reinterpret memory layouts
- Squeeze microseconds out of massive matrix operations

### Rust's Strict Safety

Rust enforces:

- Memory safety at compile time
- Ownership and borrowing rules
- Bounds checking by default

These are excellent for preventing bugs, but they can complicate **highly unstructured, fluid, hardware-close tensor manipulation** where every nanosecond matters. Writing the same low-level kernels in Rust often requires fighting the borrow checker or adding `unsafe` blocks — which partly defeats the purpose.

## What Rust Brings to the Table

Despite all this, Rust has real advantages for AI tooling:

- 🦀 **Memory safety without GC** — good for inference servers and deployment tools
- 🦀 **Fearless concurrency** — useful for data pipelines and distributed orchestration
- 🦀 **Reliable systems code** — great for model serving infrastructure, not necessarily training kernels

## Newer Rust Projects in ML

Rust is slowly entering the machine learning space through projects like:

| Project | What It Does |
|---------|--------------|
| **Burn** | Deep learning framework written in Rust |
| **candle** | Minimalist ML framework by Hugging Face |
| **dfdx** | Type-safe deep learning in Rust |
| **tch-rs** | Rust bindings for PyTorch's C++ backend |

These are promising, but they are still small compared to PyTorch/TensorFlow.

## The Real Bottlenecks of Migrating

If someone wanted to move deep learning runtimes from C++ to Rust, they would face:

1. **CUDA integration** — no native Rust equivalent
2. **Massive existing codebases** — rewriting PyTorch would take years
3. **Community momentum** — researchers and libraries are already invested in Python/C++
4. **Performance-critical kernels** — Rust safety can get in the way of micro-optimizations
5. **Vendor support** — NVIDIA optimizes for C++, not Rust

## Key Insight

> **C++ won by being there first and staying fast.** Rust may slowly take over surrounding infrastructure — serving, orchestration, data pipelines — but the core training kernels will remain C++/CUDA for the foreseeable future.

## If You're Interested

We can explore:

- How **Burn** is attempting to bring Rust into machine learning
- The specific performance bottlenecks of migrating deep learning runtimes away from C++
- Where Rust actually makes sense in the modern AI stack

## See Also

- [Fine-Tuning: Teaching a Model to Think](fine_tuning_teaching_models_to_think.md)
- [vLLM: Can It Load .pt Files?](vllm_loading_models_pt_safetensors_gguf.md)
- [Next Model: Gemma3 12B with Thinking Support](next_model_planned_gemma3_12b_thinking.md)
