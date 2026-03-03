#!/usr/bin/env python3
"""
Mac目录操作脚本 v1.0
功能：打开Finder并定位到指定目录

使用方式：
    python3 mac_finder.py "/路径/到/目录"
    python3 mac_finder.py "~/Desktop"
    python3 mac_finder.py "/Users/benson/Downloads"
"""

import os
import sys
import subprocess

def open_directory(path: str):
    """在Finder中打开指定目录"""
    
    # 展开~为实际用户目录
    path = os.path.expanduser(path)
    
    # 检查目录是否存在
    if not os.path.exists(path):
        return f"❌ 目录不存在: {path}"
    
    if not os.path.isdir(path):
        return f"❌ 不是有效目录: {path}"
    
    # 使用open命令在Finder中打开目录
    result = subprocess.run(["open", path], capture_output=True, text=True)
    
    # 激活Finder窗口让用户看到
    subprocess.run(["osascript", "-e", 'tell application "Finder" to activate'], capture_output=True)
    
    if result.returncode == 0:
        return f"✅ 已打开Finder窗口: {path}"
    else:
        return f"❌ 打开失败: {result.stderr}"

def list_common_dirs():
    """列出常用目录供用户选择"""
    home = os.path.expanduser("~")
    dirs = {
        "桌面": f"{home}/Desktop",
        "下载": f"{home}/Downloads",
        "文档": f"{home}/Documents",
        "图片": f"{home}/Pictures",
        "音乐": f"{home}/Music",
        "影片": f"{home}/Movies",
        "应用程序": "/Applications",
        "用户目录": home,
    }
    return dirs

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\n常用目录:")
        for name, path in list_common_dirs().items():
            print(f"  {name}: {path}")
        print("\n示例:")
        print('  python3 mac_finder.py "~/Desktop"')
        print('  python3 mac_finder.py "/Users/benson/Downloads"')
        sys.exit(1)
    
    path = sys.argv[1]
    result = open_directory(path)
    print(result)

if __name__ == "__main__":
    main()
