"""Fail-closed audit for the dual-mode storage mode contract.

This audit checks saved schematic net labels and the reviewed M-key authority.
It intentionally does not add graph edges or treat expected labels as proof of
physical connectivity; native ERC/PCB connectivity remains a separate gate.
"""
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parent
SCH_DEFAULT = ROOT / "STORAGE.kicad_sch"
MATRIX = ROOT / "PHASE24_DUAL_MODE_STORAGE_PIN_MATRIX.md"

REQUIRED = {
    "USB_SEL", "STORAGE_SEL", "USB_OE_N", "STORAGE_3V3", "POWER_GND",
    "M2_SATA_A_P_PCIE_TXP0", "M2_SATA_A_N_PCIE_TXN0",
    "M2_SATA_B_P_PCIE_RXN0", "M2_SATA_B_N_PCIE_RXP0",
    "M2_REFCLK_P", "M2_REFCLK_N", "M2_PERST_N", "M2_CLKREQ_N",
    "M2_PEWake_N", "M2_PEDET", "TUSB_SATA_TXP", "TUSB_SATA_TXN",
    "TUSB_SATA_RXP", "TUSB_SATA_RXN", "JMS_PCIE_TXP0",
    "JMS_PCIE_TXN0", "JMS_PCIE_RXP0", "JMS_PCIE_RXN0",
}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", nargs="?", default=str(SCH_DEFAULT))
    ap.add_argument("--allow-auto-open", action="store_true")
    args = ap.parse_args()
    text = Path(args.input).read_text()
    failures = []
    for net in sorted(REQUIRED):
        if f'(label "{net}"' not in text and f'(global_label "{net}"' not in text:
            failures.append(f"missing reviewed net label: {net}")
    for ref, mpn in (("U11", "JMS583-QHFA3A"), ("U12", "HD3SS6126RUAR"),
                     ("U13", "HD3SS3412RUAR"), ("U14", "SN74LVC1G17DBVR"),
                     ("J3", "1-2199230-4")):
        if f'(property "Reference" "{ref}"' not in text:
            failures.append(f"missing instance {ref}")
        if mpn not in text:
            failures.append(f"missing MPN {mpn}")
    if 'property "Reference" "J5"' not in text:
        failures.append("missing J5 AUTO / FORCE SATA / FORCE NVMe override")
    if 'AUTO / FORCE SATA / FORCE NVMe' not in text:
        failures.append("mode override value missing")
    for label in ("MODE_IN", "M2_PEDET", "STORAGE_SEL"):
        if text.count(f'(label "{label}"') < 1:
            failures.append(f"missing mode-control label: {label}")
    if not MATRIX.exists():
        failures.append("reviewed pin/mode matrix missing")
    if not args.allow_auto_open and "AUTO additionally requires" in MATRIX.read_text():
        failures.append("AUTO mode remains explicitly open")
    if failures:
        for item in failures:
            print("FAIL", item)
        raise SystemExit(1)
    print("PASS dual-mode mode contract")

if __name__ == "__main__":
    main()
