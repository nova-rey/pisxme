"""V1288 native coupled endpoints and saved-board negative control."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_COUPLED_1V1_SPICS_V1288.kicad_pcb'
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
b=pcbnew.LoadBoard(str(P));p=pads(b);b.BuildConnectivity();c=b.GetConnectivity();assert p[('C4','1')] in c.GetConnectedItems(p[('U1','25')]);assert p[('U2','1')] in c.GetConnectedItems(p[('U1','24')])
t=pcbnew.LoadBoard(str(P));pt=pads(t)
for q in list(t.GetTracks()):
 if q.GetNetname() in ('RTL_1V1','SPICS'):t.RemoveNative(q)
t.BuildConnectivity();assert pt[('C4','1')] not in t.GetConnectivity().GetConnectedItems(pt[('U1','25')]);assert pt[('U2','1')] not in t.GetConnectivity().GetConnectedItems(pt[('U1','24')])
print('PASS V1288 native coupled RTL_1V1/SPICS endpoints and saved-board negative control')
