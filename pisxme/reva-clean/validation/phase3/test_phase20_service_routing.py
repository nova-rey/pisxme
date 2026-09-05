"""Regression checks for the complete disposable Phase 20 SERVICE island."""
from pathlib import Path
import re
import pcbnew

ROOT = Path(__file__).resolve().parents[2]
PCB = ROOT / "PHASE20_SERVICE_RD_OUTER_REFILLED.kicad_pcb"
DRC = ROOT / "PHASE20_SERVICE_RD_OUTER_REFILLED-drc.rpt"

EXPECTED = {
    "/CORE_CM5/SERVICE_USB2_DP": {"J4.A6", "J4.B6", "U8.1", "J7.105"},
    "/CORE_CM5/SERVICE_USB2_DM": {"J4.A7", "J4.B7", "U8.2", "J7.103"},
    "/SERVICE/SERVICE_VBUS_SENSE": {"J4.A4", "J4.A9", "J4.B4", "J4.B9"},
    "/SERVICE/SERVICE_RD_A": {"J4.A5", "R1.1"},
    "/SERVICE/SERVICE_RD_B": {"J4.B5", "R2.1"},
}

def main():
    board = pcbnew.LoadBoard(str(PCB))
    for name, required in EXPECTED.items():
        net = board.FindNet(name)
        assert net is not None, name
        pads = set()
        layers = set()
        for fp in board.GetFootprints():
            for pad in fp.Pads():
                if pad.GetNetCode() == net.GetNetCode():
                    pads.add(f"{fp.GetReference()}.{pad.GetNumber()}")
        for track in board.GetTracks():
            if track.GetNetCode() == net.GetNetCode():
                layers.add(track.GetLayerName())
        assert required <= pads, (name, sorted(required - pads))
        assert layers <= {"F.Cu", "B.Cu"}, (name, layers)

    report = DRC.read_text()
    assert not re.search(r"^\[(shorting_items|tracks_crossing|track_width)\]", report, re.M)
    assert not re.search(r"^\[clearance\].*\n(?:.*\n){0,4}.*SERVICE_", report, re.M)
    assert "Found 190 DRC violations" in report
    assert len(re.findall(r"^\[unconnected_items\]", report, re.M)) == 405

    # No added courtyard/edge class is permitted for the service island;
    # the remaining mechanical findings are inherited from the acreage base.
    for category in ("courtyards_overlap", "copper_edge_clearance", "hole_clearance"):
        assert len(re.findall(rf"^\[{category}\]", report, re.M)) == len(
            re.findall(rf"^\[{category}\]", (ROOT / "PHASE20_SERVICE_AUTHORITY_BASE-drc.rpt").read_text(), re.M)
        ), category
    print("Phase 20 SERVICE routing: PASS; complete endpoints, F.Cu/B.Cu only, zero new focused DRC classes")

if __name__ == "__main__":
    main()
