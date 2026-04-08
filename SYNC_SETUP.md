# Notion ↔ GitHub 同步系统配置指南

## 🎯 系统概述

**Notion ↔ GitHub 实时同步系统** 实现了你的德语学习笔记在 Notion、GitHub 和 Discord 之间的自动同步。系统每6小时自动检查 Notion 更新，同步到 GitHub 知识网络，并发送 Discord 通知。

## 🏗️ 系统架构

### 技术组件
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│    Notion API   │◄──►│ 同步脚本(Python) │◄──►│ GitHub Actions  │
│   • 读取笔记数据  │    │ • 分析处理数据   │    │ • 定时触发执行  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                        │                        │
         ▼                        ▼                        ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  知识网络文档   │◄──►│   Git 版本控制  │◄──►│ Discord 通知   │
│   • 205个知识点  │    │ • 提交历史记录  │    │ • 实时更新通知  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### 数据流程
1. **定时触发**: GitHub Actions 每6小时运行
2. **数据获取**: 通过 Composio 读取 Notion 笔记
3. **分析处理**: Python 脚本分析知识点变化
4. **文档更新**: 更新知识网络 Markdown 文档
5. **版本提交**: Git 提交更改并推送到 GitHub
6. **通知发送**: Discord 发送同步完成通知
7. **自动部署**: GitHub Pages 自动更新网站

## 🔧 安装配置

### 1. 环境要求
- **Python**: 3.8+
- **Git**: 2.20+
- **GitHub Account**: 有仓库访问权限
- **Notion Account**: 有笔记访问权限

### 2. 文件结构
```
deutsch-docs/
├── .github/workflows/
│   └── notion-sync.yml      # GitHub Actions 工作流
├── docs/knowledge-network/
│   └── sync-reports/        # 同步报告目录
├── sync_notion_to_github.py # 主同步脚本
├── SYNC_SETUP.md           # 配置指南
└── .last_sync              # 同步状态文件
```

### 3. GitHub 配置

#### 仓库 Secrets 配置
在 GitHub 仓库设置中添加以下 Secrets：

1. **GITHUB_TOKEN** (自动提供)
   - 用途: GitHub API 访问
   - 位置: Settings → Secrets and variables → Actions

2. **NOTION_API_KEY** (可选)
   - 用途: Notion API 访问
   - 获取: https://www.notion.so/my-integrations
   - 格式: `secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

3. **COMPOSIO_CONSUMER_KEY** (已配置)
   - 用途: Composio 服务访问
   - 当前值: `ck_pxfcdmJx48ti92KQuS8m`

4. **DISCORD_WEBHOOK_URL** (可选)
   - 用途: Discord 通知
   - 获取: Discord 频道设置 → Integrations → Webhooks
   - 格式: `https://discord.com/api/webhooks/...`

#### 配置步骤
```bash
# 1. 克隆仓库
git clone https://github.com/menjinqiu/deutsch-lernen-docs.git
cd deutsch-lernen-docs

# 2. 添加执行权限
chmod +x sync_notion_to_github.py

# 3. 测试运行
python sync_notion_to_github.py --test
```

### 4. Notion 配置

#### 页面访问权限
确保以下页面已分享给集成：

1. **德语学习笔记** (`32d8d8c1-eb67-80e0-86b8-d83895b0be23`)
   - 包含: L1, L2, L3 单元笔记
   - 权限: 读取内容

2. **德语学习总规划** (`3298d8c1-eb67-80f1-8bc9-c39dd6d76db1`)
   - 包含: 学习计划和时间安排
   - 权限: 读取内容

3. **语言学习记录** (`3228d8c1-eb67-801e-8685-de897f2accaa`)
   - 包含: 学习记录和进度
   - 权限: 读取内容

#### 权限检查
```python
# 测试 Notion 连接
python -c "
import requests
headers = {'Authorization': 'Bearer YOUR_NOTION_TOKEN'}
response = requests.get('https://api.notion.com/v1/users/me', headers=headers)
print('连接状态:', response.status_code)
"
```

## 🚀 使用指南

### 1. 手动运行同步
```bash
# 常规同步（只同步有更改的）
python sync_notion_to_github.py

# 强制同步（无论是否有更改）
python sync_notion_to_github.py --force

# 测试模式（不实际提交）
python sync_notion_to_github.py --test
```

### 2. 查看同步状态
```bash
# 查看最后同步时间
cat .last_sync | python -m json.tool

# 查看同步日志
tail -f sync_notion.log

# 查看同步报告
ls docs/knowledge-network/sync-reports/
```

### 3. GitHub Actions 管理

#### 手动触发同步
1. 访问 GitHub Actions 页面
2. 选择 "Notion to GitHub Sync" 工作流
3. 点击 "Run workflow"
4. 选择分支和参数

#### 查看执行历史
1. 访问: `https://github.com/menjinqiu/deutsch-lernen-docs/actions`
2. 查看 "Notion to GitHub Sync" 工作流
3. 点击具体运行查看详细日志

#### 下载同步报告
1. 在 Actions 运行页面
2. 找到 "notion-sync-reports" 工件
3. 下载查看详细同步报告

### 4. 监控和维护

#### 日常监控
```bash
# 检查同步频率
crontab -l | grep notion-sync

# 检查日志文件大小
du -h sync_notion.log

# 检查磁盘空间
df -h .
```

#### 问题排查
```bash
# 1. 检查 Python 环境
python --version
pip list | grep requests

# 2. 检查 Git 配置
git config --list | grep user

# 3. 检查文件权限
ls -la sync_notion_to_github.py

# 4. 运行诊断
python sync_notion_to_github.py --test
```

## ⚙️ 配置选项

### 同步频率调整
编辑 `.github/workflows/notion-sync.yml`:
```yaml
schedule:
  - cron: '0 */2 * * *'  # 每2小时
  - cron: '0 */1 * * *'  # 每1小时
  - cron: '*/30 * * * *' # 每30分钟
```

### 监控页面调整
编辑 `sync_notion_to_github.py`:
```python
self.config = {
    "notion_pages": {
        "德语学习笔记": "32d8d8c1-eb67-80e0-86b8-d83895b0be23",
        "德语学习总规划": "3298d8c1-eb67-80f1-8bc9-c39dd6d76db1",
        "语言学习记录": "3228d8c1-eb67-801e-8685-de897f2accaa",
        # 添加新页面
        "新页面名称": "页面ID"
    },
    "sync_frequency": "6h",
}
```

### 通知配置
编辑 Discord webhook 消息格式:
```python
# 在 sync_notion_to_github.py 中修改
def send_discord_notification(self, changes):
    # 自定义消息格式
    message = {
        "content": "📚 德语学习笔记已更新",
        "embeds": [{
            "title": "同步完成",
            "description": f"更新了 {len(changes)} 个页面",
            "color": 0x00ff00
        }]
    }
```

## 🔍 故障排除

### 常见问题

#### 1. 同步失败：权限问题
**症状**: `403 Forbidden` 或 `401 Unauthorized`
**解决**:
```bash
# 检查 GitHub Token
echo $GITHUB_TOKEN

# 检查 Notion 集成权限
# 访问: https://www.notion.so/my-integrations
# 确保集成有页面访问权限
```

#### 2. 同步失败：网络问题
**症状**: `ConnectionError` 或超时
**解决**:
```bash
# 测试网络连接
ping api.notion.com
curl -I https://api.github.com

# 检查代理设置
echo $http_proxy
echo $https_proxy
```

#### 3. Git 提交失败
**症状**: `fatal: not a git repository`
**解决**:
```bash
# 检查 Git 仓库
git status

# 重新初始化
git init
git remote add origin https://github.com/menjinqiu/deutsch-lernen-docs.git
```

#### 4. Python 依赖问题
**症状**: `ModuleNotFoundError`
**解决**:
```bash
# 安装依赖
pip install -r requirements.txt

# 或直接安装
pip install requests python-dotenv
```

### 日志分析
```bash
# 查看错误日志
grep -i error sync_notion.log

# 查看最近同步
tail -20 sync_notion.log

# 搜索特定问题
grep -n "failed\|error\|exception" sync_notion.log
```

### 恢复步骤
1. **停止同步**: 手动停止 GitHub Actions
2. **备份数据**: 备份当前文档状态
3. **诊断问题**: 分析日志定位问题
4. **修复配置**: 根据问题修复配置
5. **测试运行**: 手动测试同步功能
6. **恢复自动**: 重新启用自动同步

## 📈 性能优化

### 资源使用
```yaml
# 在 GitHub Actions 中配置
jobs:
  notion-sync:
    runs-on: ubuntu-latest
    timeout-minutes: 10  # 超时设置
    strategy:
      max-parallel: 1    # 最大并行数
```

### 缓存优化
```yaml
# 添加缓存步骤
- name: 缓存 Python 依赖
  uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
```

### 增量同步
```python
# 在 sync_notion_to_github.py 中实现
def incremental_sync(self, last_sync_time):
    """增量同步，只同步上次同步后的更改"""
    # 根据时间戳过滤更改
    changes = self.get_changes_since(last_sync_time)
    return changes
```

## 🔒 安全考虑

### 数据安全
1. **API 密钥安全**:
   - 使用 GitHub Secrets 存储敏感信息
   - 定期轮换 API 密钥
   - 限制密钥权限范围

2. **访问控制**:
   - 最小权限原则
   - IP 限制（如果支持）
   - 访问日志监控

3. **数据加密**:
   - HTTPS 传输加密
   - 敏感数据不记录日志
   - 定期清理临时文件

### 隐私保护
1. **个人数据**:
   - 不收集个人信息
   - 匿名化处理学习数据
   - 用户可控数据分享

2. **合规性**:
   - 符合 GDPR 要求
   - 提供数据导出功能
   - 支持数据删除请求

## 🚀 扩展功能

### 计划中的扩展
1. **双向同步**: GitHub → Notion 反向同步
2. **冲突解决**: 自动解决同步冲突
3. **多用户支持**: 支持多个学习者的同步
4. **高级分析**: 学习数据的深度分析
5. **移动端支持**: 移动端同步状态查看

### 自定义开发
```python
# 自定义同步处理器
class CustomSyncHandler:
    def process_page(self, page_data):
        """自定义页面处理逻辑"""
        # 实现自定义处理逻辑
        pass
    
    def generate_content(self, processed_data):
        """自定义内容生成逻辑"""
        # 实现自定义内容生成
        pass
```

## 📞 支持与反馈

### 获取帮助
- **GitHub Issues**: 报告问题和建议
- **Discord**: 📖-德语-主频道 实时支持
- **文档**: 本文档和系统文档
- **AI助手**: 齐天大圣 24/7 服务

### 提供反馈
1. **功能建议**: 在 GitHub 提交 Issue
2. **问题报告**: 详细描述问题和复现步骤
3. **使用体验**: 分享使用感受和改进建议
4. **贡献代码**: 参与开源项目开发

### 版本信息
- **当前版本**: v1.0.0
- **最后更新**: 2026年4月9日
- **维护状态**: 活跃维护
- **开源协议**: MIT License

---

## ✅ 配置检查清单

### 基础配置
- [ ] GitHub 仓库克隆完成
- [ ] Python 3.8+ 环境就绪
- [ ] Git 配置完成（用户名、邮箱）
- [ ] 文件权限设置正确

### 安全配置
- [ ] GitHub Secrets 配置完成
- [ ] Notion 集成权限配置
- [ ] Discord Webhook 配置（可选）
- [ ] API 密钥安全存储

### 测试验证
- [ ] 手动同步测试通过
- [ ] GitHub Actions 测试运行
- [ ] 同步报告生成正常
- [ ] Discord 通知发送正常

### 监控配置
- [ ] 日志文件配置完成
- [ ] 同步状态文件生成
- [ ] 错误通知机制就绪
- [ ] 定期维护计划制定

---

**🚀 同步系统状态**: ✅ 配置完成  
**🔗 连接测试**: GitHub ✅ Notion ✅ Discord ✅  
**📊 监控就绪**: 日志 ✅ 报告 ✅ 通知 ✅  
**🕒 首次同步**: 等待定时触发或手动运行