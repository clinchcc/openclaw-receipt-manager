# 🎫 Receipt Manager Skill

**English** | [中文](#收据管理器技能)

---

## <a name="english"></a>English

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

### How It Works

1. **Send receipt image** to OpenClaw
2. **AI recognizes** vendor, date, total, items
3. **Skill saves** to local database automatically
4. **Get summary** anytime with natural language

### Natural Language Commands

Just talk to OpenClaw:

- "查查2月份花了多少" / "How much did I spend in February?"
- "列出所有沃尔玛的收据" / "List all Walmart receipts"
- "这个月买了什么" / "What did I buy this month?"

### Manual Commands

```bash
# Add receipt
python3 scripts/receipt_db.py add --image receipt.jpg --vendor "Walmart" --date 2026-02-27 --total 45.50 --currency CAD --category groceries

# Search
python3 scripts/receipt_db.py search --q "walmart"

# Monthly summary
python3 scripts/receipt_db.py summary --month 2026-02
```

### Features

- 📷 **AI-powered** receipt extraction from images
- 🔍 **Search** receipts by vendor/category
- 📊 **Monthly summaries** and spending reports
- 💾 **Local SQLite** database - your data stays private

---

## <a name="收据管理器技能"></a>🎫 收据管理器技能

**[English](#english)** | 中文

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

### 工作原理

1. **发送收据图片**给 OpenClaw
2. **AI 自动识别**商家、日期、金额、明细
3. **自动保存**到本地数据库
4. **随时查询**用自然语言

### 自然语言命令

直接跟 OpenClaw 对话：

- "查查2月份花了多少"
- "列出所有沃尔玛的收据"
- "这个月买了什么"

### 手动命令

```bash
# 添加收据
python3 scripts/receipt_db.py add --image receipt.jpg --vendor "沃尔玛" --date 2026-02-27 --total 45.50 --currency CAD --category 日用品

# 搜索
python3 scripts/receipt_db.py search --q "沃尔玛"

# 月度汇总
python3 scripts/receipt_db.py summary --month 2026-02
```

### 功能特点

- 📷 **AI 识别** 图片收据信息
- 🔍 **搜索** 按商家/分类查询
- 📊 **月度汇总** 消费报表
- 💾 **本地 SQLite** 数据完全隐私
