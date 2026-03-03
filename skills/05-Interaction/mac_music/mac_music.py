#!/usr/bin/env python3
"""
mac_music - Mac音乐控制
"""

import sys
import subprocess

def main():
    action = sys.argv[1] if len(sys.argv) > 1 else "status"
    
    if action == "play":
        subprocess.run(["osascript", "-e", "tell app \"Music\" to play"])
        print("▶️ 播放")
    elif action == "pause":
        subprocess.run(["osascript", "-e", "tell app \"Music\" to pause"])
        print("⏸️ 暂停")
    elif action == "next":
        subprocess.run(["osascript", "-e", "tell app \"Music\" to next track"])
        print("⏭️ 下一首")
    elif action == "prev":
        subprocess.run(["osascript", "-e", "tell app \"Music\" to previous track"])
        print("⏮️ 上一首")
    elif action == "status":
        result = subprocess.run([
            "osascript", "-e", 
            'tell app "Music" to if player state is playing then "playing" else "paused"'
        ], capture_output=True, text=True)
        print(f"🎵 状态: {result.stdout.strip()}")
    else:
        print(f"用法: python3 mac_music.py [play|pause|next|prev|status]")

if __name__ == "__main__":
    main()
