# Receipt Manager Skill 🎫

Automatically extract and archive receipts from chat images.

## Two Ways to Use

### Option 1: Install as OpenClaw Skill

```bash
# Clone to your skills folder
git clone https://github.com/clinchcc/openclaw-receipt-manager.git ~/.openclaw/workspace/skills/receipt-manager

# Initialize database
python3 ~/.openclaw/workspace/skills/receipt-manager/scripts/receipt_db.py init
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

**Just send a receipt image to start!** 📸→
