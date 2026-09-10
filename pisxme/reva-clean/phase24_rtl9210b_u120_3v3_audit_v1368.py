"""Native saved-board audit for the V1368 RTL_3V3 endpoint group."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_RTL9210B_U120_3V3_V1064_TRANSPLANT_V1368.kicad_pcb'
ENDS=[('U1','20'),('U1','34'),('U1','39'),('U1','52'),('C3','1')]
def pads(b): return {(f.GetReference(),str(p.GetNumber())):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),str(p.GetNumber()))
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p)
     if hasattr(x,'GetParentFootprint') and x.GetParentFootprint() is not None}|{key(p)}
b=pcbnew.LoadBoard(str(PCB)); p=pads(b); assert all(p[x].GetNetname()=='RTL_3V3' for x in ENDS); assert set(ENDS)<=reach(b,p[('U1','20')])
t=pcbnew.LoadBoard(str(PCB)); q=pads(t); victim=next(x for x in t.GetTracks() if x.GetNetname()=='RTL_3V3' and not isinstance(x,pcbnew.PCB_VIA) and x.GetStart()==q[('U1','20')].GetPosition()); t.RemoveNative(victim); assert ('U2','3') not in reach(t,pads(t)[('U1','20')])
print('PASS V1368 RTL_3V3 U1.20/U1.34/U1.39/U1.52/C3 saved-board connectivity and source-removal negative control')
