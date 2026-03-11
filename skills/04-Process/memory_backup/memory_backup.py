#!/usr/bin/env python3
"""
memory_backup - 内存备份与恢复 Meta Skill
Scheduled backup for Memory chat records with restore capability.
Composable with session-memory (data), file-organizer (files), calendar (schedule).
"""

import argparse
import json
import os
import shutil
import sys
import tarfile
import tempfile
from datetime import datetime
from pathlib import Path


def _expand(path: str) -> Path:
    return Path(os.path.expanduser(path)).resolve()


def backup(source: Path, dest_dir: Path, retention: int) -> dict:
    """Backup source (file or dir) to dest_dir. Apply retention policy."""
    if not source.exists():
        return {"error": f"Source not found: {source}"}

    dest_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    name = f"memory_backup_{timestamp}"
    archive_path = dest_dir / f"{name}.tar.gz"
    arcname = source.name if source.name else "memory"

    with tarfile.open(archive_path, "w:gz") as tf:
        tf.add(source, arcname=arcname)

    # Retention: keep only N most recent
    if retention > 0:
        backups = sorted(dest_dir.glob("memory_backup_*.tar.gz"), key=os.path.getmtime, reverse=True)
        for old in backups[retention:]:
            old.unlink()

    return {"status": "ok", "path": str(archive_path), "retention": retention}


def list_backups(backup_dir: Path) -> dict:
    """List all backup points with date/time."""
    if not backup_dir.exists():
        return {"backups": [], "count": 0}

    backups = []
    for f in sorted(backup_dir.glob("memory_backup_*.tar.gz"), key=os.path.getmtime, reverse=True):
        mtime = datetime.fromtimestamp(os.path.getmtime(f))
        backups.append({"path": str(f), "name": f.name, "created": mtime.isoformat()})

    return {"backups": backups, "count": len(backups)}


def restore(backup_path: Path, dest: Path) -> dict:
    """Restore from backup to dest directory."""
    if not backup_path.exists():
        return {"error": f"Backup not found: {backup_path}"}

    with tempfile.TemporaryDirectory() as tmp:
        with tarfile.open(backup_path, "r:gz") as tf:
            tf.extractall(tmp)
        items = list(Path(tmp).iterdir())
        if len(items) == 1 and items[0].is_dir():
            src = items[0]
            dest.parent.mkdir(parents=True, exist_ok=True)
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(src, dest)
        else:
            dest.mkdir(parents=True, exist_ok=True)
            for child in items:
                dst = dest / child.name
                if dst.exists():
                    shutil.rmtree(dst) if dst.is_dir() else dst.unlink()
                if child.is_file():
                    shutil.copy2(str(child), dst)
                else:
                    shutil.copytree(str(child), dst)

    return {"status": "ok", "restored_to": str(dest)}


def main():
    parser = argparse.ArgumentParser(description="memory_backup - Scheduled Memory Backup and Restore")
    parser.add_argument("action", choices=["backup", "list", "restore"], help="Action to perform")
    parser.add_argument("--source", default="~/.agent-memory", help="Memory source (file or dir)")
    parser.add_argument("--backup-dir", default="~/.agent-memory-backups", help="Backup directory")
    parser.add_argument("--restore-from", help="Backup path to restore from (for restore action)")
    parser.add_argument("--restore-to", default="~/.agent-memory", help="Destination for restore")
    parser.add_argument("--retention", type=int, default=10, help="Keep N recent backups (0=keep all)")
    parser.add_argument("--output", choices=["json", "print"], default="json")
    args = parser.parse_args()

    source = _expand(args.source)
    backup_dir = _expand(args.backup_dir)

    if args.action == "backup":
        result = backup(source, backup_dir, args.retention)
    elif args.action == "list":
        result = list_backups(backup_dir)
    else:  # restore
        if not args.restore_from:
            result = {"error": "--restore-from required for restore"}
        else:
            result = restore(_expand(args.restore_from), _expand(args.restore_to))

    if args.output == "print":
        if "error" in result:
            print(f"❌ {result['error']}")
            sys.exit(1)
        if args.action == "backup":
            print(f"✅ Backed up to {result['path']}")
        elif args.action == "list":
            for b in result.get("backups", []):
                print(f"  {b['name']} — {b['created']}")
        elif args.action == "restore":
            print(f"✅ Restored to {result['restored_to']}")
    else:
        print(json.dumps(result, indent=2))

    if "error" in result:
        sys.exit(1)


if __name__ == "__main__":
    main()
