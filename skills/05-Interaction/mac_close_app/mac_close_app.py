#!/usr/bin/env python3
"""
mac_close_app - 关闭Mac应用
"""

import sys
import subprocess

def main():
    if len(sys.argv) < 2:
        print("用法: python3 mac_close_app.py '应用名称'")
        sys.exit(1)
    
    app = sys.argv[1]
    subprocess.run(["osascript", "-e", f'tell app "{app}" to quit'])
    print(f"✅ 已关闭: {app}")

if __name__ == "__main__":
    main()
