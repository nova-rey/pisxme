"""Consolidated saved-board audit for the native-clean V862 support basis.

Connectivity is derived only from the loaded PCB's pads, tracks, vias and
zones. The endpoint table is assertion input; it never supplies graph edges.
"""
from pathlib import Path
import pcbnew

PCB = Path(__file__).resolve().parent / 'PHASE24_RTL9210B_V860_5V_ADD_U133_V862.kicad_pcb'
TARGETS = {
    'SPISI': (('U1','18'), ('U2','5')),
    'SPICLK': (('U1','19'), ('U2','6')),
    'SPISO3': (('U1','22'), ('U2','7')),
    'SPISO': (('U1','23'), ('U2','2')),
    'SPICS': (('U1','24'), ('U2','1')),
    'PERST_N': (('U1','14'), ('J1','50')),
    'XTAL_IN': (('U1','53'), ('Y1','1'), ('C1','1')),
    'XTAL_OUT': (('U1','54'), ('Y1','2'), ('C2','1')),
    'RSET': (('U1','51'), ('R1','1')),
    'RTL_5V': (('U1','17'), ('U1','33'), ('C5','1')),
}

def pads(board):
    return {(f.GetReference(), p.GetNumber()): p
            for f in board.GetFootprints() for p in f.Pads()}

def key(pad):
    return (pad.GetParentFootprint().GetReference(), pad.GetNumber())

def reachable(board, pad):
    board.BuildConnectivity()
    return {key(item) for item in board.GetConnectivity().GetConnectedItems(pad)
            if type(item).__name__ in ('PAD', 'PCB_PAD')}

def negative(net, src, dst, original):
    probe = pcbnew.LoadBoard(str(PCB)); pp = pads(probe)
    probe.BuildConnectivity()
    tracks = [item for item in probe.GetConnectivity().GetConnectedItems(pp[src])
              if type(item).__name__ == 'PCB_TRACK' and item.GetNetname() == net]
    assert tracks, f'{net}: no source track'
    for item in tracks:
        test = pcbnew.LoadBoard(str(PCB)); tp = pads(test)
        victim = next((x for x in test.GetTracks()
                       if type(x).__name__ == 'PCB_TRACK'
                       and x.GetNetname() == net
                       and ((x.GetStart() == item.GetStart() and x.GetEnd() == item.GetEnd())
                            or (x.GetStart() == item.GetEnd() and x.GetEnd() == item.GetStart()))), None)
        if victim is None:
            continue
        test.RemoveNative(victim)
        if dst not in (reachable(test, tp[src]) | {src}):
            return
    raise AssertionError(f'{net}: negative control did not disconnect {src}->{dst}')

board = pcbnew.LoadBoard(str(PCB)); p = pads(board)
for net, ends in TARGETS.items():
    assert all(e in p and p[e].GetNetname() == net for e in ends), (net, ends)
    source = p[ends[0]]; got = reachable(board, source) | {ends[0]}
    assert all(e in got for e in ends), (net, ends, got)
    print(net, 'endpoint: PASS')
    if net != 'RTL_5V':
        negative(net, ends[0], ends[1], p)
        print(net, 'negative control: PASS')
negative('RTL_5V', TARGETS['RTL_5V'][0], TARGETS['RTL_5V'][-1], p)
print('RTL_5V negative control: PASS')
print('V862 consolidated support audit: PASS')
