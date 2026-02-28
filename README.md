# 🎫 Receipt Manager Skill

**English** | [中文](#中文)

---

## English

### Two Ways to Use

#### Option 1: Just Drop the Page to OpenClaw!

**Simply send this skill page URL to OpenClaw**, and it will:
1. Automatically download and install the skill
2. Initialize the database
3. Ready to receive receipt images

No manual installation needed!

#### Option 2: Manual Install

```bash
# Clone to your skills folder
git clone https://github.com/clinchcc/openclaw-receipt-manager.git ~/.openclaw/workspace/skills/receipt

# Initialize database
python3 ~/.openclaw/workspace/skills/receipt/scripts/receipt_db.py init
```

Then restart OpenClaw. The skill will automatically activate when you send a receipt image.

### Features

- 📷 **Auto-extract** receipt info from images
- 🔍 **Search** receipts by vendor/category
- 📊 **Monthly summaries** and spending reports
- 💾 **Local SQLite** database - your data stays private
- 🖼️ **Image storage** for all receipts

### Commands

```bash
# Add receipt
python3 scripts/receipt_db.py add --image receipt.jpg --vendor "Walmart" --date 2026-02-27 --total 45.50 --currency CAD --category "groceries"

# Search
python3 scripts/receipt_db.py search --q "walmart"

# Monthly summary
python3 scripts/receipt_db.py summary --month 2026-02
```

---

# 🎫 收据管理器技能

**[English](#english)** | 中文

---

### 两种使用方式

#### 方式一：直接把页面丢给 OpenClaw！

**只需将此技能页面URL发送给 OpenClaw**，它将：
1. 自动下载并安装技能
2. 初始化数据库
3. 准备好接收收据图片

无需手动安装！

#### 方式二：手动安装

```bash
# 克隆到技能目录
git clone https://github.com/clinchcc/openclaw-receipt-manager.git ~/.openclaw/workspace/skills/receipt

# 初始化数据库
python3 ~/.openclaw/workspace/skills/receipt/scripts/receipt_db.py init
```

然后重启 OpenClaw。当您发送收据图片时，技能将自动激活。

### 功能特点

- 📷 **自动识别** 图片收据信息
- 🔍 **搜索** 按商家/分类查询
- 📊 **月度汇总** 消费报表
- 💾 **本地 SQLite** 数据完全隐私
- 🖼️ **图片存储** 所有收据影像

### 命令

```bash
# 添加收据
python3 scripts/receipt_db.py add --image receipt.jpg --vendor "沃尔玛" --date 2026-02-27 --total 45.50 --currency CAD --category "日用品"

# 搜索
python3 scripts/receipt_db.py search --q "沃尔玛"

# 月度汇总
python3 scripts/receipt_db.py summary --month 2026-02
```
