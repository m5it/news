<div align="center">

# ⚡ ═══════════════════ ⚡
# 🔒  C E R T B O T   D N S   C H A L L E N G E  🔒
# ⚡ ═══════════════════ ⚡

**Renewing SSL Certificates with DNS TXT Validation**

</div>

---

## 🔄 Manual DNS Challenge

When HTTP validation isn't possible (wildcard domains, internal servers), use DNS TXT records:

### Command

```bash
sudo certbot certonly --manual --preferred-challenges dns --cert-name beta.example.com-0001
```

Or specify all domains:

```bash
sudo certbot certonly --manual --preferred-challenges dns \
  -d example.com \
  -d www.example.com \
  -d beta.example.com \
  -d aiia.example.com \
  -d apis.example.com \
  -d chat.example.com \
  -d login.example.com \
  -d mail.example.com \
  -d wss.example.com
```

### Process

1. **Run command** → Certbot generates TXT values
2. **Add TXT records** to DNS server:
   - Name: `_acme-challenge.beta.example.com`
   - Value: `xJd9fP3kLm8...` (provided by certbot)
3. **Wait for propagation** (30-300 seconds)
4. **Press Enter** to validate
5. **Certificate issued** to `/etc/letsencrypt/live/`

---

## 🌐 Automated DNS (Recommended)

| Provider | Plugin | Install |
|----------|--------|---------|
| Cloudflare | certbot-dns-cloudflare | `sudo apt install certbot-dns-cloudflare` |
| Route53 | certbot-dns-route53 | `sudo apt install certbot-dns-route53` |

---

## 📋 Check Certificate Status

```bash
sudo certbot certificates
```

---

<div align="center">

### 🌟 [Back to Tech Notes →](../README_TECH.md)

</div>
