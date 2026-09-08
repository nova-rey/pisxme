"""V579: straight U1.33 RTL_5V escape to an outboard transition."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V576_RESTORE_3V3_BRIDGES.kicad_pcb'; out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V579_STRAIGHT_SOURCE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b); x.SetPosition(P(*q)); x.SetWidth(pcbnew.FromMM(.60)); x.SetDrill(pcbnew.FromMM(.30)); x.SetLayerPair(F,B); x.SetNet(n); x.SetNetCode(n.GetNetCode()); b.Add(x)
b=pcbnew.LoadBoard(str(base)); n=b.FindNet('RTL_5V')
for x in list(b.GetTracks()):
 if x.GetNetname()=='RTL_5V': b.RemoveNative(x)
for x in list(b.GetTracks()):
 if x.GetNetname()=='RTL_5V' and x.GetClass()=='Via': b.RemoveNative(x)
s(b,n,(102.05,64.8),(100.8,64.8),F); v(b,n,(100.8,64.8))
s(b,n,(102.8,58.05),(101.2,58.05),F); v(b,n,(101.2,58.05)); s(b,n,(100.8,64.8),(101.2,64.8),B); s(b,n,(101.2,64.8),(101.2,58.05),B)
s(b,n,(101.2,58.05),(104.5,58.05),B); s(b,n,(104.5,58.05),(104.5,50.5),B); s(b,n,(104.5,50.5),(95.2,50.5),B); s(b,n,(95.2,50.5),(95.2,54.8),B); v(b,n,(95.2,54.8)); s(b,n,(95.2,54.8),(95.2,55.5),F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
