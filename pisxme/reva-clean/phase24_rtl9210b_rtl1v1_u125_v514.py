"""V514: vertical U1.25 escape and early F.Cu return to U1.36."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; src=H/'PHASE24_RTL9210B_RTL1V1_U116_V506.kicad_pcb'; out=H/'PHASE24_RTL9210B_RTL1V1_U125_V514.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,a):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*a)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); b.Add(v)
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('RTL_1V1'); u=b.FindFootprintByReference('U1'); a=mm(u.FindPadByNumber('25').GetPosition()); j=mm(u.FindPadByNumber('36').GetPosition()); e=(106.4,57.3); h=(102.2,57.3); f=(101.0,57.3)
tr(b,n,F,a,e); via(b,n,e); tr(b,n,B,e,h); via(b,n,h); tr(b,n,F,h,f); tr(b,n,F,f,(101.0,j[1])); tr(b,n,F,(101.0,j[1]),j)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
