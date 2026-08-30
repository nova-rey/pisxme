#!/usr/bin/env python3
"""Materialize the proven USB3 relocation topology onto the active PCB.

This is deliberately a narrow, reviewable transformation:
* replace only U5/U6/U7/U9/U10/U11 with the verified TI-derived trial blocks;
* move only those six references to the selected A9/B8 coordinates;
* remove any pre-existing USB3 SS copper for the affected nets;
* import only the complete FAST-A A9 and FAST-B B8 trial segments/vias.

The active schematic, CM5/SXM2, PCIe, power, zones, and all other footprints
are left untouched.  The caller must run KiCad DRC and the PCIe comparison
after this transformation.
"""

from __future__ import annotations

import re
import shutil
import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ACTIVE = ROOT / "pisxme/PiSXMe.kicad_pcb"
BACKUP = ROOT / "routing/usb3-production/PiSXMe-before-usb3.kicad_pcb"
TRIAL_A = ROOT / "experiments/usb3-mux-relocation/FA_A9_relocated_symmetric_transition_north.kicad_pcb"
TRIAL_B = ROOT / "experiments/usb3-mux-relocation/FB_B8_relocated_symmetric_transition.kicad_pcb"

TARGET_REFS = {"U5", "U6", "U7", "U9", "U10", "U11"}
USB_NET_IDS = set(range(10, 18)) | set(range(61, 70)) | set(range(78, 87))


def balanced_block(text: str, start: int) -> int:
    depth = 0
    quoted = False
    escaped = False
    for pos in range(start, len(text)):
        char = text[pos]
        if quoted:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                quoted = False
            continue
        if char == '"':
            quoted = True
        elif char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return pos + 1
    raise ValueError(f"unbalanced block at {start}")


def footprint_blocks(text: str) -> dict[str, tuple[int, int, str]]:
    result: dict[str, tuple[int, int, str]] = {}
    for match in re.finditer(r"(?m)^\s*\(footprint\s+", text):
        start = match.start()
        end = balanced_block(text, start)
        block = text[start:end]
        ref = re.search(r'\(property "Reference" "([^"]+)"', block)
        if ref:
            result[ref.group(1)] = (start, end, block)
    return result


def route_lines(text: str) -> list[str]:
    return re.findall(r"(?m)^\s*\((?:segment|via)\s+[^\n]+\n?", text)


def net_id(line: str) -> int | None:
    match = re.search(r"\(net\s+(\d+)\)", line)
    return int(match.group(1)) if match else None


def apply_replacements(text: str, replacements: dict[str, str]) -> str:
    blocks = footprint_blocks(text)
    edits = []
    for ref, replacement in replacements.items():
        start, end, _ = blocks[ref]
        edits.append((start, end, replacement))
    for start, end, replacement in sorted(edits, reverse=True):
        text = text[:start] + replacement + text[end:]
    return text


def materialize_text(active: str, trial_a: str, trial_b: str) -> tuple[str, int, dict[str, str]]:

    active_blocks = footprint_blocks(active)
    a_blocks = footprint_blocks(trial_a)
    b_blocks = footprint_blocks(trial_b)
    missing = TARGET_REFS - set(active_blocks)
    if missing:
        raise SystemExit(f"active references missing: {sorted(missing)}")

    replacements = {ref: a_blocks[ref][2] for ref in ("U5", "U6", "U7")}
    replacements.update({ref: b_blocks[ref][2] for ref in ("U9", "U10", "U11")})
    for ref, block in replacements.items():
        if '(property "Reference" "' + ref + '"' not in block:
            raise SystemExit(f"replacement reference mismatch for {ref}")

    # The corrected TI-derived RKS package has 21 pads (20 perimeter pads plus
    # the exposed pad); each DQA flow-through package has 10 pads.  These
    # checks prevent an accidental return to the old study footprints.
    for ref in ("U5", "U9"):
        if replacements[ref].count("(pad ") != 21:
            raise SystemExit(f"{ref} replacement is not the corrected 21-pad RKS package")
    for ref in ("U6", "U7", "U10", "U11"):
        if replacements[ref].count("(pad ") != 10:
            raise SystemExit(f"{ref} replacement is not the corrected 10-pad DQA package")

    active = apply_replacements(active, replacements)

    # Remove only affected USB3 copper.  This is idempotent and protects the
    # script from accidentally duplicating a rerun of the production import.
    kept_lines = []
    for line in active.splitlines(keepends=True):
        if line.lstrip().startswith("(segment ") or line.lstrip().startswith("(via "):
            if net_id(line) in USB_NET_IDS:
                continue
        kept_lines.append(line)
    active = "".join(kept_lines)

    imported = []
    for line in route_lines(trial_a) + route_lines(trial_b):
        if net_id(line) not in USB_NET_IDS:
            raise SystemExit(f"unexpected imported net: {line.strip()}")
        imported.append(line)
    marker = "\t(embedded_fonts no)"
    marker_pos = active.rfind(marker)
    if marker_pos < 0:
        raise SystemExit("board-level embedded-font marker not found")
    # A CM5 footprint also contains an embedded-font token.  The board-level
    # token is the final one immediately before the board close; insert there,
    # never inside a footprint block.
    insertion = "\n".join(imported) + "\n"
    active = active[:marker_pos] + insertion + active[marker_pos:]
    return active, len(imported), replacements


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="validate and report without modifying the active PCB")
    args = parser.parse_args()

    active = ACTIVE.read_text()
    trial_a = TRIAL_A.read_text()
    trial_b = TRIAL_B.read_text()
    materialized, imported_count, replacements = materialize_text(active, trial_a, trial_b)

    if args.dry_run:
        print(f"dry-run: migrated references: {', '.join(sorted(replacements))}")
        print(f"dry-run: imported USB3 segments/vias: {imported_count}")
        print(f"dry-run: output bytes: {len(materialized)}")
        return

    BACKUP.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ACTIVE, BACKUP)
    ACTIVE.write_text(materialized)

    print(f"migrated references: {', '.join(sorted(replacements))}")
    print(f"imported USB3 segments/vias: {imported_count}")
    print(f"backup: {BACKUP}")


if __name__ == "__main__":
    main()
