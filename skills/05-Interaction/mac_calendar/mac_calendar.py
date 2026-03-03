#!/usr/bin/env python3
"""
mac_calendar - 打开日历
"""

import subprocess

subprocess.run(["open", "-a", "Calendar"])
print("✅ 已打开日历")
