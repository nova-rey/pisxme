"""V1399: F.Cu/B.Cu RTL_5V fan-in for U1.17, U1.33, and C5."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U160_1V1_TOP_SHELF_V1392.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_RTL5V_FANIN_V1399.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_5V'); assert n
tr(b,n,F,[(101.95,67.2),(106.0,67.2)]); via(b,n,(106.0,67.2)); tr(b,n,B,[(106.0,67.2),(106.0,51.0),(126.4,51.0)]); via(b,n,(126.4,51.0))
tr(b,n,F,[(101.2,73.95),(104.0,73.95)]); via(b,n,(104.0,73.95)); tr(b,n,B,[(104.0,73.95),(106.0,73.95),(106.0,67.2)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
