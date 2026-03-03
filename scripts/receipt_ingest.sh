#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <image_path> [text]"
  exit 1
fi

IMG="$1"
TXT="${2:-}"

if [[ -n "$TXT" ]]; then
  python3 "$(dirname "$0")/receipt_db.py" add --image "$IMG" --text "$TXT"
else
  python3 "$(dirname "$0")/receipt_db.py" add --image "$IMG"
fi
