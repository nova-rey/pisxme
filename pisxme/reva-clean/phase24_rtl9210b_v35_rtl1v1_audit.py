"""Native audit for the V35 lower RTL_1V1 fanout."""
import sys
import pcbnew
GROUP=[('U1','36'),('U1','40'),('U1','50'),('U1','55'),('U1','60'),('U1','63'),('C4','1')]
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
 b.BuildConnectivity(); q=pads(b); c=b.GetConnectivity().GetConnectedItems(q[GROUP[0]])
 return all(q[x] in c for x in GROUP[1:])
b=pcbnew.LoadBoard(sys.argv[1]); assert ok(b)
t=pcbnew.LoadBoard(sys.argv[1]); victim=next(x for x in t.GetTracks() if x.GetNetname()=='RTL_1V1'); t.RemoveNative(victim); assert not ok(t)
print('RTL_1V1 lower group: PASS; trace-removal negative control: PASS')
