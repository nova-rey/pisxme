"""V1275 native coupled rail endpoint and negative-control audit."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_COUPLED_PAD39_3V3_PAD40_1V1_V1275.kicad_pcb'
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
checks=[(('U1','39'),('C3','1'),'RTL_3V3'),(('U1','40'),('C4','1'),'RTL_1V1')]
b=pcbnew.LoadBoard(str(P));p=pads(b);b.BuildConnectivity()
for u,c,_ in checks:assert p[c] in b.GetConnectivity().GetConnectedItems(p[u])
for u,c,net in checks:
 t=pcbnew.LoadBoard(str(P));pt=pads(t)
 for x in list(t.GetTracks()):
  if x.GetNetname()==net and (x.GetStart()==pt[u].GetPosition() or x.GetEnd()==pt[u].GetPosition()):t.RemoveNative(x)
 t.BuildConnectivity();assert pt[c] not in t.GetConnectivity().GetConnectedItems(pt[u])
print('PASS V1275 native U1.39/U1.40 rail endpoints and two source negative controls')
