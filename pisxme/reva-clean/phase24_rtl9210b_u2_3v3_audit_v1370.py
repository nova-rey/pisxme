"""Native U2/R2/R3 RTL_3V3 support audit with source-removal control."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_RTL9210B_U2_3V3_SUPPORT_V1370.kicad_pcb'
ENDS=[('U2','3'),('U2','8'),('R2','2'),('R3','2')]
def pads(b): return {(f.GetReference(),str(p.GetNumber())):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),str(p.GetNumber()))
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if hasattr(x,'GetParentFootprint') and x.GetParentFootprint() is not None}|{key(p)}
b=pcbnew.LoadBoard(str(PCB)); p=pads(b); assert all(p[x].GetNetname()=='RTL_3V3' for x in ENDS); assert set(ENDS)<=reach(b,p[('U2','3')])
t=pcbnew.LoadBoard(str(PCB)); q=pads(t); victim=next(x for x in t.GetTracks() if x.GetNetname()=='RTL_3V3' and not isinstance(x,pcbnew.PCB_VIA) and x.GetStart()==q[('U2','3')].GetPosition()); t.RemoveNative(victim); assert ('R3','2') not in reach(t,pads(t)[('U2','3')]); print('PASS V1370 U2/R2/R3 RTL_3V3 native connectivity and source-removal negative control')
