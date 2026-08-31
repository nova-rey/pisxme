"""Regression for the native eight-pair Ethernet boundary authority."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2] / "pisxme" / "reva-clean"
PAIRS = tuple(f"CM5_GBE_TD{i}_{pol}" for i in range(4) for pol in "PN")


def main():
    for filename in ("CORE_CM5.kicad_sch", "ETHERNET.kicad_sch"):
        text = (ROOT / filename).read_text()
        for name in PAIRS:
            assert f'(global_label "{name}"' in text, (filename, name)
            assert f'(label "{name}"' not in text, (filename, name)
    netlist = ROOT / "materialize.xml"
    nets = ET.parse(netlist).getroot().findall(".//net")
    by_name = {n.attrib["name"]: {(x.attrib["ref"], x.attrib["pin"]) for x in n.findall("node")} for n in nets}
    expected = {
        "CM5_GBE_TD0_P": {("J7", "12"), ("U6", "1"), ("J2", "1")},
        "CM5_GBE_TD0_N": {("J7", "10"), ("U6", "2"), ("J2", "2")},
        "CM5_GBE_TD1_P": {("J7", "4"), ("U6", "3"), ("J2", "3")},
        "CM5_GBE_TD1_N": {("J7", "6"), ("U6", "4"), ("J2", "4")},
        "CM5_GBE_TD2_P": {("J7", "11"), ("U9", "1"), ("J2", "5")},
        "CM5_GBE_TD2_N": {("J7", "9"), ("U9", "2"), ("J2", "6")},
        "CM5_GBE_TD3_P": {("J7", "3"), ("U9", "3"), ("J2", "7")},
        "CM5_GBE_TD3_N": {("J7", "5"), ("U9", "4"), ("J2", "8")},
    }
    for name, nodes in expected.items():
        assert by_name.get(name) == nodes, (name, by_name.get(name))
    print("phase17 Ethernet hierarchy authority: PASS; MDI pairs=8")


if __name__ == "__main__":
    main()
