---
name: receipt-manager
description: Manage personal receipts and expenses. Use when: (1) User provides a receipt image, (2) User asks to add/view/search/manage receipts, (3) User wants financial summaries or monthly reports.
---

# Receipt Manager

## Overview

A skill for recording, organizing, and querying personal receipts. It provides a SQLite database for storing receipt data and a CLI script (`receipt_db.py`) for CRUD operations.

## OCR (Automatic Text Recognition)

**This skill uses a VLM-first approach for best accuracy.**

When adding a receipt:
1. **Primary**: Use VLM model capability or MCP (e.g., understand_image) to extract receipt details
2. **Backup**: Use Tesseract OCR for verification/fallback
   ```bash
   tesseract <image_path> - --psm 4
   ```
3. Compare results - use VLM as primary, OCR as validation
4. Extract: vendor name, date, total amount, line items
5. Verify the extracted data and correct if needed

**Why VLM?** Vision language models accurately read receipt details including line items, which Tesseract often misreads.


## Data Storage

- **Database:** `data/receipts/db.sqlite3`
- **Images (permanent):** `data/receipts/images/` — stored with SHA256 hash name, auto-dedup
- **Images (temp):** `data/receipts/images_tmp/` — temp location for incoming images

The database schema includes: id, vendor, receipt_date, total, currency, category, image_path, image_sha256, text, items_json.

## Quick Start

### 1. Add a Receipt

When user sends a receipt image:
1. Copy image to `data/receipts/images_tmp/<timestamp>.jpg`
2. Use VLM model or MCP to extract details
3. (Optional) Verify with Tesseract: `tesseract <image_path> - --psm 4`
4. Run: `python3 scripts/receipt_db.py add --image <temp_image_path>`
   - Auto computes SHA256, copies to `images/<sha256>.jpg`, removes temp file
   - Override with: `--vendor "..." --date "..." --total ... --currency ... --category "..." --items-json '[...]'

### 2. List Receipts

```bash
python3 scripts/receipt_db.py search --q ""
```

### 3. Monthly Summary

```bash
python3 scripts/receipt_db.py summary --month YYYY-MM
```

## Commands

- `add`: Add new receipt (requires --image)
- `search`: Search receipts by keyword
- `show`: Show receipt details by ID
- `summary`: Monthly spending summary
- `update`: Update receipt fields
- `delete`: Delete receipt by ID

## Duplicate Detection

Before adding a new receipt, check for duplicates:

1. **Query existing receipts** by vendor + receipt_date + total:
   ```python
   import sqlite3
   conn = sqlite3.connect('data/receipts/db.sqlite3')
   cursor = conn.cursor()
   cursor.execute('''
     SELECT id, vendor, receipt_date, total, currency, category, items_json
     FROM receipts 
     WHERE vendor = ? AND receipt_date = ? AND total = ?
   ''', (vendor, date, total))
   ```

2. **If duplicate found:**
   - Compare fields (vendor, date, total, currency, category, items_json)
   - List differences to user
   - Ask: "Duplicate receipt found. Differences: ... Replace?"
   - If yes, delete old one and add new; if no, skip

3. **If no duplicate:** Proceed with normal add flow

---

## Natural Language Query

Use the NLP mode for natural language queries:
```bash
python3 scripts/receipt_db.py nlp --text "查吹风机在哪个收据"
python3 scripts/receipt_db.py nlp --text "列出2月shopping类收据"
python3 scripts/receipt_db.py nlp --text "汇总 2026-02"
```

## Resources

### scripts/
- `receipt_db.py`: Main CLI tool for receipt management
