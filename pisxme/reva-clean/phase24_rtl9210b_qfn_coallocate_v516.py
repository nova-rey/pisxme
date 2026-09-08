"""V516: coallocate U1.25 by temporarily removing conflicting support spines."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; src=H/'PHASE24_RTL9210B_RTL1V1_U116_V506.kicad_pcb'; out=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V516.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,a):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*a)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); b.Add(v)
def xy(x): return (round(pcbnew.ToMM(x.GetStart().x),3),round(pcbnew.ToMM(x.GetStart().y),3),round(pcbnew.ToMM(x.GetEnd().x),3),round(pcbnew.ToMM(x.GetEnd().y),3))
b=pcbnew.LoadBoard(str(src))
remove={('XTAL_IN',(102.5,67.5,102.5,42.0)),('XTAL_OUT',(105.0,68.5,105.0,44.0)),('RTL_3V3',(101.5,67.5,101.5,56.5)),('RTL_3V3',(102.8,58.05,100.5,56.5))}
for x in list(b.GetTracks()):
 if (x.GetNetname(),xy(x)) in remove: b.RemoveNative(x)
n=b.FindNet('RTL_1V1'); u=b.FindFootprintByReference('U1'); a=mm(u.FindPadByNumber('25').GetPosition()); j=mm(u.FindPadByNumber('36').GetPosition()); e=(106.4,57.3); h=(102.0,57.3); f=(101.0,57.3)
tr(b,n,F,a,e); via(b,n,e); tr(b,n,B,e,h); via(b,n,h); tr(b,n,F,h,f); tr(b,n,F,f,(101.0,j[1])); tr(b,n,F,(101.0,j[1]),j)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
