#!/usr/bin/env python3
import re

with open('README_TECH.md', 'r') as f:
    lines = f.readlines()

# Identify entry blocks
blocks = []
current_block = []
in_entry = False
entry_start_idx = None

for i, line in enumerate(lines):
    if re.match(r'^## .*August \d+, 2026', line):
        if current_block:
            blocks.append((entry_start_idx, current_block))
        entry_start_idx = i
        current_block = [line]
        in_entry = True
    elif in_entry:
        current_block.append(line)
        if line.strip() == '---':
            blocks.append((entry_start_idx, current_block))
            current_block = []
            in_entry = False

remaining_start = blocks[-1][0] + len(blocks[-1][1]) if blocks else 0
remaining = lines[remaining_start:]

def get_date(block_lines):
    header = block_lines[0]
    m = re.search(r'August (\d+), 2026', header)
    return int(m.group(1)) if m else 0

# Sort descending by date; stable sort preserves original order for same date
blocks_sorted = sorted(blocks, key=lambda x: get_date(x[1]), reverse=True)

first_entry_line = blocks[0][0]
new_lines = lines[:first_entry_line]

for _, block in blocks_sorted:
    new_lines.extend(block)

new_lines.extend(remaining)

with open('README_TECH.md', 'w') as f:
    f.writelines(new_lines)

print("Reordered entries. New order:")
for _, block in blocks_sorted:
    print(block[0].strip())
