#!/usr/bin/env python3
"""
mac_screenshot - Mac截屏
"""

import subprocess
import os
import datetime

desktop = os.path.expanduser("~/Desktop")
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"screenshot_{timestamp}.png"
filepath = os.path.join(desktop, filename)

subprocess.run(["/usr/sbin/screencapture", filepath])
print(f"✅ 截屏已保存: {filename}")
