"""V41: co-author the Path-A SATA TX pair with separated source vias."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V40_TXN_SOURCE_TRANSITION.kicad_pcb'
OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V41_SATA_TX_PAIR.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE))
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def pad(r,n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def route(net,pts,layer):
    for a,z in zip(pts,pts[1:]):
        t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(layer);t.SetWidth(W);t.SetNet(net);t.SetNetCode(net.GetNetCode());b.Add(t)
def via(net,p):
    v=pcbnew.PCB_VIA(b);v.SetPosition(P(*p));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(net);v.SetNetCode(net.GetNetCode());b.Add(v)
for name in ('BRIDGE_SATA_TX_P','BRIDGE_SATA_TX_N'):
    n=b.FindNet('/STORAGE/'+name) or b.FindNet(name); assert n
    for t in list(b.GetTracks()):
        if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
spec=(
 ('BRIDGE_SATA_TX_P','57','C30',[(95.8,127.8),(95.8,126.0),(94.0,126.0)],[(94.0,126.0),(94.0,116.0),(103.0,116.0)]),
 ('BRIDGE_SATA_TX_N','56','C31',[(96.2,127.8),(96.2,126.8),(98.0,126.0)],[(98.0,126.0),(98.0,132.0),(103.0,132.0)]))
for name,pin,cap,fp,bp in spec:
    n=b.FindNet('/STORAGE/'+name) or b.FindNet(name); route(n,fp,F); via(n,fp[-1]); route(n,bp,B); via(n,bp[-1]); route(n,[bp[-1],xy(pad(cap,'2').GetPosition())],F)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
