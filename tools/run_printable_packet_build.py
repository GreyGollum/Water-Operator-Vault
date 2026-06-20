#!/usr/bin/env python3
"""
Dashboard-friendly launcher for printable packet builds.

This script gives the vault a stable command target for a dashboard button.

Modes:
1. Local build:
   python tools/run_printable_packet_build.py --local

2. GitHub Actions helper:
   python tools/run_printable_packet_build.py --open-actions

Local requirements:
- Python 3.12+
- python-docx
- pandoc for generic PDF/DOCX packet conversion
- xelatex if building PDFs through Pandoc

The GitHub Actions path is recommended for normal use because it builds the
same artifact ZIP on GitHub without needing local dependencies.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import webbrowser
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
ACTIONS_URL = "https://github.com/GreyGollum/Water-Operator-Vault/actions/workflows/build-printable-packets.yml"
ARTIFACT_DIR = REPO_ROOT / "08 Printable Study Materials" / "Build Artifacts"
GENERATED_DIR = REPO_ROOT / "08 Printable Study Materials" / "Generated Packets"


def run(cmd: list[str]) -> None:
    print("$ " + " ".join(cmd))
    subprocess.run(cmd, cwd=REPO_ROOT, check=True)


def local_build() -> None:
    print("Building printable packet Markdown sources...")
    run([sys.executable, "tools/build_printable_packets.py"])

    print("Building specialized DOCX layouts...")
    try:
        import docx  # noqa: F401
    except ImportError as exc:
        raise SystemExit("Missing dependency: python-docx. Install with: python -m pip install python-docx") from exc
    run([sys.executable, "tools/build_specialized_docx_packets.py"])

    pandoc = shutil.which("pandoc")
    if not pandoc:
        print("Pandoc not found; skipping generic Markdown-to-DOCX/PDF packet conversion.")
        print("Specialized DOCX files were still built in:")
        print(f"  {ARTIFACT_DIR}")
        return

    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    for md_file in GENERATED_DIR.glob("*.md"):
        base = md_file.stem
        run([pandoc, str(md_file), "-o", str(ARTIFACT_DIR / f"{base}.docx")])
        if shutil.which("xelatex"):
            run([pandoc, str(md_file), "--pdf-engine=xelatex", "-o", str(ARTIFACT_DIR / f"{base}.pdf")])
        else:
            print(f"xelatex not found; skipped PDF for {md_file.name}")

    print("Build complete:")
    print(f"  {ARTIFACT_DIR}")


def open_actions() -> None:
    print(f"Opening GitHub Actions workflow: {ACTIONS_URL}")
    webbrowser.open(ACTIONS_URL)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build or launch Water Operator Vault printable packet artifacts.")
    parser.add_argument("--local", action="store_true", help="Build printable packets locally.")
    parser.add_argument("--open-actions", action="store_true", help="Open the GitHub Actions workflow page.")
    args = parser.parse_args()

    if args.local:
        local_build()
    else:
        open_actions()


if __name__ == "__main__":
    main()
