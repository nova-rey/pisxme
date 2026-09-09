"""V1247: diverging pair source escapes; separates each pair before vias."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RAILS_REFCLK_FIXED_V1243.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_LANE0_DIVERGING_SOURCE_V1247.kicad_pcb'; F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def inside(p): return 90<=pcbnew.ToMM(p.x)<=101 and 63<=pcbnew.ToMM(p.y)<=80
def seg(b,n,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for q in list(b.GetTracks()):
 if inside(q.GetStart()) or inside(q.GetEnd()): b.RemoveNative(q)
for q in list(b.GetTracks()):
 if type(q).__name__=='PCB_VIA' and inside(q.GetPosition()): b.RemoveNative(q)
u=b.FindFootprintByReference('U1')
R=[('LANE0_RXP','64',[(94.05,71.6),(95.0,71.6),(95.0,72.4)],(95.0,72.4)),('LANE0_RXN','65',[(94.05,72.0),(92.8,72.0),(92.8,74.8)],(92.8,74.8)),('LANE0_TXN','67',[(94.05,72.8),(92.2,72.8),(92.2,76.0)],(92.2,76.0)),('LANE0_TXP','68',[(94.05,73.2),(95.6,73.2),(95.6,76.0)],(95.6,76.0))]
for name,pad,pts,vp in R:
 n=b.FindNet(name); seg(b,n,pts); via(b,n,vp)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
