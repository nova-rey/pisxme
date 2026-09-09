"""Saved-board endpoint and trace-removal audit for V851's SPI five-net field."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
PCB = H / 'PHASE24_RTL9210B_ROTATE_FLASH_270_SPI_CLEAN_CONTROLS_V851.kicad_pcb'
PAIRS = {
    'SPISI': (('U1', '18'), ('U2', '5')),
    'SPICLK': (('U1', '19'), ('U2', '6')),
    'SPISO3': (('U1', '22'), ('U2', '7')),
    'SPISO': (('U1', '23'), ('U2', '2')),
    'SPICS': (('U1', '24'), ('U2', '1')),
}

def pads(board):
    return {(f.GetReference(), p.GetNumber()): p
            for f in board.GetFootprints() for p in f.Pads()}

def key(p):
    return (p.GetParentFootprint().GetReference(), p.GetNumber())

def reach(board, pad):
    board.BuildConnectivity()
    return {key(x) for x in board.GetConnectivity().GetConnectedItems(pad)
            if type(x).__name__ in ('PAD', 'PCB_PAD')}

for net, ends in PAIRS.items():
    board = pcbnew.LoadBoard(str(PCB)); pp = pads(board)
    assert all(e in pp and pp[e].GetNetname() == net for e in ends)
    assert ends[1] in (reach(board, pp[ends[0]]) | {ends[0]})
    print(net, 'endpoint: PASS')
    board.BuildConnectivity()
    items = [x for x in board.GetConnectivity().GetConnectedItems(pp[ends[0]])
             if type(x).__name__ == 'PCB_TRACK' and x.GetNetname() == net]
    assert items
    for item in items:
        trial = pcbnew.LoadBoard(str(PCB))
        victim = next(x for x in trial.GetTracks()
                      if type(x).__name__ == 'PCB_TRACK'
                      and x.GetNetname() == net
                      and x.GetStart() == item.GetStart()
                      and x.GetEnd() == item.GetEnd())
        trial.RemoveNative(victim); qq = pads(trial)
        if ends[1] not in (reach(trial, qq[ends[0]]) | {ends[0]}):
            print(net, 'negative control: PASS'); break
    else:
        raise AssertionError(net + ' negative control failed')
