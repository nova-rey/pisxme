"""Native V702 RTL_5V audit with a targeted handoff-via negative control."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
PCB = H / 'PHASE24_RTL9210B_SUPPORT_RELOCATION_5V_U117_V702.kicad_pcb'
GROUP = [('U1', '17'), ('U1', '33'), ('C5', '1')]

def pads(board):
    return {(f.GetReference(), p.GetNumber()): p
            for f in board.GetFootprints() for p in f.Pads()}

def connected(board):
    board.BuildConnectivity()
    ps = pads(board)
    root = ps[GROUP[0]]
    items = board.GetConnectivity().GetConnectedItems(root)
    return all(ps[k] in items for k in GROUP[1:])

board = pcbnew.LoadBoard(str(PCB))
assert connected(board), 'V702 RTL_5V endpoints are not natively connected'
trial = pcbnew.LoadBoard(str(PCB))
handoff = None
for item in trial.GetTracks():
    if type(item).__name__ == 'PCB_VIA' and item.GetNetname() == 'RTL_5V':
        p = item.GetPosition()
        xy = (round(pcbnew.ToMM(p.x), 3), round(pcbnew.ToMM(p.y), 3))
        if xy == (102.2, 76.2):
            handoff = item
            break
assert handoff is not None, 'V702 handoff via missing'
trial.RemoveNative(handoff)
assert not connected(trial), 'handoff-via removal unexpectedly preserved connectivity'
print('PASS V702 native U1.17/U1.33/C5.1 connectivity; handoff-via negative control PASS')
