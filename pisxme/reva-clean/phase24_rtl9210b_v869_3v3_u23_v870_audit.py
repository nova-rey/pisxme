"""Saved-board RTL_3V3 U2.3/U2.8/C3.1 audit with negative control."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_RTL9210B_V869_3V3_U23_V870.kicad_pcb'
ENDS=(('U2','3'),('U2','8'),('C3','1'))
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),p.GetNumber())
def reach(b,p): b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}
b=pcbnew.LoadBoard(str(PCB));p=pads(b);assert all(e in p and p[e].GetNetname()=='RTL_3V3' for e in ENDS);assert all(e in (reach(b,p[ENDS[0]])|{ENDS[0]}) for e in ENDS);print('RTL_3V3 U2.3/U2.8/C3.1: PASS')
b.BuildConnectivity();items=[x for x in b.GetConnectivity().GetConnectedItems(p[ENDS[0]]) if type(x).__name__=='PCB_TRACK' and x.GetNetname()=='RTL_3V3'];assert items
for item in items:
 t=pcbnew.LoadBoard(str(PCB));victim=next((x for x in t.GetTracks() if type(x).__name__=='PCB_TRACK' and x.GetNetname()=='RTL_3V3' and ((x.GetStart()==item.GetStart() and x.GetEnd()==item.GetEnd()) or (x.GetStart()==item.GetEnd() and x.GetEnd()==item.GetStart()))),None)
 if victim is None: continue
 t.RemoveNative(victim);q=pads(t)
 if ENDS[2] not in (reach(t,q[ENDS[0]])|{ENDS[0]}): print('RTL_3V3 negative control: PASS');break
else: raise AssertionError('negative control failed')
