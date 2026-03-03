#!/usr/bin/env python3
"""
mac_file_move - 移动文件
"""

import sys
import shutil
import os

def main():
    if len(sys.argv) < 3:
        print("用法: python3 mac_file_move.py 源 目标")
        sys.exit(1)
    
    src = os.path.expanduser(sys.argv[1])
    dst = os.path.expanduser(sys.argv[2])
    
    try:
        shutil.move(src, dst)
        print(f"✅ 已移动: {src} -> {dst}")
    except Exception as e:
        print(f"❌ 移动失败: {e}")

if __name__ == "__main__":
    main()
