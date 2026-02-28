---
name: receipt-manager
description: Manage personal receipts and expenses. Use when: (1) User provides a receipt image, (2) User asks to add/view/search/manage receipts, (3) User wants financial summaries or monthly reports.
---

# Receipt Manager

Automatically extract and archive receipts from chat images.

## Trigger Keywords

- receipt, 收据, 发票, expense, 报销, 花费, 消费

## How It Works

1. **Send receipt image** to OpenClaw
2. **AI recognizes** vendor, date, total, items
3. **Skill saves** to local database automatically
4. **Get summary** anytime with natural language

## Commands

### Natural Language

Just talk to OpenClaw:
- "查查2月份花了多少" / "How much did I spend in February?"
- "列出所有沃尔玛的收据" / "List all Walmart receipts"
- "这个月买了什么"

### CLI Commands

```bash
# Initialize (first time)
python3 scripts/receipt_db.py init

# Add receipt
python3 scripts/receipt_db.py add --image receipt.jpg --vendor "Walmart" --date 2026-02-27 --total 45.50 --currency CAD --category groceries

# Search
python3 scripts/receipt_db.py search --q "walmart"

# Monthly summary
python3 scripts/receipt_db.py summary --month 2026-02

# List
python3 scripts/receipt_db.py list --category groceries
```

## Data Storage

- Database: `data/receipts/db.sqlite3`
- Images: `data/receipts/images/`

## Configuration

Categories are auto-detected: grocery, dining, transport, health, shopping, travel, utilities
