"""Native-netlist regression for the Phase 18 storage USB3 boundary."""
from pathlib import Path
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[2]


def test_tusb9261_usb3_uses_authoritative_physical_pins():
    netlist = ROOT / "phase18-net.xml"
    assert netlist.exists(), "run kicad-cli sch export netlist in reva-clean first"
    root = ET.parse(netlist).getroot()
    expected = {
        "CM5_USB3_RX_N": ("128", "45"),
        "CM5_USB3_RX_P": ("130", "46"),
        "CM5_USB3_TX_N": ("140", "42"),
        "CM5_USB3_TX_P": ("142", "43"),
    }
    nets = {n.get("name"): n for n in root.findall(".//nets/net")}
    for name, pins in expected.items():
        nodes = {(x.get("ref"), x.get("pin")) for x in nets[name].findall("node")}
        assert nodes == {("J7", pins[0]), ("U7", pins[1])}
