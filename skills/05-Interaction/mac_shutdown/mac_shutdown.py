#!/usr/bin/env python3
"""
mac_shutdown - 关机Mac
"""

import subprocess

confirm = input("确定要关机吗? (y/n): ")
if confirm.lower() == 'y':
    subprocess.run(["sudo", "shutdown", "-h", "now"])
    print("✅ Mac正在关机...")
else:
    print("已取消")
