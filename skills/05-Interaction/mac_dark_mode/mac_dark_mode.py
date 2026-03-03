#!/usr/bin/env python3
"""
mac_dark_mode - 切换深色/浅色模式
"""

import sys
import subprocess

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "toggle"
    
    if mode == "on":
        subprocess.run(["defaults", "write", "AppleInterfaceStyle", "Dark"])
        print("🌙 已切换到深色模式")
    elif mode == "off":
        subprocess.run(["defaults", "delete", "AppleInterfaceStyle"])
        print("☀️ 已切换到浅色模式")
    elif mode == "toggle":
        result = subprocess.run(["defaults", "read", "AppleInterfaceStyle"], capture_output=True, text=True)
        if "Dark" in result.stdout:
            subprocess.run(["defaults", "delete", "AppleInterfaceStyle"])
            print("☀️ 已切换到浅色模式")
        else:
            subprocess.run(["defaults", "write", "AppleInterfaceStyle", "Dark"])
            print("🌙 已切换到深色模式")
    else:
        print("用法: python3 mac_dark_mode.py [on|off|toggle]")

if __name__ == "__main__":
    main()
