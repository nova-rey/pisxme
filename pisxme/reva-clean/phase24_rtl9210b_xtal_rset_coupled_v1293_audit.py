"""V1293 native coupled endpoints and saved-board negative controls."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_XTAL_RSET_COUPLED_CLEAN_V1293.kicad_pcb'
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
b=pcbnew.LoadBoard(str(P));p=pads(b);b.BuildConnectivity();c=b.GetConnectivity();assert p[('Y1','1')] in c.GetConnectedItems(p[('U1','53')]);assert p[('R1','1')] in c.GetConnectedItems(p[('U1','51')])
t=pcbnew.LoadBoard(str(P));pt=pads(t)
for q in list(t.GetTracks()):
 if q.GetNetname() in ('XTAL_IN','RSET'):t.RemoveNative(q)
t.BuildConnectivity();assert pt[('Y1','1')] not in t.GetConnectivity().GetConnectedItems(pt[('U1','53')]);assert pt[('R1','1')] not in t.GetConnectivity().GetConnectedItems(pt[('U1','51')])
print('PASS V1293 native coupled XTAL_IN/RSET endpoints and saved-board negative controls')
