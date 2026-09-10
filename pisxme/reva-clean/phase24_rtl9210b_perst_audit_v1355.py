"""Native control-net audit for the V1355 PERST/CLKREQ/PEDET coauthor."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
PCB = H / 'PHASE24_RTL9210B_PERST_LOWER_SHELF_V1355.kicad_pcb'

def pads(board):
    return {(f.GetReference(), str(p.GetNumber())): p
            for f in board.GetFootprints() for p in f.Pads()}

def connected(board, source, endpoints):
    board.BuildConnectivity(); p = pads(board)
    items = board.GetConnectivity().GetConnectedItems(p[source])
    return all(p[k] in items for k in endpoints)

checks = [
    (('U1', '13'), [('R3', '1'), ('J1', '52')], 'CLKREQ_N'),
    (('U1', '8'), [('R2', '1'), ('J1', '69')], 'PEDET'),
    (('U1', '14'), [('J1', '50')], 'PERST_N'),
]
for source, endpoints, name in checks:
    board = pcbnew.LoadBoard(str(PCB)); assert connected(board, source, endpoints), name
    board = pcbnew.LoadBoard(str(PCB)); p = pads(board)
    victim = next(x for x in board.GetTracks()
                  if x.GetNetname() == name and not isinstance(x, pcbnew.PCB_VIA)
                  and x.GetStart() == p[source].GetPosition())
    board.RemoveNative(victim)
    assert not connected(board, source, endpoints), name + ' negative control'
print('PASS V1355 native PERST/CLKREQ/PEDET endpoint connectivity and source-removal negative controls')
