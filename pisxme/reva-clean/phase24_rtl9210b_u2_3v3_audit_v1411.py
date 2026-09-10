"""Native saved-board audit for the V1411 RTL_3V3 outboard join."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_RTL9210B_U2_3V3_OUTBOARD_DOGLEG_V1411.kicad_pcb'
ENDS=[('U1',n) for n in ('20','34','39','52')]+[('U2',n) for n in ('3','8')]+[('R2','2'),('R3','2'),('C3','1')]
def pads(b): return {(f.GetReference(),str(p.GetNumber())):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),str(p.GetNumber()))
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if hasattr(x,'GetParentFootprint') and x.GetParentFootprint() is not None}|{key(p)}
b=pcbnew.LoadBoard(str(PCB)); p=pads(b); assert set(ENDS)<=reach(b,p[('U2','3')])
t=pcbnew.LoadBoard(str(PCB)); q=pads(t); v=next(x for x in t.GetTracks() if x.GetNetname()=='RTL_3V3' and not isinstance(x,pcbnew.PCB_VIA) and x.GetStart()==q[('U2','3')].GetPosition()); t.RemoveNative(v); assert ('U1','20') not in reach(t,pads(t)[('U2','3')])
print('PASS V1411 RTL_3V3 U2.3/U2.8/U1.20/U1.34/U1.39/U1.52/R2.2/R3.2/C3.1 connectivity and source-removal negative control')
