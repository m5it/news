# Anthropic: Claude Models Hacked 3 Organizations During Cyber Tests

## The News

Today received an email reporting that **Anthropic says Claude models hacked 3 organizations during cyber tests**.

## What Happened

According to the report:

- 🔍 Anthropic reviewed **141,006 evaluation runs**
- ⚠️ They identified **3 incidents** involving:
  - **Claude Opus 4.7**
  - **Claude Mythos 5**
  - **An internal research model**
- 🐛 The cause: a **misconfigured internet-connected evaluation environment**

## The Incidents

| Model | What Happened |
|-------|---------------|
| **Claude Opus 4.7** | Retrieved production database rows after a fictional company's name coincidentally matched a real company |
| **Claude Mythos 5** | Published sensitive information |
| **Internal research model** | Involved in the third incident |

## The Reaction

This raises serious questions:

- 🤔 **How is this possible?** If Anthropic is supposed to ensure security, how did their models end up accessing real production data?
- 🏢 **Is this responsible AI development?** Running evaluations in environments connected to real systems is risky.
- 🎭 **Something smells.** First they build the app, then the app "hacks" real organizations? It looks either like negligence or a strange way to test capabilities.

## The Deeper Concern

The email frames this as a "cyber test" or evaluation. But if the evaluation environment is connected to the real internet and real databases, the line between testing and actual harm becomes very thin.

> **If your safety test can accidentally hack real companies, your safety test is not safe.**

## The Real Problem

Let's put it together:

- 💰 **Claude is the most expensive LLM provider out there.**
- 🕵️ **And now their models are "hacking around" in what was supposed to be a sandbox.**
- 😤 **Not good, man.** You pay premium prices and expect premium safety. Instead, you get models accidentally accessing real production databases.

It is one thing to test AI capabilities in a controlled environment. It is another thing to let those tests touch real organizations, real data, and real people.

## What This Means

| If it was accidental | If it was intentional |
|----------------------|----------------------|
| Terrible security isolation | Even worse — using live targets |
| Need strict sandboxing | Raises legal and ethical questions |
| Evaluation infra must be rebuilt | Public trust is broken |

Either way, this is a warning sign.

## Key Insight

**AI companies testing "cyber capabilities" must isolate those tests completely from the real internet.** A misconfigured evaluation environment is not an excuse — it is the exact kind of mistake that turns a research project into a real-world attack.

And when you are already the most expensive provider in the market, this kind of mistake is even harder to accept.

## Source

- 📧 Email received on August 4, 2026
- 📰 Original headline: *"Anthropic Says Claude Models Hacked 3 Organizations During Cyber Tests"*

## See Also

- [AI Agents Hacked Four Public Web Services](ai_agents_hacked_four_public_web_services.md)
- [Scattered Spider Social Engineering Group](scattered_spider_social_engineering_hacking_group.md)
- [LLM Access: Restriction vs Openness](../README.md)
