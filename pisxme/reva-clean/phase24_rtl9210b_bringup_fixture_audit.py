#!/usr/bin/env python3
"""Assertion-only audit of the isolated RTL9210B bring-up fixture."""
from __future__ import annotations

import argparse
import re
import sys
import tempfile
from pathlib import Path

PCB = Path(__file__).resolve().parent / "PHASE24_RTL9210B_BRINGUP_FIXTURE.kicad_pcb"


def audit(text: str) -> None:
    for token in (
        '"RTL_5V"', '"RTL_3V3"', '"RTL_1V1"', '"SSD_3V3"', '"PEDET"',
        '"LANE0_TXP"', '"LANE0_TXN"', '"LANE0_RXP"', '"LANE0_RXN"',
        '"REFCLK_P"', '"REFCLK_N"', '"PERST_N"', '"CLKREQ_N"',
        '"SPICS"', '"SPICLK"', '"SPISI"', '"SPISO"', '"RSET"',
        '"XTAL_IN"', '"XTAL_OUT"', '"ISOLATEB"',
    ):
        if token not in text:
            raise AssertionError(f"missing fixture net {token}")
    if text.count('(footprint "RTL9210B-CG_QUALIFICATION"') != 1:
        raise AssertionError("missing or duplicate RTL9210B footprint")
    if text.count('(footprint "BRINGUP_M2_MKEY"') != 1:
        raise AssertionError("missing or duplicate M-key fixture")
    for ref in ("Y1", "U2", "R1", "R2", "R3", "TP1", "TP8"):
        if f'"Reference" "{ref}"' not in text:
            raise AssertionError(f"missing support/test reference {ref}")
    # Corrected shared-lane physical ownership, not the quarantined WIP order.
    for net, contact in (("LANE0_TXP", '49'), ("LANE0_TXN", '47'),
                         ("LANE0_RXP", '43'), ("LANE0_RXN", '41')):
        if not re.search(rf'\(pad "{contact}" .*?\(net \d+ "{net}"\)', text):
            raise AssertionError(f"M-key contact {contact} lacks {net}")
    if not re.search(r'\(pad "69" .*?\(net \d+ "GND"\)', text):
        raise AssertionError("RTL exposed pad 69 is not grounded")
    print("PASS isolated RTL9210B bring-up fixture authority")


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
            before, after = text.split('(footprint "BRINGUP_M2_MKEY"', 1)
            after = after.replace('(net 14 "LANE0_TXP")', '(net 14 "BROKEN_TXP")', 1)
            bad = before + '(footprint "BRINGUP_M2_MKEY"' + after
            fh.write(bad)
            fh.flush()
            try:
                audit(Path(fh.name).read_text())
            except AssertionError:
                print("PASS negative control: removed TX authority fails")
            else:
                print("FAIL negative control did not fail")
                return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
