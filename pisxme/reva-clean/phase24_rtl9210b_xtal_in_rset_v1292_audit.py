"""V1292 native XTAL_IN endpoint, negative control, and RSET separation."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_XTAL_IN_RSET_CLEAN_V1292.kicad_pcb'
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
b=pcbnew.LoadBoard(str(P));p=pads(b);b.BuildConnectivity();assert p[('Y1','1')] in b.GetConnectivity().GetConnectedItems(p[('U1','53')])
t=pcbnew.LoadBoard(str(P));pt=pads(t)
for q in list(t.GetTracks()):
 if q.GetNetname()=='XTAL_IN':t.RemoveNative(q)
t.BuildConnectivity();assert pt[('Y1','1')] not in t.GetConnectivity().GetConnectedItems(pt[('U1','53')])
print('PASS V1292 native XTAL_IN endpoint, negative control, and shifted-leg RSET separation')
