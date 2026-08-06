# LLM Training Progress: Gemma 12B & Qwen2.5 7B on v5 AIIA Datasets

## Today's Update

We learned some important things about LLM training today.

## What We Are Running

| Model | Dataset | Status |
|-------|---------|--------|
| **Gemma 12B** | v5 AIIA datasets | Created and running |
| **Qwen2.5 7B** | v5 AIIA datasets | Training in progress |

## Amazing Loss Improvement

The Qwen2.5 7B training shows excellent progress:

- 📉 **Loss dropped from 1.9 to 0.3**
- 🔄 **Still running the last round of steps**
- 🎯 **Expected final loss: around 0.3–0.2**

This is a huge improvement and shows the model is really learning the AIIA patterns.

## Why This Matters

- ✅ **v5 AIIA datasets are working well** — better than previous versions.
- 🧠 **Qwen2.5 7B is a strong base** — it can absorb the framework commands effectively.
- 🚀 **Gemma 12B is the next big target** — more parameters plus thinking support.

## Next Focus

After these runs finish, we will shift focus to:

> **Training 3B and 4B models** to see what they are capable of with specific training and our framework.

These smaller models should be able to handle much longer context on 16GB GPUs, which is perfect for AIIA sessions and complete workflows.

## Key Insight

**Big models show impressive loss curves, but smaller models may be the practical future for AIIA.** With the right training data, a 3B or 4B model could become a fast, long-context, local agent.

## Hear You Soon, People

The training continues. More results coming soon.

## See Also

- [Qwen2.5-Coder 7B AIIA v2 — Thinking Support](qwen25_coder_aiia_v2_thinking.md)
- [Smaller Models, Longer Context](smaller_models_longer_context_training.md)
- [Next Model: Gemma3 12B with Thinking Support](next_model_planned_gemma3_12b_thinking.md)
- [Fine-Tuning: Teaching a Model to Think](fine_tuning_teaching_models_to_think.md)
