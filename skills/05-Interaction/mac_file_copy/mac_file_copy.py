#!/usr/bin/env python3
"""
mac_file_copy - 复制文件
"""

import sys
import shutil
import os

def main():
    if len(sys.argv) < 3:
        print("用法: python3 mac_file_copy.py 源文件 目标路径")
        sys.exit(1)
    
    src = os.path.expanduser(sys.argv[1])
    dst = os.path.expanduser(sys.argv[2])
    
    try:
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)
        print(f"✅ 已复制: {src} -> {dst}")
    except Exception as e:
        print(f"❌ 复制失败: {e}")

if __name__ == "__main__":
    main()
