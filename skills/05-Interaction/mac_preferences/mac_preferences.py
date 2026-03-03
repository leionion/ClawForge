#!/usr/bin/env python3
"""
mac_preferences - 打开系统偏好设置
"""

import sys
import subprocess

PANELS = {
    "general": "General",
    "desktop": "DesktopScreenEffectPref",
    "display": "DisplaysPref",
    "sound": "SoundPref",
    "network": "NetworkPref",
    "bluetooth": "BluetoothPref",
    "keyboard": "KeyboardPref",
    "mouse": "MousePref",
    "trackpad": "TrackpadPref",
    "printer": "PrintFaxPref",
    "color": "ColorSyncPref",
    "accounts": "AccountsPref",
    "icloud": "MobileSyncPref",
    "appstore": "AppStorePref",
    "security": "SecurityPref",
    "privacy": "PrivacyPref",
    "softwareupdate": "SoftwareUpdatePref",
    "networkfolder": "ConnectedServers",
    "fonts": "FontsPref",
    "dock": "DockPref",
    "Mission Control": "MissionControlPref",
    "startup": "StartupDiskPref",
    "users": "UsersGroupPref",
    "fuel": "FuelInjectionPref",
    "infrared": "IRPref",
    "bluetooth": "BluetoothPref",
    "sharing": "SharingPref",
    "spotlight": "SpotlightPref",
    "notifications": "NotificationCenterPref",
}

def main():
    if len(sys.argv) < 2:
        print("用法: python3 mac_preferences.py [面板名]")
        print("\n可用面板:")
        for k in PANELS.keys():
            print(f"  - {k}")
        sys.exit(1)
    
    panel = sys.argv[1].lower()
    if panel in PANELS:
        subprocess.run(["open", "x-apple.systempreferences:", f"com.apple.preference.{PANELS[panel]}"])
        print(f"✅ 已打开: {panel}")
    else:
        print(f"未知面板: {panel}")
        print("使用 'python3 mac_preferences.py' 查看可用面板")

if __name__ == "__main__":
    main()
