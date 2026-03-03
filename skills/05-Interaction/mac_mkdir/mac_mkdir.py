#!/usr/bin/env python3
"""
mac_mkdir - 新建文件夹
"""

import sys
import os

def main():
    if len(sys.argv) < 2:
        print("用法: python3 mac_mkdir.py 目录名")
        sys.exit(1)
    
    path = os.path.expanduser(sys.argv[1])
    
    try:
        os.makedirs(path, exist_ok=True)
        print(f"✅ 已创建目录: {path}")
    except Exception as e:
        print(f"❌ 创建失败: {e}")

if __name__ == "__main__":
    main()
