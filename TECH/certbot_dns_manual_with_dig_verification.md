# Certbot DNS Manual Mode with DNS Propagation Verification

## The Problem

Automatic HTTP-01 challenge fails when:
- Firewall blocks port 80/443
- Reverse proxies interfere
- ISP blocks incoming connections
- Complex network topologies

## Solution: DNS-01 Manual Challenge

### Step 1: Request Certificate with Manual DNS

```bash
sudo certbot certonly --manual --preferred-challenges dns -d www.aiia-frame.work -d aiia-frame.work
```

### Step 2: Certbot Shows TXT Record

```
Please deploy a DNS TXT record under the name:
_acme-challenge.www.aiia-frame.work

With the following value:
xJdJzXvN7xYvKxLqP9mN8oR3sT5uV2wX4yZ6aB8cD0eF2gH4iJ6kL8mN0oP2qR4sT6u

Before continuing, verify the TXT record has been deployed.
```

### Step 3: Add TXT Record in DNS Provider

Add the TXT record in your DNS panel (Cloudflare, GoDaddy, etc.)

### Step 4: CRITICAL - Wait for Propagation

**Don't rush!** DNS propagation takes time (30 seconds to 5+ minutes).

### Step 5: Verify with dig

Check if the record is live before continuing:

```bash
# Check the TXT record
dig TXT _acme-challenge.www.aiia-frame.work

# Expected output should show:
;; ANSWER SECTION:
_acme-challenge.www.aiia-frame.work. 300 IN TXT "xJdJzXvN7xYvKxLqP9mN8oR3sT5uV2wX4yZ6aB8cD0eF2gH4iJ6kL8mN0oP2qR4sT6u"
```

### Step 6: Continue Only When dig Shows Record

If dig returns the TXT value, press **ENTER** in certbot to continue.

If dig returns empty or old value, **WAIT** and retry dig.

## Troubleshooting

### dig returns empty?

- DNS provider delay: Wait 2-5 minutes
- Wrong DNS server: Try `dig @8.8.8.8 TXT _acme-challenge.www.aiia-frame.work`
- Typo in record name: Check `_acme-challenge` spelling

### Certificate not generating?

- Make sure to validate ALL domains requested
- Each domain has its own `_acme-challenge` TXT record
- Remove old TXT records after success (cleanup)

### Automation Alternative

For automated renewal, use DNS provider plugins:

```bash
# Cloudflare example
sudo certbot certonly --dns-cloudflare --dns-cloudflare-credentials ~/.secrets/cloudflare.ini -d aiia-frame.work -d *.aiia-frame.work
```

Available plugins: `certbot-dns-cloudflare`, `certbot-dns-route53`, `certbot-dns-google`, etc.

## Key Insight

**Patience is the solution.** DNS propagation is not instant. Use `dig` to verify before telling certbot to continue. Rushing causes "TXT record not found" errors.

## See Also

- [RSYNC with SSH Keys](rsync_sync_with_different_port_and_sshkey.md)
- [Network Debugging](../DEFAULT/NETWORK_DEBUG.md)
