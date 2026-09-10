"""V1407: localized RTL_3V3 B.Cu power island for U2/U1 support."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U160_1V1_TOP_SHELF_V1392.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_3V3_LOCAL_POWER_ZONE_V1407.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3'); assert n
tr(b,n,F,[(113.8,76.4),(113.8,77.5)]); via(b,n,(113.8,77.5))
poly=pcbnew.VECTOR_VECTOR2I()
for x,y in [(100.2,71.5),(115.0,71.5),(115.0,82.5),(100.2,82.5)]: poly.append(P(x,y))
z=pcbnew.ZONE(b); z.SetLayer(B); z.SetNet(n); z.SetNetCode(n.GetNetCode()); z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL); z.AddPolygon(poly); b.Add(z)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
