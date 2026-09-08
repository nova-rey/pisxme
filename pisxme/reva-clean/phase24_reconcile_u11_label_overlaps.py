#!/usr/bin/env python3
"""Remove overlapping stale U11 labels at the two affected native endpoints."""
from pathlib import Path
import re

SCH = Path(__file__).resolve().parent / "STORAGE.kicad_sch"
ATOM = re.compile(r'\(label "([^"]*)" \(at 70 ([0-9.]+) 0\).*?\(uuid ([0-9a-f-]{36})\)\)')

def main():
    text = SCH.read_text()
    for y, wanted in (("191.035", "JMS_GPIO7_NC"), ("156.745", "JMS_REXT")):
        matches = list(ATOM.finditer(text))
        group = [m for m in matches if m.group(2) == y]
        if len(group) != 4:
            raise SystemExit(f"refusing U11 endpoint scope at {y}: {len(group)} != 4")
        keep = next((m for m in reversed(group) if m.group(1) == wanted), None)
        if keep is None:
            raise SystemExit(f"missing authoritative {wanted} label at {y}")
        keep_atom = keep.group(0)
        remaining = 1
        def replace(match):
            nonlocal remaining
            if match.group(2) != y:
                return match.group(0)
            if match.group(0) == keep_atom and remaining:
                remaining -= 1
                return keep_atom
            return ""
        text = ATOM.sub(replace, text)
    SCH.write_text(text)
    print("reconciled U11 pin-12/pin-39 overlapping labels")

if __name__ == "__main__":
    main()
