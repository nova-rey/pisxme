"""V508: upper-bank U1.25 escape with an early B.Cu/F.Cu return."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; src=H/'PHASE24_RTL9210B_RTL1V1_U116_V506.kicad_pcb'; out=H/'PHASE24_RTL9210B_RTL1V1_U125_V508.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,a):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*a)); v.SetNet(n); v.SetNetCode(n.GetNetCode()); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); b.Add(v)
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('RTL_1V1'); u=b.FindFootprintByReference('U1'); a=mm(u.FindPadByNumber('25').GetPosition()); e=(104.8,57.3); h=(101.2,57.3); j=(99.5,59.2)
tr(b,n,F,a,(104.8,a[1])); tr(b,n,F,(104.8,a[1]),e); via(b,n,e); tr(b,n,B,e,h); via(b,n,h); tr(b,n,F,h,(99.5,h[1])); tr(b,n,F,(99.5,h[1]),j)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
