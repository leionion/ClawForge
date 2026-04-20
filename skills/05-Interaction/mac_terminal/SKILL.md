---
name: mac-terminal
description: "Opens macOS Terminal.app and executes a shell command in a new or existing window, with optional automatic sudo password entry via System Events. Use when the user asks to open a terminal, run a shell command, execute a CLI command in Terminal, launch Terminal.app, or run something with sudo on macOS."
---

# mac-terminal — macOS Terminal Automation

Opens Terminal.app and executes shell commands via AppleScript, with optional automatic password entry for sudo commands.

## Usage

```bash
# Open Terminal and run a command
python3 mac_terminal.py "命令"

# Run a sudo command with automatic password entry (requires Accessibility permission)
python3 mac_terminal.py "sudo 命令" "密码"
```

## Examples

```bash
# Check version
python3 mac_terminal.py "openclaw-cn --version"

# Restart a service
python3 mac_terminal.py "openclaw-cn gateway restart"
```

## How it works

- Activates or opens Terminal.app via `osascript`
- Executes the command in the frontmost Terminal window (or creates a new one)
- If a password argument is provided, waits for the sudo prompt and types it via System Events keystroke simulation

## Requirements

- **macOS** with Terminal.app
- **Accessibility permission** required for automatic password entry (System Preferences > Privacy & Security > Accessibility)
