#!/usr/bin/env python3
"""
mac_print - 打开打印队列
"""

import subprocess

subprocess.run(["open", "-a", "Printer Setup Utility"])
print("✅ 已打开打印队列")
