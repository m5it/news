
import re

with open('README.md', 'r') as f:
    content = f.read()

# Fix the broken section around Salespeople/NVIDIA/Altered Carbon
# Pattern: duplicate Salespeople header + NVIDIA header without body
broken_pattern = r'## 🛒 August 25, 2026 — Salespeople Need Training in People Skills\s*\n\s*---\s*\n\s*## 🤖 August 24, 2026 — NVIDIA and Poolside: A Strategic Partnership\?\s*\n\s*## 📺 August 24, 2026 — TV Series Recommendation: Altered Carbon'

# We need to reconstruct this area:
# - Keep one Salespeople entry (already exists before this)
# - Add NVIDIA entry with proper body
# - Keep Altered Carbon entry

nvidia_entry = """## 🤖 August 24, 2026 — NVIDIA and Poolside: A Strategic Partnership?

> 🤖 **AI Business** | 🏢 **NVIDIA** | 🌊 **Poolside**

- 📰 **Reading that NVIDIA and Poolside are making agreements.**
- 🏢 **NVIDIA is the big, old, well-known company.**
- 🌊 **Poolside is a new startup, but built by people already known from GitHub.**
- 🤔 **It looks like they are just creating another company to protect themselves** if anything goes wrong — a separate brand, separate liability, same people.
- 🎯 **What do I think will come from this?** We will see soon. :D
- 🐐 **Bip bip.**

**Key insight:** Big companies often use new startups as shields or experiments. If Poolside succeeds, NVIDIA wins. If it fails or causes controversy, NVIDIA keeps its distance. The real question is not who owns the company on paper, but who benefits when things go right — and who pays when things go wrong.

---

## 📺 August 24, 2026 — TV Series Recommendation: Altered Carbon"""

replacement = nvidia_entry

new_content = re.sub(broken_pattern, replacement, content, flags=re.DOTALL)

# Remove any remaining duplicate Salespeople entries
# Keep only the first occurrence
pattern = r'(## 🛒 August 25, 2026 — Salespeople Need Training in People Skills.*?\*\*Key insight:\*\* Selling is not just about talking.*?\n\n---\n\n)'
match = re.search(pattern, new_content, re.DOTALL)
if match:
    first_entry = match.group(1)
    # Remove all occurrences and then put first one back in correct place
    rest = new_content.replace(first_entry, '')
    # Find where to insert it back: after KosDB entry
    insert_marker = 'Sometimes silence from big names is the loudest compliment.\n\n---\n\n'
    insert_pos = rest.find(insert_marker) + len(insert_marker)
    new_content = rest[:insert_pos] + first_entry + rest[insert_pos:]

with open('README.md', 'w') as f:
    f.write(new_content)

print("Fixed README.md")
