#!/usr/bin/env python3
"""Create an exact, source-only candidate for the V100 PCIe label cluster.

The root contract already carries global ``V100_PET0_P/N`` labels.  The
V100_PCIE child has one local label for each corresponding wire, which KiCad
reports as a local/global collision.  This producer changes only those two
serialized label records and never edits symbols, wires, hierarchy pins,
coordinates, UUIDs, or PCB files.  It writes a separate output by default so
the canonical source cannot be changed accidentally.
"""

from __future__ import annotations

import argparse
from pathlib import Path


TARGETS = (
    (
        "V100_PET0_P",
        "100.32 102.54 0",
        "c0000000-0000-0000-0000-000000000002",
    ),
    (
        "V100_PET0_N",
        "100.32 105.08 0",
        "c0000000-0000-0000-0000-000000000003",
    ),
)


def promote(text: str) -> tuple[str, int]:
    changed = 0
    for name, at, uuid in TARGETS:
        local = (
            f'(label "{name}" (at {at}) '
            f'(effects (font (size 1.27 1.27)) (justify left)) '
            f'(uuid {uuid}))'
        )
        global_ = (
            f'(global_label "{name}" (shape bidirectional) (at {at}) '
            f'(effects (font (size 1.27 1.27)) (justify left)) '
            f'(uuid {uuid}))'
        )
        if text.count(global_) == 1 and text.count(local) == 0:
            continue
        if text.count(local) != 1 or text.count(global_) != 0:
            raise ValueError(
                f"{name}: expected exactly one local target and no promoted target"
            )
        text = text.replace(local, global_)
        changed += 1
    if changed != len(TARGETS):
        raise ValueError(f"expected {len(TARGETS)} promotions, made {changed}")
    return text, changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    source = args.input.read_text(encoding="utf-8")
    candidate, changed = promote(source)
    args.output.write_text(candidate, encoding="utf-8")
    print(f"promoted={changed} output={args.output}")


if __name__ == "__main__":
    main()
