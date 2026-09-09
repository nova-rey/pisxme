"""Saved-board physical connectivity audit and negative control for V1144."""
from pathlib import Path
import pcbnew

PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_XTALOUT_VIA_CLEARANCE_V1144.kicad_pcb'
END=(('U1','54'),('Y1','2'),('C2','1'))
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def same_component(b,a,z):
    b.BuildConnectivity(); q=pads(b); seen={a}; todo=[q[a]]
    while todo:
        for item in b.GetConnectivity().GetConnectedItems(todo.pop()):
            if type(item).__name__ not in ('PAD','PCB_PAD'): continue
            k=(item.GetParentFootprint().GetReference(),item.GetNumber())
            if k not in seen: seen.add(k); todo.append(item)
    return z in seen
b=pcbnew.LoadBoard(str(PCB)); p=pads(b)
assert all(p[x].GetNetname()=='XTAL_OUT' for x in END)
assert all(same_component(b,END[0],x) for x in END[1:])
assert sum(1 for x in b.GetTracks() if x.GetNetname()=='XTAL_OUT' and type(x).__name__=='PCB_VIA')==2
print('V1144 XTAL_OUT U1.54/Y1.2/C2.1 physical connectivity: PASS')
for target in END[1:]:
    t=pcbnew.LoadBoard(str(PCB)); q=pads(t); start=q[END[0]].GetPosition()
    seg=next(x for x in t.GetTracks() if x.GetNetname()=='XTAL_OUT' and type(x).__name__=='PCB_TRACK' and (x.GetStart()==start or x.GetEnd()==start))
    t.RemoveNative(seg); assert not same_component(t,END[0],target)
    print(target,'source-trace negative control: PASS')
