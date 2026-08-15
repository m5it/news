
import re

with open('README_TECH.md', 'r') as f:
    content = f.read()

# Split into header and entries
# Header ends at the first ## 
header_match = re.search(r'^(.*?\n## ✅ August 14, 2026 — AIIA Framework ReplaceLine Tool Is Working)', content, re.DOTALL)
if not header_match:
    print("Could not find header")
    exit(1)

header = header_match.group(1).replace('## ✅ August 14, 2026 — AIIA Framework ReplaceLine Tool Is Working', '').rstrip() + '\n\n'

# Extract each entry
entries = {}

patterns = {
    'replace': r'## ✅ August 14, 2026 — AIIA Framework ReplaceLine Tool Is Working.*?(?=\n---\n\n## |$)',
    'space': r'## 🚀 August 14, 2026 — Data Centers in Space: The Future Is Coming.*?(?=\n---\n\n## |$)',
    'callers': r'## ⚠️ August 15, 2026 — Warning: Do Not Let Callers Tell You What to Do.*?(?=\n---\n\n## |$)',
    'sql': r'## 🛡️ August 15, 2026 — SQL Injection Attacks Coming From IONOS IP Range.*?(?=\n---\n\n## |$)',
    'ollama': r'## 🐛 August 15, 2026 — Ollama Remote Access: Probably My iptables or Routing.*?(?=\n---\n\n## |$)',
}

for key, pattern in patterns.items():
    match = re.search(pattern, content, re.DOTALL)
    if match:
        entries[key] = match.group(0).rstrip() + '\n'
    else:
        print(f"Could not find entry: {key}")
        exit(1)

# Build new order: callers, sql, ollama, replace, space
new_entries = [
    entries['callers'],
    entries['sql'],
    entries['ollama'],
    entries['replace'],
    entries['space'],
]

# Get the rest after the last matched entry (which is ollama originally, but now we need everything after space)
# Find where the space entry ends in original
rest_start = content.find(entries['space']) + len(entries['space'])
rest = content[rest_start:]

# Remove leading --- if present
rest = rest.lstrip()
if rest.startswith('---\n'):
    rest = rest[4:]

new_content = header + '\n---\n\n'.join(new_entries) + '\n\n---\n\n' + rest

with open('README_TECH.md', 'w') as f:
    f.write(new_content)

print("Reordered successfully")
