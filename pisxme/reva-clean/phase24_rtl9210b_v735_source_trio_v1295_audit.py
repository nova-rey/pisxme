"""V1295 native rotated source-trio endpoints and negative controls."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_V735_SOURCE_TRIO_V1295.kicad_pcb'
def pads(b):
 return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def chk(b,a,z):
 p=pads(b);b.BuildConnectivity();assert p[z] in b.GetConnectivity().GetConnectedItems(p[a])
b=pcbnew.LoadBoard(str(P));chk(b,('U1','25'),('C4','1'));chk(b,('U1','34'),('C3','1'))
t=pcbnew.LoadBoard(str(P));pt=pads(t)
for q in list(t.GetTracks()):
 if q.GetNetname() in ('RTL_1V1','RTL_3V3'):t.RemoveNative(q)
t.BuildConnectivity();assert pt[('C4','1')] not in t.GetConnectivity().GetConnectedItems(pt[('U1','25')]);assert pt[('C3','1')] not in t.GetConnectivity().GetConnectedItems(pt[('U1','34')])
print('PASS V1295 native rotated RTL_1V1/RTL_3V3 source trio and saved-board negative controls')
