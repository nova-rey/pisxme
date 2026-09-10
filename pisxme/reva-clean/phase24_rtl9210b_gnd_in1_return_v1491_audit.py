"""Saved-board audit and negative control for the V1491 GND return field."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent; PCB=ROOT/'PHASE24_RTL9210B_GND_REROUTE_RTL3V3_V1491.kicad_pcb'
def key(x):
 return (x.GetParentFootprint().GetReference(),x.GetNumber()) if type(x).__name__=='PAD' else type(x).__name__
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
b=pcbnew.LoadBoard(str(PCB)); ps=pads(b); b.BuildConnectivity(); c=b.GetConnectivity()
for k in (('U1','45'),('U1','66'),('U1','69')): assert ps[k].GetNetname()=='GND'
items=c.GetConnectedItems(ps[('U1','69')]); assert ps[('U1','45')] in items and ps[('U1','66')] in items
assert any(x.GetNetname()=='GND' and type(x).__name__=='PCB_VIA' and abs(x.GetPosition()[0]/1e6-97.2)<.01 for x in b.GetTracks())
print('V1491 native GND QFN field + In1 return: PASS')
# Removing the sole QFN-to-In1 stitch must break the QFN field from the
# remote return; this guards against synthetic connectivity assumptions.
t=pcbnew.LoadBoard(str(PCB)); q=pads(t); stitch=next(x for x in t.GetTracks() if type(x).__name__=='PCB_VIA' and x.GetNetname()=='GND' and abs(x.GetPosition()[0]/1e6-97.2)<.01); t.RemoveNative(stitch); t.BuildConnectivity(); cc=t.GetConnectivity(); remote=next(x for x in t.GetTracks() if type(x).__name__=='PCB_VIA' and x.GetNetname()=='GND' and abs(x.GetPosition()[0]/1e6-115.6)<.01); assert remote not in cc.GetConnectedItems(q[('U1','69')]); print('removed QFN stitch negative control: PASS')
