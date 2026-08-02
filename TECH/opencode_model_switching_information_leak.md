# OpenCode Model Switching Can Leak Information

## The Observation

When using **OpenCode**, switching between models can lead to an **information leak** in the workflow.

## What Happens

1. You start working with **Big Pickle** (or another model)
2. The model understands the plan it is preparing
3. You switch to a different model, like **Kimi-K3**
4. The new model **does not know what the previous model was working on**
5. Even though the **same chat history is visible**

## Why This Is a Problem

- 📉 **Context loss:** The second model sees the messages but misses the implicit plan/intent
- 🔁 **Broken workflow:** Tasks that were mid-progress get reinterpreted from scratch
- 💥 **Potential errors:** The new model may undo, misinterpret, or duplicate work
- 🔓 **Information leak risk:** If the first model had established a specific structure or plan, that "understanding" is not transferred

## When It Happens

- Switching from **Big Pickle** to **Kimi-K3**
- Likely affects other model pairs on OpenCode too
- Especially problematic in long, multi-step coding or planning sessions

## What Helps

1. **Re-state the plan explicitly** after switching models
2. **Summarize current state** before switching
3. **Pin the goal** in the first message to the new model
4. **Avoid switching mid-task** unless necessary
5. **Use one model per complete task** when possible

## Implications for AIIA

This is why AIIA Framework emphasizes:

- Explicit session state
- Tool-call history
- Clear, structured plans
- File-based context that survives model changes

The tool history tells the next model what actually happened, even if the "understanding" is lost.

## See Also

- [AIIA v1 — First Published Model](aiia_v1_first_published_model.md)
- [Training Llama 3.2 & Kimi K3](training_llama32_and_kimi_k3_with_aiia_datasets.md)
