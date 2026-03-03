#!/usr/bin/env python3
"""
mac_input_source - 切换输入法
"""

import sys
import subprocess

def main():
    # 列出当前输入法
    result = subprocess.run([
        "osascript", "-e", 
        'tell app "System Events" to get name of every item of (get value of attribute "AXFocusedUIElement" of application process "System Events")'
    ], capture_output=True, text=True)
    
    # 使用快捷键切换输入法
    subprocess.run(["osascript", "-e", 'tell app "System Events" to key code 49 using {control down, option down}'])
    print("✅ 已切换输入法")

if __name__ == "__main__":
    main()
