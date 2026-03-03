#!/usr/bin/env python3
"""
mac_file_delete - 删除文件
"""

import sys
import os
import shutil

def main():
    if len(sys.argv) < 2:
        print("用法: python3 mac_file_delete.py 文件/目录")
        sys.exit(1)
    
    path = os.path.expanduser(sys.argv[1])
    
    if not os.path.exists(path):
        print(f"❌ 文件不存在: {path}")
        sys.exit(1)
    
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
        print(f"✅ 已删除: {path}")
    except Exception as e:
        print(f"❌ 删除失败: {e}")

if __name__ == "__main__":
    main()
