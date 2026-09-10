"""V38: route CM5 USB3 TX_N around the local PER0_P source corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V37_FILLED.kicad_pcb'
OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V38_TXN_LEFT_ESCAPE.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('/CORE_CM5/CM5_USB3_TX_N') or b.FindNet('CM5_USB3_TX_N'); assert n
for t in list(b.GetTracks()):
    if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
j=b.FindFootprintByReference('J7'); u=b.FindFootprintByReference('U12'); assert j and u
def xy(q): return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
s=xy(j.FindPadByNumber('140').GetPosition()); e=xy(u.FindPadByNumber('12').GetPosition())
pts=[s,(67.0,s[1]),(67.0,92.0),(77.0,92.0)]
def seg(a,z,l=F):
    t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
for a,z in zip(pts,pts[1:]): seg(a,z)
v=pcbnew.PCB_VIA(b);v.SetPosition(P(77.0,92.0));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
seg((77.0,92.0),e,pcbnew.B_Cu)
seg((159.0,136.2),(149.8,136.2),pcbnew.B_Cu)
seg((149.8,136.2),(153.5,136.2),F)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
