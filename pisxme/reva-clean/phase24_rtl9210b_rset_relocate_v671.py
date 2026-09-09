"""V671: relocate the RSET endpoint to free the lower 3V3 corridor."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V35_U2_LEFT_RAILS_5V_PLUS_3V3_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_RSET_RELOCATED_V671.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l)
 q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.60))
 q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n)
 q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RSET')
for q in list(b.GetTracks()):
 if q.GetNetname()=='RSET': b.RemoveNative(q)
r=b.FindFootprintByReference('R1'); p=next(x for x in r.Pads() if str(x.GetNumber())=='1')
r.Move(P(112.4,86.0)-p.GetPosition())
# Native U1.51 -> moved R1.1, with a dedicated west/B.Cu perimeter.
t(b,n,F,(94.05,73.2),(92.5,73.2)); v(b,n,(92.5,73.2))
t(b,n,B,(92.5,73.2),(92.5,84.0)); t(b,n,B,(92.5,84.0),(112.4,84.0)); v(b,n,(112.4,84.0))
t(b,n,F,(112.4,84.0),(112.4,86.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
