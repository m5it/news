<div align="center">

# ⚡ ═══════════════════════════════════════ ⚡
# 💻  T E C H   N O T E S   💻
# ⚡ ═══════════════════════════════════════ ⚡

**Practical Knowledge for Digital Craftsmanship.**

[![Tech Notes](https://img.shields.io/badge/💻-Tech%20Notes-orange)](#tech-notes)
[![Main News](https://img.shields.io/badge/📰-Main%20News%20→-brightgreen)](README.md)

</div>

---

> 🔧 **General Principle:** *Understanding the tools we use daily transforms frustration into capability.*
> These notes capture solutions to real problems encountered while building, connecting, and maintaining systems.

---

## 🔄 July 19, 2026 — RSYNC with Custom SSH Ports

> 🌐 **Networking** | 🔐 **SSH Configuration**

- 🚀 **The Problem** — Default rsync tries SSH on port 22, but many servers (including our git infrastructure) run on non-standard ports for security.
- 💡 **The Solution** — Use `-e "ssh -p PORT"` option to specify alternate ports inline, or configure `~/.ssh/config` for clean, reusable connections.
- 📚 **Full Guide:** [RSYNC_AND_NOT_DEFAULT_PORT.md](RSYNC_AND_NOT_DEFAULT_PORT.md) — Complete methods, examples, and common pitfalls explained.

**Key takeaway:** SSH config file is the cleanest approach for repeated operations. One setup, use everywhere.

---

<div align="center">

### 🌟 [Back to Main News →](README.md)

*Tech notes capture solutions worth sharing.*

</div>
