"""V1284 native SPICS endpoint and saved-board negative control."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_SPICS_LOW_ESCAPE_V1284.kicad_pcb'
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
b=pcbnew.LoadBoard(str(P));p=pads(b);u=p[('U1','24')];f=p[('U2','1')];b.BuildConnectivity();assert f in b.GetConnectivity().GetConnectedItems(u)
t=pcbnew.LoadBoard(str(P));pt=pads(t)
for q in list(t.GetTracks()):
 if q.GetNetname()=='SPICS':t.RemoveNative(q)
t.BuildConnectivity();assert pt[('U2','1')] not in t.GetConnectivity().GetConnectedItems(pt[('U1','24')])
print('PASS V1284 native U1.24-to-U2.1 SPICS endpoint and saved-board negative control')
