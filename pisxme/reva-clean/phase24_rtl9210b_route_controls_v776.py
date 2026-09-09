"""V776: separate CLKREQ_N from PEDET with an ordinary B.Cu handoff."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V760_RAIL_CONTROL_PLACEMENT_V774.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V760_CONTROL_ROUTED_V776.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('PEDET'); t(b,n,F,(101.95,70.4),(103.0,70.4)); t(b,n,F,(103.0,70.4),(107.0,67.0))
n=b.FindNet('CLKREQ_N'); t(b,n,F,(101.95,68.4),(103.0,68.4)); v(b,n,(103.0,68.4)); t(b,n,B,(103.0,68.4),(106.5,70.0)); v(b,n,(106.5,70.0)); t(b,n,F,(106.5,70.0),(107.0,70.0))
n=b.FindNet('RTL_3V3'); t(b,n,F,(108.2,67.0),(108.2,70.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
