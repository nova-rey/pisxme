#!/usr/bin/env python3
"""Verify the support fixture contains only intended saved support tracks."""
from __future__ import annotations

import argparse
import re
import sys
import tempfile
from pathlib import Path

PCB = Path(__file__).resolve().parent / "PHASE24_RTL9210B_BRINGUP_SUPPORT_ROUTED.kicad_pcb"
EXPECTED = ("XTAL_IN", "XTAL_OUT", "RSET", "SPICS", "SPISO", "SPISI", "SPICLK", "SPISO3")


def audit(text: str) -> None:
    for name in EXPECTED:
        code = re.search(rf'\(net (\d+) "{name}"\)', text)
        if not code:
            raise AssertionError(f"missing net {name}")
        if not re.search(rf'\(segment .*?\(net {code.group(1)}\)\)', text, re.S):
            raise AssertionError(f"no saved track for {name}")
    # No high-speed signal may be introduced by this support-only author.
    for name in ("LANE0_TXP", "LANE0_TXN", "LANE0_RXP", "LANE0_RXN", "USB_TXP0", "USB_RXP0"):
        code = re.search(rf'\(net (\d+) "{name}"\)', text)
        if code and re.search(rf'\(segment .*?\(net {code.group(1)}\)\)', text, re.S):
            raise AssertionError(f"support author routed forbidden high-speed net {name}")
    print("PASS support-only saved-track audit")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--negative-control", action="store_true")
    args = ap.parse_args()
    if not PCB.exists():
        print(f"FAIL missing {PCB}")
        return 1
    text = PCB.read_text(errors="replace")
    try:
        audit(text)
    except AssertionError as exc:
        print(f"FAIL {exc}")
        return 1
    if args.negative_control:
        with tempfile.NamedTemporaryFile("w", suffix=".kicad_pcb") as fh:
            bad = re.sub(r'\(segment .*?\(net 22\)\)', '', text, count=1, flags=re.S)
            fh.write(bad)
            fh.flush()
            try:
                audit(Path(fh.name).read_text())
            except AssertionError:
                print("PASS negative control: missing support track fails")
            else:
                print("FAIL negative control did not fail")
                return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
