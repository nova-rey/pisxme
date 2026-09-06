#!/usr/bin/env python3
"""Native-netlist assertions for the isolated RTL9210B reference fixture.

The XML files are exported by KiCad 10.0.5 from the retained community
schematics. This audit asserts facts present in those netlists; it never adds
graph edges or treats expected connectivity as physical connectivity.
"""
from pathlib import Path
import argparse
import re
import sys
import tempfile

ROOT = Path(__file__).resolve().parent / "authority-inventory" / "rtl9210b"
RTL = ROOT / "RTL9210B_0.xml"
M2 = ROOT / "M.2_0.xml"

def must(text, pattern, label):
    if not re.search(pattern, text):
        raise AssertionError(label)

def audit(rtl, m2):
    r = Path(rtl).read_text(errors="replace")
    m = Path(m2).read_text(errors="replace")
    for pin, name in (("8", "PEDET"), ("13", "CLKREQ"), ("14", "PERST"),
                      ("41", "USB_TXP0"), ("42", "USB_TXN0"),
                      ("46", "USB_RXP0"), ("47", "USB_RXN0"),
                      ("61", "PCIE_REFCLKP"), ("62", "PCIE_REFCLKM"),
                      ("64", "SATA_RXIP/PCIE_RXIP_0"),
                      ("65", "SATA_RXIN/PCIE_RXIN_0"),
                      ("67", "SATA_TXON/PCIE_TXON_0"),
                      ("68", "SATA_TXOP/PCIE_TXOP_0"),
                      ("69", "GNDPAD")):
        must(r, rf'<pin num="{pin}" name="[^"]*{re.escape(name)}[^"]*"',
             f"RTL9210B pin {pin} {name}")
    for name in ("PDET", "PCIE_REFCLK+", "PCIE_REFCLK-", "PERST#", "CLKREQ#",
                 "DEVSLP"):
        must(m, rf'name="/[^"]*{re.escape(name)}', f"M.2 net {name}")
    must(m, r'<node ref="CN6" pin="69" pinfunction="PEDET_69"',
         "M.2 contact 69 PEDET")

if not RTL.exists() or not M2.exists():
    raise SystemExit("FAIL missing native XML receipt")

try:
    audit(RTL, M2)
except AssertionError as e:
    print(f"FAIL {e}")
    raise SystemExit(1)
print("PASS native RTL9210B/M.2 netlist assertions")

parser = argparse.ArgumentParser()
parser.add_argument("--negative-control", action="store_true")
args = parser.parse_args()
if args.negative_control:
    with tempfile.TemporaryDirectory() as td:
        bad = Path(td) / "bad.xml"
        bad.write_text(RTL.read_text(errors="replace").replace("PEDET", "REMOVED", 1))
        try:
            audit(bad, M2)
        except AssertionError:
            print("PASS negative control: removed RTL PEDET evidence fails")
        else:
            print("FAIL negative control did not fail")
            raise SystemExit(1)
