#!/usr/bin/env python3
"""
mac_ip - 查看IP地址
"""

import subprocess

# 内网IP
result = subprocess.run(["ipconfig", "getifaddr", "en0"], capture_output=True, text=True)
internal = result.stdout.strip()

# 外网IP
external = subprocess.run(["curl", "-s", "ifconfig.me"], capture_output=True, text=True).stdout.strip()

print(f"🌐 内网IP: {internal}")
print(f"🌍 外网IP: {external}")
