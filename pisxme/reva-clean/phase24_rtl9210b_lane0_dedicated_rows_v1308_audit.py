"""V1308 saved-board lane audit; expected connectivity supplies assertions only."""
from pathlib import Path
import pcbnew

PCB = Path(__file__).resolve().parent / "PHASE24_RTL9210B_LANE0_DEDICATED_ROWS_V1308.kicad_pcb"
PAIRS = [("64", "43", "LANE0_RXP"), ("65", "41", "LANE0_RXN"),
         ("67", "47", "LANE0_TXN"), ("68", "49", "LANE0_TXP")]

def pads(board):
    return {(f.GetReference(), p.GetNumber()): p
            for f in board.GetFootprints() for p in f.Pads()}

def linked(board, a, z):
    board.BuildConnectivity(); p = pads(board)
    return p[z] in board.GetConnectivity().GetConnectedItems(p[a])

board = pcbnew.LoadBoard(str(PCB))
assert all(linked(board, ("U1", u), ("J1", j)) for u, j, _ in PAIRS)

# Remove each pair's complete source cohort from a fresh native board.  A
# passing audit must then lose only that pair's endpoint connection.
for u, j, net in PAIRS:
    trial = pcbnew.LoadBoard(str(PCB)); p = pads(trial)
    src = p[("U1", u)].GetPosition()
    cohort = [q for q in trial.GetTracks() if q.GetNetname() == net]
    assert cohort, net + " source cohort missing"
    for q in cohort:
        trial.RemoveNative(q)
    assert not linked(trial, ("U1", u), ("J1", j)), net + " negative control did not fail"

print("PASS V1308 native four-pair endpoint connectivity; four complete source-cohort negative controls PASS")
