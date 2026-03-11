# memory_backup - 内存备份与恢复

**功能**: 定时备份 Memory 聊天记录并支持恢复。满足 Demand #2: Scheduled Memory Backup and Restore。

**用法**:
```bash
# 手动备份 (可由 calendar/cron 定时触发)
python3 memory_backup.py backup [--source ~/.agent-memory] [--backup-dir ~/.agent-memory-backups] [--retention 10]

# 列出所有备份点
python3 memory_backup.py list [--backup-dir ~/.agent-memory-backups]

# 从指定备份恢复
python3 memory_backup.py restore --restore-from <path> [--restore-to ~/.agent-memory]
```

**参数**:
- `--source`: 内存数据源 (session-memory 默认 ~/.agent-memory)
- `--backup-dir`: 备份存放目录
- `--retention`: 保留最近 N 个备份 (0=全部保留)
- `--restore-from`: 要恢复的备份文件路径
- `--restore-to`: 恢复目标目录

**输出** (JSON):
- backup: `{status, path, retention}`
- list: `{backups: [{path, name, created}], count}`
- restore: `{status, restored_to}`

**与现有技能组合** (Related Skills):
- 数据: `session-memory` (读写) → 本技能备份/恢复
- 调度: `calendar` → 定时触发 backup
- 文件: `file-organizer` → 备份文件管理

**定时示例** (cron):
```
0 */6 * * * cd /path/to/skill && python3 memory_backup.py backup
```
