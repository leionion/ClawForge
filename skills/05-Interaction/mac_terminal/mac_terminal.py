#!/usr/bin/env python3
"""
Mac终端自动化脚本 v1.3
功能：
1. 打开Terminal.app
2. 执行命令并保持交互
3. 检测密码提示并自动输入（可选）

使用方式：
    python terminal_automation.py "命令" [密码]
"""

import os
import sys
import time
import subprocess
import re
import threading

def open_terminal():
    """打开Terminal.app并激活"""
    # 检查是否已有Terminal在运行
    script = '''
    tell application "Terminal"
        activate
        if (count of windows) is 0 then
            do script ""
        end if
    end tell
    '''
    subprocess.run(["osascript", "-e", script])
    time.sleep(0.3)
    return "Terminal已激活"

def run_command(command: str, password: str = None):
    """在Terminal中执行命令"""
    
    # 转义命令中的引号
    escaped_command = command.replace('"', '\\"')
    
    # 使用AppleScript执行命令（复用已有窗口或创建新窗口）
    script = f'''
    tell application "Terminal"
        activate
        if (count of windows) > 0 then
            do script "{escaped_command}" in front window
        else
            do script "{escaped_command}"
        end if
    end tell
    '''
    
    try:
        subprocess.run(["osascript", "-e", script], timeout=3, capture_output=True)
    except subprocess.TimeoutExpired:
        pass  # 超时是正常的，命令在终端中执行
    
    # 如果提供了密码，尝试自动输入
    if password:
        # 等待密码提示出现
        time.sleep(1.5)
        try_auto_type_password(password)
    
    return f"命令已发送: {command}"

def try_auto_type_password(password: str):
    """尝试自动输入密码（需要辅助功能权限）"""
    try:
        # 使用System Events模拟按键
        # 先输入密码
        subprocess.run([
            "osascript", "-e", 
            f'tell app "System Events" to keystroke "{password}"'
        ], timeout=2)
        # 回车
        subprocess.run([
            "osascript", "-e", 
            'tell app "System Events" to keystroke return'
        ], timeout=2)
        print("密码已自动输入")
    except Exception as e:
        print(f"自动输入密码失败: {e}")
        print("请手动在终端中输入密码")

def check_password_prompt(output: str) -> bool:
    """检测是否需要密码"""
    patterns = [
        r"Password:",
        r"password for .*:",
        r"\[sudo\] password",
    ]
    for pattern in patterns:
        if re.search(pattern, output, re.IGNORECASE):
            return True
    return False

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\n示例:")
        print('  python3 terminal_automation.py "openclaw-cn gateway status"')
        print('  python3 terminal_automation.py "sudo openclaw-cn gateway restart" "your_password"')
        sys.exit(1)
    
    command = sys.argv[1]
    password = sys.argv[2] if len(sys.argv) > 2 else None
    
    print("激活Terminal并执行命令...")
    open_terminal()
    run_command(command, password)
    
    print("\n✅ Terminal已打开，请查看窗口")

if __name__ == "__main__":
    main()
