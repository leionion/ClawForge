#!/usr/bin/env python3
"""
mac_dictionary - 打开词典
"""

import subprocess

subprocess.run(["open", "-a", "Dictionary"])
print("✅ 已打开词典")
