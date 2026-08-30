#!/usr/bin/env python3
"""Regression test for the KiCad-native root/child hierarchy authoring path."""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GENERATOR = ROOT / "phase3_scaffold.py"
ROOT_SCHEMATIC = ROOT / "PiSXMe_RevA_Clean.kicad_sch"
CHILD_SCHEMATICS = sorted(
    path for path in ROOT.glob("*.kicad_sch") if path != ROOT_SCHEMATIC
)


def balanced(text: str, start: int) -> int:
    depth = 0
    quoted = False
    escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if quoted and escaped:
            escaped = False
        elif quoted and char == "\\":
            escaped = True
        elif char == '"':
            quoted = not quoted
        elif not quoted:
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0:
                    return index
    raise AssertionError("unbalanced schematic expression")


def main() -> None:
    subprocess.run(["python3", str(GENERATOR)], cwd=ROOT, check=True)

    root_text = ROOT_SCHEMATIC.read_text()
    assert root_text.count('(wire\n') == sum(
        child.read_text().count('(hierarchical_label "') for child in CHILD_SCHEMATICS
    )
    assert root_text.count('(sheet_instances (path "/" (page "1")))') == 1

    for child in CHILD_SCHEMATICS:
        text = child.read_text()
        lib_start = text.index("(lib_symbols")
        lib_end = balanced(text, lib_start)
        contract_start = text.index("(symbol \"PiSXMeRevAClean:")
        assert lib_start < contract_start < lib_end, child.name
        assert '(sheet_instances' in text
        assert '(at -5.08 -' in text or '(at -5.08 0' in text

    with tempfile.TemporaryDirectory(
        prefix="pisxme-phase3-erc-", dir=Path.home()
    ) as tmp:
        report = Path(tmp) / "erc.rpt"
        result = subprocess.run(
            [
                "xvfb-run",
                "-a",
                "kicad-cli",
                "sch",
                "erc",
                "--exit-code-violations",
                "--severity-error",
                "--output",
                str(report),
                str(ROOT_SCHEMATIC),
            ],
            cwd=ROOT,
            check=False,
        )
        assert result.returncode == 0, report.read_text() if report.exists() else result
        assert "[hier_label_mismatch]" not in report.read_text()

    print("native hierarchy authoring regression: PASS")


if __name__ == "__main__":
    main()
