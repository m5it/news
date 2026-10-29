#!/usr/bin/env python3
"""
news_parser.py — robust parser/normalizer for news project.

Handles:
- README.md, README_TECH.md, README_SPORT.md, any README_*.md
- DETAIL dirs: TECH/, SPORT/, DEFAULT/, PRIVATE/, root *.md files
- Separation bug: -- (2 dashes) vs --- (3 dashes), plus spacing variations
- Header normalization: # -> ## (old entries used single #)
- Extracts: date, title, emoji, tags, body, key_insight, links
"""
import re
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Tuple
from datetime import datetime

# --- Regexes ---
# Separator: line that is only 2+ dashes (with optional whitespace) -> normalize to ---
SEP_RE = re.compile(r'^\s*-{2,}\s*$', re.MULTILINE)

# Header: ## or # + date + separator + title
# Examples:
#   ## October 29, 2026 - Musica que me gusta
#   # September 27, 2026 - What changed when you become "old"
#   # Oktober 1 or 2 (not sure), 2026 - Alicia del Rio muy bien dicho!
#   ## 🌍 September 2, 2026 — Ceuta: Send Them Back
HEADER_RE = re.compile(
    r'^(#{1,2})\s+(.+?)\s*[—–\-]\s*(.+)$',
    re.MULTILINE
)

# Tags line: > 🔧 **Something** | 🧠 **Tags** |
TAG_LINE_RE = re.compile(r'^\s*>\s*(.+)$', re.MULTILINE)

# Key insight: **Key insight:** ...
KEY_INSIGHT_RE = re.compile(r'\*\*Key insight:\*\*\s*(.+?)(?=\n---|\Z)', re.DOTALL | re.IGNORECASE)

# Links: markdown [text](path) and <a href="path">
MD_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
HTML_LINK_RE = re.compile(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', re.IGNORECASE)


@dataclass
class NewsEntry:
    raw_header: str
    header_level: str  # "#" or "##"
    date_str: str      # e.g. "October 29, 2026" or "Oktober 1 or 2 (not sure), 2026"
    title: str
    emoji: str = ""
    tags: str = ""     # raw tag line content
    body: str = ""
    key_insight: str = ""
    links: List[Tuple[str, str]] = field(default_factory=list)  # (text, href)
    source_file: str = ""
    category: str = ""  # derived: main, tech, sport, etc.
    start_line: int = 0
    end_line: int = 0
    raw_block: str = ""

    @property
    def normalized_header(self) -> str:
        # Always normalize to ## + emoji if present
        # Keep original date_str and title, but use ## and em dash
        emoji_part = f"{self.emoji} " if self.emoji else ""
        return f"## {emoji_part}{self.date_str} — {self.title}"

    @property
    def has_detail_file(self) -> bool:
        return any(href.startswith("TECH/") or href.startswith("SPORT/") or href.startswith("DEFAULT/") or href.startswith("PRIVATE/") for _, href in self.links)

    def to_markdown(self) -> str:
        """Serialize back to normalized markdown block (no trailing separator)."""
        parts = [self.normalized_header, ""]
        if self.tags:
            parts.append(f"> {self.tags}")
            parts.append("")
        if self.body:
            parts.append(self.body.strip())
            parts.append("")
        if self.key_insight:
            parts.append(f"**Key insight:** {self.key_insight.strip()}")
            parts.append("")
        return "\n".join(parts).strip()


def _extract_emoji(title_or_header: str) -> Tuple[str, str]:
    """If title starts with emoji, separate it. Returns (emoji, rest)."""
    # Simple: if first char is not ascii letter/digit/#/space
    stripped = title_or_header.strip()
    if not stripped:
        return "", stripped
    first = stripped[0]
    # emoji often is outside ascii, or we detect leading emoji pattern
    # Check if first char ord > 127 and not part of date
    if ord(first) > 127:
        # take first token if it's emoji
        m = re.match(r'^(\S+)\s+(.*)', stripped)
        if m and ord(m.group(1)[0]) > 127:
            return m.group(1), m.group(2)
    return "", stripped


def fix_separators(content: str) -> str:
    """Normalize all separator lines (--, ---, ----, etc.) to ---."""
    # Replace any line that is only 2+ dashes with ---
    return SEP_RE.sub("---", content)


def normalize_headers(content: str) -> str:
    """Normalize single # headers that look like news entries to ##."""
    def repl(m):
        hashes = m.group(1)
        date_part = m.group(2).strip()
        title_part = m.group(3).strip()
        # Heuristic: if date_part contains a year (e.g. 2026) it's a news header
        if re.search(r'\b\d{4}\b', date_part):
            # Normalize to ## and em dash
            return f"## {date_part} — {title_part}"
        else:
            # Likely a decorative header like "# 🌟 ═══", leave as is
            return m.group(0)
    return HEADER_RE.sub(repl, content)


def parse_entries(content: str, source_file: str = "", category: str = "") -> List[NewsEntry]:
    """Parse markdown content into NewsEntry list. Handles normalized + legacy."""
    # First normalize separators for parsing stability (but keep original raw for debug)
    # We'll split on normalized separators
    normalized = fix_separators(content)
    # Split into blocks: header -> until next --- or next header
    # Strategy: find all header positions, then slice content between separators
    entries = []
    lines = normalized.splitlines()
    # We need to detect entry boundaries: header line followed by content until separator line "---"
    # Simpler: split by separator lines, then check which chunks start with header
    # Keep line numbers for editing

    # Build list of separator line indices
    sep_indices = [i for i, l in enumerate(lines) if l.strip() == "---"]

    # Find header line indices
    header_indices = []
    for i, l in enumerate(lines):
        if HEADER_RE.match(l) and re.search(r'\b\d{4}\b', l):
            # exclude decorative headers like "# 🌟 ═══" — they don't have year
            header_indices.append(i)

    for idx, h_idx in enumerate(header_indices):
        raw_header = lines[h_idx]
        m = HEADER_RE.match(raw_header)
        if not m:
            continue
        header_level = m.group(1)
        date_str = m.group(2).strip()
        title = m.group(3).strip()

        # Extract emoji from title or date_str (some headers like "🌍 September 2, 2026")
        emoji = ""
        # date_str may start with emoji
        em, rest_date = _extract_emoji(date_str)
        if em:
            emoji = em
            date_str = rest_date
        em2, rest_title = _extract_emoji(title)
        if em2 and not emoji:
            emoji = em2
            title = rest_title
        elif em2:
            # If both have emoji, prefer date one, but keep title emoji as part of title?
            pass

        # Determine block end: next separator after header, or before next header
        # Find next sep index > h_idx
        next_sep = None
        for s in sep_indices:
            if s > h_idx:
                next_sep = s
                break
        next_header = header_indices[idx + 1] if idx + 1 < len(header_indices) else None

        # Block end is min(next_sep, next_header_before_sep?)
        # Typically: header ... body ... separator -> next header
        # So end is next_sep if exists, else next_header or len(lines)
        if next_sep is not None:
            # If there's a header before next_sep, that means missing separator (rare), use header
            if next_header is not None and next_header < next_sep:
                end_idx = next_header
            else:
                end_idx = next_sep
        else:
            end_idx = next_header if next_header is not None else len(lines)

        block_lines = lines[h_idx:end_idx]
        # Remove trailing empty lines before separator
        block_text = "\n".join(block_lines).strip()

        # Now parse sub-parts from block_text
        # Tags: first line after header that starts with >
        tags = ""
        body = ""
        key_insight = ""

        # Remove header from block for parsing body
        after_header = "\n".join(block_lines[1:]).strip()

        # Find tags: consecutive > lines at top of after_header
        tag_lines = []
        remaining_lines = after_header.splitlines()
        cursor = 0
        for line in remaining_lines:
            if line.strip().startswith(">"):
                tag_lines.append(line.strip().lstrip(">").strip())
                cursor += 1
            elif line.strip() == "" and tag_lines:
                # allow blank line after tags but peek: if next is also tag, continue
                # else break tag collection
                # Look ahead
                nxt = remaining_lines[cursor] if cursor < len(remaining_lines) else ""
                if nxt.strip().startswith(">"):
                    cursor += 1
                    continue
                else:
                    cursor += 1
                    break
            else:
                if tag_lines:
                    break
                # If no tags found yet and line is not tag, keep scanning? But tags are at top only.
                break

        if tag_lines:
            tags = " | ".join(tag_lines)

        # Remaining body after tags
        body_raw = "\n".join(remaining_lines[cursor:]).strip()

        # Extract Key insight if present
        ki_match = KEY_INSIGHT_RE.search(body_raw)
        if ki_match:
            key_insight = ki_match.group(1).strip()
            # Remove it from body
            body = body_raw[:ki_match.start()].strip()
        else:
            body = body_raw

        # Extract links from body
        links = []
        for text, href in MD_LINK_RE.findall(body):
            links.append((text, href))
        for href, text in HTML_LINK_RE.findall(body):
            links.append((text.strip() or href, href))

        # Clean body trailing separators artifacts (should already be removed)
        body = re.sub(r'\n---\s*$', '', body).strip()

        entry = NewsEntry(
            raw_header=raw_header,
            header_level=header_level,
            date_str=date_str,
            title=title,
            emoji=emoji,
            tags=tags,
            body=body,
            key_insight=key_insight,
            links=links,
            source_file=source_file,
            category=category,
            start_line=h_idx + 1,
            end_line=end_idx + 1,
            raw_block=block_text,
        )
        entries.append(entry)

    return entries


def normalize_file_content(content: str) -> str:
    """Full normalization: fix separators + fix headers + ensure consistent spacing."""
    content = fix_separators(content)
    content = normalize_headers(content)
    # Ensure separators have exactly \n\n---\n\n between entries (and single \n after header block)
    # Collapse multiple blank lines around separators to standard
    # Pattern: \n* ---\n* -> \n\n---\n\n
    content = re.sub(r'\n*\n---\n*\n', '\n\n---\n\n', content)
    # Ensure file ends with single newline
    if not content.endswith("\n"):
        content += "\n"
    return content


def scan_categories(root: Path = Path(".")) -> dict:
    """Scan project root for categories (dirs + README files).
    Returns dict: category_name -> {"path": Path, "type": "dir"|"readme", "count": int}
    """
    root = Path(root)
    cats = {}
    # README files are categories themselves
    for p in root.glob("README*.md"):
        name = p.stem  # README, README_TECH, README_SPORT, etc.
        cats[name.lower()] = {"path": p, "type": "readme", "count": 0}
    # Directories that contain .md files
    for d in root.iterdir():
        if d.is_dir() and not d.name.startswith(".") and d.name not in ("__pycache__", "plans"):
            md_files = list(d.glob("*.md"))
            if md_files or d.name in ("TECH", "SPORT", "DEFAULT", "PRIVATE"):
                cats[d.name.lower()] = {"path": d, "type": "dir", "count": len(md_files)}
    # Root loose markdown files (not README/DONATE etc) as "root" category
    root_mds = [p for p in root.glob("*.md") if p.name.startswith("README") is False and p.name not in ("DONATE.md", "PROJECT.md", "PLAN.md")]
    if root_mds:
        cats["_root"] = {"path": root, "type": "root_mds", "count": len(root_mds), "files": root_mds}
    return cats


def parse_all(root: Path = Path(".")) -> dict:
    """Parse all categories and return dict category -> entries/files."""
    root = Path(root)
    result = {}
    cats = scan_categories(root)
    for cat_name, info in cats.items():
        if info["type"] == "readme":
            try:
                content = info["path"].read_text(encoding="utf-8")
                entries = parse_entries(content, source_file=str(info["path"]), category=cat_name)
                result[cat_name] = {"info": info, "entries": entries, "content": content}
            except Exception as e:
                result[cat_name] = {"info": info, "entries": [], "error": str(e), "content": ""}
        elif info["type"] == "dir":
            # List files in dir as entries (detail articles)
            files = sorted(info["path"].glob("*.md"))
            file_entries = []
            for f in files:
                try:
                    txt = f.read_text(encoding="utf-8")
                    file_entries.append({"path": f, "content": txt, "size": len(txt)})
                except Exception as e:
                    file_entries.append({"path": f, "error": str(e)})
            result[cat_name] = {"info": info, "files": file_entries}
        elif info["type"] == "root_mds":
            files = info.get("files", [])
            file_entries = []
            for f in files:
                try:
                    txt = f.read_text(encoding="utf-8")
                    file_entries.append({"path": f, "content": txt, "size": len(txt)})
                except Exception as e:
                    file_entries.append({"path": f, "error": str(e)})
            result[cat_name] = {"info": info, "files": file_entries}
    return result


def parse_date(date_str: str) -> Optional[datetime]:
    """Try to parse date_str like 'October 29, 2026' or 'Oktober 1 or 2 (not sure), 2026'."""
    # Clean: remove emojis, notes in parens, extra words
    s = date_str.strip()
    # Remove parenthetical
    s = re.sub(r'\(.*?\)', '', s).strip()
    # Take last attempt to find Month Day, Year
    m = re.search(r'([A-Za-z]+)\s+(\d{1,2})(?:\s+or\s+\d{1,2})?\s*,?\s*(\d{4})', s)
    if not m:
        return None
    month_raw = m.group(1).lower()
    day = int(m.group(2))
    year = int(m.group(3))
    month_map = {
        'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,'august':8,'september':9,'october':10,'november':11,'december':12,
        'januar':1,'februar':2,'märz':3,'oktober':10,'dezember':12, # german typos
    }
    month = month_map.get(month_raw)
    if not month:
        try:
            month = datetime.strptime(month_raw[:3], '%b').month
        except:
            return None
    try:
        return datetime(year, month, day)
    except:
        return None

def month_key(dt: datetime) -> str:
    return dt.strftime("%Y-%m")

def archive_header_for_month(year: int, month: int) -> str:
    """Generate README header for monthly archive, similar to README_2026_07.md:1"""
    month_name = datetime(year, month, 1).strftime("%B")
    return f"""<div align="center">

# 🌟 ═══════════════════ 🌟
# 📰  P E R S O N A L   N E W S   📰
# 🌟 ═══════════════════ 🌟

**Teaching People Ethical Mastery of Their Own Potential.**

[![Current News](https://img.shields.io/badge/📰-Current%20News-brightgreen)](README.md)
[![Archive Index](https://img.shields.io/badge/📚-Archive%20Index-blue)](README_ARCHIVE.md)
[![Tech Notes](https://img.shields.io/badge/💻-Tech%20Notes-orange)](README_TECH.md)
[![Sport News](https://img.shields.io/badge/⚽-Sport%20News-red)](README_SPORT.md)

</div>

---

> 💡 **General Principle:** *True consciousness begins with knowledge and skepticism.* 

---

"""

def archive_footer_for_month(year: int, month: int, count: int, start_str: str, end_str: str) -> str:
    return f"""
<div align="center">

## ✨ ✨ ✨

### 📰 [Back to Current News →](README.md)

### 📚 [View Archive Index →](README_ARCHIVE.md)

**Last Updated:** {datetime.now().strftime("%B %d, %Y")}  
*News from {start_str} — {end_str} ({count} entries)*

---

🌟 *"The furthest we will go, is limited only by the belief in what we can become."* 🌟

</div>
"""

def update_archive_index(archive_root: Path = Path(".")):
    """Rebuild README_ARCHIVE.md table from existing README_*.md files."""
    idx_path = archive_root / "README_ARCHIVE.md"
    # Find archive files README_2026_07.md etc
    arch_files = sorted(archive_root.glob("README_2*.md"))
    rows = []
    for p in arch_files:
        try:
            content = p.read_text(encoding="utf-8")
            entries = parse_entries(content, str(p))
            if not entries:
                continue
            # infer period from first/last entry dates
            dates = [parse_date(e.date_str) for e in entries]
            dates = [d for d in dates if d]
            if dates:
                dates_sorted = sorted(dates)
                period = f"{dates_sorted[0].strftime('%B %d')} — {dates_sorted[-1].strftime('%B %d, %Y')}"
            else:
                period = f"{len(entries)} entries"
            # month label
            m = re.search(r'README_(\d{4})_(\d{2})', p.name)
            if m:
                year, mon = int(m.group(1)), int(m.group(2))
                label = datetime(year, mon, 1).strftime("%B %Y")
            else:
                label = p.stem
            rows.append(f"| **{label}** | [{p.name}]({p.name}) | {period} |")
        except Exception:
            continue
    rows.sort(reverse=True)
    # Build file if exists, else template
    if idx_path.exists():
        orig = idx_path.read_text(encoding="utf-8")
        # replace table rows between "| Month |" header and "\n---"
        table = "| Month | File | Period |\n|-------|------|--------|\n" + "\n".join(rows) + "\n"
        if "| Month | File | Period |" in orig:
            new_content = re.sub(r'\| Month \| File \| Period \|.*?\n---', table + "\n---", orig, flags=re.DOTALL)
            idx_path.write_text(new_content, encoding="utf-8")
        else:
            # append
            pass
    return rows

def archive_entries(source_path: Path, entries_to_move: List[NewsEntry], archive_path: Optional[Path] = None, update_index: bool = True) -> dict:
    """Move entries_to_move from source_path to archive_path.
    If archive_path is None, auto-create README_YYYY_MM.md based on first entry month.
    Returns {"moved": int, "source_remaining": int, "archive_total": int, "archive_path": Path}
    """
    source_path = Path(source_path)
    content = source_path.read_text(encoding="utf-8")
    all_entries = parse_entries(content, str(source_path))

    # Build set of identities to move (by date_str+title)
    move_keys = {(e.date_str, e.title) for e in entries_to_move}
    remaining = [e for e in all_entries if (e.date_str, e.title) not in move_keys]
    moved = [e for e in all_entries if (e.date_str, e.title) in move_keys]

    if not moved:
        return {"moved": 0, "source_remaining": len(all_entries), "archive_total": 0, "archive_path": archive_path}

    # Determine archive_path if not given: use month of first moved entry
    if archive_path is None:
        dt = parse_date(moved[0].date_str)
        if dt:
            archive_path = source_path.parent / f"README_{dt.year}_{dt.strftime('%m')}.md"
        else:
            archive_path = source_path.parent / "README_ARCHIVE_MANUAL.md"

    # Load or create archive content
    if archive_path.exists():
        arch_content = archive_path.read_text(encoding="utf-8")
        arch_entries = parse_entries(arch_content, str(archive_path))
        # Merge: add moved, sort by date descending (newest first) — keep parser order? We'll sort
        arch_entries.extend(moved)
        # Deduplicate by key
        seen = set()
        deduped = []
        for e in arch_entries:
            k = (e.date_str, e.title)
            if k not in seen:
                seen.add(k)
                deduped.append(e)
        arch_entries = deduped
    else:
        arch_entries = moved
        # Create header
        dt = parse_date(moved[0].date_str) or datetime.now()
        arch_content = archive_header_for_month(dt.year, dt.month)
        arch_entries_header = arch_content
        # We'll write header + entries + footer later

    # Sort archive entries by date descending (best effort)
    def dt_key(e):
        d = parse_date(e.date_str)
        return d or datetime.min
    arch_entries_sorted = sorted(arch_entries, key=dt_key, reverse=True)

    # Write archive file
    if archive_path.exists():
        # Preserve existing header: everything before first entry
        orig_arch = archive_path.read_text(encoding="utf-8")
        lines = orig_arch.splitlines()
        first_h = None
        for i, l in enumerate(lines):
            if re.match(r'^#{1,2}\s+', l) and re.search(r'\b\d{4}\b', l):
                first_h = i
                break
        header = "\n".join(lines[:first_h]).strip() if first_h is not None else ""
        # If file was an archive with our template, header already good; else use template
        if not header or "<div align" not in header:
            dt0 = parse_date(arch_entries_sorted[0].date_str) or datetime.now()
            header = archive_header_for_month(dt0.year, dt0.month).strip()
        # Footer handling: detect existing footer div
        footer = ""
        if "<div align=\"center\">" in orig_arch and "Back to Current News" in orig_arch:
            last_div = orig_arch.rfind('<div align="center">')
            footer_candidate = orig_arch[last_div:].strip()
            if "Back to Current News" in footer_candidate:
                # we'll regenerate footer with new count/period
                pass
        # Build new archive
        parts = [header.strip()] if header else []
        for e in arch_entries_sorted:
            parts.append(e.to_markdown())
        # Generate new footer
        dates = [parse_date(e.date_str) for e in arch_entries_sorted if parse_date(e.date_str)]
        if dates:
            dmin, dmax = min(dates), max(dates)
            period_start = dmin.strftime("%B %d")
            period_end = dmax.strftime("%B %d, %Y")
            dtf = max(dates)
            footer = archive_footer_for_month(dtf.year, dtf.month, len(arch_entries_sorted), period_start, period_end)
        new_arch_content = "\n\n---\n\n".join(parts) + (footer if footer else "") + "\n"
        new_arch_content = normalize_file_content(new_arch_content)
        archive_path.write_text(new_arch_content, encoding="utf-8")
    else:
        # New file
        dt0 = parse_date(arch_entries_sorted[0].date_str) or datetime.now()
        header = archive_header_for_month(dt0.year, dt0.month).strip()
        dates = [parse_date(e.date_str) for e in arch_entries_sorted if parse_date(e.date_str)]
        footer = ""
        if dates:
            dmin, dmax = min(dates), max(dates)
            footer = archive_footer_for_month(dmax.year, dmax.month, len(arch_entries_sorted), dmin.strftime("%B %d"), dmax.strftime("%B %d, %Y"))
        parts = [header]
        for e in arch_entries_sorted:
            parts.append(e.to_markdown())
        new_arch_content = "\n\n---\n\n".join(parts) + footer + "\n"
        new_arch_content = normalize_file_content(new_arch_content)
        archive_path.write_text(new_arch_content, encoding="utf-8")

    # Write source file without moved entries (keep header/footer)
    # Reuse same header/footer logic as in editor's _write_entries_back
    lines = content.splitlines()
    first_h = None
    for i, l in enumerate(lines):
        if re.match(r'^#{1,2}\s+', l) and re.search(r'\b\d{4}\b', l) and re.search(r'[—–\-]', l):
            first_h = i
            break
    header_src = "\n".join(lines[:first_h]).strip() if first_h is not None else ""
    footer_src = ""
    if "<div align=\"center\">" in content and content.rstrip().endswith("</div>"):
        last_div = content.rfind('<div align="center">')
        if last_div != -1:
            cand = content[last_div:].strip()
            if "Back to Current News" not in cand and "Back to Main News" not in cand:
                footer_src = ""
            else:
                # Keep only if it's after last entry; for main README we normally don't have footer
                if first_h is not None and last_div > content.find(lines[first_h]):
                    footer_src = "\n\n" + cand
    parts_src = [header_src.strip()] if header_src else []
    for e in remaining:
        parts_src.append(e.to_markdown())
    new_src = "\n\n---\n\n".join(parts_src) + (footer_src if footer_src else "") + "\n"
    new_src = normalize_file_content(new_src)
    source_path.write_text(new_src, encoding="utf-8")

    if update_index:
        update_archive_index(source_path.parent)

    return {"moved": len(moved), "source_remaining": len(remaining), "archive_total": len(arch_entries_sorted), "archive_path": archive_path}

# CLI for testing / migration
if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="News parser / normalizer")
    ap.add_argument("--fix", action="store_true", help="Fix separators and headers in place")
    ap.add_argument("--check", action="store_true", help="Check and report issues")
    ap.add_argument("--stats", action="store_true", help="Show stats for all categories")
    ap.add_argument("files", nargs="*", help="Files to process (default: README.md README_TECH.md)")
    args = ap.parse_args()

    targets = args.files if args.files else ["README.md", "README_TECH.md"]
    if args.stats:
        data = parse_all(Path("."))
        for cat, v in data.items():
            if "entries" in v:
                print(f"{cat}: {len(v['entries'])} entries from {v['info']['path']}")
            elif "files" in v:
                print(f"{cat}: {len(v['files'])} detail files in {v['info']['path']}")

    if args.check:
        for fn in targets:
            if not Path(fn).exists():
                print(f"skip {fn} (not found)")
                continue
            content = Path(fn).read_text(encoding="utf-8")
            bad_seps = len(re.findall(r'^\s*-{2}\s*$', content, re.MULTILINE))  # exactly --
            total_seps = len(re.findall(r'^\s*-{2,}\s*$', content, re.MULTILINE))
            headers1 = len(re.findall(r'^# [^#]', content, re.MULTILINE))
            headers2 = len(re.findall(r'^## ', content, re.MULTILINE))
            print(f"{fn}: separators={total_seps} (bad --={bad_seps}), #={headers1} ##={headers2}")
            entries = parse_entries(content, source_file=fn)
            print(f"  parsed {len(entries)} entries")

    if args.fix:
        for fn in targets:
            if not Path(fn).exists():
                continue
            content = Path(fn).read_text(encoding="utf-8")
            fixed = normalize_file_content(content)
            if fixed != content:
                Path(fn).write_text(fixed, encoding="utf-8")
                print(f"fixed {fn}")
            else:
                print(f"no changes {fn}")
