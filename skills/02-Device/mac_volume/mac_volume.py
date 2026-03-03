#!/usr/bin/env python3
"""
mac_volume - 音量调节
"""

import sys
import subprocess

def main():
    if len(sys.argv) < 2:
        # 获取当前音量
        result = subprocess.run(["osascript", "-e", "output volume of (get volume settings)"], capture_output=True, text=True)
        print(f"🔊 当前音量: {result.stdout.strip()}%")
        sys.exit(0)
    
    level = int(sys.argv[1])
    if 0 <= level <= 100:
        subprocess.run(["osascript", "-e", f"set volume output volume {level}"])
        print(f"✅ 音量已设置为: {level}%")
    else:
        print("请输入0-100之间的数字")

if __name__ == "__main__":
    main()
