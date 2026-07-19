# RSYNC with Non-Default SSH Port

When your SSH server runs on a port other than 22 (the default), you need to tell rsync how to connect properly.

---

## The Problem

By default, rsync uses SSH on port 22:
```bash
rsync ./file user@host:/dest/    # Tries SSH on port 22
```

If your server uses port 2222 (or any other), this fails.

---

## Solutions

### Method 1: Inline Port with -e Option

```bash
rsync -e "ssh -p 2222" source/ user@host:/destination/
```

Or compact form:
```bash
rsync -e "ssh -p2222" source/ user@host:/dest/
```

### Method 2: Multiple SSH Options

Combine port with other SSH options:
```bash
rsync -e "ssh -p 2222 -i ~/.ssh/key -o StrictHostKeyChecking=no" source/ user@host:/dest/
```

### Method 3: SSH Config File (Recommended)

Edit `~/.ssh/config`:

```bash
Host myserver
    HostName 192.168.58.242
    User git
    Port 2222
    IdentityFile ~/.ssh/id_ed25519
```

Then use rsync normally:
```bash
rsync -avz ./myfile myserver:/path/to/repo/
```

### Method 4: Escape Sequences (Within Scripts)

From shell scripts, change colors dynamically:
```bash
echo -e "\e]10;#00ff00\a"  # Set foreground
echo -e "\e]11;#333333\a"  # Set background
```

---

## ⚠️ Common Mistake

Do NOT use `--port` for SSH:
```bash
rsync --port 2222  # ❌ WRONG - this sets rsync daemon port, not SSH!
```

The `--port` option only works with `rsync://` protocol, not SSH.

---

## Full Working Example

```bash
# Sync local project to git server on port 2222
rsync -avz --delete -e "ssh -p 2222" ./project/ git@192.168.58.242:/srv/git/repo/
```

**Options explained:**
- `-a` : Archive mode (preserves permissions, timestamps)
- `-v` : Verbose output
- `-z` : Compress during transfer
- `--delete` : Remove files on destination not present in source
- `-e "ssh -p 2222"` : Use SSH on custom port

---

## Verification

Test your SSH connection first:
```bash
ssh -p 2222 git@192.168.58.242
```

If SSH works, rsync will work too.

---

*2026.07.19 — Tech Notes*
