"""V572: fix V571's missing 3V3 bridge and replace its diagonal escape."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V562.kicad_pcb'; out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V572_3V3_BRIDGE.kicad_pcb'
F,B,L=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.In2_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b); x.SetPosition(P(*q)); x.SetWidth(pcbnew.FromMM(.60)); x.SetDrill(pcbnew.FromMM(.30)); x.SetLayerPair(F,B); x.SetNet(n); x.SetNetCode(n.GetNetCode()); b.Add(x)
b=pcbnew.LoadBoard(str(base))
for x in list(b.GetTracks()):
 if x.GetNetname()=='RTL_3V3': b.RemoveNative(x)
n3=b.FindNet('RTL_3V3')
for a,z in [((102.05,65.2),(104.4,65.2)),((104.4,65.2),(104.4,65.95)),((104.4,65.95),(104.4,68.5)),((102.05,59.6),(100.5,59.6)),((109.95,65.2),(112,65.2)),((102.6,53),(102.6,51)),((100.1,53),(100.1,51)),((110.2,53),(110.2,51)),((99.7,70),(99.7,68)),((93.7,70),(93.7,72))]: s(b,n3,a,z,F)
for q in [(104.4,68.5),(100.5,59.6),(112,65.2),(102.6,51),(100.1,51),(110.2,51),(99.7,68),(93.7,72)]: v(b,n3,q)
for a,z in [((102.6,51),(110.2,51)),((100.1,51),(102.6,51)),((100.5,59.6),(100.1,51)),((100.5,59.6),(100.5,66.5)),((100.5,66.5),(104.4,68.5)),((104.4,68.5),(112,65.2)),((104.4,68.5),(99.7,68)),((99.7,68),(93.7,72))]: s(b,n3,a,z,L)
n5=b.FindNet('RTL_5V'); next(x for x in b.Footprints() if x.GetReference()=='C5').SetPosition(P(96,55.5))
s(b,n5,(102.05,64.8),(101.5,64.85),F); s(b,n5,(101.5,64.85),(101.2,64.2),F); v(b,n5,(101.2,64.2))
s(b,n5,(102.8,58.05),(101.2,58.05),F); v(b,n5,(101.2,58.05)); s(b,n5,(101.2,64.2),(101.2,58.05),B)
s(b,n5,(101.2,58.05),(104.5,58.05),B); s(b,n5,(104.5,58.05),(104.5,50.5),B); s(b,n5,(104.5,50.5),(95.2,50.5),B); s(b,n5,(95.2,50.5),(95.2,54.8),B); v(b,n5,(95.2,54.8)); s(b,n5,(95.2,54.8),(95.2,55.5),F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
