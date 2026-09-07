#!/usr/bin/env python3
"""Cross-check Path-B facts against the retained RTL9210B Rev. 1.1 PDF.

This is an evidence audit, not a production-authority claim.  It deliberately
checks the primary technical document independently of the community KiCad
symbol/XML and includes a mutation negative control.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

PDF = Path(__file__).resolve().parent / "authority-inventory/rtl9210b/community-lz1/rtl9210b.pdf"


def extract(pdf: Path) -> str:
    try:
        result = subprocess.run(
            ["pdftotext", "-layout", str(pdf), "-"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise AssertionError(f"pdftotext extraction failed: {exc}") from exc
    return result.stdout


def audit(text: str) -> None:
    required = {
        "mode": r"PEDET\s+I\s+8\s+1:\s*PCIE MODE\s+0:\s*SATA MODE",
        "isolate": r"ISOLATEBPIN\s+O\s+12.*?control SATA power",
        "clock": r"XTAL_AVDD33\s+PI\s+52.*?XTAL_IN\s+I\s+53.*?25MHz",
        "rails": r"LDO_5TO3_OUT.*?34.*?LDO_5TO3_IN.*?33.*?SWR_5TO1_OUT.*?16.*?SWR_5TO1_IN.*?17",
        "rset": r"RSET\s+I\s+51",
        "usb": r"USB_TXP0\s+O\s+41.*?USB_TXN0\s+O\s+42.*?USB_RXP0\s+I\s+46",
        "pcie": r"PCIE_REFCLKP\s+O\s+61.*?PCIE_REFCLKN\s+O\s+62.*?PCIE_RXIP_0\s+I\s+64.*?PCIE_RXIN_0\s+I\s+65.*?PCIE_TXOP_0\s+O\s+68.*?PCIE_TXON_0\s+O\s+67",
        "sideband": r"PERSTBPIN\s+O\s+14.*?CLKREQB\s+I/O/D\s+13",
        "sata": r"SATA_RXIP\s+I\s+64.*?SATA _RXIN\s+I\s+65.*?SATA _TXOP\s+O\s+68.*?SATA _TXON\s+O\s+67",
        "exposed": r"GND\s+G\s+69\s+Ground \(Exposed Pad\)",
        "spi": r"SPICSB.*?SPI Flash Chip Select.*?SPISO2.*?SPISO3",
        "flash_boundary": r"SPI Flash size \(firmware size\) is based on features.*?contact\s+Realtek",
    }
    for label, pattern in required.items():
        if not re.search(pattern, text, flags=re.S):
            raise AssertionError(f"PDF assertion failed: {label}")
    print(f"PASS retained RTL9210B Rev. 1.1 PDF assertions ({len(required)} groups)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--negative-control", action="store_true")
    args = ap.parse_args()
    if not PDF.exists():
        print(f"FAIL missing {PDF}")
        return 1
    text = extract(PDF)
    try:
        audit(text)
    except AssertionError as exc:
        print(f"FAIL {exc}")
        return 1
    if args.negative_control:
        with tempfile.NamedTemporaryFile("w", suffix=".txt") as fh:
            mutated = re.sub(r"PEDET\s+I\s+8", "REMOVED I 8", text, count=1)
            fh.write(mutated)
            fh.flush()
            try:
                audit(Path(fh.name).read_text())
            except AssertionError:
                print("PASS negative control: removed PEDET PDF evidence fails")
            else:
                print("FAIL negative control did not fail")
                return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
