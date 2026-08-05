# Training Models to Think Conditionally Based on System Prompt

## The Training Setup

Today we experimented with a mixed training dataset:

| Dataset Type | Percentage |
|--------------|------------|
| **Without thinking tag** | 70% |
| **With thinking tag** | 30% |

## What We Expected

We wanted to see if the model could learn **when to think** and **when to respond directly**, depending on the instruction it received.

## What Happened

The model learned exactly that:

- 🧠 **If the system prompt asks the model to think**, it will reason step by step.
- ⚡ **If the system prompt does not ask for thinking**, it will answer directly.

> The model's thinking behavior became **conditional on the system prompt**.

## Why This Works

By mixing both styles during training:

- The model sees examples of direct responses (70%)
- The model sees examples of structured reasoning (30%)
- It learns to recognize the trigger in the system prompt
- It adapts its output format accordingly

This is more flexible than training a model that always thinks or never thinks.

## The Pattern

| System Prompt | Model Behavior |
|---------------|----------------|
| "Think step by step" or "Use reasoning" | Produces thinking blocks |
| "Answer directly" or no thinking instruction | Produces concise response |

## Why This Matters for AIIA

Not every task needs deep reasoning. Sometimes a quick answer is better. Sometimes a plan is necessary. With this conditional training:

- 🚀 **Fast tasks stay fast**
- 🧠 **Hard tasks get reasoning**
- 🎯 **One model can serve both modes**

## Key Insight

> **You can train a model to be a switchable thinker.** The system prompt becomes the switch. 70% direct data teaches normal behavior. 30% thinking data teaches reasoning when requested.

## See Also

- [Fine-Tuning: Teaching a Model to Think](fine_tuning_teaching_models_to_think.md)
- [Qwen2.5-Coder 7B AIIA v2 — Thinking Support](qwen25_coder_aiia_v2_thinking.md)
- [Baking System Prompt into Ollama Modelfile](baking_system_prompt_into_ollama_modelfile.md)
