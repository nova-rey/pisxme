#!/usr/bin/env python3
"""Create a disposable source-level M.2 power reconciliation candidate.

The connector pin names remain M2_3V3 in the embedded symbol.  Only the
saved J3 instance labels are changed to STORAGE_3V3, so the board generator
can own one real supply net rather than inventing PCB-only copper.
"""
from pathlib import Path
import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--root-input", type=Path)
    ap.add_argument("--root-output", type=Path)
    a = ap.parse_args()
    text = a.input.read_text()
    marker = '(property "Reference" "J3"'
    j3 = text.index(marker)
    # J3's pin labels are immediately before its instance declaration and
    # use the native x=240 connector-pin endpoint.  Avoid embedded symbol
    # definitions and any other contract labels.
    start = text.rfind('(label "M2_CONFIG3" (at 240 211.99', 0, j3)
    if start < 0:
        raise SystemExit("J3 label block not found")
    block = text[start:j3]
    old = '(label "M2_3V3" (at 240 '
    count = block.count(old)
    if count != 9:
        raise SystemExit(f"expected 9 J3 M2 power labels, found {count}")
    block = block.replace(old, '(label "STORAGE_3V3" (at 240 ')
    text = text[:start] + block + text[j3:]
    # The child sheet exports this rail at its native hierarchy boundary.
    # Preserve the rest of the sheet contract and update only this port.
    child_port = '(hierarchical_label "M2_3V3"'
    if text.count(child_port) != 1:
        raise SystemExit("expected exactly one child M2_3V3 hierarchical port")
    text = text.replace(child_port, '(hierarchical_label "STORAGE_3V3"', 1)
    a.output.write_text(text)
    if (a.root_input is None) != (a.root_output is None):
        raise SystemExit("--root-input and --root-output must be supplied together")
    if a.root_input:
        root = a.root_input.read_text()
        sheet_pin = '(pin "M2_3V3" bidirectional (at 70 156 180)'
        root_label = '(global_label "M2_3V3" (shape bidirectional) (at 60 156 0)'
        if root.count(sheet_pin) != 1 or root.count(root_label) != 1:
            raise SystemExit("root M2_3V3 storage boundary not uniquely found")
        root = root.replace(sheet_pin, '(pin "STORAGE_3V3" bidirectional (at 70 156 180)', 1)
        root = root.replace(root_label, '(global_label "STORAGE_3V3" (shape bidirectional) (at 60 156 0)', 1)
        a.root_output.write_text(root)
        print(f"wrote {a.root_output} with storage hierarchy port reconciled")
    print(f"wrote {a.output} with {count} J3 power labels assigned to STORAGE_3V3")

if __name__ == "__main__":
    main()
