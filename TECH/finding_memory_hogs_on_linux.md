# Finding What Uses a Lot of Memory on Linux

## The Problem

Sometimes your system slows down, starts swapping, or an OOM (Out Of Memory) killer terminates processes. You need to find what's eating RAM.

## Quick Commands

### 1. `free` — Total Memory Overview

```bash
free -h
```

Shows total, used, free, shared, buffers/cache, and swap.

### 2. `htop` — Interactive Process Viewer

```bash
htop
```

- Sort by memory: press `F6` → select `MEMORY`
- Kill processes: press `F9`
- Search: press `F3`

### 3. `top` — Classic Process Monitor

```bash
top -o %MEM
```

### 4. `ps` — Fast Command-Line List

```bash
ps aux --sort=-%mem | head -20
```

Shows top 20 memory-consuming processes.

### 5. `smem` — Most Accurate Memory Reporting

```bash
sudo smem -r -c "pid user command rss pss uss" | head -20
```

- **RSS** — Resident Set Size
- **PSS** — Proportional Set Size (accounts for shared memory)
- **USS** — Unique Set Size (memory only this process uses)

## GPU / VRAM

### NVIDIA

```bash
nvidia-smi
```

Watch continuously:

```bash
watch -n 1 nvidia-smi
```

### AMD

```bash
rocm-smi
```

### Intel

```bash
intel_gpu_top
```

## My Favorite Combo

```bash
# RAM hogs
ps aux --sort=-%mem | head -10

# GPU hogs
nvidia-smi
```

## When to Use What

| Situation | Tool |
|-----------|------|
| Quick total overview | `free -h` |
| Interactive exploration | `htop` |
| Scripting / logging | `ps` |
| Accurate shared memory | `smem` |
| GPU memory | `nvidia-smi` |

## Pro Tip

If a process keeps growing over time, it's likely a **memory leak**. Use:

```bash
watch -n 5 'ps aux --sort=-%mem | head -10'
```

This refreshes every 5 seconds so you can spot the culprit.

## See Also

- [AIIA v1 — First Published Model](aiia_v1_first_published_model.md)
- [Training Llama 3.2 & Kimi K3](training_llama32_and_kimi_k3_with_aiia_datasets.md)
