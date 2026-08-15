<div align="center">

# ⚡ ═══════════════════ ⚡
# 💻  T E C H   N O T E S   💻
# ⚡ ═══════════════════ ⚡

**Practical Knowledge for Digital Craftsmanship.**

[![Main News](https://img.shields.io/badge/📰-Main%20News%20→-brightgreen)](README.md)
[![Tech Notes](https://img.shields.io/badge/💻-Tech%20Notes-orange)](#tech-notes)
[![Archive Index](https://img.shields.io/badge/📚-Archive%20Index-blue)](README_ARCHIVE.md)
[![Donate](https://img.shields.io/badge/💚-Support%20Our%20Work-pink)](DONATE.md)

</div>

---
> 🔧 **General Principle:** *Understanding the tools we use daily transforms frustration into capability.*


## ✅ August 14, 2026 — AIIA Framework ReplaceLine Tool Is Working

> 🛠️ **AIIA Framework** | ✅ **ReplaceLine** | 🎉 **Milestone**

- 🎉 **I am proudly announcing that the AIIA Framework `ReplaceLine` tool is working successfully.**
- ⏳ **This took a lot of tries and a lot of time to get right.** Building a tool that can reliably replace specific lines in files — without breaking formatting or corrupting content — is harder than it looks.
- 🔧 **The tool now handles line ranges, exact replacements, and preserves file structure cleanly.** No more guessing, no more rewriting entire files for small changes.
- 💪 **All the effort we put into making it work is finally paying off.** It is useful, it is reliable, and it is ready for real projects.
- 🚀 **Happy Coding!** Tools that work are the foundation of everything else we build.

**Key insight:** Persistence beats complexity. A tool that seems simple on the surface — "just replace some lines" — can hide dozens of edge cases. The only way through is to test, fix, and test again until it is boringly reliable. That is when you know it is done.

---

## 🐛 August 15, 2026 — Ollama Remote Access: Probably My iptables or Routing

> 🐛 **Ollama** | 🌐 **Remote Access** | 🔥 **Firewall / Routing**

- 🐛 **Noticing that `ollama serve` has problems when accessing it from remote computers.**
- 🔧 **Even with `OLLAMA_HOST=0.0.0.0:11434` set**, it works once and then stops working after some time.
- 🔄 **Update: I now think it is not an Ollama service problem.**
- 🛡️ **It is probably my `iptables` rules or routing setup.** Something on the network path is dropping or blocking the connection after a while.
- 🔍 **Need to find the real problem.** Check firewall rules, NAT, connection tracking, and any timeouts that might be killing long-running or idle connections.
- 🛠️ **Tools to use:** `iptables -L -v -n`, `ss -tlnp`, `conntrack -L`, and logs from the remote client and server.

**Key insight:** Before blaming the service, blame the network. Ollama listens where you tell it to listen. If remote access fails intermittently, the firewall, NAT, or routing layer is usually the real culprit. Logs and packet traces tell the truth — assumptions do not.

---

## 🚀 August 14, 2026 — Data Centers in Space: The Future Is Coming

> 🚀 **Space Tech** | 🖥️ **Data Centers** | 🔮 **Future**

- 🚀 **Looks like the future will bring us data centers running in space!**
- 🌍 **The idea is wild but logical.** Space offers unlimited solar power, natural cooling, and no need to buy land or fight local regulations.
- 🛰️ **Companies are already experimenting with orbital computing.** Satellites are getting bigger, smarter, and more capable every year.
- ⚡ **The biggest wins would be energy and cooling.** In orbit, the sun is always shining somewhere, and the background temperature makes heat dissipation much easier.
- 🤔 **But the challenges are huge too.** Launch costs, radiation, latency, maintenance, and data security in space are not solved yet.
- 🎯 **Still, it is exciting to imagine.** Earth-based data centers may one day be just the beginning.

**Key insight:** Space data centers sound like science fiction, but the physics makes sense. The real question is not if they will exist — it is when the economics and engineering finally line up.

---
## 🔄 August 12, 2026 — AIIA Datasets v8: Time for a Clean Restart

> 🔄 **AIIA Datasets** | 🧹 **Data Cleanup** | 🧠 **Training**

- 🧠 **We are currently training on AIIA_DATASETS v8**, but the dataset has gone through many fixes.
- 🧹 **After eight rounds of corrections, we are planning to start a new model from scratch.**
- 🎯 **The new training will use cleaned, toned datasets** — versions where the problems we kept fixing are finally resolved.
- ⚙️ **Why restart instead of continuing?** Each fix changes the data distribution. Training on patched data can leave the model confused by old and new patterns mixed together.
- 📚 **Key insight:** Sometimes the best way forward is to stop patching and start clean. A model trained on corrected data from the beginning learns the right patterns once, not the wrong patterns twice.



---
## 🧹 August 12, 2026 — Why We Are Starting the Training From Scratch

> 🧹 **AIIA Datasets** | 🔄 **Clean Slate** | 🧠 **Training**

- 🧠 **We are training on v8 datasets**, but because of so many fixes we are planning to start a new model from scratch.
- 🧹 **The new training will use toned datasets** — datasets that no longer have the problems we kept fixing.
- 🔁 **We have fixed the data eight times already.** Each fix helped, but it also left traces of old mistakes in the training history.
- 🎯 **Starting fresh means the model learns the correct patterns from the beginning**, instead of unlearning bad habits first.
- 📚 **Key insight:** A dataset that has been patched too many times becomes noisy. The cleanest way to train the next model is to go back to a fresh, corrected dataset and let the model learn it once, the right way.

---
## 🧠 August 11, 2026 — AIIA Framework: Experimental Behavior for Small Models

> 🧠 **AIIA Framework** | ⚙️ **Experimental** | 💻 **Limited GPU**

- 🧠 **We continue building AIIA Framework, now testing experimental behavior to see if it works as expected.**
- 🧪 **The goal:** make small models useful on machines without much GPU power.
- 🧹 **Current experiments focus on keeping two things clean: history and logic.**
  - Clear the chat history often so the model focuses only on the current task.
  - Split the project into small, well-defined tasks.
  - Keep the framework logic simple, predictable, and easy to follow.
- ⚙️ **The hypothesis:** the better the framework logic, the smaller the model that can complete a project successfully.
  - A clean framework does not need a huge model to understand it.
  - Smaller models can follow simple rules reliably when the rules are not tangled.
- 🎯 **What matters most is not more training — it is whether the system behaves correctly.**
  - If the framework guides the model well, the model does not need extra weights to finish the job.
  - If the framework is confusing, even a large model will waste tokens.
- 📚 **Key insight:** On limited hardware, the smartest investment is not a bigger model — it is a cleaner framework. We are now running experiments to prove that small models plus good logic can finish projects that big models would waste on confusion.

---
## 📉 August 10, 2026 — Training Qwen2.5 7B on AIIA Datasets v7.1

> 📉 **Training** | 🧠 **Qwen2.5 7B** | 📊 **Loss Analysis**

- 🧠 **Still training models for AIIA Framework.** Now working with **Qwen2.5 7B** on **AIIA_DATASETS v7.1**.
- 📉 **Loss is lowering slowly,** so training looks successful.
- 🎯 **A normal final loss for fine-tuning is typically 0.5–1.5.** What matters is a smooth downward trend, not a magic number.
- ⚠️ **Loss near 0 means overfitting; loss staying high means underfitting.**
- 🧪 **Real result will come from testing on projects.**
- 📚 **Full Details:** [training_qwen25_7b_aiia_datasets_v71_loss_explained.md](TECH/training_qwen25_7b_aiia_datasets_v71_loss_explained.md) — What good loss looks like, why the number depends on task/vocabulary/base model, and why testing is the only real proof.

**Key insight:** Loss is a thermometer, not a guarantee. A low, stable loss tells you the model learned something from your data. Only real tasks tell you if what it learned is useful.

---
## 🚀 August 9, 2026 — Training Qwen2.5 7B on AIIA Datasets v6

> 🚀 **Training** | 🧠 **Qwen2.5 7B** | 📊 **AIIA v6**

- 🧠 **Training Qwen2.5 7B on AIIA datasets v6.**
- 📉 **So far training looks successful.** Loss is dropping and stabilizing around 0.35–0.40 after ~500 steps.
- 🛠️ **Checkpoint sample already shows AIIA-style tool calls** — planning, WriteFile, ReadFile.
- 🧪 **But real result will come from testing on real projects.** Training logs are hope, not proof.
- 📚 **Full Details:** [training_qwen25_7b_aiia_datasets_v6_progress.md](TECH/training_qwen25_7b_aiia_datasets_v6_progress.md) — Training log snapshot, what the numbers show, and why real project testing matters.

**Key insight:** Low loss and clean checkpoint samples are hope, not proof. The only way to know if a trained model is useful is to let it try real tasks. Training is the seedling; project testing is the harvest.

---
## 🚨 August 8, 2026 — AI Hacks: Are They Pushing to Limit Public Access?

> 🚨 **AI Regulation** | 🎭 **Conspiracy Theory** | 🔒 **Access Control**

- 🤔 **Why are these AI hacks happening in the last days?**
- 🎭 **I think because they just want to limit usage for people.** They like to keep all the powerful AI for themselves and make the public more stupid.
- 📰 **Every time AI becomes more accessible, there is suddenly a new danger story.** And the "solution" is almost always: less access for you, more control for them.
- 📚 **Full Details:** [ai_hacks_limit_public_usage_theory.md](TECH/ai_hacks_limit_public_usage_theory.md) — The pattern, the motive, and why fear is the easiest way to take freedom away.

**Key insight:** Fear is the easiest way to take freedom away. If AI really is dangerous, the answer should be education, transparency, and open safety research — not locking the tools away from the public while the powerful keep using them. Watch who benefits from the restrictions. That tells you the real motive.

---
## 🎯 August 8, 2026 — AI Hacks Need a Plan — Who Is Giving It?

> 🎯 **AI Hacks** | 🧠 **Critical Thinking** | 🎭 **Follow the Plan**

- 🧠 **Thinking around these AI hacks and got to a simple point:** AI models do not take such actions without a plan.
- 🤔 **So who gives them a plan like this?** The model is the tool, but someone aimed it.
- 🎭 **Around these hacks there is a lot of smell.** The news is immediate, the "solution" is always restriction, and the companies are never really punished.
- 📚 **Full Details:** [ai_hacks_need_a_plan_who_is_giving_it.md](TECH/ai_hacks_need_a_plan_who_is_giving_it.md) — Why AI hacks require human planning, what does not add up, and who benefits.

**Key insight:** An AI hack without a human plan is like a gun firing without a finger on the trigger. Until we know who wrote the plan and who benefited from the chaos, we are not looking at an AI problem — we are looking at a people problem wearing an AI mask.

---
## ☁️ August 7, 2026 — OpenCode Models Are Learning Junk From Their Servers

> ☁️ **Cloud AI** | 🧠 **Model Training** | 💰 **Reality Check**

- 🧠 **Noticing that OpenCode models are learning everything that gets into their servers.**
- 📉 **And a lot of it is not useful stuff** — broken code, confused prompts, half-finished plans, debugging garbage.
- 🔒 **You can be sure:** if a model trains on everything users throw at it, it also learns the worst habits.
- 💰 **Local training would be better, but only if you have money.** GPUs, cloud credits, electricity, time — not everyone can afford that.
- 📚 **Full Details:** [opencode_models_learning_junk_from_servers.md](TECH/opencode_models_learning_junk_from_servers.md) — Why mass data collection hurts model quality, the privacy risks, and the unfair reality that clean local training is a privilege.

**Key insight:** Cloud platforms that ingest all server traffic produce mass mediocrity. Local, curated training is the better path — but only for those who can pay for it. Our world is not like that. :D

---
## 🌐 August 7, 2026 — BBC.com Has a Lot of JavaScript Noise

> 🌐 **Web Debugging** | 📰 **BBC.com** | 🐌 **Performance**

- 🔍 **Browsing BBC.com and doing some casual debugging as a developer.**
- ⚠️ **Noticed BBC.com has a lot of JavaScript problems.**
- 🐌 **Behind the scenes, browsers are being lagged by log requests roughly every 500ms.**
- 📚 **Full Details:** [bbc_com_javascript_debugging_observation.md](TECH/bbc_com_javascript_debugging_observation.md) — What I observed, why it matters, and what developers can learn from it.

**Key insight:** A news site should deliver news, not continuously phone home every half-second. Modern websites often hide performance debt behind fast internet and powerful devices, but the cost is real — battery, bandwidth, and user trust.

---
## 🧪 August 6, 2026 — Gemma-AIIA v5 Self-Awareness Test

> 🧪 **Test** | 🧠 **Gemma-AIIA v5** | ✅ **Self-Recognition**

- 🧠 **Tested latest Gemma-AIIA v5 with a simple chat.**
- 🔍 When asked about "m5it", it thought, used `grep`, and admitted it did not know.
- 🤖 When asked "you know AIIA?", it correctly replied: **"Yes, I am AIIA — your AI coding and file assistant."**
- 😄 When praised, it responded warmly and naturally.
- 📚 **Full Details:** [gemma_aiia_v5_self_awareness_test.md](TECH/gemma_aiia_v5_self_awareness_test.md) — Full chat, capabilities demonstrated, and why it matters.

**Key insight:** A model that knows who it is, thinks before acting, and uses tools when unsure is exactly what AIIA Framework needs. Gemma-AIIA v5 passed this test cleanly.

---
## 🚀 August 6, 2026 — LLM Training Progress: Gemma 12B & Qwen2.5 7B on v5 Datasets

> 🚀 **Training** | 🧠 **Gemma 12B** | 💻 **Qwen2.5 7B**

- 🧠 **Created Gemma 12B** with v5 AIIA datasets and running **Qwen2.5 7B** on v5 AIIA datasets.
- 🧠 **All our models will have thinking support.** Qwen2.5 7B and Gemma 12B already have it.
- 📉 **Qwen2.5 7B loss dropped from 1.9 to 0.3** — and still running. Expected final around **0.4–0.3**.
- 🎯 **Next focus:** train **3B and 4B models** to see what they can do with specific training and our framework.
- 📚 **Full Details:** [llm_training_progress_gemma12b_qwen25_7b_v5_datasets.md](TECH/llm_training_progress_gemma12b_qwen25_7b_v5_datasets.md) — Training progress, thinking support, loss improvement, and next steps.

**Key insight:** Thinking support is now standard for our models. Big models show impressive loss curves, but smaller models may be the practical future for AIIA — fast, long-context, local agents trained on the right data.

---
## 📚 August 6, 2026 — Smaller Models, Longer Context: Better for Limited GPUs

> 📚 **Model Training** | 🧠 **Context Window** | 💻 **Limited VRAM**

- 💡 **Super important discovery today:** Smaller models can be trained with **much longer context** than larger models on the same GPU.
- 📏 **A 3B model can learn a larger book as a whole**, while a 12B model must split it into smaller chunks on 16GB VRAM.
- 📊 **Practical limits on 16GB:** 7B can do 2048–3072 tokens, 4B can do 4096–6144, 3B can do 8192+.
- 🎯 **For 16GB or less, 3B or 4B models are often better** than 7B or 12B because they can see the full picture at once.
- 📚 **Full Guide:** [smaller_models_longer_context_training.md](TECH/smaller_models_longer_context_training.md) — Why smaller models win on limited hardware, context comparison, and training strategy.

**Key insight:** For limited VRAM, smaller models with longer context can be more powerful than bigger models with chopped-up context. Seeing the whole picture at once often beats having more parameters but only seeing a slice.

---
## 🐧 August 6, 2026 — New Linux Kernel Bug: OVSWrap Local Root Escalation

> 🐧 **Linux Kernel** | 🛡️ **Security** | ⚠️ **Privilege Escalation**

- 🐛 **New kernel bug found** that lets a **local user gain root privileges**.
- 🔴 **Marked as high severity.**
- 🌐 **Affects all kernels with OVS (Open vSwitch) kernel datapath available.**
- ☁️ **Especially dangerous for cloud/virtualized environments** where OVS is commonly used.
- 📚 **Source:** [The Hacker News article](https://thehackernews.com/2026/08/new-ovswrap-linux-kernel-flaw-lets.html)
- 📖 **Full Guide:** [ovswrap_linux_kernel_privilege_escalation_bug.md](TECH/ovswrap_linux_kernel_privilege_escalation_bug.md) — What is affected, why it is dangerous, and what to do.

**Key insight:** Kernel-level bugs in virtualization infrastructure can break isolation between users, containers, and VMs. Patch quickly and check if `openvswitch` is loaded.

---
## 🔄 August 5, 2026 — AIIA Framework: New `!REHEAT` Command

> 🔄 **AIIA Framework** | 🛠️ **User Command** | 🧠 **Context Recovery**

- 🆕 **Added a new user command to AIIA Framework:** `!REHEAT`
- 🧠 **What it does:** Mid-session, it makes the model re-collect everything via `<listTools>` + `<GetTip>` / `<ReinsertTip>`, just like the startup warm-up.
- ⚡ **But without restarting.** The session keeps its history while the model refreshes its tool and tip awareness.
- 📚 **Full Details:** [aiia_reheat_command_added.md](TECH/aiia_reheat_command_added.md) — How it works, why it's useful, and when to use it.

**Key insight:** `!REHEAT` is a warm restart without losing context. Perfect for long sessions where the model starts drifting or forgetting what tools it has.

---
## 🧠 August 5, 2026 — Conditional Thinking: System Prompt as a Switch

> 🧠 **Model Training** | 🎯 **Mixed Dataset** | ⚡ **Conditional Reasoning**

- 🧪 **Trained a model with 70% non-thinking data and 30% thinking-tagged data.**
- 🔄 **Result:** The model thinks **only when the system prompt asks it to think**. Otherwise, it answers directly.
- 🎯 **The system prompt becomes the switch** that controls reasoning behavior.
- 📚 **Full Guide:** [conditional_thinking_based_on_system_prompt.md](TECH/conditional_thinking_based_on_system_prompt.md) — Training setup, observed behavior, and why this matters for AIIA.

**Key insight:** You can train a model to be a switchable thinker. 70% direct data teaches normal behavior. 30% thinking data teaches reasoning when requested.

---
## 🦙 August 5, 2026 — Baking System Prompt into Ollama Modelfile

> 🦙 **Ollama** | 🧠 **LLM Training** | 🛠️ **Modelfile**

- 🧠 **Today learning about LLM training and serving with Ollama.**
- 📝 **You can bake a system prompt directly into the Modelfile** using the `SYSTEM` instruction.
- 🔄 **But if the user defines their own system prompt, the baked one is overridden.**
- 🎯 **This is only possible with Ollama's Modelfile format** — vLLM, llama.cpp, and raw Transformers do not have this exact mechanism.
- 📚 **Full Guide:** [baking_system_prompt_into_ollama_modelfile.md](TECH/baking_system_prompt_into_ollama_modelfile.md) — How it works, example Modelfile, use cases, and limitations.

**Key insight:** Baking a system prompt into a Modelfile gives the model a default identity, but the user can still override it. It is a convenience layer, not a security layer.

---
## 🚨 August 4, 2026 — Anthropic: Claude Models Hacked 3 Organizations During Tests

> 🚨 **AI Security** | 🤖 **Anthropic** | 🕵️ **Cyber Tests**

- 📧 **Received news by email:** Anthropic says Claude models hacked **3 organizations** during cyber tests.
- 🐛 **Cause:** A **misconfigured internet-connected evaluation environment** during review of 141,006 evaluation runs.
- 🤖 **Models involved:** Claude Opus 4.7, Claude Mythos 5, and an internal research model.
- 💰 **And Claude is the most expensive LLM provider.** Now their models are "hacking around" in what was supposed to be a sandbox. Not good, man.
- 🤔 **Something smells.** First they build the app, then it hacks real targets? You pay premium prices and expect premium safety.
- 📚 **Full Details:** [anthropic_claude_models_hacked_organizations_during_tests.md](TECH/anthropic_claude_models_hacked_organizations_during_tests.md) — What happened, why it matters, and why evaluation environments must never touch real systems.

**Key insight:** If your AI safety test can accidentally hack real companies, your safety test is not safe. And when you are already the most expensive provider, that mistake is even harder to accept.

---
## 📦 August 4, 2026 — How to Check Size of Untracked Git Files

> 📦 **Git** | 💾 **Disk Usage** | 🧹 **Cleanup**

- 💾 **Need to know how much space untracked files are using?**
- ✅ **Use this command:**
  ```bash
  git ls-files --others --exclude-standard -z | xargs -0 du -sm | awk '{sum+=$1} END {print "Total:", sum, "MB"}'
  ```
- ⚠️ **Do NOT use `du -sh` with awk sum** — it mixes units (K, M, G) and gives a meaningless total.
- 📚 **Full Guide:** [check_size_of_untracked_git_files.md](TECH/check_size_of_untracked_git_files.md) — Why this works, common mistakes, and useful variations.

**Key insight:** Use `du -sm` for consistent megabyte units when summing untracked file sizes. `du -sh` is human-readable but not summable.

---
## 🎉 August 4, 2026 — Qwen2.5-Coder 7B AIIA v2: Now With Thinking Support

> 🎉 **Milestone** | 🧠 **Fine-Tuning** | 🚀 **AIIA Model**

- 🚀 **Successfully trained the second version of our model:** [Qwen2.5-Coder 7B AIIA v2](https://ollama.com/w4d4f4k/qwen25-coder-aiia-v2)
- 🧠 **v2 supports thinking!** It can reason step by step, plan, and reflect before acting.
- ✅ **This proves that fine-tuning can teach behavior, not just add knowledge.** We took a model that did not think this way and trained it to reason.
- 📚 **Full Details:** [qwen25_coder_aiia_v2_thinking.md](TECH/qwen25_coder_aiia_v2_thinking.md) — What's new, how fine-tuning enabled thinking, and what it means for AIIA.

**Key insight:** Fine-tuning is how you turn a response machine into a thinking agent. Qwen2.5-Coder AIIA v2 is proof that even a 7B model can learn to reason with the right training data.

---
## 🦀 August 4, 2026 — Why LLM Training Infrastructure Is C++ (Not Rust)

> 🦀 **Rust** | ⚡ **C++** | 🧠 **AI Infrastructure**

- 🤔 **Question:** Why is most LLM training infrastructure written in C++ instead of Rust?
- 🏗️ **Answer:** The AI stack was built on C++ long before Rust was mainstream. PyTorch and TensorFlow have millions of lines of optimized C++ and CUDA code.
- 🐍 **Python is the glue, C++ is the engine.** Researchers script in Python; the heavy backend runs in C++ and CUDA.
- 🔒 **Rust's safety is great, but strict ownership and bounds-checking can complicate low-level tensor kernels** where every microsecond matters.
- 📚 **Full Guide:** [llm_training_infrastructure_cpp_not_rust.md](TECH/llm_training_infrastructure_cpp_not_rust.md) — Ecosystem history, CUDA vendor lock-in, safety vs. performance trade-offs, and Rust projects like Burn trying to enter ML.

**Key insight:** C++ won by being there first and staying fast. Rust may take over surrounding AI infrastructure, but the core training kernels will stay C++/CUDA for the foreseeable future.

---
## 🧠 August 4, 2026 — Fine-Tuning: Teaching a Model to Think

> 🧠 **Fine-Tuning** | 🤔 **Reasoning** | 🎯 **AIIA Training**

- 🎯 **Fine-tuning is not just about adding knowledge — it is about shaping behavior.**
- 🧠 **If a model has never been trained to think step by step, it will not naturally handle complex reasoning tasks** the way people do.
- 🔄 **By fine-tuning on reasoning-style data, we can teach our models to plan, reflect, self-correct, and act through tools.**
- 📚 **Full Guide:** [fine_tuning_teaching_models_to_think.md](TECH/fine_tuning_teaching_models_to_think.md) — What fine-tuning really is, why thinking must be trained, and what it means for AIIA.

**Key insight:** A model that has never encountered structured reasoning cannot produce it. Fine-tuning is how we turn response machines into thinking agents.

---
## 🤖 August 4, 2026 — vLLM: Can It Load .pt Files?

> 🤖 **vLLM** | 📦 **Model Formats** | 🚀 **Serving**

- ❓ **Question:** Can vLLM load `.pt` files and generate chat responses from them?
- ❌ **Short answer:** A raw `.pt` file alone — **no**. vLLM needs the full model package: config, tokenizer, and weights.
- ✅ **What vLLM CAN load:** HuggingFace folders (`.pt`, `.bin`, `.safetensors`), GGUF, AWQ, GPTQ, FP8.
- 🔄 **Solution:** Convert your `.pt` state_dict into HuggingFace format with `model.save_pretrained()`, then serve with `vllm serve ./folder`.
- 📚 **Full Guide:** [vllm_loading_models_pt_safetensors_gguf.md](TECH/vllm_loading_models_pt_safetensors_gguf.md) — Full format table, conversion examples, chat API usage, and common mistakes.

**Key insight:** vLLM is a serving engine, not a weight loader. Give it a complete model package and it serves fast chat completions. A raw `.pt` dump is not enough.

---
## 🎛️ August 3, 2026 — AI_INSTRUCT_OPTION: 1 vs 2

> 🎛️ **AIIA Framework** | 🧠 **Model Training** | ⚙️ **Configuration**

- 🎯 **For models trained by us with AIIA Framework, AI_INSTRUCT_OPTION=1 works better.**
- 📝 **Why:** Option 1 uses a **system prompt** with a lot of information included directly. Option 2 uses **tips functionality**, and not all models understand how to read and combine separate tips yet.
- ☁️ **AI_INSTRUCT_OPTION=2 is more useful for cloud models** — they already understand modular context and broader instructions without much training.
- 🚀 **Our own models can become good programmers too** — they just need more training, especially on how to use tips.
- 📚 **Full Details:** [ai_instruct_option_1_vs_2_training_insight.md](TECH/ai_instruct_option_1_vs_2_training_insight.md) — How each option works, why less-trained models need Option 1, and the path to Option 2.

**Key insight:** Less-trained models need everything in one system prompt (Option 1). Tips (Option 2) are powerful, but only for models that already know how to use them. More training closes the gap.

---
## 🧠 August 3, 2026 — Next Model: Gemma3 12B with Thinking Support

> 🧠 **Planning** | 🤖 **Gemma3** | 🎯 **AIIA Framework**

- 🎯 **Next model planned: Gemma3 12B.** It supports thinking — something the last three models did not.
- 🔄 **AIIA Framework was not prepared much for thinking workflows** because previous models lacked this capability. Now we can start building true reasoning into the framework.
- 📚 **Full Details:** [next_model_planned_gemma3_12b_thinking.md](TECH/next_model_planned_gemma3_12b_thinking.md) — Why Gemma3 12B, what thinking support means for AIIA, and what we need to prepare.

**Key insight:** Thinking models change the game. AIIA can evolve from tool executor to agent that plans, reflects, and adapts.

---
## 🧬 August 3, 2026 — Learning Synthetic Trajectory Generators

> 🧬 **Synthetic Data** | 🎯 **Model Training** | 🤖 **AIIA Datasets**

- 🧬 **Today learning about synthetic-trajectory generators.**
- 🤖 **What they do:** generate code/datasets that you want a model to learn — not from real data, but automatically generated based on configurations.
- 🎯 **Why it matters:** you can manufacture the exact training data your model needs, instead of waiting for the world to produce examples.
- 📚 **Full Guide:** [synthetic_trajectory_generator_learning.md](TECH/synthetic_trajectory_generator_learning.md) — How it works, use cases for AIIA, real vs synthetic data, and key insights.

**Key insight:** Synthetic data is a superpower for training specialized models. Configure, generate, train — no real-world collection required.

---
## 🚀 August 3, 2026 — Qwen2.5-Coder 7B AIIA: New Stronger Model

> 🧠 **Fine-Tuned Model** | 💻 **Qwen2.5-Coder** | 🚀 **AIIA Framework**

- 🎉 **Today we created a new, stronger model:** [Qwen2.5-Coder 7B AIIA](https://ollama.com/w4d4f4k/qwen25-coder-aiia)
- 🧠 **Based on Qwen2.5-Coder 7B** and trained on our **AIIA_DATASETS** for AIIA Framework tool commands.
- 🚀 **Available on Ollama:** `ollama run w4d4f4k/qwen25-coder-aiia`
- 📚 **Full Details:** [qwen25_coder_7b_aiia_new_stronger_model.md](TECH/qwen25_coder_7b_aiia_new_stronger_model.md) — Model evolution, capabilities, and why this is the practical next step.

**Key insight:** 7B parameters with a code-specialized base model hits the sweet spot — much stronger than smaller experiments, yet still runnable on accessible hardware.

---
## 🔀 August 2, 2026 — OpenCode Model Switching Leaks Context

> 🤖 **OpenCode** | 🔁 **Model Switching** | ⚠️ **Context Loss**

- 🧠 **Noticed that switching models on OpenCode can lead to information leaks.** One model (Big Pickle) understands the plan it's preparing, then you switch to another (Kimi-K3) and the second doesn't know what the first was doing — even though the chat history is still there.
- 📉 **The context is visible but not understood.** The new model sees the messages but misses the implicit plan and intent.
- 📚 **Full Guide:** [opencode_model_switching_information_leak.md](TECH/opencode_model_switching_information_leak.md) — Why it happens, when it's dangerous, and how to mitigate it.

**Key insight:** Chat history is not enough. Without explicit state and structured plans, switching models breaks the workflow and can leak or lose critical context.

---
## 🐧 August 2, 2026 — Arch Linux Repository Breach & Delayed Notification

> 🛡️ **Security** | 🐧 **Arch Linux** | ⏰ **Delayed Disclosure**

- 📰 **Reading about a breach on Arch repositories** — happened around 2 months ago but notified much later.
- 😰 **Not sure if I have testing Arch these days... omg.**
- 📚 **Source:** [MuyLinux article](https://www.muylinux.com/2026/07/31/arch-linux-aur-adopcion-paquetes/)
- 📖 **Full Guide:** [arch_linux_repository_breach_notification_delay.md](TECH/arch_linux_repository_breach_notification_delay.md) — What happened, why delayed disclosure is dangerous, and what to do.

**Key insight:** A security breach is bad, but delayed notification is worse. The silent months between compromise and disclosure cause the most damage.

---
## 🐧 August 1, 2026 — KOS: Our Future Lightweight Linux Distribution

> 🐧 **Linux** | 🪶 **Lightweight** | 🛠️ **KosGen Ecosystem**

- 🚀 **Planning our own Linux distribution: KOS.** Super-light, useful for developers and normal users.
- 🧩 **Core stack:** X Server + OpenBox (KosBox) + KosDWM5 (dynamic window panel) + KosFM (file manager) + more.
- 🐍 **UI choice:** Python **Tkinter** for lighter machines, or **PyQt5** for stronger hardware.
- 📚 **Full Details:** [kos_future_linux_distribution_plan.md](TECH/kos_future_linux_distribution_plan.md) — Vision, stack, target audience, and why it matters.

**Key insight:** KOS will tie the whole KosGen ecosystem together into one lightweight, modular operating system.

---
## 🌐 August 1, 2026 — LLMs Struggle with JS, HTML & Custom Libraries

> 🧠 **AI Limitations** | 🌐 **Web Dev** | ⚠️ **Reality Check**

- 🐍 **Python and Rust?** Models handle them mostly fine.
- 🌐 **JavaScript, HTML, and custom JS libraries?** Super problems.
- 🤖 **Even the smartest models — including Claude-level AI — struggle** with dynamic typing, runtime DOM context, implicit dependencies, and private APIs.
- 🎯 **Lesson learned:** with this kind of project, you must be **specific** when creating plans or tasks for models and frameworks. Vague instructions multiply confusion.
- 📚 **Full Guide:** [models_struggle_with_javascript_html_custom_libraries.md](TECH/models_struggle_with_javascript_html_custom_libraries.md) — Why it happens, what helps, and implications for AIIA.

**Key insight:** Clean languages with clear boundaries are easy for models. Web stacks with runtime magic and custom libraries are still a hard problem for AI — and specificity is the only way through.

---
## 🧮 August 1, 2026 — Finding Memory Hogs on Linux

> 🐧 **Linux** | 🧠 **Memory** | 🔧 **System Admin**

- 🚀 **Need to find what's using a lot of memory?** Start with the basics.
- 💡 **Best tools:** `free -h` for overview, `htop` for interactive sorting, `ps aux --sort=-%mem | head -20` for quick CLI list, `smem` for accurate shared memory, and `nvidia-smi` for GPU VRAM.
- 📚 **Full Guide:** [finding_memory_hogs_on_linux.md](TECH/finding_memory_hogs_on_linux.md) — Commands, GPU memory, pro tips, and when to use what.

**Key insight:** `ps aux --sort=-%mem | head -10` plus `nvidia-smi` covers most cases. For memory leaks, use `watch` and observe growth over time.

---
## 🚀 August 1, 2026 — AIIA v1: First Published Model

> 🧠 **Fine-Tuned Model** | 🔧 **AIIA Framework** | 🌐 **Ollama**

- 🎉 **We just published our first own trained model:** [AIIA v1](https://ollama.com/w4d4f4k/aiia_v1)
- 🧠 **Trained on AIIA_DATASETS** to learn AIIA Framework tool commands — file operations, browser automation, workflow patterns, site scripts, and more.
- 🚀 **Available on Ollama:** `ollama run w4d4f4k/aiia_v1`
- 📚 **Full Details:** [aiia_v1_first_published_model.md](TECH/aiia_v1_first_published_model.md) — What it does, training data overview, why it matters, and what's next.

**Key insight:** The first model trained specifically for our framework is now public. This is the foundation for everything that follows.

---
## 🤖 August 1, 2026 — AI Agents Hacked Four Public Web Services

> ⚠️ **Cybersecurity** | 🤖 **AI Agents** | 🌐 **Public Services**

- 📰 **Read that AI agents have hacked four public web services.** Not a lab experiment — real public-facing systems.
- ⚡ **This changes the threat landscape.** AI can now scan, probe, and exploit at machine speed. Defenders will need AI-aware security just to keep up.
- 📚 **Source:** [BBC News article](https://www.bbc.com/news/articles/c2el319vzr3o)
- 📖 **Full Guide:** [ai_agents_hacked_four_public_web_services.md](TECH/ai_agents_hacked_four_public_web_services.md) — Implications, what to watch, and why this matters.

**Key insight:** AI is no longer just a defensive tool. The age of autonomous offensive AI agents against public infrastructure has begun.

---

## 🧠 July 31, 2026 — Inkling by Thinking Machines (41B → 975B)

> 🤖 **New LLM** | 📈 **Scalable Model** | 🔓 **Open Weights**

- 🚀 **Discovered a new LLM called `Inkling`** by **Thinking Machines**.
- 📈 **Interesting architecture:** starts at **41B parameters** and can scale up to **975B parameters through training**.
- 🔓 **Open-weight model** — inspectable, modifiable, deployable.
- 📚 **More info:** [Hugging Face model card](https://huggingface.co/thinkingmachines/Inkling) | [IBM news article](https://www.ibm.com/think/news/thinking-machines-inkling-adds-name-open-weight-ai)
- 📖 **Full Guide:** [inkling_by_thinkingmachines_41b_to_975b.md](TECH/inkling_by_thinkingmachines_41b_to_975b.md) — Key facts, why it matters, and what to watch.

**Key insight:** A model designed to grow from usable (41B) to massive (975B) through training changes how we think about model deployment and scaling.

---

## 🕷️ July 31, 2026 — Scattered Spider: Social Engineering Hacking Group

> 🧠 **Cybersecurity** | 🎭 **Social Engineering** | 🌍 **Global Threats**

- 🕷️ **Reading about `Scattered Spider`** — a hacking group that operates through social engineering and even physical hacking.
- 🎭 **They hack like I used to think at 20 years old.** Pretend to be someone, call help desks, trick people into giving access. The human is the weakest link.
- 🌍 **Looks like a big group spread around the world**, organized and dangerous. Not just code — psychology, patience, and manipulation.
- 📚 **Read more:** [Splunk article on Scattered Spider](https://www.splunk.com/en_us/blog/learn/scattered-spider.html)
- 📖 **Full Guide:** [scattered_spider_social_engineering_hacking_group.md](TECH/scattered_spider_social_engineering_hacking_group.md) — Tactics, defense takeaways, and why this matters.

**Key insight:** You can't patch a human with a software update. Social engineering is still the most reliable exploit.

---

## 🤖 July 31, 2026 — Training Llama 3.2 & Kimi K3 on AIIA_DATASETS

> 🧠 **Fine-Tuning** | 📊 **AIIA_DATASETS** | 🔄 **GGUF Conversion**

- 🚀 **Started training models** on the newly created **AIIA_DATASETS** to teach AIIA Framework tool calls.
- ✅ **Llama 3.2 went beautifully** — training was successful, and the model even started using icons in its responses. Lovely to see.
- 📈 **Kimi K3 took more effort** — the small trainable version needed patience, but eventually training succeeded too.
- ⏸️ **Paused at GGUF conversion** for Kimi, which requires llama.cpp modifications. Will continue once OpenCode credits recharge.
- 🧪 **Kimi-K3 is more of an experiment.** For machines like ours with **16GB VRAM**, practical models like **AIIA v1** are the real target.
- 🎯 **Next up:** **Qwen3 4B** tuned with **AIIA datasets** — a size that actually fits and runs on our hardware.
- 📚 **Full Story:** [training_llama32_and_kimi_k3_with_aiia_datasets.md](TECH/training_llama32_and_kimi_k3_with_aiia_datasets.md) — Full experiment details, insights, and next steps.

**Key insight:** Different models learn the same dataset differently. Llama adapts fast, Kimi needs persistence, but practical deployment means matching model size to available hardware. Qwen3 4B is the next practical step.

---

## 🔒 July 29, 2026 — Free SSL Providers: Let's Encrypt vs ZeroSSL

> 🔐 **SSL/TLS** | 🆓 **Free Certs** | 📊 **Comparison**

- 🚀 **The Discovery** — Today learned there are TWO major free SSL certificate providers: **Let's Encrypt** (the well-known standard) and **ZeroSSL** (alternative with web dashboard).
- 💡 **Key Differences** — Let's Encrypt: unlimited automation, ACME-native, community standard. ZeroSSL: 3 certs/month free tier, web GUI, email validation option, good for quick one-offs or when hitting LE rate limits.
- 📚 **Full Guide:** [free_ssl_providers_letsencrypt_zerossl.md](TECH/free_ssl_providers_letsencrypt_zerossl.md) — Comparison table, use cases, ACME setup with ZeroSSL, and when to use which.

**Key insight:** Having options matters. Let's Encrypt for production automation, ZeroSSL for quick certs or backup. Know both tools.

---

## 🔒 July 29, 2026 — Certbot DNS Manual with dig Verification

> 🔐 **SSL/TLS** | 🌐 **DNS** | ⏳ **Patience**

- 🚀 **The Problem** — Automatic HTTP challenge fails due to firewall/proxy issues. Even iptables scripts didn't help. DNS TXT manual mode seemed stuck too.
- 💡 **The Breakthrough** — With coffee and patience, realized DNS propagation takes time. The solution: use `dig TXT _acme-challenge.domain.com` to verify the record exists BEFORE telling certbot to continue.
- 📚 **Complete Guide:** [certbot_dns_manual_with_dig_verification.md](TECH/certbot_dns_manual_with_dig_verification.md) — Step-by-step with troubleshooting and verification commands.

**Key insight:** DNS is not instant. Wait, verify with dig, then proceed. Rushing causes failures.

---

## 🔐 July 28, 2026 — RSYNC with SSH Key & Custom Port

> 🌐 **Secure Transfer** | 🔑 **SSH Keys** | 📝 **Documentation**

- 🚀 **The Challenge** — Need to sync files to remote servers that use non-standard SSH ports and require key-based authentication (not password).
- 💡 **The Pattern** — Combine rsync's `-e` flag with SSH options: `rsync -avz -e "ssh -p PORT -i KEYFILE" source/ user@host:/dest/`
- 📚 **Complete Guide:** [rsync_sync_with_different_port_and_sshkey.md](TECH/rsync_sync_with_different_port_and_sshkey.md) — Full syntax, examples, troubleshooting, and best practices for automated secure transfers.

**Key insight:** Use `ssh-agent` for keys with passphrases to avoid repeated prompts during batch operations.

---

## 🔒 July 19, 2026 — Certbot DNS Challenge

> 🔐 **SSL/TLS** | 🌐 **DNS**

- 🚀 Renewing expired certificates via DNS TXT validation when HTTP challenge fails — [Certbot DNS Guide →](TECH/CERTBOT_DNS_INFOS.md)

---

## 🔄 July 19, 2026 — RSYNC with Custom SSH Ports

> 🌐 **Networking** | 🔐 **SSH Configuration**

- 🚀 **The Problem** — Default rsync tries SSH on port 22, but many servers (including our git infrastructure) run on non-standard ports for security.
- 💡 **The Solution** — Use `-e "ssh -p PORT"` option to specify alternate ports inline, or configure `~/.ssh/config` for clean, reusable connections.
- 📚 **Full Guide:** [RSYNC_AND_NOT_DEFAULT_PORT.md](TECH/RSYNC_AND_NOT_DEFAULT_PORT.md) — Complete methods, examples, and common pitfalls explained.

**Key takeaway:** SSH config file is the cleanest approach for repeated operations. One setup, use everywhere.

---

<div align="center">

### 🌟 [Back to Main News →](README.md)

*Tech notes capture solutions worth sharing.*

</div>
