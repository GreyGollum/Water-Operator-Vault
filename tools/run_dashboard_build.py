#!/usr/bin/env python3
"""
Run the Water Operator Vault local dashboard build.

Designed to be launched from an Obsidian dashboard button through a shell-command
plugin, or manually from a terminal.

What it does:
- validates quiz JSON
- smoke-tests quiz app shell
- rebuilds printable Markdown packet sources
- rebuilds specialized DOCX print packets
- writes a dashboard build report

It does not upload artifacts or run GitHub Actions. GitHub Actions remains the
cloud-build path for downloadable PDF/DOCX ZIP artifacts.
"""

from __future__ import annotations

import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REPORT = REPO_ROOT / "09 Verification and Sources" / "Dashboard Build Report.md"

STEPS = [
    ("Validate quiz JSON", [sys.executable, "tools/validate_quiz_json.py"]),
    ("Smoke-test quiz app shell", [sys.executable, "tools/smoke_test_quiz_app.py"]),
    ("Build printable Markdown packet sources", [sys.executable, "tools/build_printable_packets.py"]),
    ("Build specialized DOCX packets", [sys.executable, "tools/build_specialized_docx_packets.py"]),
]


def run_step(name: str, command: list[str]) -> dict:
    print(f"\n=== {name} ===")
    completed = subprocess.run(
        command,
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.stdout:
        print(completed.stdout)
    if completed.stderr:
        print(completed.stderr, file=sys.stderr)
    return {
        "name": name,
        "command": " ".join(command),
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
        "passed": completed.returncode == 0,
    }


def write_report(results: list[dict]) -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now().isoformat(timespec="seconds")
    passed = all(result["passed"] for result in results)
    lines = [
        "---",
        "type: dashboard-build-report",
        "project: Water Operator Vault",
        "area: local-build",
        f"status: {'passed' if passed else 'failed'}",
        f"last_run: {now}",
        "---",
        "",
        "# Dashboard Build Report",
        "",
        "## Summary",
        "",
        "```yaml",
        f"last_run: {now}",
        f"build_passes: {str(passed).lower()}",
        f"step_count: {len(results)}",
        f"failed_steps: {sum(1 for result in results if not result['passed'])}",
        "```",
        "",
        "## Steps",
        "",
        "| Step | Status | Command |",
        "|---|---|---|",
    ]
    for result in results:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(f"| {result['name']} | {status} | `{result['command']}` |")

    lines.extend(["", "## Outputs", ""])
    lines.extend(
        [
            "- `09 Verification and Sources/Quiz JSON Validation Report.md`",
            "- `09 Verification and Sources/Quiz App Smoke Test Report.md`",
            "- `08 Printable Study Materials/Generated Packets/Water-Operator-Vault-Flashcards-Packet.md`",
            "- `08 Printable Study Materials/Generated Packets/Water-Operator-Vault-Practice-Exam-Packet.md`",
            "- `08 Printable Study Materials/Generated Packets/Water-Operator-Vault-Source-and-Verification-Packet.md`",
            "- `08 Printable Study Materials/Build Artifacts/Water-Operator-Vault-Flashcards-Packet.docx`",
            "- `08 Printable Study Materials/Build Artifacts/Water-Operator-Vault-Practice-Exam-Packet.docx`",
        ]
    )

    if not passed:
        lines.extend(["", "## Errors", ""])
        for result in results:
            if not result["passed"]:
                lines.append(f"### {result['name']}")
                lines.append("")
                lines.append("```text")
                lines.append(result["stderr"] or result["stdout"] or "No output captured.")
                lines.append("```")
                lines.append("")

    lines.extend(
        [
            "",
            "## Related",
            "",
            "- [[Release Readiness Status]]",
            "- [[Quiz App Status]]",
            "- [[08 Printable Study Materials/DOCX Layout Specification]]",
        ]
    )
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    results = [run_step(name, command) for name, command in STEPS]
    write_report(results)
    if not all(result["passed"] for result in results):
        print(f"\nBuild failed. See: {REPORT}", file=sys.stderr)
        sys.exit(1)
    print(f"\nBuild passed. See: {REPORT}")


if __name__ == "__main__":
    main()
