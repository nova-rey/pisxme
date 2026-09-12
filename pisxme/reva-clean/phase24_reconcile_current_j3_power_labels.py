#!/usr/bin/env python3
"""Reconcile current J3 instance power labels to the storage rail.

Only labels in the serialized J3 instance are changed. Embedded symbol pin
names and unrelated M2 labels are deliberately left untouched. The caller
must validate the resulting native netlist before promotion.
"""
from pathlib import Path
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("output", type=Path)
    args = ap.parse_args()
    text = args.input.read_text(encoding="utf-8")
    marker = '(property "Reference" "J3"'
    j3 = text.index(marker)
    start = text.rfind('(label "M2_CONFIG3"', 0, j3)
    if start < 0:
        raise SystemExit("J3 instance label block not found")
    block = text[start:j3]
    old = '(label "M2_3V3"'
    count = block.count(old)
    if count != 9:
        raise SystemExit(f"expected nine J3 M2_3V3 instance labels, found {count}")
    block = block.replace(old, '(label "STORAGE_3V3"')
    args.output.write_text(text[:start] + block + text[j3:], encoding="utf-8")
    print(f"reconciled={count} J3 instance power labels output={args.output}")


if __name__ == "__main__":
    main()
