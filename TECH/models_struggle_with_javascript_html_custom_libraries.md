# Why LLMs Struggle with JavaScript, HTML, and Custom Libraries

## The Observation

Models have a lot of problems depending on which language you work with.

- **Python** → Usually fine
- **Rust** → Usually fine
- **JavaScript** → Problems start appearing
- **HTML** → More problems
- **User's own JavaScript libraries** → Super problems

Even the smartest models — including Claude-level AI — struggle with these.

## Why This Happens

| Factor | Impact |
|--------|--------|
| **Dynamic typing** | JavaScript's loose types confuse models |
| **DOM + runtime context** | HTML/JS live in browsers, not just files |
| **Implicit dependencies** | Models can't see what's loaded in the page |
| **Custom libraries** | No training data for your private API |
| **Callback/async patterns** | Promises, events, closures are hard to trace |
| **Mixed file types** | HTML, CSS, JS, JSON all interacting |

## The Real Pain

When a model works with Python or Rust, the boundaries are clean:

- File A defines function
- File B imports it
- Types tell the model what's happening

With JavaScript + custom libraries:

- Functions are attached to objects dynamically
- `window.myLib.doThing()` might exist only at runtime
- HTML structure affects JS behavior
- Event listeners hide logic
- Minified or bundled code is unreadable

Even Claude-level models hit walls here.

## What Helps

1. **Give context** — paste the relevant library code or API docs
2. **Show examples** — working snippets teach faster than descriptions
3. **Break tasks down** — one DOM change at a time
4. **Use explicit IDs/classes** — make HTML targets obvious
5. **Test incrementally** — run, check console, fix one error
6. **Document your own library** — models can't guess your custom API
7. **Be specific in plans and tasks** — vague instructions multiply confusion when working with models and frameworks

## Implications for AIIA

This is exactly why the AIIA Framework uses:

- Explicit tool calls
- File-based context
- Session history
- Browser automation with observable state

The more structure we give the model, the less it has to guess.

## See Also

- [AIIA v1 — First Published Model](aiia_v1_first_published_model.md)
- [AIIA Framework](https://github.com/m5it/AIIA)
- [Training Llama 3.2 & Kimi K3](training_llama32_and_kimi_k3_with_aiia_datasets.md)
