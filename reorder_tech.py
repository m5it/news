
import re

with open('README_TECH.md', 'r') as f:
    content = f.read()

# Find the two August 14 entries at the top (ReplaceLine + Data Centers)
pattern = r'(## ✅ August 14, 2026 — AIIA Framework ReplaceLine Tool Is Working.*?\*\*Key insight:\*\* Space data centers sound like science fiction.*?\n)'

match = re.search(pattern, content, re.DOTALL)
if match:
    aug14_block = match.group(1)
    # Remove it from current position
    content_without = content[:match.start()] + content[match.end():]
    
    # Find position after Ollama August 15 entry
    ollama_pattern = r'(## 🐛 August 15, 2026 — Ollama Remote Access: Probably My iptables or Routing.*?\*\*Key insight:\*\* Before blaming the service, blame the network.*?\n\n---\n\n)'
    ollama_match = re.search(ollama_pattern, content_without, re.DOTALL)
    if ollama_match:
        insert_pos = ollama_match.end()
        new_content = content_without[:insert_pos] + aug14_block + content_without[insert_pos:]
        with open('README_TECH.md', 'w') as f:
            f.write(new_content)
        print("Reordered successfully")
    else:
        print("Could not find Ollama entry")
else:
    print("Could not find August 14 block")
