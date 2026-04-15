---
name: mac-clipboard
description: "Reads the current Mac clipboard (pasteboard) contents to stdout or writes new text to the clipboard using pbcopy/pbpaste. Use when the user asks to copy, paste, read clipboard, write to clipboard, check pasteboard contents, or transfer text via the macOS clipboard."
---

# mac-clipboard — Clipboard Read/Write

Reads and writes macOS clipboard contents using `pbcopy` and `pbpaste`.

## Usage

```bash
# Read current clipboard contents
python3 mac_clipboard.py

# Write text to clipboard
python3 mac_clipboard.py "Hello, world!"

# Write with explicit -w flag
python3 mac_clipboard.py -w "text to copy"
```

## How it works

- **Read**: calls `pbpaste` and prints clipboard contents to stdout
- **Write**: pipes text to `pbcopy` via stdin

## Example output

```
📋 当前剪贴板内容:
Hello, world!
```

On successful write:
```
✅ 已写入剪贴板
```
