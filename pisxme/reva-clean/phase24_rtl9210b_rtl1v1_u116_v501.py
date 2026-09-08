"""V501: C4 beside U1.16 with a separated bottom-layer branch."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_SOURCE_FIELD_V498.kicad_pcb'; out=H/'PHASE24_RTL9210B_RTL1V1_U116_V501.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,a):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*a)); v.SetNet(n); v.SetNetCode(n.GetNetCode()); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); b.Add(v)
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('RTL_1V1'); u=b.FindFootprintByReference('U1'); c=b.FindFootprintByReference('C4'); c.SetPosition(P(114,59))
a=mm(u.FindPadByNumber('16').GetPosition()); z=mm(c.FindPadByNumber('1').GetPosition()); v1=(110.8,60.5); v2=(z[0],60.5)
tr(b,n,F,a,(v1[0],a[1])); tr(b,n,F,(v1[0],a[1]),v1); via(b,n,v1); tr(b,n,B,v1,v2); via(b,n,v2); tr(b,n,F,v2,z)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
