#!/usr/bin/env python3
"""
mac_restart - 重启Mac
"""

import subprocess
import sys

confirm = input("确定要重启Mac吗? (y/n): ")
if confirm.lower() == 'y':
    subprocess.run(["sudo", "shutdown", "-r", "now"])
    print("✅ Mac正在重启...")
else:
    print("已取消")
