
with open('README_TECH.md', 'r') as f:
    original = f.read()

# Header part
header_end = original.find('## ✅ August 14, 2026 — AIIA Framework ReplaceLine Tool Is Working')
header = original[:header_end].rstrip() + '\n\n'

# Extract entries by finding their starts and the next ## or end
def extract_entry(text, start_marker):
    start = text.find(start_marker)
    if start == -1:
        return None
    # find next entry start (line starting with ## )
    next_entry = text.find('\n## ', start + 1)
    if next_entry == -1:
        return text[start:]
    return text[start:next_entry]

entries = {
    'replace': extract_entry(original, '## ✅ August 14, 2026 — AIIA Framework ReplaceLine Tool Is Working'),
    'space': extract_entry(original, '## 🚀 August 14, 2026 — Data Centers in Space: The Future Is Coming'),
    'callers': extract_entry(original, '## ⚠️ August 15, 2026 — Warning: Do Not Let Callers Tell You What to Do'),
    'sql': extract_entry(original, '## 🛡️ August 15, 2026 — SQL Injection Attacks Coming From IONOS IP Range'),
    'ollama': extract_entry(original, '## 🐛 August 15, 2026 — Ollama Remote Access: Probably My iptables or Routing'),
}

# Get rest after last entry (which is space in original)
rest_start = original.find(entries['space']) + len(entries['space'])
rest = original[rest_start:].lstrip()

# Build new content: callers, sql, ollama, replace, space, then rest
new_entries = [
    entries['callers'].rstrip(),
    entries['sql'].rstrip(),
    entries['ollama'].rstrip(),
    entries['replace'].rstrip(),
    entries['space'].rstrip(),
]

new_content = header + '\n\n---\n\n'.join(new_entries) + '\n\n---\n\n' + rest

with open('README_TECH.md', 'w') as f:
    f.write(new_content)

print("Rebuilt successfully")
