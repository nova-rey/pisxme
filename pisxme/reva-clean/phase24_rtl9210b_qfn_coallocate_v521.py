"""V521: join U1.34 RTL_3V3 to the existing C3-side 3V3 handoff."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; src=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V520.kicad_pcb'; out=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V521.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,a):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*a));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());v.SetWidth(pcbnew.FromMM(.6));v.SetDrill(pcbnew.FromMM(.3));b.Add(v)
b=pcbnew.LoadBoard(str(src));n=b.FindNet('RTL_3V3');u=b.FindFootprintByReference('U1');a=mm(u.FindPadByNumber('34').GetPosition());e=(102.8,57.0);h=(109.5,57.0);j=(109.5,57.2)
tr(b,n,F,a,e);via(b,n,e);tr(b,n,B,e,h);tr(b,n,B,h,j);via(b,n,j)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
