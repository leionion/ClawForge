#!/usr/bin/env python3
"""
mac_mail - 打开Mail应用
"""

import subprocess

subprocess.run(["open", "-a", "Mail"])
print("✅ 已打开Mail")
