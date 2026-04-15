---
name: mac-brightness
description: "Adjusts Mac screen brightness by setting a specific level (0–1), increasing, or decreasing display brightness via the brightness CLI tool. Use when the user asks to change, dim, brighten, increase, decrease, or check macOS display brightness or backlight level."
---

# mac-brightness — Screen Brightness Control

Adjusts Mac screen brightness using the `brightness` CLI tool (installed via Homebrew).

## Prerequisites

```bash
brew install brightness
```

## Usage

```bash
# Set brightness to 50%
python3 mac_brightness.py 0.5

# Set brightness to max
python3 mac_brightness.py 1.0

# Set brightness to minimum (not off)
python3 mac_brightness.py 0.1
```

The `level` argument accepts a float between `0` (off) and `1` (full brightness).

## How it works

The script calls the `brightness` CLI tool via `subprocess.run(["brightness", level])`. If the tool is not installed, it prints an error prompting `brew install brightness`.

## Error handling

- **Missing tool**: prints `❌ 请先安装: brew install brightness` — install with `brew install brightness`
- **Out of range**: values outside 0–1 are rejected with a message
