#!/usr/bin/env python3
"""
mac_empty_trash - 清空回收站
"""

import subprocess

confirm = input("确定要清空回收站吗? (y/n): ")
if confirm.lower() == 'y':
    subprocess.run(["rm", "-rf", "~/.Trash/*"])
    print("✅ 回收站已清空")
else:
    print("已取消")
