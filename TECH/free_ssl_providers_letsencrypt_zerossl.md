# Free SSL Certificate Providers: Let's Encrypt vs ZeroSSL

## The Discovery

Today I learned there are **two major free SSL certificate providers**:

1. **Let's Encrypt** — The most widely known, backed by the non-profit Internet Security Research Group (ISRG)
2. **ZeroSSL** — A newer alternative with some different features and limits

## Quick Comparison

| Feature | Let's Encrypt | ZeroSSL |
|---------|---------------|---------|
| **Price** | Free | Free (paid tiers available) |
| **Certificate Duration** | 90 days | 90 days (free tier) |
| **Rate Limits** | 50 certs/week per domain | 3 certs/month (free tier) |
| **Validation Methods** | HTTP-01, DNS-01, TLS-ALPN-01 | HTTP, DNS, Email |
| **Wildcard Support** | Yes (DNS-01 only) | Yes (paid tiers) |
| **ACME Support** | Native | Yes (via ACME v2) |
| **Dashboard** | No (command line only) | Yes (web dashboard) |

## When to Use Which?

### Let's Encrypt — Best For:
- High-volume automation (unlimited certs with proper rate limit handling)
- Full ACME integration (certbot, acme.sh, etc.)
- Wildcard certificates (with DNS challenge)
- Maximum community support and documentation

### ZeroSSL — Best For:
- Quick one-off certificates via web dashboard
- When you hit Let's Encrypt rate limits
- Email validation (no need to configure DNS or HTTP)
- Teams that want a GUI for certificate management

## Using ZeroSSL with ACME

ZeroSSL supports ACME v2 protocol, so you can use it with certbot:

```bash
# Get credentials from ZeroSSL dashboard first
certbot certonly --server https://acme.zerossl.com/v2/DV90 \
  --eab-kid YOUR_EAB_KID \
  --eab-hmac-key YOUR_EAB_HMAC_KEY \
  -d example.com
```

## Key Insight

**Having options matters.** When Let's Encrypt hits its limits or when you need a quick cert without complex DNS setup, ZeroSSL is your backup. For production automation at scale, Let's Encrypt remains the standard. Know both tools — use the right one for the job.

## See Also

- [Certbot DNS Manual Guide](certbot_dns_manual_with_dig_verification.md)
- [Certbot DNS Challenge](CERTBOT_DNS_INFOS.md)
