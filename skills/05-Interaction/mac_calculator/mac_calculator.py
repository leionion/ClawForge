#!/usr/bin/env python3
"""
mac_calculator - 打开计算器
"""

import subprocess

subprocess.run(["open", "-a", "Calculator"])
print("✅ 已打开计算器")
