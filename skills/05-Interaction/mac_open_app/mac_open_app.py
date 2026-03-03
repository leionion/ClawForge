#!/usr/bin/env python3
"""
mac_open_app - 打开Mac应用
"""

import sys
import subprocess

def main():
    if len(sys.argv) < 2:
        print("用法: python3 mac_open_app.py '应用名称'")
        print("示例: python3 mac_open_app.py 'Safari'")
        sys.exit(1)
    
    app = sys.argv[1]
    subprocess.run(["open", "-a", app])
    print(f"✅ 已打开: {app}")

if __name__ == "__main__":
    main()
