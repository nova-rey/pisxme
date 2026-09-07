"""Saved-board native audit for the V35 moved XTAL/RSET support cluster."""
from pathlib import Path
import sys
import pcbnew

def pads(board, net):
    out=[]
    for f in board.GetFootprints():
        for p in f.Pads():
            if p.GetNetname()==net: out.append((f.GetReference(),p.GetName()))
    return set(out)

def connected(board, net):
    board.BuildConnectivity()
    return {tuple(x.split(':',1)) for x in []}  # replaced below

def audit(path, negative=False):
    b=pcbnew.LoadBoard(str(path)); b.BuildConnectivity()
    expected={'XTAL_IN':{('U1','53'),('Y1','1'),('C1','1')},
              'XTAL_OUT':{('U1','54'),('Y1','2'),('C2','1')},
              'RSET':{('U1','51'),('R1','1')}}
    for net,want in expected.items():
        actual=set(); c=b.GetConnectivity()
        for f in b.GetFootprints():
            for p in f.Pads():
                if p.GetNetname()!=net: continue
                group=c.GetConnectedItems(p)
                if any(type(q).__name__=='PAD' and q.GetNetname()==net for q in group):
                    actual.add((f.GetReference(),p.GetName()))
        missing=want-actual
        if missing: raise AssertionError(f'{net}: missing {sorted(missing)}')
        print(net+': PASS '+str(sorted(want)))
    if negative:
        removed=None
        for x in list(b.GetTracks()):
            if x.GetNetname()=='XTAL_OUT': removed=x; b.RemoveNative(x); break
        b.BuildConnectivity()
        lost=False
        for f in b.GetFootprints():
            for p in f.Pads():
                if p.GetNetname()=='XTAL_OUT' and (f.GetReference(),p.GetName()) in expected['XTAL_OUT']:
                    group=b.GetConnectivity().GetConnectedItems(p)
                    if len([q for q in group if type(q).__name__=='PAD' and q.GetNetname()=='XTAL_OUT']) < 3: lost=True
        if not lost: raise AssertionError('negative control unexpectedly passed')
        print('negative control: PASS (removed XTAL_OUT trace breaks connectivity)')

if __name__=='__main__':
    audit(Path(sys.argv[1]) if len(sys.argv)>1 else Path('PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35.kicad_pcb'), '--negative-controls' in sys.argv)
