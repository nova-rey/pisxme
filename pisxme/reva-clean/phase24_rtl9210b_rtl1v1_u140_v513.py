"""V513: wide outside-envelope U1.40-to-U1.50 via escape."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; src=H/'PHASE24_RTL9210B_RTL1V1_U116_V506.kicad_pcb'; out=H/'PHASE24_RTL9210B_RTL1V1_U140_V513.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,a):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*a)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); b.Add(v)
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('RTL_1V1'); u=b.FindFootprintByReference('U1'); a=mm(u.FindPadByNumber('40').GetPosition()); z=mm(u.FindPadByNumber('50').GetPosition()); e=(108.0,60.0); h=(108.0,64.8)
tr(b,n,F,a,(103.0,60.0)); tr(b,n,F,(103.0,60.0),e); via(b,n,e); tr(b,n,B,e,h); via(b,n,h); tr(b,n,F,h,z)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
