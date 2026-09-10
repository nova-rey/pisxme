"""V46: move the CM5 USB3 TX_N source via left of the REFCLK B.Cu crossing."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V45_SELECTOR_TXN_SOUTH.kicad_pcb'
OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V46_CM5_TXN_SOURCE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE))
def route(n,pts,l):
    for a,z in zip(pts,pts[1:]):
        t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(n,p):
    v=pcbnew.PCB_VIA(b); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
n=b.FindNet('CM5_USB3_TX_N'); assert n
for t in list(b.GetTracks()):
    if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
route(n,[(70.04,106.3),(70.0,106.3)],F); via(n,(70.0,106.3))
route(n,[(70.0,106.3),(70.0,92.0),(77.0,92.0),(159.0,136.2),(149.8,136.2)],B)
via(n,(149.8,136.2)); route(n,[(149.8,136.2),(153.5,136.2)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
