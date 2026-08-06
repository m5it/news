# AIIA Framework: New `!REHEAT` User Command

## What's New

We added a new user command to the **AIIA Framework**:

```text
!REHEAT
```

## What It Does

Running `!REHEAT` in the middle of a session makes the model **re-collect everything** just like the startup warm-up, but **without restarting** the session.

Specifically, it re-runs:

- `<listTools>` — refresh the available tool list
- `<GetTip>` / `<ReinsertTip>` — reload relevant tips into context

## Why This Is Useful

During a long session, the model can lose track of tools, tips, or context. Instead of starting over, the user can simply type:

```text
!REHEAT
```

This restores the model's awareness of the AIIA environment without losing the conversation history.

## How It Works

| Phase | Normal Startup | `!REHEAT` |
|-------|--------------|-----------|
| Tool list loaded | ✅ Yes | ✅ Yes |
| Tips reloaded | ✅ Yes | ✅ Yes |
| Session restarted | ✅ Yes | ❌ No |
| Conversation history preserved | ❌ No | ✅ Yes |

## Use Cases

- 🔄 **Long sessions** — model starts forgetting tool availability
- 🧠 **After context drift** — bring the model back on track
- 🛠️ **Tool awareness** — remind the model what it can do
- ⚡ **Faster recovery** — no need to restart and re-explain the task

## Key Insight

> **A warm restart without losing context.** `!REHEAT` gives the model a fresh view of its own capabilities while keeping the conversation intact.

## See Also

- [AIIA v1 — First Published Model](aiia_v1_first_published_model.md)
- [Qwen2.5-Coder 7B AIIA v2 — Thinking Support](qwen25_coder_aiia_v2_thinking.md)
- [AI_INSTRUCT_OPTION: 1 vs 2](ai_instruct_option_1_vs_2_training_insight.md)
