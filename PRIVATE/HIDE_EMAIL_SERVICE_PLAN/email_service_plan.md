# Email Hiding Service - grandekos.com

## Concept
Service for hiding users' real email addresses by providing alias/redirect emails.

**Example:**
- Real email: `joe@gmail.com`
- Our alias: `hidden-joe@grandekos.com`

## Architecture

```
Sender → hidden-joe@grandekos.com → Python Service → joe@gmail.com
```

## Key Components

1. **MX Records** - Point `grandekos.com` to mail server
2. **Mail Server** - Receive emails (Postfix or Python `aiosmtpd`)
3. **Database** - Map aliases to real emails
4. **Forwarding Logic** - Rewrite headers and relay
5. **SPF/DKIM/DMARC** - Critical for deliverability

## Python Implementation Options

### Option A: SMTP Server (Full Control)
```python
from aiosmtpd.controller import Controller

class CustomHandler:
    async def handle_DATA(self, server, session, envelope):
        # Parse email, lookup alias, forward to real address
        pass

controller = Controller(CustomHandler(), hostname='0.0.0.0', port=25)
```

### Option B: API + External Mail Service
- Use AWS SES, SendGrid, or Mailgun
- Python app manages alias mappings and API calls

## Challenges & Solutions

| Issue | Solution |
|-------|----------|
| Spam reputation | Rate limiting, abuse detection |
| Email authentication | SPF, DKIM, DMARC records |
| Privacy compliance | GDPR/CCPA compliance |
| Blacklist prevention | Monitor IP reputation |
| Bounce handling | Process delivery failures |

## MVP Approach

1. Postfix mail server + Python scripts for alias management
2. SQLite/PostgreSQL for mapping database
3. Web UI for users to create/manage aliases
4. SRS (Sender Rewriting Scheme) for SPF issues

## Business Model

- **Free tier**: 5-10 aliases
- **Paid tier**: Unlimited aliases, custom domains, analytics
- **API access** for developers
