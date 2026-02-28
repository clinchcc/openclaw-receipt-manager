#!/usr/bin/env python3
"""
Receipt skill handler for OpenClaw.
Receives extracted receipt info and saves to database.
"""

import sys
import json
import argparse
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

def handle(data):
    """Handle receipt data from OpenClaw."""
    required = ['vendor', 'total']
    for field in required:
        if field not in data:
            return {"ok": False, "error": f"missing {field}"}

    # Build command - always need an image, use placeholder if not provided
    image_path = data.get('image', 'placeholder.jpg')
    
    cmd = [
        "python3", 
        str(SCRIPT_DIR / "receipt_db.py"),
        "add",
        "--image", image_path,
        "--vendor", data['vendor'],
        "--total", str(data['total']),
        "--date", data.get('date', '2026-01-01'),
        "--currency", data.get('currency', 'CAD'),
        "--category", data.get('category', 'other'),
    ]
    
    if data.get('text'):
        cmd.extend(["--text", data['text']])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            return {"ok": True, "message": f"✅ 已保存收据: {data['vendor']} ${data['total']} {data.get('currency', 'CAD')}"}
        else:
            return {"ok": False, "error": result.stderr}
    except Exception as e:
        return {"ok": False, "error": str(e)}

if __name__ == '__main__':
    try:
        data = json.load(sys.stdin)
        result = handle(data)
        print(json.dumps(result))
    except Exception as e:
        print(json.dumps({"ok": False, "error": str(e)}))
