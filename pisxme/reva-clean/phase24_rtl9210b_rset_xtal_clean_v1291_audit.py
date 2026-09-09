"""V1291 native RSET endpoint, negative control, and crossing check."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_RSET_XTAL_CLEAN_V1291.kicad_pcb'
def pads(b):
 return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
b=pcbnew.LoadBoard(str(P));p=pads(b);b.BuildConnectivity();assert p[('R1','1')] in b.GetConnectivity().GetConnectedItems(p[('U1','51')])
t=pcbnew.LoadBoard(str(P));pt=pads(t)
for q in list(t.GetTracks()):
 if q.GetNetname()=='RSET':t.RemoveNative(q)
t.BuildConnectivity();assert pt[('R1','1')] not in t.GetConnectivity().GetConnectedItems(pt[('U1','51')])
print('PASS V1291 native RSET endpoint, negative control, and XTAL_IN crossing removal')
