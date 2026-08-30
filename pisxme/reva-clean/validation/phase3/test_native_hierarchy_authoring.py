#!/usr/bin/env python3
"""Regression test for the KiCad-native root/child hierarchy authoring path."""

from __future__ import annotations

import subprocess
import tempfile
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GENERATOR = ROOT / "phase3_scaffold.py"


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
    # The generator is intentionally destructive within its output directory.
    # Exercise it in a disposable copy so this regression test cannot erase
    # later-phase child-sheet authoring in the live clean project.
    with tempfile.TemporaryDirectory(prefix="pisxme-phase3-authoring-") as tmp:
        isolated = Path(tmp) / "reva-clean"
        shutil.copytree(ROOT, isolated)
        # Preserve the generator's historical fixture lookup relative to its
        # temporary copy without depending on the live workspace path.
        fixture = Path("/tmp/work/skidl_spike/golden_hierarchy.kicad_sch")
        fixture.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT.parents[1] / "work/skidl_spike/golden_hierarchy.kicad_sch", fixture)
        generator = isolated / GENERATOR.name
        root_schematic = isolated / "PiSXMe_RevA_Clean.kicad_sch"
        child_schematics = sorted(
            path for path in isolated.glob("*.kicad_sch") if path != root_schematic
        )
        subprocess.run(["python3", str(generator)], cwd=isolated, check=True)

        root_text = root_schematic.read_text()
        assert root_text.count('(wire\n') == sum(
            child.read_text().count('(hierarchical_label "') for child in child_schematics
        )
        assert root_text.count('(sheet_instances (path "/" (page "1")))') == 1

        for child in child_schematics:
            text = child.read_text()
            lib_start = text.index("(lib_symbols")
            lib_end = balanced(text, lib_start)
            contract_start = text.index("(symbol \"PiSXMeRevAClean:")
            assert lib_start < contract_start < lib_end, child.name
            assert '(sheet_instances' in text
            assert '(at -5.08 -' in text or '(at -5.08 0' in text
            assert len(re.findall(r'property "Reference" "X_[A-Z0-9_]+"', text)) == 1

        with tempfile.TemporaryDirectory(prefix="pisxme-phase3-erc-", dir=Path.home()) as erc_tmp:
            report = Path(erc_tmp) / "erc.rpt"
            result = subprocess.run(
                [
                    "xvfb-run", "-a", "kicad-cli", "sch", "erc",
                    "--exit-code-violations", "--severity-error",
                    "--output", str(report), str(ROOT / "PiSXMe_RevA_Clean.kicad_sch"),
                ], cwd=ROOT, check=False,
            )
            assert result.returncode == 0, report.read_text() if report.exists() else result
            assert "[hier_label_mismatch]" not in report.read_text()

    print("native hierarchy authoring regression: PASS")


if __name__ == "__main__":
    main()
