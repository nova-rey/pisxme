"""Native connectivity regression for the complete Phase 24 clock fixture."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BOARD = R / "PHASE24_COMPLETE_CLOCK_FIXTURE_V2.kicad_pcb"
DRC = R / "PHASE24_COMPLETE_CLOCK_FIXTURE_V2-drc.rpt"
GROUPS = {
    "/STORAGE/BRIDGE_XI": {"Y1.1", "R23.1", "C42.1"},
    "/STORAGE/BRIDGE_XO": {"Y1.3", "R23.2", "C43.1"},
    "/STORAGE/BRIDGE_VSSOSC": {"Y1.2", "Y1.4", "C42.2", "C43.2"},
}

def pads(board):
    return {f"{fp.GetReference()}.{p.GetNumber()}": p
            for fp in board.GetFootprints() for p in fp.Pads()}

def test_clock_native_connectivity():
    board = pcbnew.LoadBoard(str(BOARD)); board.BuildConnectivity()
    allpads = pads(board); conn = board.GetConnectivity()
    for net, expected in GROUPS.items():
        for member in expected:
            assert member in allpads
            assert allpads[member].GetNetname() == net
            seen = {f"{i.GetParentFootprint().GetReference()}.{i.GetNumber()}"
                    for i in conn.GetConnectedItems(allpads[member])
                    if type(i).__name__ == "PAD"}
            assert expected <= seen | {member}, (net, member, seen)

def test_clock_native_drc_has_no_clock_short_or_crossing():
    report = DRC.read_text()
    assert "[shorting_items]" not in report
    assert "[tracks_crossing]" not in report

if __name__ == "__main__":
    test_clock_native_connectivity()
    test_clock_native_drc_has_no_clock_short_or_crossing()
    print("Phase24 complete clock fixture V2: PASS")
