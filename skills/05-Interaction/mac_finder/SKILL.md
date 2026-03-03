# mac_finder - Mac目录操作

**版本:** 1.0

**描述:** 打开Finder并定位到指定目录

## 功能

- 在Finder中打开指定目录
- 支持~展开为用户目录
- 提供常用目录快捷选择

## 使用方法

```bash
# 打开指定目录
python3 mac_finder.py "目录路径"

# 示例
python3 mac_finder.py "~/Downloads"
python3 mac_finder.py "/Users/benson/Desktop"
python3 mac_finder.py "/Applications"
```

## 常用目录

| 名称 | 路径 |
|------|------|
| 桌面 | ~/Desktop |
| 下载 | ~/Downloads |
| 文档 | ~/Documents |
| 图片 | ~/Pictures |
| 音乐 | ~/Music |
| 影片 | ~/Movies |
| 应用程序 | /Applications |

---

**平台:** macOS
