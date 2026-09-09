"""V1272 native pad-25/source-cohort audit."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_PAD25_1V1_V1272.kicad_pcb'
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
b=pcbnew.LoadBoard(str(P));p=pads(b);u=p[('U1','25')];c=p[('C4','1')];b.BuildConnectivity();assert c in b.GetConnectivity().GetConnectedItems(u)
t=pcbnew.LoadBoard(str(P));pt=pads(t)
for x in list(t.GetTracks()):
 if x.GetNetname()=='RTL_1V1' and (x.GetStart()==pt[('U1','25')].GetPosition() or x.GetEnd()==pt[('U1','25')].GetPosition()):t.RemoveNative(x)
t.BuildConnectivity();assert pt[('C4','1')] not in t.GetConnectivity().GetConnectedItems(pt[('U1','25')])
print('PASS V1272 native U1.25-to-C4 RTL_1V1 endpoint and source negative control')
