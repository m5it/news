# Qwen2.5-Coder 7B AIIA v2: Now With Thinking Support

## 🎉 The Milestone

Today we successfully trained the **second version** of our model:

**[Qwen2.5-Coder 7B AIIA v2](https://ollama.com/w4d4f4k/qwen25-coder-aiia-v2)**

## What's New in v2

| Feature | v1 | v2 |
|---------|----|----|
| AIIA Framework tool calls | ✅ | ✅ |
| Coding tasks | ✅ | ✅ |
| **Thinking / reasoning support** | ❌ | ✅ |
| Multi-step planning | ❌ | ✅ |
| Self-reflection before acting | ❌ | ✅ |

## Why This Is a Big Deal

- 🧠 **Thinking support means the model can reason step by step** before producing an answer or using a tool.
- 🔄 **This proves that fine-tuning can teach behavior**, not just add knowledge.
- 🚀 **We took a base model that did not think in this way** and trained it to plan, reflect, and reason.
- 🎯 **AIIA Framework can now evolve** toward true agent behavior instead of simple command execution.

## How Fine-Tuning Made This Possible

The previous version worked well for coding and tool calls, but it did not reason deeply. With v2, we trained on reasoning-style data that showed the model:

1. **Read the task carefully**
2. **Break it into steps**
3. **Think through each step**
4. **Decide which tool to use**
5. **Reflect on the result**
6. **Continue or finish**

This is exactly what "thinking" means in practice.

## What This Proves

> **Fine-tuning is not just about making a model know more. It is about teaching the model how to think.**

A model that has never seen structured reasoning will not produce it. But with the right training data, even a 7B model can learn to plan and reflect.

## Try It

```bash
ollama run w4d4f4k/qwen25-coder-aiia-v2
```

## What's Next

- 📈 Continue improving thinking quality with more synthetic reasoning data
- 🔧 Integrate thinking mode deeper into AIIA Framework
- 🧠 Prepare Gemma3 12B with thinking support as the next major target

## See Also

- [Qwen2.5-Coder 7B AIIA v1](qwen25_coder_7b_aiia_new_stronger_model.md)
- [Fine-Tuning: Teaching a Model to Think](fine_tuning_teaching_models_to_think.md)
- [Next Model: Gemma3 12B with Thinking Support](next_model_planned_gemma3_12b_thinking.md)
- [AIIA v1 — First Published Model](aiia_v1_first_published_model.md)
