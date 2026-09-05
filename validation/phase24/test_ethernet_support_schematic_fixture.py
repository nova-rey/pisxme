"""Regression for the disposable native Ethernet support schematic fixture."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "pisxme/reva-clean"
NETLIST = R / "PHASE24_ETHERNET_SUPPORT_FIXTURE3.xml"
ERC = R / "PHASE24_ETHERNET_SUPPORT_FIXTURE_ROOT2-erc.rpt"
SOURCE = R / "PHASE24_ETHERNET_SUPPORT_FIXTURE.kicad_sch"

EXPECTED = {
    "/ETH_CT1": {"C48.1", "J2.9"},
    "/ETH_CT2": {"C49.1", "J2.10"},
    "/ETH_CT3": {"C50.1", "J2.11"},
    "/ETH_CT4": {"C51.1", "J2.12"},
    "/ETH_CT_COMMON": {"C52.1", "R26.2", "R27.2", "R28.2", "R29.2"},
    "GBE_SHIELD": {"C52.2", "J2.17", "J2.18"},
    "/ETH_POWER": {"J2.13", "J2.15"},
    "/GBE_LED_Y_K": {"J2.14", "R30.2"},
    "/GBE_LED_G_K": {"J2.16", "R31.2"},
    "CM5_ETH_LED2": {"R30.1"},
    "CM5_ETH_LED3": {"R31.1"},
}

def block(text, name):
    start = text.rfind(f'(name "{name}")')
    assert start >= 0, f"missing net {name}"
    end = re.search(r'\n\s*\(name |\n\s*\)\s*\n\s*\(net', text[start + 1:], re.S)
    return text[start:] if not end else text[start:start + 1 + end.start()]

def main():
    assert "Errors 0" in ERC.read_text()
    source = SOURCE.read_text()
    assert "PROVISIONAL_NOT_PROCUREMENT_AUTHORITY" in source
    text = NETLIST.read_text()
    for name, members in EXPECTED.items():
        got = {f"{r}.{p}" for r, p in re.findall(r'\(ref "([^"]+)"\).*?\(pin "([^"]+)"\)', block(text, name), re.S)}
        assert members <= got, f"{name}: missing {sorted(members - got)}; got {sorted(got)}"
    print("phase24 Ethernet support schematic fixture: PASS")

if __name__ == "__main__":
    main()
