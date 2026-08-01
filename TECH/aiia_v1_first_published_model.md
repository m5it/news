# AIIA v1: Our First Published Model

## 🚀 The Milestone

We just published our **first own trained model**: **AIIA v1**.

- **Model URL:** [ollama.com/w4d4f4k/aiia_v1](https://ollama.com/w4d4f4k/aiia_v1)
- **Purpose:** Learned to use **AIIA Framework** tool commands
- **Training Data:** Custom **AIIA_DATASETS**

## What It Can Do

AIIA v1 was trained to understand and invoke AIIA Framework tools, including:

- **File operations:** ReplaceLine, ReadFile, WriteFile
- **Workflow patterns:** modify-verify-revert, regex boundaries, ReplaceLine workflows
- **Browser automation:** JavaFX WebView-based interactions
- **Site-specific scripts:** GitHub profile extraction, custom site automation
- **Specialized agents:** booksmith, developer, generalist, media analyst, researcher
- **Session handling:** multi-turn task execution with tool calls
- **Edge cases:** multiline content, special characters, image generation workflows

## Training Data Overview

The model was trained on curated datasets from real AIIA sessions:

| Category | Examples |
|----------|----------|
| **Workflow patterns** | modify_verify_revert, regex_boundary, replaceline_workflow |
| **Instructor datasets** | booksmith, developer, generalist, mediaanalyst, researcher |
| **Browser automation** | javafx_browser_automation |
| **Site scripts** | github.com profile extractor, custom site scripts |
| **Session data** | Multiple cleared sessions (302, 314-324, 327, 329, 340, 342, etc.) |
| **Test cases** | multiline, special characters, task demos |

## Why This Matters

- 🧠 **First model we trained ourselves** for our own framework
- 🔧 **Understands our tools** — not generic chat, but AIIA-specific function calling
- 📊 **Built on real data** — from actual AIIA sessions and use cases
- 🌐 **Publicly available** — anyone can pull and test it via Ollama
- 🚀 **Foundation for v2, v3...** — this is just the beginning

## How to Try It

```bash
ollama run w4d4f4k/aiia_v1
```

Then give it AIIA-style tasks and watch it invoke tools.

## What's Next

- Continue training larger versions (Kimi-K3 from 0.4B is in progress)
- Improve tool-call accuracy
- Add more specialized agent datasets
- Convert to GGUF for broader deployment

## See Also

- [AIIA Framework](https://github.com/m5it/AIIA)
- [AIIA_DATASETS](https://github.com/m5it/AIIA_DATASETS)
- [Training Llama 3.2 & Kimi K3](training_llama32_and_kimi_k3_with_aiia_datasets.md)
