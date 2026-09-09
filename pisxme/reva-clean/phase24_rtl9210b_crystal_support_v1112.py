"""V1112: same-side upper-right crystal support cell, no transition vias."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_RSET_V1092.kicad_pcb';OUT=H/'PHASE24_RTL9210B_CRYSTAL_SUPPORT_V1112.kicad_pcb';F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for q in list(b.GetTracks()):
 if q.GetNetname() in ('XTAL_IN','XTAL_OUT','RSET'):b.RemoveNative(q)
d=P(22,-4)
for ref in ('Y1','C1','C2','R1'):
 f=b.FindFootprintByReference(ref);f.SetPosition(f.GetPosition()+d)
ni,no,nr=(b.FindNet(x) for x in ('XTAL_IN','XTAL_OUT','RSET'))
tr(b,ni,[(94.05,67.2),(95.5,67.2),(99.0,64.0),(110.0,55.0)]);tr(b,ni,[(99.0,64.0),(110.0,58.0)])
tr(b,no,[(94.05,67.6),(96.5,67.6),(101.0,64.5),(111.4,55.0)]);tr(b,no,[(101.0,64.5),(113.0,58.0)])
tr(b,nr,[(94.8,66.05),(97.0,64.0),(110.0,61.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
