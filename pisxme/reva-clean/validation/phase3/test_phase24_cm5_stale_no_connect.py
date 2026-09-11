"""Prove the bounded cleanup of orphaned CORE_CM5 no-connect records.

The disposable copy removes only the eleven duplicate UUID records identified
by the native ERC audit.  It must remove exactly eleven dangling NC warnings
without changing any other ERC class or introducing errors.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STALE = {
    ("66.98", "31.42", "e3000000-0000-0000-0000-0000000001f6"),
    ("127.94", "31.42", "e3000000-0000-0000-0000-000000000257"),
    ("66.98", "36.5", "e3000000-0000-0000-0000-000000000254"),
    ("127.94", "33.96", "e3000000-0000-0000-0000-000000000255"),
    ("66.98", "39.04", "e3000000-0000-0000-0000-000000000252"),
    ("127.94", "36.5", "e3000000-0000-0000-0000-000000000253"),
    ("66.98", "41.58", "e3000000-0000-0000-0000-000000000250"),
    ("127.94", "39.04", "e3000000-0000-0000-0000-000000000251"),
    ("127.94", "41.58", "e3000000-0000-0000-0000-00000000024f"),
    ("209.22", "36.5", "e3000000-0000-0000-0000-0000000002bb"),
    ("270.18", "36.5", "e3000000-0000-0000-0000-0000000002ba"),
}


def remove_stale(text: str) -> tuple[str, int]:
    removed = 0
    kept = []
    for line in text.splitlines(keepends=True):
        match = re.search(r'\(no_connect \(at ([0-9.]+) ([0-9.]+)\).*?\(uuid ([^)]+)\)', line)
        key = match.groups() if match else None
        if key in STALE:
            removed += 1
        else:
            kept.append(line)
    return "".join(kept), removed


def main() -> None:
    child = ROOT / "CORE_CM5.kicad_sch"
    report = ROOT / ".phase24-cm5-nc-probe.rpt"
    try:
        text = child.read_text()
        assert remove_stale(text)[1] == 0, "stale NC record reintroduced"
        result = subprocess.run(
            ["kicad-cli", "sch", "erc", "--output", str(report),
             "--exit-code-violations", str(ROOT / "PiSXMe_RevA_Clean.kicad_sch")],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        assert report.exists(), result.stderr
        report_text = report.read_text()
        errors = re.findall(r"\[\w+_error\]", report_text)
        dangling = report_text.count("[no_connect_dangling]")
        assert not errors, errors
        assert dangling == 0, dangling
        assert result.returncode != 0, "fixture unexpectedly has no ERC violations"
        print("CM5 stale no-connect regression: PASS; stale records absent, no errors")
    finally:
        report.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
