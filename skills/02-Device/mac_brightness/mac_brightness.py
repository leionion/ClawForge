#!/usr/bin/env python3
"""
mac_brightness - 屏幕亮度调节
注意: 需要安装 brightness 命令 (brew install brightness)
"""

import sys
import subprocess

def main():
    # 尝试使用AppleScript（需要第三方工具）
    # 或使用系统内置 brightness
    if len(sys.argv) < 2:
        print("用法: python3 mac_brightness.py 0.5")
        print("注意: 需要安装 brightness 工具 (brew install brightness)")
        sys.exit(0)
    
    level = float(sys.argv[1])
    if 0 <= level <= 1:
        result = subprocess.run(["brightness", str(level)], capture_output=True)
        if result.returncode == 0:
            print(f"✅ 亮度已设置为: {int(level*100)}%")
        else:
            print("❌ 请先安装: brew install brightness")
    else:
        print("请输入0-1之间的数字")

if __name__ == "__main__":
    main()
