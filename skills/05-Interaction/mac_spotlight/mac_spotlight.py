#!/usr/bin/env python3
"""
mac_spotlight - 打开聚焦搜索
"""

import subprocess

subprocess.run(["open", "-a", "Spotlight"])
print("✅ 已打开聚焦搜索")
