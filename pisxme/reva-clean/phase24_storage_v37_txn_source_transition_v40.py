"""V40: early B.Cu transition for CM5 USB3 TX_N, retaining V37 endpoint launch."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V37_FILLED.kicad_pcb'; OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V40_TXN_SOURCE_TRANSITION.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('/CORE_CM5/CM5_USB3_TX_N') or b.FindNet('CM5_USB3_TX_N'); assert n
for t in list(b.GetTracks()):
    if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
j=b.FindFootprintByReference('J7');u=b.FindFootprintByReference('U12'); assert j and u
def xy(q): return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
s=xy(j.FindPadByNumber('140').GetPosition()); e=xy(u.FindPadByNumber('12').GetPosition())
def seg(a,z,l):
    t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
vsrc=(72.0,s[1]); vdst=(77.0,92.0)
seg(s,vsrc,F); seg(vsrc,(72.0,92.0),B); seg((72.0,92.0),vdst,B)
for p in (vsrc,vdst):
    v=pcbnew.PCB_VIA(b);v.SetPosition(P(*p));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
seg((149.8,136.2),e,F)
v=pcbnew.PCB_VIA(b);v.SetPosition(P(149.8,136.2));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
seg(vdst,(159.0,136.2),B); seg((159.0,136.2),(149.8,136.2),B)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
