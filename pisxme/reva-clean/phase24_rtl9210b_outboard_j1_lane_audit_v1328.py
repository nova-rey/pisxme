"""Native V1328 lane connectivity audit with source-removal controls."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
PCB=H/'PHASE24_RTL9210B_OUTBOARD_J1_COAUTHORED_V1328.kicad_pcb'
LANES=[('LANE0_RXP','64','43',(95.0,72.4),(94.05,71.6)),('LANE0_RXN','65','41',(92.8,70.8),(94.05,72.0)),('LANE0_TXN','67','47',(92.2,72.6),(94.05,72.8)),('LANE0_TXP','68','49',(90.8,76.8),(94.05,73.2))]
def pads(b): return {(f.GetReference(),str(p.GetNumber())):p for f in b.GetFootprints() for p in f.Pads()}
def source_via(b,net,xy):
    q=pcbnew.VECTOR2I_MM(*xy)
    return next(x for x in b.GetTracks() if isinstance(x,pcbnew.PCB_VIA) and x.GetNetname()==net and x.GetPosition()==q)
def connected(b,a): return b.GetConnectivity().GetConnectedItems(a)
b=pcbnew.LoadBoard(str(PCB)); ps=pads(b); b.BuildConnectivity()
for net,u,j,sv,_ in LANES:
    assert ps[('J1',j)] in connected(b,ps[('U1',u)]), net+' endpoint missing'
    assert source_via(b,net,sv) in connected(b,ps[('U1',u)]), net+' source transition missing'
for net,u,j,sv,up in LANES:
    t=pcbnew.LoadBoard(str(PCB)); pt=pads(t); v=source_via(t,net,sv)
    removed=False
    for x in list(t.GetTracks()):
        if x.GetNetname()==net and not isinstance(x,pcbnew.PCB_VIA) and x.GetStart()==pcbnew.VECTOR2I_MM(*up):
            t.RemoveNative(x); removed=True; break
    assert removed, net+' negative-control trace not found'
    t.BuildConnectivity(); assert pt[('J1',j)] not in connected(t,pt[('U1',u)]), net+' negative control did not disconnect'
print('PASS V1328 native four-lane endpoints and four source-removal negative controls')
