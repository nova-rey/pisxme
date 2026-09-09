"""V1134 saved-board RTL_3V3 audit and source-trace negative control."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_RTL3V3_STUB_SCRUB_V1134.kicad_pcb'
END=[('U1','20'),('U1','34'),('U1','39'),('U1','52'),('U2','3'),('U2','8'),('R2','2'),('R3','2'),('C3','1')]
def key(p): return (p.GetParentFootprint().GetReference(),p.GetNumber())
def pads(b): return {key(p):p for f in b.GetFootprints() for p in f.Pads()}
def reach(b,p):
 b.BuildConnectivity();return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if x.GetParentFootprint()}|{key(p)}
b=pcbnew.LoadBoard(str(PCB));p=pads(b);assert all(p[e].GetNetname()=='RTL_3V3' for e in END);assert set(END)<=reach(b,p[END[0]]);print('V1134 RTL_3V3 endpoint group: PASS')
t=pcbnew.LoadBoard(str(PCB));q=pads(t);start=q[('U1','52')].GetPosition();seg=next(x for x in t.GetTracks() if type(x).__name__=='PCB_TRACK' and x.GetNetname()=='RTL_3V3' and (x.GetStart()==start or x.GetEnd()==start));t.RemoveNative(seg);assert ('C3','1') not in reach(t,q[('U1','52')]);print('U1.52 source-trace negative control: PASS')
