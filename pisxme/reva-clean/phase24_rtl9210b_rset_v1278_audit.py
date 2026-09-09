"""V1278 native RSET endpoint and trace-removal negative control."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_RSET_LIVE_PAD_V1278.kicad_pcb'
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
b=pcbnew.LoadBoard(str(P));p=pads(b);u=p[('U1','51')];r=p[('R1','1')];b.BuildConnectivity();assert r in b.GetConnectivity().GetConnectedItems(u)
t=pcbnew.LoadBoard(str(P));pt=pads(t)
for x in list(t.GetTracks()):
 if x.GetNetname()=='RSET' and (x.GetStart()==pt[('U1','51')].GetPosition() or x.GetEnd()==pt[('U1','51')].GetPosition()):t.RemoveNative(x)
t.BuildConnectivity();assert pt[('R1','1')] not in t.GetConnectivity().GetConnectedItems(pt[('U1','51')])
print('PASS V1278 native U1.51-to-R1.1 RSET endpoint and source negative control')
