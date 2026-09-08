"""Native audit for the V35 upper RTL_3V3 field."""
import sys
import pcbnew
GROUP=[('U1','20'),('U1','34'),('R2','2'),('R3','2'),('C3','1')]
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
 b.BuildConnectivity();q=pads(b);c=b.GetConnectivity().GetConnectedItems(q[GROUP[0]])
 return all(q[x] in c for x in GROUP[1:])
b=pcbnew.LoadBoard(sys.argv[1]);assert ok(b)
source=pcbnew.LoadBoard(sys.argv[1]);victims=[x for x in source.GetTracks() if x.GetNetname()=='RTL_3V3']
assert victims
for i in range(len(victims)):
 t=pcbnew.LoadBoard(sys.argv[1]);ts=[x for x in t.GetTracks() if x.GetNetname()=='RTL_3V3'];t.RemoveNative(ts[i])
 if not ok(t): print('RTL_3V3 upper group: PASS; trace-removal negative control: PASS');break
else: raise AssertionError('trace-removal negative control unexpectedly passed')
