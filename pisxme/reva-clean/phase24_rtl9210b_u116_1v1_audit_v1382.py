"""Native saved-board audit for V1382 U1.16 RTL_1V1."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_RTL9210B_U116_1V1_LOWER_HANDOFF_V1382.kicad_pcb'
ENDS=[('U1','16'),('U1','36'),('U1','40'),('U1','50'),('U1','55'),('C4','1')]
def pads(b): return {(f.GetReference(),str(p.GetNumber())):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),str(p.GetNumber()))
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if hasattr(x,'GetParentFootprint') and x.GetParentFootprint() is not None}|{key(p)}
b=pcbnew.LoadBoard(str(PCB)); p=pads(b); assert set(ENDS)<=reach(b,p[('U1','16')])
t=pcbnew.LoadBoard(str(PCB)); q=pads(t); victim=next(x for x in t.GetTracks() if x.GetNetname()=='RTL_1V1' and not isinstance(x,pcbnew.PCB_VIA) and x.GetStart()==q[('U1','16')].GetPosition()); t.RemoveNative(victim); assert ('C4','1') not in reach(t,pads(t)[('U1','16')]); print('PASS V1382 U1.16 RTL_1V1 native connectivity and source-removal negative control')
