# BBC.com JavaScript Debugging Observation

## What I Noticed

While browsing [BBC.com](https://www.bbc.com) and checking the news, I did some casual debugging of the page — something I do from time to time as a developer.

What I found was not great:

- ⚠️ **BBC.com has a lot of JavaScript problems.**
- 🐌 **Behind the scenes, user browsers are being lagged by log requests sent roughly every 500ms.**
- 🔍 **The page is doing a lot of JS activity** that may not be visible to normal users but is clearly measurable in the browser's developer tools.

## What This Looks Like

For a regular visitor, BBC.com loads and works. But if you open the browser's Network or Performance tab, you can see:

- Repeated logging/analytics requests firing frequently
- JavaScript execution that keeps the browser busy
- Network activity happening on a short interval — around every 500ms

This is the kind of thing most users never notice, but it can:

- 🔋 Drain battery faster on mobile devices
- 🐌 Slow down older or lower-powered machines
- 📡 Use more bandwidth than necessary
- 🔒 Potentially leak browsing behavior through frequent tracking calls

## Why This Matters

BBC is a huge, well-funded news organization. If their site has this much background JavaScript noise, it says something about how modern web development often prioritizes analytics, ads, and tracking over clean, fast user experience.

For developers, it is also a reminder:

- 🧹 **Just because a site "works" does not mean it is well-built.**
- 📊 **Analytics and logging should be batched or throttled**, not fired constantly.
- 🐛 **Debugging real production sites is a good habit.** You learn what not to do by watching what big sites actually do.

## Key Insight

> **A news site should deliver news, not continuously phone home every half-second.** Modern websites often hide performance debt behind fast internet and powerful devices, but the cost is real — battery, bandwidth, and user trust.

## See Also

- [LLMs Struggle with JS, HTML & Custom Libraries](models_struggle_with_javascript_html_custom_libraries.md)
- [OpenCode Model Switching Leaks Context](opencode_model_switching_information_leak.md)
