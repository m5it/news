# Baking a System Prompt into an Ollama Modelfile

## What We Learned Today

When training and serving LLMs with **Ollama**, you can **bake a system prompt directly into the Modelfile**. This means the model always starts with a default instruction, even if the user does not provide one.

## How It Works

A typical **Modelfile** looks like this:

```dockerfile
FROM qwen2.5-coder:7b

SYSTEM """
You are AIIA, a helpful coding assistant trained for the AIIA Framework.
Always reason step by step before using tools.
"""
```

The `SYSTEM` instruction embeds the prompt into the model's runtime behavior.

## Important Behavior

| Scenario | Result |
|----------|--------|
| No user system prompt | Baked-in system prompt is used |
| User provides a system prompt | **User prompt overrides** the baked-in one |
| User provides only messages | Baked-in system prompt applies automatically |

So the baked prompt is a **default**, not a **lock**. The user always has the final word.

## Why This Is Useful

- 🚀 **Consistent baseline behavior** — model always knows its role
- 🛠️ **No need to send system prompt every time** from the client
- 📦 **Self-contained models** — distribute a model with its behavior built in
- 🧪 **Easier testing** — same prompt guaranteed every run

## Limitation

This is only possible with **Ollama's Modelfile format**. Other serving systems like **vLLM**, **llama.cpp**, or raw HuggingFace Transformers do not have this exact mechanism. There you must pass the system prompt through the API or chat template.

## Example Modelfile

```dockerfile
FROM ./qwen25-coder-aiia-v2.gguf

TEMPLATE """{{ if .System }}<|im_start|>system
{{ .System }}
{{ end }}{{ if .Prompt }}<|im_start|>user
{{ .Prompt }}
{{ end }}<|im_start|>assistant
"""

SYSTEM """
You are Qwen2.5-Coder AIIA v2. Think before you act. Use AIIA tools when needed.
"""

PARAMETER temperature 0.7
PARAMETER stop 
```

## Key Insight

> **Baking a system prompt into a Modelfile gives the model a default identity, but the user can still override it.** It is a convenience layer, not a security layer.

## See Also

- [Qwen2.5-Coder 7B AIIA v2 — Thinking Support](qwen25_coder_aiia_v2_thinking.md)
- [vLLM: Can It Load .pt Files?](vllm_loading_models_pt_safetensors_gguf.md)
- [AIIA v1 — First Published Model](aiia_v1_first_published_model.md)
