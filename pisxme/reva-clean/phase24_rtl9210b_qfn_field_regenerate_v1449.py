"""V1449: coupled QFN support-field regeneration on accepted V1428."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_QFN_FIELD_REGENERATE_V1449.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return p.x/1e6,p.y/1e6
def tr(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); names=('RTL_3V3','RTL_1V1','RSET','GND','XTAL_IN','XTAL_OUT'); ns={x:b.FindNet(x) for x in names}
codes={x:ns[x].GetNetCode() for x in names}
for item in list(b.GetTracks()):
 if item.GetNetCode() not in codes.values(): continue
  # Remove only copper wholly within the local QFN source-field window.
 if isinstance(item,pcbnew.PCB_VIA):
  x,y=xy(item.GetPosition()); local=90<=x<=96 and 64<=y<=76
 else:
  a,z=xy(item.GetStart()),xy(item.GetEnd()); local=all(90<=x<=96 and 64<=y<=76 for x,y in (a,z))
 if local: b.Remove(item)
tr(b,ns['RTL_3V3'],F,[(94.05,66.8),(93.4,66.8),(93.4,65.0)]); via(b,ns['RTL_3V3'],93.4,65.0); tr(b,ns['RTL_3V3'],B,[(93.4,65.0),(100.5,65.0),(100.5,64.0)])
tr(b,ns['RTL_1V1'],F,[(94.05,68.0),(95.0,68.0)]); via(b,ns['RTL_1V1'],95.0,68.0); tr(b,ns['RTL_1V1'],B,[(95.0,68.0),(95.0,75.0),(102.5,75.0)])
tr(b,ns['RSET'],F,[(94.8,66.05),(94.0,64.8),(88.0,64.8),(88.0,65.0)])
tr(b,ns['XTAL_IN'],F,[(94.05,67.2),(93.5,67.2),(93.0,66.6),(91.5,66.0)]); via(b,ns['XTAL_IN'],91.5,66.0); tr(b,ns['XTAL_IN'],B,[(91.5,66.0),(85.5,66.0),(85.5,62.0)]); via(b,ns['XTAL_IN'],85.5,62.0); tr(b,ns['XTAL_IN'],F,[(85.5,62.0),(88.0,62.0),(88.0,59.0)])
tr(b,ns['XTAL_OUT'],F,[(94.05,67.6),(93.5,67.6),(93.0,68.4),(91.5,69.5)]); via(b,ns['XTAL_OUT'],91.5,69.5); tr(b,ns['XTAL_OUT'],B,[(91.5,69.5),(85.5,69.5),(85.5,77.0),(85.5,59.5)]); via(b,ns['XTAL_OUT'],85.5,59.5); tr(b,ns['XTAL_OUT'],F,[(85.5,59.5),(89.4,59.5),(89.4,59.0),(89.4,60.0),(91.0,62.0)])
tr(b,ns['GND'],F,[(97.2,66.05),(98.0,70.0)]); tr(b,ns['GND'],F,[(94.05,72.4),(98.0,70.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
