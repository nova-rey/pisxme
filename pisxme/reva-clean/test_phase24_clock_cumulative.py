"""Regression checks for the complete clock composition on the Phase 24 ancestor."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BOARD_PATH = ROOT / "PHASE24_LOCAL_REPAIRS_CLOCK_COMPLETE.kicad_pcb"
DRC_PATH = ROOT / "PHASE24_LOCAL_REPAIRS_CLOCK_COMPLETE-drc.rpt"
GROUPS = {
    "XI": {"Y1.1", "R23.1", "C42.1"},
    "XO": {"Y1.3", "R23.2", "C43.1"},
    "VSSOSC": {"Y1.2", "Y1.4", "C42.2", "C43.2"},
}


def native_component(board, token):
    ref, pin = token.split(".")
    pad = next(p for p in board.FindFootprintByReference(ref).Pads()
               if p.GetNumber() == pin)
    connectivity = board.GetConnectivity()
    return {f"{item.GetParentFootprint().GetReference()}.{item.GetNumber()}"
            for item in connectivity.GetConnectedItems(pad)
            if type(item).__name__ == "PAD"}


def main():
    board = pcbnew.LoadBoard(str(BOARD_PATH))
    board.BuildConnectivity()
    for name, expected in GROUPS.items():
        anchor = next(iter(expected))
        actual = native_component(board, anchor)
        missing = expected - actual
        assert not missing, f"{name} native component missing {sorted(missing)}"
    report = DRC_PATH.read_text(errors="replace")
    assert "[shorting_items]" not in report
    assert "[tracks_crossing]" not in report
    print("PASS: cumulative clock native components and short/crossing regression")


if __name__ == "__main__":
    main()
