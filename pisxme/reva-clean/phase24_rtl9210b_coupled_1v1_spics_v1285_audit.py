"""V1285 native coupled endpoint and negative-control audit."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_COUPLED_1V1_SPICS_V1285.kicad_pcb'
def pads(b):
 return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def check(b,ends):
 p=pads(b);b.BuildConnectivity();assert p[ends[1]] in b.GetConnectivity().GetConnectedItems(p[ends[0]])
b=pcbnew.LoadBoard(str(P));check(b,[("U1","25"),("C4","1")]);check(b,[("U1","24"),("U2","1")])
t=pcbnew.LoadBoard(str(P));pt=pads(t)
for q in list(t.GetTracks()):
 if q.GetNetname() in ('RTL_1V1','SPICS'):t.RemoveNative(q)
t.BuildConnectivity();assert pt[("C4","1")] not in t.GetConnectivity().GetConnectedItems(pt[("U1","25")]);assert pt[("U2","1")] not in t.GetConnectivity().GetConnectedItems(pt[("U1","24")])
print('PASS V1285 native coupled RTL_1V1/SPICS endpoints and saved-board negative control')
