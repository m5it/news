# Rsync with SSH Key and Custom Port

## Basic Syntax

```bash
rsync -avz -e "ssh -p PORT -i /path/to/private_key" /source/ user@host:/destination/
```

## Examples

### Example 1: Custom port (2222) with specific SSH key
```bash
rsync -avz -e "ssh -p 2222 -i ~/.ssh/id_rsa_custom" /home/t3ch/data/ t3ch@192.168.1.100:/home/t3ch/backup/
```

### Example 2: With progress bar
```bash
rsync -avz --progress -e "ssh -p 2222 -i ~/.ssh/my_key" /local/path/ user@host:/remote/path/
```

### Example 3: Dry run (test without copying)
```bash
rsync -avzn -e "ssh -p 2222 -i ~/.ssh/my_key" /local/path/ user@host:/remote/path/
```
> **Note:** The `-n` flag means dry run - no files are actually transferred.

### Example 4: SSH key with passphrase
If your key has a passphrase and you want to avoid typing it repeatedly:
```bash
eval $(ssh-agent)
ssh-add ~/.ssh/my_key
rsync -avz -e "ssh -p 2222" /local/path/ user@host:/remote/path/
```

## Flag Breakdown

| Flag | Description |
|------|-------------|
| `-a` | Archive mode (permissions, symlinks, etc.) |
| `-v` | Verbose output |
| `-z` | Compress during transfer |
| `-e "ssh ..."` | Specify SSH command with options |
| `-p PORT` | SSH port number |
| `-i KEY` | SSH private key file path |
| `-n` | Dry run (no actual transfer) |
| `--progress` | Show progress bar |

## Troubleshooting

### Permission denied (publickey)
- Check key permissions: `chmod 600 ~/.ssh/my_key`
- Verify key is added: `ssh-add -l`

### Connection refused
- Verify port is correct: `ssh -p PORT user@host` (test first)
- Check firewall rules on destination

### Rsync not found on remote
- Install rsync on destination: `sudo apt install rsync`

## See Also
- [SSH Key Management](../DEFAULT/SSH_KEYS.md)
- [Port Forwarding](../DEFAULT/PORT_FORWARD.md)
