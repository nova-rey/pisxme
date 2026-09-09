"""V1263 native saved-board RXN endpoint and source negative-control audit."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_RXN_SOURCE_REHOME_FOR_SUPPORT_V1263.kicad_pcb'
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def via_at(b,net,xy):
    target=pcbnew.VECTOR2I_MM(*xy)
    return next(x for x in b.GetTracks() if type(x).__name__=='PCB_VIA' and x.GetNetname()==net and x.GetPosition()==target)
b=pcbnew.LoadBoard(str(P));p=pads(b);u=p[('U1','65')];j=p[('J1','41')];v=via_at(b,'LANE0_RXN',(91.0,69.8));b.BuildConnectivity()
items=b.GetConnectivity().GetConnectedItems(u);assert j in items and v in items
t=pcbnew.LoadBoard(str(P));pt=pads(t);sv=via_at(t,'LANE0_RXN',(91.0,69.8))
for x in list(t.GetTracks()):
    if x.GetNetname()=='LANE0_RXN' and (x is sv or (type(x).__name__!='PCB_VIA' and x.GetStart()==pt[('U1','65')].GetPosition())): t.RemoveNative(x)
t.BuildConnectivity();assert pt[('J1','41')] not in t.GetConnectivity().GetConnectedItems(pt[('U1','65')])
print('PASS V1263 native RXN endpoint and source-cohort negative control')
