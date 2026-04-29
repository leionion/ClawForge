---
name: mac-activate
description: "Brings a specified macOS application to the foreground using osascript, making its window visible and focused. Use when the user asks to switch to an app, bring an app to front, activate an application, focus a window, or show a running app on macOS."
---

# mac-activate — Bring an App to the Foreground

Activates a specified macOS application and brings its window to the front using AppleScript.

## Usage

```bash
python3 mac_activate.py "Finder"
python3 mac_activate.py "Terminal"
python3 mac_activate.py "Safari"
python3 mac_activate.py "Google Chrome"
```

## How it works

- Sends `tell application "<name>" to activate` via `osascript`
- Can also list currently running (non-background) apps via System Events

## Requirements

- **macOS** with `osascript` (pre-installed)
