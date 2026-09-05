"""Audit clean Ethernet support against CM5IO and EDAC authorities."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
SCHEMATIC = ROOT / "ETHERNET.kicad_sch"
ROOT_SCHEMATIC = ROOT / "PiSXMe_RevA_Clean.kicad_sch"
EDAC_AUTHORITY = ROOT / "authority-inventory/primary-docs/ethernet-magjack/EDAC_A70-112-331N126_AUTHORITY.md"
CM5IO_SCHEMATIC = ROOT / "authority-inventory/cm5io-rev2/CM5_GPIO.kicad_sch"
CT_NETS = ("ETH_CT1", "ETH_CT2", "ETH_CT3", "ETH_CT4")
LED_NETS = ("GBE_LED_Y_A", "GBE_LED_Y_K", "GBE_LED_G_A", "GBE_LED_G_K")

def refs(text):
    return tuple(sorted(set(re.findall(r'\(property "Reference" "([A-Z][A-Z0-9_#-]*)"', text))))

def occurrences(text, names):
    return {n: len(re.findall(rf'(?<![A-Za-z0-9_]){re.escape(n)}(?![A-Za-z0-9_])', text)) for n in names}

def main():
    sch = SCHEMATIC.read_text()
    root = ROOT_SCHEMATIC.read_text()
    edac = EDAC_AUTHORITY.read_text()
    donor = CM5IO_SCHEMATIC.read_text()
    support = tuple(r for r in refs(sch) if r.startswith(("CCT", "RCT")))
    print("support component references:", support or "NONE")
    print("center-tap occurrences:", occurrences(sch, CT_NETS))
    print("LED occurrences:", occurrences(sch, LED_NETS))
    print("EDAC values present:", all(x in edac for x in ("22 nF", "75", "1 nF")))
    print("CM5IO LED authority present:", all(x in donor for x in ("Reference\" \"R2", "Reference\" \"R3", "470R")))
    print("root GBE_LED contract labels:", len(re.findall(r'\bGBE_LED\b', root)))
    print("child GBE_LED hierarchical labels:", len(re.findall(r'hierarchical_label "GBE_LED"', sch)))
    if support:
        raise SystemExit("unexpected support references already present")
    print("PHASE24_ETHERNET_SUPPORT_AUTHORITY_AUDIT=PASS_WITH_OPEN_SCHEMATIC_GAP")

if __name__ == "__main__":
    main()
