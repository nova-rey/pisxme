"""Saved-board PEDET audit and source-trace negative control."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_PEDET_ROUTE_V1124.kicad_pcb'
END=[('U1','8'),('R2','1'),('J1','69')]
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ident(x): return (x.GetParentFootprint().GetReference(),x.GetNumber())
def reach(b,p):
 b.BuildConnectivity();return {ident(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}
b=pcbnew.LoadBoard(str(PCB));p=pads(b);assert all(p[x].GetNetname()=='PEDET' for x in END);assert all(x in reach(b,p[END[0]]) for x in END);print('V1126 PEDET endpoints: PASS')
t=pcbnew.LoadBoard(str(PCB));q=pads(t);start=q[END[0]].GetPosition();seg=next(x for x in t.GetTracks() if x.GetNetname()=='PEDET' and type(x).__name__=='PCB_TRACK' and (x.GetStart()==start or x.GetEnd()==start));t.RemoveNative(seg);assert END[2] not in reach(t,q[END[0]]);print('PEDET source-trace negative control: PASS')
