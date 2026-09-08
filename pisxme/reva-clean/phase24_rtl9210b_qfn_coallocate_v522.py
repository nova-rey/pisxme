"""V522: coallocate U1.34 through the U1.39 3V3 handoff and outer B.Cu rail."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; src=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V520.kicad_pcb'; out=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V522.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,a):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*a)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); b.Add(v)
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('RTL_3V3'); u=b.FindFootprintByReference('U1'); a=mm(u.FindPadByNumber('34').GetPosition())
# Leave the top-pad field to the left, then join the already validated U1.39
# handoff.  The outer B.Cu rail stays outside the 1V1 channel.
tr(b,n,F,a,(101.3,58.05)); via(b,n,(101.3,58.05)); tr(b,n,B,(101.3,58.05),(101.3,60.4)); via(b,n,(101.3,60.4)); tr(b,n,F,(101.3,60.4),(102.05,60.4))
tr(b,n,B,(100.5,60.4),(100.5,56.5)); tr(b,n,B,(100.5,56.5),(109.5,56.5)); tr(b,n,B,(109.5,56.5),(109.5,57.2))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
