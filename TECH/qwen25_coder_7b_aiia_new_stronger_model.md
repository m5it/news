# Qwen2.5-Coder 7B AIIA: New Stronger Model

## 🚀 The Milestone

Today we created a **new, stronger model** based on **Qwen2.5-Coder 7B**, fine-tuned for the **AIIA Framework**.

- **Model URL:** [ollama.com/w4d4f4k/qwen25-coder-aiia](https://ollama.com/w4d4f4k/qwen25-coder-aiia)
- **Base Model:** Qwen2.5-Coder 7B
- **Purpose:** AIIA Framework tool commands and workflows
- **Training Data:** AIIA_DATASETS

## Why Qwen2.5-Coder 7B?

| Advantage | Why It Matters |
|-----------|----------------|
| **Larger than AIIA v1** | More capacity to learn complex tool patterns |
| **Code-focused base** | Already strong at structured reasoning and code generation |
| **Practical size** | 7B fits well on consumer hardware with 16GB VRAM |
| **Better than Kimi-K3 experiment** | More stable and practical for real use |

## What It Can Do

Trained on the same AIIA_DATASETS as AIIA v1, including:

- **File operations:** ReplaceLine, ReadFile, WriteFile
- **Workflow patterns:** modify-verify-revert, regex boundaries, ReplaceLine workflows
- **Browser automation:** JavaFX WebView-based interactions
- **Site-specific scripts:** GitHub profile extraction, custom site automation
- **Specialized agents:** booksmith, developer, generalist, media analyst, researcher
- **Session handling:** multi-turn task execution with tool calls
- **Edge cases:** multiline content, special characters, image generation workflows

## How to Try It

```bash
ollama run w4d4f4k/qwen25-coder-aiia
```

## Model Evolution

| Model | Base | Size | Status |
|-------|------|------|--------|
| **AIIA v1** | Llama 3.2 | Small | ✅ Published, first model |
| **Kimi-K3** | Kimi K3 0.4B | Tiny | 🧪 Experimental |
| **Qwen2.5-Coder-AIIA** | Qwen2.5-Coder 7B | 7B | 🚀 **New, stronger** |

## Key Insight

**Bigger practical models win.** The jump to 7B parameters with a code-specialized base model gives much better tool-calling reliability than smaller experiments, while still running on accessible hardware.

## What's Next

- Continue training on more AIIA sessions
- Improve tool-call accuracy
- Test on real-world tasks
- Possibly train larger versions if hardware allows

## See Also

- [AIIA v1 — First Published Model](aiia_v1_first_published_model.md)
- [Training Llama 3.2 & Kimi K3](training_llama32_and_kimi_k3_with_aiia_datasets.md)
- [AIIA_DATASETS](https://github.com/m5it/AIIA_DATASETS)
- [AIIA Framework](https://github.com/m5it/AIIA)
