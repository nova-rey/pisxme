"""Native saved-board audit for V1384 U1.25 RTL_1V1 fanout.

Connectivity is derived only from pcbnew's saved-board copper connectivity;
the expected endpoint list is an assertion, not a synthetic graph.
"""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
PCB = H / "PHASE24_RTL9210B_U125_1V1_FANOUT_V1384.kicad_pcb"
ENDS = [("U1", n) for n in ("16", "25", "36", "40", "50", "55")] + [("C4", "1")]

def pads(board):
    return {(f.GetReference(), str(p.GetNumber())): p
            for f in board.GetFootprints() for p in f.Pads()}

def key(pad):
    return (pad.GetParentFootprint().GetReference(), str(pad.GetNumber()))

def reach(board, pad):
    board.BuildConnectivity()
    return ({key(item) for item in board.GetConnectivity().GetConnectedItems(pad)
             if hasattr(item, "GetParentFootprint")
             and item.GetParentFootprint() is not None} | {key(pad)})

board = pcbnew.LoadBoard(str(PCB))
board_pads = pads(board)
assert set(ENDS) <= reach(board, board_pads[("U1", "25")])

# Negative control: removing the required source segment must break the
# saved-board connectivity; no expected edge is injected by this test.
negative = pcbnew.LoadBoard(str(PCB))
negative_pads = pads(negative)
victim = next(track for track in negative.GetTracks()
              if track.GetNetname() == "RTL_1V1"
              and not isinstance(track, pcbnew.PCB_VIA)
              and track.GetStart() == negative_pads[("U1", "25")].GetPosition())
negative.RemoveNative(victim)
assert ("C4", "1") not in reach(negative, pads(negative)[("U1", "25")])

print("PASS V1384 RTL_1V1 U1.16/U1.25/U1.36/U1.40/U1.50/U1.55/C4 connectivity and source-removal negative control")
