"""Native saved-board audit for V590; expected groups supply assertions only."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
PCB = H / 'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V590_PEDET_TOP_PERIMETER.kicad_pcb'

GROUPS = {
    'RTL_5V': [('U1','17'), ('U1','33'), ('C5','1')],
    'RTL_3V3': [('U1','20'), ('U1','34'), ('U1','39'), ('U1','52'),
                ('R2','2'), ('R3','2'), ('C3','1'), ('U2','3'), ('U2','8')],
    'PEDET': [('U1','8'), ('R2','1'), ('J1','69')],
}

def pads(board):
    return {(f.GetReference(), str(p.GetNumber())): p
            for f in board.GetFootprints() for p in f.Pads()}

def connected(board, group):
    board.BuildConnectivity()
    ps = pads(board)
    items = board.GetConnectivity().GetConnectedItems(ps[group[0]])
    return all(ps[item] in items for item in group[1:])

def main():
    b = pcbnew.LoadBoard(str(PCB))
    result = {name: connected(b, group) for name, group in GROUPS.items()}
    assert all(result.values()), result
    for name, group in GROUPS.items():
        t = pcbnew.LoadBoard(str(PCB))
        victims = [x for x in t.GetTracks() if x.GetNetname() == name]
        assert victims, name
        for x in victims:
            t.RemoveNative(x)
        assert not connected(t, group), name
    print('PASS V590 native 5V/3V3/PEDET connectivity; independent trace-removal negative controls PASS')

if __name__ == '__main__':
    main()
