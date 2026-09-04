"""Native-netlist regression for the Phase 18 storage USB3 boundary."""
from pathlib import Path
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[2]


def test_tusb9261_usb3_uses_authoritative_physical_pins():
    netlist = ROOT / "phase18-net.xml"
    assert netlist.exists(), "run kicad-cli sch export netlist in reva-clean first"
    root = ET.parse(netlist).getroot()
    expected = {
        "CM5_USB3_RX_N": ("J7", "128", "45"),
        "CM5_USB3_RX_P": ("J7", "130", "46"),
        "CM5_USB3_TX_N": ("J7", "140", "42"),
        "CM5_USB3_TX_P": ("J7", "142", "43"),
        "BRIDGE_SATA_RX_N": ("J3", "4", "59"),
        "BRIDGE_SATA_RX_P": ("J3", "3", "60"),
        "BRIDGE_SATA_TX_N": ("J3", "2", "56"),
        "BRIDGE_SATA_TX_P": ("J3", "1", "57"),
        "M2_3V3": ("J3", "5", None),
        "M2_GND": ("J3", "6", None),
    }
    nets = {n.get("name"): n for n in root.findall(".//nets/net")}
    for name, pins in expected.items():
        net = nets.get(name) or next(n for key, n in nets.items() if key.endswith("/" + name))
        nodes = {(x.get("ref"), x.get("pin")) for x in net.findall("node")}
        expected_nodes = {(pins[0], pins[1])}
        if name == "M2_3V3":
            expected_nodes.add(("X7", "4"))
        if pins[2] is not None:
            expected_nodes.add(("U7", pins[2]))
        assert nodes == expected_nodes
