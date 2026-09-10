"""Native saved-board audit for V1415 RTL_5V fan-in."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_RTL9210B_RTL5V_U117_FCU_RIGHT_V1415.kicad_pcb'
ENDS=[('U1','17'),('U1','33'),('C5','1')]
def pads(b): return {(f.GetReference(),str(p.GetNumber())):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),str(p.GetNumber()))
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if hasattr(x,'GetParentFootprint') and x.GetParentFootprint() is not None}|{key(p)}
b=pcbnew.LoadBoard(str(PCB)); p=pads(b); assert set(ENDS)<=reach(b,p[('U1','17')])
t=pcbnew.LoadBoard(str(PCB)); q=pads(t); v=next(x for x in t.GetTracks() if x.GetNetname()=='RTL_5V' and not isinstance(x,pcbnew.PCB_VIA) and x.GetStart()==q[('U1','17')].GetPosition()); t.RemoveNative(v); assert ('C5','1') not in reach(t,pads(t)[('U1','17')])
print('PASS V1415 RTL_5V U1.17/U1.33/C5.1 connectivity and source-removal negative control')
