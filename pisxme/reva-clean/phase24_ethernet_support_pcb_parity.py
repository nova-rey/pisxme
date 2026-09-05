"""Check Ethernet support PCB pads against the saved production netlist."""
from pathlib import Path
import xml.etree.ElementTree as ET
import pcbnew

R = Path(__file__).resolve().parent
PCB = R / "PHASE24_ETHERNET_SUPPORT_MATERIALIZED.kicad_pcb"
XML = R / "phase24-production.xml"
REFS = {"C48", "C49", "C50", "C51", "C52", "R26", "R27", "R28", "R29", "R30", "R31"}


def main():
    root = ET.parse(XML).getroot()
    expected = {}
    for net in root.findall(".//net"):
        for node in net.findall("node"):
            if node.get("ref") in REFS:
                expected[(node.get("ref"), node.get("pin"))] = net.get("name")
    board = pcbnew.LoadBoard(str(PCB))
    assert set(ref for ref, _ in expected) == REFS
    for ref in sorted(REFS):
        fp = board.FindFootprintByReference(ref)
        assert fp is not None, ref
        for pad in fp.Pads():
            key = (ref, str(pad.GetNumber()))
            assert key in expected, key
            assert pad.GetNetname() == expected[key], (key, pad.GetNetname(), expected[key])
            assert pad.GetLayerSet().Contains(pcbnew.B_Cu), (key, pad.GetLayerSet().FmtHex())
    print("Phase24 Ethernet PCB parity: PASS; 11 support footprints and all pad nets match native production netlist")


if __name__ == "__main__":
    main()
