---
name: memory-backup
description: "Creates scheduled tar.gz backups of agent memory or chat history, lists existing backup snapshots, and restores from a previous backup point with automatic retention policy. Use when the user asks to back up, export, save, snapshot, or restore chat history, conversation logs, agent memory, or session data."
---

# memory-backup — Agent Memory Backup & Restore

Creates compressed backups of agent memory/chat history and restores from previous snapshots. Supports configurable retention policies and scheduled execution via cron.

## Usage

```bash
# Back up agent memory (default source: ~/.agent-memory)
python3 memory_backup.py backup

# Back up a custom source with retention of 5 snapshots
python3 memory_backup.py backup --source ~/my-memory --retention 5

# List all available backup points
python3 memory_backup.py list

# Restore from a specific backup
python3 memory_backup.py restore --restore-from ~/.agent-memory-backups/memory_backup_20240115_120000.tar.gz
```

## Parameters

| Flag | Default | Description |
|------|---------|-------------|
| `--source` | `~/.agent-memory` | Memory source directory or file |
| `--backup-dir` | `~/.agent-memory-backups` | Where backups are stored |
| `--retention` | `10` | Keep N most recent backups (0 = keep all) |
| `--restore-from` | — | Backup file path (required for restore) |
| `--restore-to` | `~/.agent-memory` | Restore destination |
| `--output` | `json` | Output format (`json` or `print`) |

## Output examples

**Backup:**
```json
{"status": "ok", "path": "/Users/you/.agent-memory-backups/memory_backup_20240115_120000.tar.gz", "retention": 10}
```

**List:**
```json
{"backups": [{"path": "...", "name": "memory_backup_20240115_120000.tar.gz", "created": "2024-01-15T12:00:00"}], "count": 1}
```

**Restore:**
```json
{"status": "ok", "restored_to": "/Users/you/.agent-memory"}
```

## Scheduled backups (cron)

```cron
0 */6 * * * cd /path/to/skill && python3 memory_backup.py backup
```

## Error handling

- **Source not found**: returns `{"error": "Source not found: <path>"}`
- **Missing --restore-from**: returns `{"error": "--restore-from required for restore"}`
- **Restore overwrites destination**: existing files at restore target are replaced — back up first if uncertain

## Related skills

- **session-memory**: the data source this skill backs up
- **calendar**: trigger scheduled backups
- **file-organizer**: manage backup files
