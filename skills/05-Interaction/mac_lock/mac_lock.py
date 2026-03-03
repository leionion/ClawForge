#!/usr/bin/env python3
"""
mac_lock - 锁定Mac屏幕
"""

import subprocess

subprocess.run(["pmset", "displaysleepnow"])
print("✅ 屏幕已锁定")
