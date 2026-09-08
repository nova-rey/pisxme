#!/usr/bin/env python3
"""Make generated schematic label UUIDs unique, preserving all label atoms."""
from collections import Counter
from pathlib import Path
import re

SCH = Path(__file__).resolve().parent / "STORAGE.kicad_sch"
ATOM = re.compile(r'\(label "[^"]*" \(at [^)]*\).*?\(uuid ([0-9a-f-]{36})\)\)')

def main():
    text = SCH.read_text()
    counts = Counter(m.group(1) for m in ATOM.finditer(text))
    duplicate_count = sum(value - 1 for value in counts.values() if value > 1)
    if duplicate_count == 0:
        print("label UUIDs already unique")
        return
    if duplicate_count != 203:
        raise SystemExit(f"refusing unexpected duplicate label scope: {duplicate_count}")
    seen = Counter(); serial = 0
    def replace(match):
        nonlocal serial
        uuid = match.group(1); seen[uuid] += 1
        if seen[uuid] == 1:
            return match.group(0)
        serial += 1
        new_uuid = f"f4000000-0000-0000-0000-{serial:012x}"
        return match.group(0).replace(uuid, new_uuid)
    out = ATOM.sub(replace, text)
    if serial != 203:
        raise SystemExit(f"refusing unexpected replacement count: {serial}")
    SCH.write_text(out)
    print(f"reconciled {serial} duplicate generated label UUIDs")

if __name__ == "__main__":
    main()
