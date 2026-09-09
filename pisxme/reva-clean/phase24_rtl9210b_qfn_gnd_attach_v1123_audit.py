"""Saved-board audit and negative controls for V1123 QFN GND attachments."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_QFN_GND_ATTACH_V1123.kicad_pcb'
END=[('U1','45'),('U1','66'),('U1','69')]
def pads(b):
 return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ident(x): return (x.GetParentFootprint().GetReference(),x.GetNumber())
def reach(b,p):
 b.BuildConnectivity();return {ident(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}
b=pcbnew.LoadBoard(str(PCB));p=pads(b);assert all(p[x].GetNetname()=='GND' for x in END)
assert all(x in reach(b,p[('U1','69')]) or x==('U1','69') for x in END);print('V1123 GND endpoints: PASS')
for target in (('U1','45'),('U1','66')):
 t=pcbnew.LoadBoard(str(PCB));q=pads(t);start=q[target].GetPosition();seg=next(x for x in t.GetTracks() if x.GetNetname()=='GND' and type(x).__name__=='PCB_TRACK' and (x.GetStart()==start or x.GetEnd()==start));t.RemoveNative(seg);assert ('U1','69') not in reach(t,q[target]);print(target,'negative control: PASS')
