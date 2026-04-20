---
name: mac-dark-mode
description: "Toggles macOS dark mode on, off, or auto-toggle by reading and writing the AppleInterfaceStyle user default. Use when the user asks to enable dark mode, disable dark mode, switch to light mode, toggle appearance, or change the macOS theme."
---

# mac-dark-mode — Toggle macOS Dark/Light Mode

Switches macOS between dark and light appearance modes using `defaults` commands.

## Usage

```bash
# Toggle between dark and light mode
python3 mac_dark_mode.py

# Enable dark mode
python3 mac_dark_mode.py on

# Enable light mode
python3 mac_dark_mode.py off
```

## How it works

- Reads `AppleInterfaceStyle` via `defaults read` to detect current mode
- Writes or deletes `AppleInterfaceStyle` to switch modes
- No argument toggles automatically based on current state
