"""V1111: underside crystal/RSET support-cell experiment from V1092."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_RSET_V1092.kicad_pcb';OUT=H/'PHASE24_RTL9210B_CRYSTAL_UNDERSIDE_V1111.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for q in list(b.GetTracks()):
 if q.GetNetname() in ('XTAL_IN','XTAL_OUT','RSET'):b.RemoveNative(q)
for ref in ('Y1','C1','C2','R1'):
 f=b.FindFootprintByReference(ref);f.SetLayer(B)
ni,no,nr=(b.FindNet(x) for x in ('XTAL_IN','XTAL_OUT','RSET'))
via(b,ni,(91.4,67.2));tr(b,ni,B,[(91.4,67.2),(91.4,64.0),(88.0,64.0),(88.0,62.0)]);tr(b,ni,B,[(88.0,62.0),(88.0,59.0)])
via(b,no,(90.4,67.6));tr(b,no,B,[(90.4,67.6),(90.4,64.8),(89.4,64.8),(89.4,59.0)]);tr(b,no,B,[(89.4,64.8),(91.0,64.8),(91.0,62.0)])
via(b,nr,(96.5,66.05));tr(b,nr,B,[(96.5,66.05),(96.5,65.0),(88.0,65.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
