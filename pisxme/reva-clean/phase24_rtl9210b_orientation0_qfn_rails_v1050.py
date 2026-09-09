"""V1050: route U1.20 3V3 through an immediate B.Cu transition."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_ORIENTATION0_QFN_RAILS_V1048.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_ORIENTATION0_QFN_RAILS_V1050.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
# Preserve V1048's clean local field and add only U1.20's right-edge escape.
add(b,n,[(101.95,72.4),(103.0,72.4)],F); via(b,n,(103.0,72.4)); add(b,n,[(103.0,72.4),(108.0,72.4),(108.0,64.0)],B)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
