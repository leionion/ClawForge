#!/usr/bin/env python3
"""
mac_eject - 弹出光盘/存储设备
"""

import subprocess

def main():
    # 列出可弹出设备
    result = subprocess.run(["diskutil", "list"], capture_output=True, text=True)
    print("可用存储设备:")
    print(result.stdout)
    
    if len(result.stdout.split()) < 5:
        print("未找到可弹出设备")
        return
    
    # 尝试弹出所有可弹出设备
    subprocess.run(["drutil", "eject"])
    print("✅ 已尝试弹出设备")

if __name__ == "__main__":
    main()
