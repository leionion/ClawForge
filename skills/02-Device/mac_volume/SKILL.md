---
name: mac-volume
description: "Gets or sets the macOS system output volume (0–100) using osascript. Use when the user asks to check the volume, change the volume, turn volume up or down, mute, set audio level, or adjust sound output on macOS."
---

# mac-volume — macOS Volume Control

Reads the current system volume or sets it to a specific level (0–100) using `osascript`.

## Usage

```bash
# Check current volume
python3 mac_volume.py

# Set volume to 50%
python3 mac_volume.py 50

# Mute (set to 0)
python3 mac_volume.py 0

# Max volume
python3 mac_volume.py 100
```

## How it works

- **Read**: runs `osascript -e "output volume of (get volume settings)"` to get current level
- **Write**: runs `osascript -e "set volume output volume <level>"` to set the level
- Accepts integer values from 0 to 100
