# Next Model Planned: Gemma3 12B with Thinking Support

## The Plan

The next model we plan to train is **Gemma3 12B**.

## Why Gemma3 12B?

- 🧠 **It supports thinking** — unlike the last three models we trained.
- 🔄 **AIIA Framework needs to evolve** for reasoning-heavy workflows.
- 📈 **12B parameters** — a good balance between capability and hardware requirements.

## What "Thinking Support" Means

| Without Thinking | With Thinking |
|------------------|---------------|
| Model responds immediately | Model can reason step by step |
| Single-pass tool calls | Multi-step planning before acting |
| Reactive | Proactive |
| Good for simple tasks | Better for complex workflows |

## Why This Matters for AIIA

The last three models did not support thinking, so the AIIA Framework was not prepared much in this direction. With Gemma3 12B, we can start building:

- **Multi-step reasoning** before tool execution
- **Self-correction loops** — model checks its own plan
- **Better error recovery** — think, retry, adapt
- **Complex task decomposition** — break big goals into smaller steps

## The Roadmap

| Model | Size | Thinking | Status |
|-------|------|----------|--------|
| **AIIA v1** | Small | ❌ No | ✅ Published |
| **Kimi-K3** | 0.4B | ❌ No | 🧪 Experimental |
| **Qwen2.5-Coder-AIIA** | 7B | ❌ No | 🚀 Published |
| **Gemma3-AIIA** | 12B | ✅ Yes | 🎯 Planned |

## What to Prepare

Before training Gemma3 12B, we need:

1. **Thinking-style datasets** in AIIA_DATASETS
2. **Tool-call patterns** that include reasoning steps
3. **Session examples** showing plan-then-act behavior
4. **Evaluation metrics** for reasoning quality
5. **Hardware check** — 12B needs more VRAM and time

## Key Insight

**Thinking models change the game.** AIIA Framework was built for tool execution, but with reasoning support, it can become a true agent that plans, reflects, and adapts.

## See Also

- [Qwen2.5-Coder 7B AIIA](qwen25_coder_7b_aiia_new_stronger_model.md)
- [Training Llama 3.2 & Kimi K3](training_llama32_and_kimi_k3_with_aiia_datasets.md)
- [AIIA_DATASETS](https://github.com/m5it/AIIA_DATASETS)
