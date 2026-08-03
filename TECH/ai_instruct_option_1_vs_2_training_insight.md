# AI_INSTRUCT_OPTION: 1 vs 2 for Trained Models

## The Observation

When using models trained by us with the **AIIA Framework**, it is more useful to set **AI_INSTRUCT_OPTION=1** instead of **2**.

## What Each Option Does

| Option | How It Works | Best For |
|--------|--------------|----------|
| **AI_INSTRUCT_OPTION=1** | Uses a **system prompt** with a lot of information included directly | Less-trained models |
| **AI_INSTRUCT_OPTION=2** | Uses **tips functionality** — context is injected as separate tips | Cloud / general models |

## Why Option 1 Works Better for Less-Trained Models

- 📝 **System prompt carries everything** — the model gets all instructions, examples, and context in one place.
- 🧠 **Easier to follow** — less-trained models don't need to figure out how to retrieve or combine scattered tips.
- 🎯 **More deterministic** — the model sees the full picture before responding.
- 🚀 **Better tool-call accuracy** — fewer mistakes when invoking AIIA tools.

## Why Option 2 Exists

- ☁️ **Cloud models are generalists** — they already know how to work with structured tips and context.
- 🧩 **Tips are modular** — easier to update, swap, or extend without rewriting the whole system prompt.
- 🌐 **Useful for quick prototyping** with powerful cloud models.

## Why Less-Trained Models Struggle with Option 2

- ❓ **Not all models understand the tips mechanism** — they don't know how to read, prioritize, or combine separate tip entries.
- 🔀 **Context gets fragmented** — instructions are scattered instead of centralized.
- 📉 **Requires more training** — the model needs to learn both the framework AND how to use the tips system.

## The Future

> *"I think it is possible to train our models to become good programmers as well — just need more training."*

With enough training, our own models could:
- Handle Option 2's tips functionality correctly
- Match or exceed cloud models on programming tasks
- Run locally with full AIIA capability

## Recommendation

| Model Type | Recommended Option | Why |
|------------|-------------------|-----|
| AIIA-trained local models (less trained) | `AI_INSTRUCT_OPTION=1` | System prompt is easier to follow |
| Cloud / general models | `AI_INSTRUCT_OPTION=2` | They understand modular tips |
| Heavily trained local models (future) | `AI_INSTRUCT_OPTION=2` | After training them on tips usage |

## Key Insight

**Less-trained models need everything in one system prompt.** Tips are powerful, but only for models that already understand how to use them. Train more, then switch to Option 2.

## See Also

- [Qwen2.5-Coder 7B AIIA](qwen25_coder_7b_aiia_new_stronger_model.md)
- [AIIA v1 — First Published Model](aiia_v1_first_published_model.md)
- [Training Llama 3.2 & Kimi K3](training_llama32_and_kimi_k3_with_aiia_datasets.md)
