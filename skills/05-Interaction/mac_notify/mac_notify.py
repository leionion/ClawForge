#!/usr/bin/env python3
"""
mac_notify - 发送系统通知
"""

import sys
import subprocess

def main():
    if len(sys.argv) < 2:
        print("用法: python3 mac_notify.py '标题' '内容'")
        sys.exit(1)
    
    title = sys.argv[1]
    content = sys.argv[2] if len(sys.argv) > 2 else ""
    
    script = f'display notification "{content}" with title "{title}"'
    subprocess.run(["osascript", "-e", script])
    print(f"✅ 已发送通知: {title}")

if __name__ == "__main__":
    main()
