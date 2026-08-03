# AI_INSTRUCT_OPTION: 1 vs 2 for Trained Models

## The Observation

When using models trained by us with the **AIIA Framework**, it is more useful to set **AI_INSTRUCT_OPTION=1** instead of **2**.

## What Each Option Does

| Option | Best For | Why |
|--------|----------|-----|
| **AI_INSTRUCT_OPTION=1** | Our trained models | Models trained on AIIA datasets respond better with this instruction format |
| **AI_INSTRUCT_OPTION=2** | Cloud models | Models like Claude, GPT-4, etc. understand better without extensive training |

## Why Option 1 Works Better for Our Models

- 🎯 **Trained specifically on AIIA patterns** — the model learned the Option 1 style
- 🔧 **Better tool-call accuracy** — fewer mistakes when invoking AIIA tools
- 🧠 **Cleaner reasoning** — follows the framework's expected structure
- 🚀 **More reliable output** — less drift, more consistent behavior

## Why Option 2 Exists

- ☁️ **Cloud models are generalists** — they don't need framework-specific training
- 📝 **They understand broader instructions** with less context
- 🌐 **Useful for quick prototyping** without preparing datasets

## The Future

> *"I think it is possible to train our models to become good programmers as well — just need more training."*

With enough training data, our own models could match or exceed cloud models on programming tasks while running locally.

## Recommendation

| Model Type | Recommended Option |
|------------|-------------------|
| AIIA-trained local models | `AI_INSTRUCT_OPTION=1` |
| Cloud / general models | `AI_INSTRUCT_OPTION=2` |

## See Also

- [Qwen2.5-Coder 7B AIIA](qwen25_coder_7b_aiia_new_stronger_model.md)
- [AIIA v1 — First Published Model](aiia_v1_first_published_model.md)
- [Training Llama 3.2 & Kimi K3](training_llama32_and_kimi_k3_with_aiia_datasets.md)
