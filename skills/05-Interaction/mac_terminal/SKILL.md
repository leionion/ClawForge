# mac_terminal - Mac终端自动化

**版本:** 1.0

**描述:** 自动打开Terminal.app并执行命令

## 功能

- 激活或打开Terminal.app
- 在Terminal中执行指定命令
- 可选：自动输入密码

## 使用方法

```bash
# 基本用法 - 打开Terminal并执行命令
python3 mac_terminal.py "命令"

# 带密码执行（需要辅助功能权限）
python3 mac_terminal.py "sudo 命令" "密码"
```

## 示例

```bash
# 查看版本
python3 mac_terminal.py "openclaw-cn --version"

# 重启服务
python3 mac_terminal.py "openclaw-cn gateway restart"
```

## 注意事项

- 自动输入密码需要Mac系统偏好设置 > 隐私与安全性 > 辅助功能 中授权
- 每次执行会在Terminal中创建新标签页

---

**平台:** macOS
