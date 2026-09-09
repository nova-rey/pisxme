"""V1296 native RTL_5V endpoint and saved-board negative-control audit."""
from pathlib import Path
import pcbnew

P = Path(__file__).resolve().parent / 'PHASE24_RTL9210B_V735_SOURCE_RAILS_V1296.kicad_pcb'

def pads(board):
    return {(f.GetReference(), p.GetNumber()): p
            for f in board.GetFootprints() for p in f.Pads()}

def connected(board, pads_by_key, a, z):
    board.BuildConnectivity()
    assert pads_by_key[z] in board.GetConnectivity().GetConnectedItems(pads_by_key[a])

board = pcbnew.LoadBoard(str(P))
pa = pads(board)
connected(board, pa, ('U1', '33'), ('C5', '1'))

negative = pcbnew.LoadBoard(str(P))
pn = pads(negative)
for track in list(negative.GetTracks()):
    if track.GetNetname() == 'RTL_5V':
        negative.RemoveNative(track)
negative.BuildConnectivity()
assert pn[('C5', '1')] not in negative.GetConnectivity().GetConnectedItems(pn[('U1', '33')])
print('PASS V1296 native rotated RTL_5V source rail and saved-board negative control')
