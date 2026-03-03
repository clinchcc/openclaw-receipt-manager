# Receipt Manager

Receipt management skill for [OpenClaw](https://github.com/nicepkg/openclaw) — track expenses, search receipts, and get monthly summaries. All data stored locally.

## Features

- **VLM-first OCR** — uses vision language models for accurate receipt reading, with Tesseract as fallback
- **SQLite storage** — lightweight local database with image deduplication (SHA256)
- **Natural language queries** — search receipts in plain English or Chinese
- **Monthly summaries** — spending breakdowns by category
- **Auto-categorization** — grocery, dining, transport, health, shopping, travel, utilities
- **Duplicate detection** — prevents adding the same receipt twice

## Quick Start

```bash
# Clone
git clone https://github.com/clinchcc/openclaw-receipt-manager.git ~/.openclaw/workspace/skills/receipt

# Initialize database
python3 scripts/receipt_db.py init

# Send a receipt image to OpenClaw and it handles the rest
```

## CLI Usage

```bash
# Add a receipt
python3 scripts/receipt_db.py add --image ~/Downloads/receipt.jpg \
  --vendor "Costco" --date "2026-03-01" --total 85.42 --currency CAD

# Search receipts
python3 scripts/receipt_db.py search --q "costco"

# Show receipt details
python3 scripts/receipt_db.py show --id 1

# Monthly summary
python3 scripts/receipt_db.py summary --month 2026-03

# Natural language query
python3 scripts/receipt_db.py nlp --text "list all grocery receipts from February"

# Update a receipt
python3 scripts/receipt_db.py update --id 1 --category grocery

# Delete a receipt
python3 scripts/receipt_db.py delete --id 1
```

## Project Structure

```
receipt-manager/
├── SKILL.md              # OpenClaw skill definition
├── README.md
├── scripts/
│   ├── receipt_db.py     # Main CLI tool
│   └── receipt_ingest.sh # Image ingestion helper
└── data/receipts/        # Created on init
    ├── db.sqlite3        # SQLite database
    ├── images/           # Permanent image store (SHA256 named)
    └── images_tmp/       # Temp incoming images
```

## Privacy

All data is stored **locally** — nothing is sent to the cloud.
