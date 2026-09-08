"""Native audit for the complete V35 RTL_3V3 endpoint group."""
import sys,pcbnew
GROUP=[('U1','20'),('U1','34'),('U1','39'),('U1','52'),('R2','2'),('R3','2'),('C3','1'),('U2','3'),('U2','8')]
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
 b.BuildConnectivity();q=pads(b);c=b.GetConnectivity().GetConnectedItems(q[GROUP[0]]);return all(q[x] in c for x in GROUP[1:])
b=pcbnew.LoadBoard(sys.argv[1]);assert ok(b)
src=pcbnew.LoadBoard(sys.argv[1]);ts=[x for x in src.GetTracks() if x.GetNetname()=='RTL_3V3'];assert ts
for i in range(len(ts)):
 t=pcbnew.LoadBoard(sys.argv[1]);cand=[x for x in t.GetTracks() if x.GetNetname()=='RTL_3V3'];t.RemoveNative(cand[i])
 if not ok(t):print('RTL_3V3 full group: PASS; trace-removal negative control: PASS');break
else:raise AssertionError('trace-removal negative control unexpectedly passed')
