"""Native saved-board audit for the V488 crystal support primitive."""
import pcbnew
from pathlib import Path

PCB = Path(__file__).resolve().parent / 'PHASE24_RTL9210B_CRYSTAL_SUPPORT_V488.kicad_pcb'
GROUPS = {
    'XTAL_IN': [('U1','53'), ('Y1','1'), ('C1','1')],
    'XTAL_OUT': [('U1','54'), ('Y1','2'), ('C2','1')],
}

def padmap(board):
    return {(f.GetReference(), p.GetNumber()): p
            for f in board.GetFootprints() for p in f.Pads()}

def connected(board, group):
    board.BuildConnectivity()
    pads = padmap(board)
    root = pads[group[0]]
    items = board.GetConnectivity().GetConnectedItems(root)
    return all(pads[item] in items for item in group[1:])

def main():
    board = pcbnew.LoadBoard(str(PCB))
    result = {name: connected(board, group) for name, group in GROUPS.items()}
    if not all(result.values()):
        board.BuildConnectivity(); pads = padmap(board)
        for name, group in GROUPS.items():
            root = pads[group[0]]
            items = board.GetConnectivity().GetConnectedItems(root)
            print(name, [(x, pads[x] in items) for x in group])
        raise AssertionError(result)
    for name in GROUPS:
        trial = pcbnew.LoadBoard(str(PCB))
        victims = [item for item in trial.GetTracks() if item.GetNetname() == name]
        assert victims, name
        for item in victims:
            trial.RemoveNative(item)
        assert not connected(trial, GROUPS[name]), name
    print('PASS V488 native XTAL_IN/XTAL_OUT connectivity; two trace-removal negative controls PASS')

if __name__ == '__main__':
    main()
