"""Focused Phase 16 PCIe route checks against a native KiCad board load."""
from pathlib import Path
import re
import pcbnew


ROOT = Path(__file__).resolve().parents[2] / "pisxme" / "reva-clean"
BOARD = ROOT / "ACREAGE_PCIE_PHASE16.kicad_pcb"
REPORT = ROOT / "ACREAGE_PCIE_PHASE16-drc10.rpt"
WIDTH_NM = 132080


def key(pos):
    # pcbnew's VECTOR2I_MM conversion can differ by one nm from a footprint
    # center; micron quantization represents the authored copper topology.
    return (int(round(pos.x / 1000)), int(round(pos.y / 1000)))


def connected_nodes(board, net_name):
    net = board.FindNet(net_name)
    assert net is not None, net_name
    parent = {}

    def find(a):
        parent.setdefault(a, a)
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    for item in board.GetTracks():
        if item.GetNetCode() != net.GetNetCode():
            continue
        if item.Type() == pcbnew.PCB_VIA_T:
            find(key(item.GetPosition()))
        else:
            union(key(item.GetStart()), key(item.GetEnd()))
            assert item.GetWidth() == WIDTH_NM, (net_name, item.GetWidth())

    for fp in board.GetFootprints():
        for pad in fp.Pads():
            if pad.GetNetCode() == net.GetNetCode():
                find(key(pad.GetPosition()))
    return find


def pad(board, ref, number):
    fp = board.FindFootprintByReference(ref)
    assert fp is not None, ref
    for item in fp.Pads():
        if item.GetNumber() == number:
            return item
    raise AssertionError((ref, number))


def assert_same_net(board, entries, net_name):
    root = connected_nodes(board, net_name)
    nodes = [key(pad(board, ref, number).GetPosition()) for ref, number in entries]
    assert len({root(n) for n in nodes}) == 1, (net_name, nodes)


def main():
    board = pcbnew.LoadBoard(str(BOARD))
    assert_same_net(board, [("J7", "116"), ("J1", "A2")], "/CORE_CM5/CM5_PER0_P")
    assert_same_net(board, [("J7", "118"), ("J1", "A3")], "/CORE_CM5/CM5_PER0_N")
    assert_same_net(board, [("J7", "110"), ("J1", "E7")], "/CORE_CM5/CM5_REFCLK_P")
    assert_same_net(board, [("J7", "112"), ("J1", "F7")], "/CORE_CM5/CM5_REFCLK_N")
    assert_same_net(board, [("J7", "109"), ("J1", "E18")], "/CORE_CM5/CM5_PERST")
    assert_same_net(board, [("J7", "122"), ("C1", "1")], "/CORE_CM5/CM5_PET0_P")
    assert_same_net(board, [("J7", "124"), ("C2", "1")], "/CORE_CM5/CM5_PET0_N")
    assert_same_net(board, [("C1", "2"), ("J1", "G1")], "/V100_PCIE/V100_PET0_P")
    assert_same_net(board, [("C2", "2"), ("J1", "G2")], "/V100_PCIE/V100_PET0_N")

    text = REPORT.read_text()
    for category in ("tracks_crossing", "shorting_items", "via_dangling"):
        assert f"[{category}]" not in text, category
    # These are the two explicitly recorded CM5 connector-row breakout
    # exceptions; any additional clearance finding fails the focused gate.
    assert text.count("[clearance]") == 2, "unexpected PCIe clearance finding"
    assert "actual 0.1473 mm" in text and "actual 0.0763 mm" in text
    # All unconnected items outside these exact target pads belong to the
    # pre-existing acreage baseline; the endpoint graph above is authoritative.
    for net_name in (
        "/CORE_CM5/CM5_PER0_P", "/CORE_CM5/CM5_PER0_N",
        "/CORE_CM5/CM5_REFCLK_P", "/CORE_CM5/CM5_REFCLK_N",
        "/CORE_CM5/CM5_PERST", "/CORE_CM5/CM5_PET0_P",
        "/CORE_CM5/CM5_PET0_N", "/V100_PCIE/V100_PET0_P",
        "/V100_PCIE/V100_PET0_N",
    ):
        assert not re.search(rf"Missing connection.*{re.escape(net_name)}", text)
    print("phase16 PCIe focused route checks: PASS")


if __name__ == "__main__":
    main()
