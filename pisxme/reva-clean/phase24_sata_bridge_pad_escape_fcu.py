"""Disposable all-F.Cu U7 SATA bridge-side escape candidate.

This is a route-development experiment only.  It keeps the bridge-side
segments above/below the U7 field and avoids the frozen PCIe B.Cu corridor.
"""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_ISLAND_COHERENT_USB3_REPAIRED.kicad_pcb'
OUT=R/'PHASE24_STORAGE_ISLAND_COHERENT_USB3_SATA_BRIDGE_ESCAPE_FCU.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.13208)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):
    q=p.GetPosition() if hasattr(p,'GetPosition') else p
    return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def pad(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def track(b,net,a,z):
    t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(F); t.SetWidth(W); t.SetNet(net); b.Add(t)
b=pcbnew.LoadBoard(str(BASE))
jobs=(('TX_P','57','C30','2'),('TX_N','56','C31','2'),('RX_P','60','C32','2'),('RX_N','59','C33','2'))
for t in list(b.GetTracks()):
    if t.GetNetname() in {'/STORAGE/BRIDGE_SATA_'+x[0] for x in jobs}: b.Remove(t)
routes={
 'TX_P':[(110.5,98.0),(116.5,98.0),(117.5,97.0)],
 'TX_N':[(111.0,99.0),(114.0,99.0),(114.0,113.0),(117.5,113.0)],
 'RX_P':[(108.0,97.0),(122.5,97.0),(123.5,97.0)],
 'RX_N':[(109.5,102.0),(106.0,102.0),(106.0,115.0),(122.5,115.0),(123.5,113.0)],
}
for key,jp,cap,cp in jobs:
    net=b.FindNet('/STORAGE/BRIDGE_SATA_'+key)
    src=xy(pad(b,'U7',jp)); dst=xy(pad(b,cap,cp)); pts=[src]+routes[key]+[dst]
    for a,z in zip(pts,pts[1:]): track(b,net,a,z)
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
