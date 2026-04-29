---
name: mac-finder
description: "Opens macOS Finder at a specified directory path, with tilde expansion and common-directory shortcuts. Use when the user asks to open a folder, navigate to a directory, browse files, show a path in Finder, or open Downloads/Desktop/Documents on macOS."
---

# mac-finder — Open Finder at a Directory

Opens Finder and navigates to a specified directory path. Supports `~` expansion and validates that the path exists before opening.

## Usage

```bash
# Open a specific directory in Finder
python3 mac_finder.py "~/Downloads"
python3 mac_finder.py "/Users/benson/Desktop"
python3 mac_finder.py "/Applications"
```

## Common directories

| Name | Path |
|------|------|
| Desktop | ~/Desktop |
| Downloads | ~/Downloads |
| Documents | ~/Documents |
| Pictures | ~/Pictures |
| Music | ~/Music |
| Movies | ~/Movies |
| Applications | /Applications |

## How it works

- Expands `~` to the user's home directory via `os.path.expanduser`
- Validates that the path exists and is a directory
- Opens the directory with `open` and activates Finder via `osascript`
