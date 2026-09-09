"""V1273 native pad-34/source-cohort audit."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_PAD34_3V3_V1273.kicad_pcb'
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
b=pcbnew.LoadBoard(str(P));p=pads(b);u=p[('U1','34')];c=p[('C3','1')];b.BuildConnectivity();assert c in b.GetConnectivity().GetConnectedItems(u)
t=pcbnew.LoadBoard(str(P));pt=pads(t)
for x in list(t.GetTracks()):
 if x.GetNetname()=='RTL_3V3' and (x.GetStart()==pt[('U1','34')].GetPosition() or x.GetEnd()==pt[('U1','34')].GetPosition()):t.RemoveNative(x)
t.BuildConnectivity();assert pt[('C3','1')] not in t.GetConnectivity().GetConnectedItems(pt[('U1','34')])
print('PASS V1273 native U1.34-to-C3 RTL_3V3 endpoint and source negative control')
