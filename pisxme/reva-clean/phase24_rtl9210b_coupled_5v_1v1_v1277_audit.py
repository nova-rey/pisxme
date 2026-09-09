"""V1277 native coupled RTL_5V/RTL_1V1 endpoint audit."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_COUPLED_5V_1V1_SOURCEFIELD_V1277.kicad_pcb'
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
checks=[(('U1','25'),('C4','1'),'RTL_1V1'),(('U1','33'),('C5','1'),'RTL_5V')]
b=pcbnew.LoadBoard(str(P));p=pads(b);b.BuildConnectivity()
for u,c,_ in checks:assert p[c] in b.GetConnectivity().GetConnectedItems(p[u])
for u,c,net in checks:
 t=pcbnew.LoadBoard(str(P));pt=pads(t)
 for x in list(t.GetTracks()):
  if x.GetNetname()==net and (x.GetStart()==pt[u].GetPosition() or x.GetEnd()==pt[u].GetPosition()):t.RemoveNative(x)
 t.BuildConnectivity();assert pt[c] not in t.GetConnectivity().GetConnectedItems(pt[u])
print('PASS V1277 native U1.25/C4 and U1.33/C5 endpoints; two source negative controls')
