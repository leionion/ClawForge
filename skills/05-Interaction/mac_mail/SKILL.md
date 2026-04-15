---
name: mac-mail
description: "Opens the macOS Mail application (Mail.app) using the open command. Use when the user asks to open email, launch Apple Mail, check mail, start Mail.app, or access the macOS email client."
---

# mac-mail — Open Mail Application

Opens the macOS built-in Mail application.

## Usage

```bash
python3 mac_mail.py
```

## How it works

Runs `open -a Mail` via `subprocess.run`, which launches Mail.app or brings it to the foreground if already running.

## Example output

```
✅ 已打开Mail
```
