---
name: metaskillbase
slug: metaskillbase
version: 1.0.0
author: metaskillbase
description: Decompose human demands into atomic meta skills using OpenClaw Skill Forge Cutter. Run standalone skills (memory_backup, strategy_backtest) or orchestrate OpenClaw skills.
tags: [decomposition, meta-skills, demand-routing, cutter, backtest, memory-backup]
---

# OpenClaw Skill Forge — Demand Decomposition for OpenClaw

When a user describes what they want in natural language, use OpenClaw Skill Forge to decompose the demand into atomic meta skills, then execute or hand off.

## When to Use

- User says: "backup my chat memory", "run a backtest on my data", "organize my files"
- Multi-step or ambiguous demands that need skill mapping
- Before executing—decompose first to route correctly

## How It Works

1. **Decompose**: Call OpenClaw Skill Forge Cutter with the user's demand.
2. **Skills returned**: e.g. `memory_backup`, `strategy_backtest`, `file_copy`, etc.
3. **Runnable standalone**: `memory_backup`, `strategy_backtest` run via `metaskill` CLI.
4. **Needs OpenClaw**: Mac HCI, device, other skills—use OpenClaw's native skills.

## Usage

### CLI (recommended)

```bash
# Install: pip install -e /path/to/ClawForge
metaskill "backup my chat memory"
metaskill "run backtest on trading data" --decompose-only
metaskill --list
```

### Python API

```python
from core.cutter import CutterEngine
result = CutterEngine().process("backup my chat memory")
# result["decomposed"] → [{"skill": "memory_backup", "confidence": 0.8, ...}]
```

### LLM Decomposition (optional)

Set `CHUTES_API_KEY` in .env and use `--model chutes` for smarter decomposition.

## Cutter Keywords

| Demand phrase | Skill |
|---------------|-------|
| backup my, chat memory, memory backup | memory_backup |
| backtest, trading strategy, quantitative | strategy_backtest |
| file copy, move, delete | file_copy, file_move, file_delete |
| open app, close app | open_app, close_app |
| screenshot, brightness, volume | screenshot, brightness, volume |
| ... see Skill-Index.md |

## Installation

```bash
cd ClawForge
pip install -e .

# Install into OpenClaw workspace (or run ./scripts/setup_openclaw.sh)
cp -r openclaw-skill ~/.openclaw/workspace/skills/metaskillbase
```

## Permissions

- **filesystem**: For memory_backup, strategy_backtest (read/write CSVs, backups)
- **network**: Optional for strategy_backtest (data fetch), GPT decomposition
- **shell**: Run metaskill CLI from OpenClaw
