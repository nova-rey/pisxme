"""V570: upper-perimeter RTL_5V loop, avoiding the 1V1 B.Cu spine."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V562.kicad_pcb'; out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V570_RTL5V_UPPER_LOOP.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b); x.SetPosition(P(*q)); x.SetWidth(pcbnew.FromMM(.60)); x.SetDrill(pcbnew.FromMM(.30)); x.SetLayerPair(F,B); x.SetNet(n); x.SetNetCode(n.GetNetCode()); b.Add(x)
b=pcbnew.LoadBoard(str(base)); n=b.FindNet('RTL_5V'); next(x for x in b.Footprints() if x.GetReference()=='C5').SetPosition(P(96,55.5))
s(b,n,(102.05,64.8),(101.5,64.85),F); s(b,n,(101.5,64.85),(101.2,64.2),F); v(b,n,(101.2,64.2))
s(b,n,(102.8,58.05),(101.2,58.05),F); v(b,n,(101.2,58.05)); s(b,n,(101.2,64.2),(101.2,58.05),B)
s(b,n,(101.2,58.05),(104.5,58.05),B); s(b,n,(104.5,58.05),(104.5,50.5),B); s(b,n,(104.5,50.5),(95.2,50.5),B); s(b,n,(95.2,50.5),(95.2,54.8),B); v(b,n,(95.2,54.8)); s(b,n,(95.2,54.8),(95.2,55.5),F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
