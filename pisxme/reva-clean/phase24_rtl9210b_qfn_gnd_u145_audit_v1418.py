"""Native saved-board audit for the isolated U1.45 GND launch."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_RTL9210B_QFN_GND_U145_V1418.kicad_pcb'
def pads(b): return {(f.GetReference(),str(p.GetNumber())):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),str(p.GetNumber()))
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if hasattr(x,'GetParentFootprint') and x.GetParentFootprint() is not None}|{key(p)}
b=pcbnew.LoadBoard(str(PCB)); p=pads(b); assert {('U1','45'),('U1','69')}<=reach(b,p[('U1','45')])
t=pcbnew.LoadBoard(str(PCB)); q=pads(t); v=next(x for x in t.GetTracks() if x.GetNetname()=='GND' and not isinstance(x,pcbnew.PCB_VIA) and x.GetStart()==q[('U1','45')].GetPosition()); t.RemoveNative(v); assert ('U1','69') not in reach(t,pads(t)[('U1','45')])
print('PASS V1418 U1.45-to-exposed GND native connectivity and source-removal negative control')
