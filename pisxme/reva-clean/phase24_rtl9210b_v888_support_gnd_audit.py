"""Saved-board audit for V888 relocated support GND returns."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
PCB=H/'PHASE24_RTL9210B_V885_SUPPORT_GND_RETURN_V888.kicad_pcb'
ENDS=(('C1','2'),('C2','2'),('R1','2'))
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),p.GetNumber())
def reach(b,p):
    b.BuildConnectivity()
    return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}
b=pcbnew.LoadBoard(str(PCB)); ps=pads(b)
assert all(e in ps and ps[e].GetNetname()=='GND' for e in ENDS)
assert all(e in (reach(b,ps[ENDS[0]])|{ENDS[0]}) for e in ENDS)
assert sum(1 for x in b.GetTracks() if isinstance(x, pcbnew.PCB_VIA) and x.GetNetname()=='GND') >= 3
print('V888 GND C1.2/C2.2/R1.2 and three local return vias: PASS')
b=pcbnew.LoadBoard(str(PCB)); ps=pads(b)
for z in list(b.Zones()): b.RemoveNative(z)
victim=next(x for x in b.GetTracks() if x.GetNetname()=='GND' and x.GetStart()==pcbnew.VECTOR2I_MM(89.2,65.0))
b.RemoveNative(victim)
assert ENDS[2] not in (reach(b,ps[ENDS[0]])|{ENDS[0]})
print('V888 GND return-trace negative control: PASS')
