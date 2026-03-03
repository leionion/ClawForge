#!/usr/bin/env python3
"""
mac_clipboard - 剪贴板操作
"""

import sys
import subprocess

def read_clipboard():
    result = subprocess.run(["pbpaste"], capture_output=True, text=True)
    return result.stdout

def write_clipboard(text):
    process = subprocess.Popen(["pbcopy"], stdin=subprocess.PIPE)
    process.communicate(text.encode())

def main():
    if len(sys.argv) < 2:
        # 读取剪贴板
        content = read_clipboard()
        print(f"📋 当前剪贴板内容:\n{content}")
    elif sys.argv[1] == "-w" and len(sys.argv) > 2:
        # 写入剪贴板
        write_clipboard(sys.argv[2])
        print("✅ 已写入剪贴板")
    else:
        content = " ".join(sys.argv[1:])
        write_clipboard(content)
        print("✅ 已写入剪贴板")

if __name__ == "__main__":
    main()
