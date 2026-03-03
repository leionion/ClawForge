#!/usr/bin/env python3
"""
mac_activate - Mac应用激活脚本
功能：将指定应用激活到前台，让用户能看到

使用方式：
    python3 mac_activate.py "Finder"
    python3 mac_activate.py "Terminal"
    python3 mac_activate.py "Google Chrome"
"""

import os
import sys
import subprocess

def activate_app(app_name: str):
    """激活指定应用到前台"""
    
    # 使用osascript激活应用
    script = f'tell application "{app_name}" to activate'
    result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    
    if result.returncode == 0:
        return f"✅ 已激活: {app_name}"
    else:
        return f"❌ 激活失败: {result.stderr}"

def list_running_apps():
    """列出正在运行的应用"""
    script = '''
    tell application "System Events"
        set appList to name of every process whose background only is false
        return appList
    end tell
    '''
    result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    if result.returncode == 0:
        apps = [a.strip() for a in result.stdout.split(', ')]
        return apps
    return []

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\n用法示例:")
        print('  python3 mac_activate.py "Finder"')
        print('  python3 mac_activate.py "Terminal"')
        print('  python3 mac_activate.py "Safari"')
        print("\n当前运行中的应用:")
        for app in list_running_apps()[:10]:
            print(f"  - {app}")
        sys.exit(1)
    
    app_name = sys.argv[1]
    result = activate_app(app_name)
    print(result)

if __name__ == "__main__":
    main()
