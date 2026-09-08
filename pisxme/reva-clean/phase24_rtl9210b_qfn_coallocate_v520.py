"""V520: coallocate 1V1/XTAL_IN after clearing the local 3V3 spine."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; src=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V516.kicad_pcb'; out=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V520.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,a):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*a)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); b.Add(v)
def xy(x): return tuple(round(pcbnew.ToMM(q),3) for q in (x.GetStart().x,x.GetStart().y,x.GetEnd().x,x.GetEnd().y))
b=pcbnew.LoadBoard(str(src)); remove={('RSET',(100.8,66.5,100.8,73.0)),('RTL_3V3',(100.5,60.4,100.5,56.5)),('RTL_3V3',(100.5,56.5,100.5,41.0))}
for x in list(b.GetTracks()):
 if (x.GetNetname(),xy(x)) in remove: b.RemoveNative(x)
for x in list(b.GetTracks()):
 if isinstance(x,pcbnew.PCB_VIA) and x.GetNetname()=='RTL_3V3' and round(pcbnew.ToMM(x.GetPosition().x),3)==101.5 and round(pcbnew.ToMM(x.GetPosition().y),3)==67.5: b.RemoveNative(x)
n=b.FindNet('RTL_1V1'); u=b.FindFootprintByReference('U1'); a=mm(u.FindPadByNumber('25').GetPosition()); j=mm(u.FindPadByNumber('36').GetPosition()); e=(106.4,57.3); h=(101.5,57.3); f=(101.0,57.3)
tr(b,n,F,a,e); via(b,n,e); tr(b,n,B,e,h); via(b,n,h); tr(b,n,F,h,f); tr(b,n,F,f,(101.0,j[1])); tr(b,n,F,(101.0,j[1]),j)
xt=b.FindNet('XTAL_IN'); tr(b,xt,B,(102.5,67.5),(99.8,67.5)); via(b,xt,(99.8,67.5)); tr(b,xt,B,(99.8,67.5),(99.8,42.0)); tr(b,xt,B,(99.8,42.0),(102.5,42.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
