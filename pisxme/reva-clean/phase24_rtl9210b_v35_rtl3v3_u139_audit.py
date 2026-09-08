"""Native audit for the U1.39/U2.8 RTL_3V3 discriminator."""
import sys,pcbnew
GROUP=[('U1','39'),('U2','8')]
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
 b.BuildConnectivity();q=pads(b);c=b.GetConnectivity().GetConnectedItems(q[GROUP[0]]);return all(q[x] in c for x in GROUP[1:])
b=pcbnew.LoadBoard(sys.argv[1]);assert ok(b)
source=pcbnew.LoadBoard(sys.argv[1]);ts=[x for x in source.GetTracks() if x.GetNetname()=='RTL_3V3'];assert ts
for i in range(len(ts)):
 t=pcbnew.LoadBoard(sys.argv[1]);cand=[x for x in t.GetTracks() if x.GetNetname()=='RTL_3V3'];t.RemoveNative(cand[i])
 if not ok(t):print('U1.39/U2.8 RTL_3V3: PASS; trace-removal negative control: PASS');break
else:raise AssertionError('trace-removal negative control unexpectedly passed')
