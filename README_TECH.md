<div align="center">

# ⚡ ═══════════════════ ⚡
# 💻  T E C H   N O T E S   💻
# ⚡ ═══════════════════ ⚡

**Practical Knowledge for Digital Craftsmanship.**

[![Tech Notes](https://img.shields.io/badge/💻-Tech%20Notes-orange)](#tech-notes)
[![Main News](https://img.shields.io/badge/📰-Main%20News%20→-brightgreen)](README.md)

</div>

---

> 🔧 **General Principle:** *Understanding the tools we use daily transforms frustration into capability.*
> These notes capture solutions to real problems encountered while building, connecting, and maintaining systems.

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
