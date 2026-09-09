"""V1266 native saved-board coupled source-field audit."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_COUPLED_RXN_1V1_SOURCEFIELD_V1266.kicad_pcb'
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
b=pcbnew.LoadBoard(str(P));p=pads(b);b.BuildConnectivity()
for u,j in [(('U1','65'),('J1','41')),(('U1','60'),('C4','1')),(('U1','63'),('C4','1'))]: assert p[j] in b.GetConnectivity().GetConnectedItems(p[u])
for u in [('U1','65'),('U1','60'),('U1','63')]:
 t=pcbnew.LoadBoard(str(P));pt=pads(t)
 for x in list(t.GetTracks()):
  if x.GetNetname() in ('LANE0_RXN','RTL_1V1') and (x.GetStart()==pt[u].GetPosition() or x.GetEnd()==pt[u].GetPosition()):t.RemoveNative(x)
 t.BuildConnectivity();target=('J1','41') if u[1]=='65' else ('C4','1');assert pt[target] not in t.GetConnectivity().GetConnectedItems(pt[u])
print('PASS V1266 native RXN plus two RTL_1V1 endpoints and three source negative controls')
