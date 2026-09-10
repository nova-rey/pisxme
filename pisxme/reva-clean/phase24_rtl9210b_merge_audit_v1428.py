"""Saved-board audit for composed accepted Path-B primitives (V1428)."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb'
def pads(b): return {(f.GetReference(),str(p.GetNumber())):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),str(p.GetNumber()))
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if hasattr(x,'GetParentFootprint') and x.GetParentFootprint() is not None}|{key(p)}
b=pcbnew.LoadBoard(str(PCB)); p=pads(b)
assert {('J1',str(n)) for n in (2,4,6,8)} <= reach(b,p[('J1','2')])
assert {('U1','45'),('U1','69')} <= reach(b,p[('U1','45')])
t=pcbnew.LoadBoard(str(PCB)); q=pads(t); v=next(x for x in t.GetTracks() if x.GetNetname()=='SSD_3V3' and not isinstance(x,pcbnew.PCB_VIA) and x.GetStart()==q[('J1','2')].GetPosition()); t.RemoveNative(v)
assert ('J1','4') not in reach(t,pads(t)[('J1','2')])
t=pcbnew.LoadBoard(str(PCB)); q=pads(t); v=next(x for x in t.GetTracks() if x.GetNetname()=='GND' and not isinstance(x,pcbnew.PCB_VIA) and x.GetStart()==q[('U1','45')].GetPosition()); t.RemoveNative(v)
assert ('U1','69') not in reach(t,pads(t)[('U1','45')])
print('PASS V1428 composed V1418 GND + V1420 SSD_3V3 native connectivity and two source-removal controls')
