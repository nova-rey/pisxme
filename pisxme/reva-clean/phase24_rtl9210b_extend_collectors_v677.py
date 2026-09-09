"""V677: extend the retained V676 source transitions to same-net collectors."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U139_U140_AROUND_V676.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_EXTEND_COLLECTORS_V677.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l)
 q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30))
 q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n3=b.FindNet('RTL_3V3'); n1=b.FindNet('RTL_1V1')
# U1.39: lower-side handoff to the existing RTL_3V3 trunk transition.
t(b,n3,B,(91.0,68.4),(91.0,64.0)); t(b,n3,B,(91.0,64.0),(100.4,60.8))
v(b,n3,(100.4,60.8))
# U1.40: return to the existing F.Cu RTL_1V1 collector at x=88.
t(b,n1,F,(92.0,70.0),(90.0,70.0)); t(b,n1,F,(90.0,70.0),(88.0,68.8))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
