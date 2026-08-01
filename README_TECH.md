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
> These notes capture solutions to real problems encountered while building, connecting, and maintaining systems.

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
