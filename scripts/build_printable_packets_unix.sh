#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

echo ""
echo "==============================================="
echo "Water Operator Vault - Build Printable Packets"
echo "==============================================="
echo ""

if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 was not found. Install Python 3.12+ and try again."
  exit 1
fi

echo "Installing/updating Python DOCX dependency..."
python3 -m pip install python-docx

echo ""
echo "Building printable packets locally..."
python3 tools/run_printable_packet_build.py --local

echo ""
echo "Done. Output folder:"
echo "08 Printable Study Materials/Build Artifacts"
