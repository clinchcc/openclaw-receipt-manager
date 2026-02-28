<!-- Language Toggle -->
<div align="right">
  <button onclick="toggleLang()" style="padding:8px 16px;cursor:pointer;">🇨🇳 中文</button>
</div>

---

<!-- English Section -->
<div id="en">

# Receipt Manager Skill 🎫

Automatically extract and archive receipts from chat images.

## Two Ways to Use

### Option 1: Install as OpenClaw Skill

```bash
# Clone to your skills folder
git clone https://github.com/clinchcc/openclaw-receipt.git ~/.openclaw/workspace/skills/receipt

# Initialize database
python3 ~/.openclaw/workspace/skills/receipt/scripts/receipt_db.py init
```

Then restart OpenClaw. The skill will automatically activate when you send a receipt image.

### Option 2: Just Send Receipt to Chat! 🤳

**Simply send a receipt image to OpenClaw**, and it will:
1. Automatically extract vendor, date, total, and items
2. Save to local database
3. Provide summary

No installation needed!

---

## Features

- 📷 **Auto-extract** receipt info from images
- 🔍 **Search** receipts by vendor/category
- 📊 **Monthly summaries** and spending reports
- 💾 **Local SQLite** database - your data stays private
- 🖼️ **Image storage** for all receipts

## Commands (after skill installed)

```bash
# Add receipt manually
python3 scripts/receipt_db.py add --image receipt.jpg --vendor "Walmart" --date 2026-02-27 --total 45.50 --currency CAD --category "groceries"

# Search
python3 scripts/receipt_db.py search --q "walmart"

# Monthly summary
python3 scripts/receipt_db.py summary --month 2026-02

# Natural language
python3 scripts/receipt_db.py nlp --text "2月份花了多少"
```

## Data Location

- Database: `data/receipts/db.sqlite3`
- Images: `data/receipts/images/`

---

**Just send a receipt image to start!** 📸

</div>

---

<!-- 中文 Section -->
<div id="zh" style="display:none;">

# 收据管理器技能 🎫

自动从聊天图片中提取并归档收据。

## 两种使用方式

### 方式一：安装为 OpenClaw 技能

```bash
# 克隆到技能目录
git clone https://github.com/clinchcc/openclaw-receipt.git ~/.openclaw/workspace/skills/receipt

# 初始化数据库
python3 ~/.openclaw/workspace/skills/receipt/scripts/receipt_db.py init
```

然后重启 OpenClaw。当您发送收据图片时，技能将自动激活。

### 方式二：直接发送收据图片！🤳

**只需将收据图片发送给 OpenClaw**，它将：
1. 自动提取商家、日期、总价和明细
2. 保存到本地数据库
3. 提供汇总

无需安装！

---

## 功能特点

- 📷 **自动识别** 图片收据信息
- 🔍 **搜索** 按商家/分类查询
- 📊 **月度汇总** 消费报表
- 💾 **本地 SQLite** 数据完全隐私
- 🖼️ **图片存储** 所有收据影像

## 命令（安装后使用）

```bash
# 手动添加收据
python3 scripts/receipt_db.py add --image receipt.jpg --vendor "沃尔玛" --date 2026-02-27 --total 45.50 --currency CAD --category "日用品"

# 搜索
python3 scripts/receipt_db.py search --q "沃尔玛"

# 月度汇总
python3 scripts/receipt_db.py summary --month 2026-02

# 自然语言
python3 scripts/receipt_db.py nlp --text "2月份花了多少"
```

## 数据位置

- 数据库: `data/receipts/db.sqlite3`
- 图片: `data/receipts/images/`

---

**直接发送收据图片即可开始使用！** 📸

</div>

---

<script>
function toggleLang() {
  var en = document.getElementById('en');
  var zh = document.getElementById('zh');
  if (en.style.display === 'none') {
    en.style.display = 'block';
    zh.style.display = 'none';
  } else {
    en.style.display = 'none';
    zh.style.display = 'block';
  }
}
</script>
