#!/usr/bin/env python3
"""Assertion-only audit for the isolated RTL9210B-CG qualification bundle.

This intentionally does not make RTL9210B production authority. It checks that
the retained community artifacts are internally coherent and that the local
qualification footprint is SMD, while leaving electrical/application-circuit
approval as an explicit gate.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent / "authority-inventory" / "rtl9210b"
sym = ROOT / "community-lz1" / "easyeda2kicad.kicad_sym"
sch = ROOT / "community-lz1" / "RTL9210b_0.kicad_sch"
bad_fp = ROOT / "community-lz1" / "QFN-68_L8.0-W8.0-P0.40-BL-EP4.8.kicad_mod"
fp = ROOT / "RTL9210B-CG_QUALIFICATION.kicad_mod"

expected = {
    "8": "GPIO6",
    "13": "CLKREQPIN",
    "14": "PERSTBPIN",
    "19": "SPICLK",
    "24": "SPICS",
    "33": "LDO-5TO3-IN",
    "34": "LDO-5TO3-OUT",
    "37": "HSDP",
    "38": "HSDM",
    "41": "USB_TXP0",
    "42": "USB_TXN0",
    "46": "USB_RXP0",
    "47": "USB_RXN0",
    "61": "PCIE_REFCLKP",
    "62": "PCIE_REFCLKM",
    "64": "SATA_RXIP/PCIE_RXIP_0",
    "65": "SATA_RXIN/PCIE_RXIN_0",
    "67": "SATA_TXON/PCIE_TXON_0",
    "68": "SATA_TXOP/PCIE_TXOP_0",
    "69": "GNDPAD",
}

def fail(msg):
    print(f"FAIL {msg}")
    return 1

for p in (sym, sch, bad_fp, fp, ROOT / "community-lz1" / "rtl9210b.pdf"):
    if not p.exists():
        sys.exit(fail(f"missing {p}"))

text = sym.read_text(errors="replace")
pins = {}
for block in re.findall(r"\(pin .*?\n\s*\(name \"([^\"]+)\".*?\n\s*\(number \"([^\"]+)\"", text, re.S):
    name, number = block
    pins[number] = name

for number, fragment in expected.items():
    if number not in pins or fragment not in pins[number]:
        sys.exit(fail(f"symbol pin {number} lacks {fragment!r}; got {pins.get(number)!r}"))
print(f"PASS symbol expected pins ({len(pins)} pins parsed)")

bad = bad_fp.read_text(errors="replace")
good = fp.read_text(errors="replace")
if "(attr through_hole)" not in bad:
    sys.exit(fail("corroborating footprint no longer records expected bad metadata"))
if "(attr smd)" not in good:
    sys.exit(fail("qualification footprint is not marked SMD"))
pad_numbers = re.findall(r"\(pad ([0-9]+)\s+smd\b", good)
if len(pad_numbers) != 69 or set(pad_numbers) != {str(i) for i in range(1, 70)}:
    sys.exit(fail(f"qualification footprint pad set is not 1..69: {len(pad_numbers)} pads"))
if not re.search(r"\(pad 69\s+smd\s+rect .*?size 4\.800 4\.800", good, re.S):
    sys.exit(fail("qualification footprint lacks 4.8 mm exposed pad 69"))
if "(layer F.Fab)" not in good or "4.60" not in good:
    sys.exit(fail("qualification footprint lacks explicit body/fabrication and conservative courtyard"))
print("PASS qualification footprint is 69-pad SMD with exposed pad 69")

sch_text = sch.read_text(errors="replace")
for token in ("SATA_TXOP/PCIE_TXOP_0", "SATA_RXIN/PCIE_RXIN_0", "PEDET", "PCIE_REFCLKP", "SPICS"):
    if token not in sch_text:
        sys.exit(fail(f"community schematic lacks {token}"))
print("PASS community schematic contains shared-lane, PEDET, REFCLK, and SPI evidence")
print("PASS this audit is evidence-only; production authority gates remain explicit")
