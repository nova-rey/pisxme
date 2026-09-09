"""V1276 native pad-33/source-cohort audit."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_PAD33_5V_V1276.kicad_pcb'
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
b=pcbnew.LoadBoard(str(P));p=pads(b);u=p[('U1','33')];c=p[('C5','1')];b.BuildConnectivity();assert c in b.GetConnectivity().GetConnectedItems(u)
t=pcbnew.LoadBoard(str(P));pt=pads(t)
for x in list(t.GetTracks()):
 if x.GetNetname()=='RTL_5V' and (x.GetStart()==pt[('U1','33')].GetPosition() or x.GetEnd()==pt[('U1','33')].GetPosition()):t.RemoveNative(x)
t.BuildConnectivity();assert pt[('C5','1')] not in t.GetConnectivity().GetConnectedItems(pt[('U1','33')])
print('PASS V1276 native U1.33-to-C5 RTL_5V endpoint and source negative control')
