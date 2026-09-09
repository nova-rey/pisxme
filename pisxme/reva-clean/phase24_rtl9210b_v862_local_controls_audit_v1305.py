"""V1305 saved-board PEDET/CLKREQ_N local-control audit."""
from pathlib import Path
import pcbnew

P = Path(__file__).resolve().parent / 'PHASE24_RTL9210B_V860_5V_ADD_U133_V862.kicad_pcb'
TARGETS = {
    'PEDET': (('U1','8'), ('R2','1')),
    'CLKREQ_N': (('U1','13'), ('R3','1')),
}

def pads(b):
    return {(f.GetReference(), p.GetNumber()): p
            for f in b.GetFootprints() for p in f.Pads()}
def key(p):
    return (p.GetParentFootprint().GetReference(), p.GetNumber())
def reach(b, p):
    b.BuildConnectivity()
    return {key(x) for x in b.GetConnectivity().GetConnectedItems(p)
            if type(x).__name__ in ('PAD', 'PCB_PAD')}

for net, ends in TARGETS.items():
    b = pcbnew.LoadBoard(str(P)); p = pads(b)
    assert all(e in p and p[e].GetNetname() == net for e in ends), (net, ends)
    assert ends[1] in (reach(b, p[ends[0]]) | {ends[0]}), (net, ends)
    print(net, 'endpoint: PASS')
    b.BuildConnectivity()
    source_tracks = [x for x in b.GetConnectivity().GetConnectedItems(p[ends[0]])
                     if type(x).__name__ == 'PCB_TRACK' and x.GetNetname() == net]
    assert source_tracks, net
    for item in source_tracks:
        t = pcbnew.LoadBoard(str(P)); q = pads(t)
        victim = next((x for x in t.GetTracks()
                       if type(x).__name__ == 'PCB_TRACK'
                       and x.GetNetname() == net
                       and ((x.GetStart() == item.GetStart() and x.GetEnd() == item.GetEnd())
                            or (x.GetStart() == item.GetEnd() and x.GetEnd() == item.GetStart()))), None)
        if victim is None:
            continue
        t.RemoveNative(victim)
        assert ends[1] not in (reach(t, q[ends[0]]) | {ends[0]}), net
        print(net, 'negative control: PASS')
        break
    else:
        raise AssertionError(net + ' negative control failed')
print('V1305 local PEDET/CLKREQ_N control audit: PASS')
