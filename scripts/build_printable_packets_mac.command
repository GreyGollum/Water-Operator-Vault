#!/bin/bash
set -euo pipefail

# Water Operator Vault - Mac Clickable Printable Packet Builder
# Double-click this file in Finder, or run it from Obsidian Shell Commands / macOS Shortcuts.
# Output folder: 08 Printable Study Materials/Build Artifacts

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

clear || true

echo ""
echo "==============================================="
echo "Water Operator Vault - Build Printable Packets"
echo "==============================================="
echo ""

if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
else
  echo "ERROR: Python was not found."
  echo "Install Python 3.12+ and try again."
  echo ""
  read -n 1 -s -r -p "Press any key to close..."
  exit 1
fi

echo "Using Python: $($PYTHON_BIN --version)"
echo ""

echo "Installing/updating Python DOCX dependency..."
$PYTHON_BIN -m pip install python-docx

echo ""
echo "Building printable packets locally..."
$PYTHON_BIN tools/run_printable_packet_build.py --local

echo ""
echo "Done. Output folder:"
echo "08 Printable Study Materials/Build Artifacts"
echo ""
read -n 1 -s -r -p "Press any key to close..."
