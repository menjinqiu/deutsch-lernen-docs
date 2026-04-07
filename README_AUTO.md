# 自动化推送系统

本目录包含 Discord 德语学习文档的自动化推送系统。

## 🚀 系统架构

```
Discord 内容更新 → 本地文档更新 → 自动 Git 提交 → 推送到 GitHub → 自动部署网站
```

## 📁 文件说明

### 核心文件
- `auto_push.py` - 自动推送主脚本
- `config.json` - 系统配置
- `auto_push.log` - 运行日志

### 文档文件
- `docs/` - 文档内容目录
- `mkdocs.yml` - 网站配置
- `.github/workflows/deploy.yml` - GitHub Actions 工作流

## 🔧 使用方法

### 手动运行
```bash
cd C:\Users\men\.openclaw\workspace\deutsch-docs
python auto_push.py
```

### 自动运行（Windows 任务计划）
1. 创建基本任务
2. 触发器：每30分钟
3. 操作：启动程序 `pythonw.exe`
4. 参数：`C:\Users\men\.openclaw\workspace\deutsch-docs\auto_push.py`
5. 起始于：`C:\Users\men\.openclaw\workspace\deutsch-docs`

### OpenClaw Cron 配置
```yaml
# 在 OpenClaw 配置中添加
cron:
  - schedule: "*/30 * * * *"
    command: "cd C:/Users/men/.openclaw/workspace/deutsch-docs && python auto_push.py"
    channel: "discord"
```

## ⚙️ 配置说明

### Git 配置
```json
{
  "repo_path": "文档仓库路径",
  "remote_url": "GitHub 仓库地址",
  "branch": "推送分支"
}
```

### 自动化配置
```json
{
  "check_interval_minutes": 30,
  "max_retries": 3,
  "retry_delay_seconds": 10
}
```

### Discord 集成
```json
{
  "channel_id": "Discord 频道ID",
  "notify_on_success": true,
  "notify_on_failure": true
}
```

## 🔒 安全配置

### 使用 Token（推荐）
1. 设置环境变量：`GITHUB_TOKEN`
2. 在 `config.json` 中启用 `use_token: true`

### 使用 SSH 密钥
1. 生成 SSH 密钥：`ssh-keygen -t ed25519`
2. 添加公钥到 GitHub
3. 在 `config.json` 中设置 `ssh_key_path`

## 🐛 故障排除

### 常见问题
1. **推送失败**：检查网络连接和权限
2. **认证失败**：验证 Token 或 SSH 密钥
3. **合并冲突**：手动解决冲突后重试

### 日志查看
```bash
# 查看最新日志
tail -f auto_push.log

# 搜索错误
grep -i error auto_push.log
```

## 📊 监控指标

### 成功指标
- 推送成功率
- 平均推送时间
- 文档更新频率

### 失败指标
- 认证失败次数
- 网络错误次数
- 合并冲突次数

## 🔄 工作流程

### 正常流程
1. 检测文档变化
2. 添加到暂存区
3. 提交更改
4. 推送到 GitHub
5. GitHub Actions 自动部署
6. Discord 发送通知

### 错误处理
1. 重试机制（最多3次）
2. 失败通知
3. 日志记录

## 🚀 快速开始

### 第一次设置
1. 确保 Git 已安装并配置
2. 设置 GitHub 认证（Token 或 SSH）
3. 运行测试：`python auto_push.py --test`

### 日常维护
1. 定期检查日志
2. 更新配置（如需要）
3. 监控推送状态

## 📞 支持

### 问题报告
1. 查看 `auto_push.log` 获取详细错误
2. 在 Discord 报告问题
3. 提供相关配置信息

### 功能请求
1. 在 GitHub 创建 Issue
2. 描述需求场景
3. 提供优先级评估

---

**维护者**：齐天大圣德语教练 🐒  
**最后更新**：2026年4月7日  
**版本**：v1.0.0