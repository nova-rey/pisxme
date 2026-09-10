"""Native saved-board audit for the V1374 U1.50 RTL_1V1 repair."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_RTL9210B_U150_1V1_UPPER_V1374.kicad_pcb'
ENDS=[('U1','36'),('U1','40'),('U1','50'),('C4','1')]
def pads(b): return {(f.GetReference(),str(p.GetNumber())):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),str(p.GetNumber()))
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if hasattr(x,'GetParentFootprint') and x.GetParentFootprint() is not None}|{key(p)}
b=pcbnew.LoadBoard(str(PCB)); p=pads(b); assert set(ENDS)<=reach(b,p[('U1','50')])
t=pcbnew.LoadBoard(str(PCB)); q=pads(t); victim=next(x for x in t.GetTracks() if x.GetNetname()=='RTL_1V1' and not isinstance(x,pcbnew.PCB_VIA) and x.GetStart()==q[('U1','50')].GetPosition()); t.RemoveNative(victim); assert ('C4','1') not in reach(t,pads(t)[('U1','50')])
print('PASS V1374 U1.36/U1.40/U1.50/C4 RTL_1V1 native connectivity and source-removal negative control')
