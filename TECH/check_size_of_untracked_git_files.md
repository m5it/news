# How to Check the Size of Untracked Git Files

## The Problem

You want to know how much disk space your **untracked files** are using before deciding whether to commit, ignore, or delete them.

## The Solution

```bash
git ls-files --others --exclude-standard -z | xargs -0 du -sm | awk '{sum+=$1} END {print "Total:", sum, "MB"}'
```

## What Each Part Does

| Command Part | Purpose |
|--------------|---------|
| `git ls-files --others` | List files that Git is **not tracking** |
| `--exclude-standard` | Respect `.gitignore` — skip ignored files |
| `-z` | Output null-separated filenames (safe for spaces/special chars) |
| `xargs -0` | Read null-separated input |
| `du -sm` | Show size of each file in **megabytes** |
| `awk '{sum+=$1} END {print "Total:", sum, "MB"}'` | Sum the first column and print total |

## Why This Command Is Reliable

- ✅ Only counts **untracked files**
- ✅ Ignores files listed in `.gitignore`
- ✅ Handles filenames with spaces
- ✅ Uses `-sm` so units are consistent (megabytes), not mixed like `du -sh`

## Common Mistake

Do **not** use `du -sh` with awk sum:

```bash
# BAD — mixes units (K, M, G) and gives wrong total
git ls-files --others --exclude-standard -z | xargs -0 du -sh | awk '{sum+=$1} END {print "Total:", sum}'
```

`du -sh` outputs human-readable sizes like `1.2M`, `500K`, `3.4G`. `awk` only sees the number, not the unit, so the total is meaningless.

## Variations

### Total in bytes, then convert to MB precisely

```bash
git ls-files --others --exclude-standard -z | xargs -0 du -sb | awk '{sum+=$1} END {printf "%.2f MB\n", sum/1024/1024}'
```

### List each untracked file with its size

```bash
git ls-files --others --exclude-standard -z | xargs -0 du -sh
```

### Include modified tracked files too

```bash
{
  git diff --name-only -z
  git ls-files --others --exclude-standard -z
} | xargs -0 du -sm | awk '{sum+=$1} END {print "Total:", sum, "MB"}'
```

### Find the biggest untracked files

```bash
git ls-files --others --exclude-standard -z | xargs -0 du -sm | sort -nr | head -20
```

## Real-World Example

If you have directories like:

```
space/hf_cache/
space/qwen25_ft/
space/qwen_ft/hf_train/
space/thinking_dataset/
```

The command will expand them and report the total size of every untracked file inside.

## Key Insight

**Use `du -sm`, not `du -sh`, when summing sizes.** Consistent units are the only way to get a correct total.

## See Also

- [vLLM: Can It Load .pt Files?](vllm_loading_models_pt_safetensors_gguf.md)
- [Qwen2.5-Coder 7B AIIA v2 — Thinking Support](qwen25_coder_aiia_v2_thinking.md)
- [Finding Memory Hogs on Linux](finding_memory_hogs_on_linux.md)
