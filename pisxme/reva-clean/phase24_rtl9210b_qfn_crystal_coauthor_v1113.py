"""V1113: co-author U1.52/U1.55 QFN departures with XTAL_IN."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_RSET_V1092.kicad_pcb';OUT=H/'PHASE24_RTL9210B_QFN_CRYSTAL_COAUTHOR_V1113.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for q in list(b.GetTracks()):
 a=q.GetStart();z=q.GetEnd(); name=q.GetNetname()
 if name=='RTL_3V3' and ((a==P(94.05,66.8) or z==P(94.05,66.8) or a==P(93.0,66.8) or z==P(93.0,66.8) or a==P(93.0,68.4) or z==P(93.0,68.4))): b.RemoveNative(q)
 if name=='RTL_1V1' and (a==P(94.05,68.0) or z==P(94.05,68.0) or a==P(92.8,68.0) or z==P(92.8,68.0) or a==P(92.8,69.3) or z==P(92.8,69.3) or a==P(92.8,75.0) or z==P(92.8,75.0)): b.RemoveNative(q)
 if name=='RTL_3V3' and type(q).__name__=='PCB_VIA' and q.GetPosition()==P(93.0,66.8): b.RemoveNative(q)
 if name=='RTL_1V1' and type(q).__name__=='PCB_VIA' and q.GetPosition()==P(92.8,75.0): b.RemoveNative(q)
ni,n3,n1=(b.FindNet(x) for x in ('XTAL_IN','RTL_3V3','RTL_1V1'))
# Relocated U1.52 3V3 transition joins the existing B.Cu 3V3 field at y=68.4.
tr(b,n3,F,[(94.05,66.8),(96.5,66.8)]);via(b,n3,(96.5,66.8));tr(b,n3,B,[(96.5,66.8),(96.5,68.4)]);tr(b,n3,B,[(96.5,68.4),(100.9,68.4)])
# U1.55 1V1 takes the right-side shelf and rejoins the existing collector.
tr(b,n1,F,[(94.05,68.0),(95.0,68.0)]);via(b,n1,(95.0,68.0));tr(b,n1,B,[(95.0,68.0),(95.0,75.0),(102.5,75.0)]);via(b,n1,(102.5,75.0))
# XTAL_IN uses the vacated left departure and original support endpoints.
tr(b,ni,F,[(94.05,67.2),(93.2,67.2),(93.0,67.5),(91.5,68.6)]);via(b,ni,(91.5,68.6));tr(b,ni,B,[(91.5,68.6),(91.5,75.0),(85.5,75.0),(85.5,62.0)]);via(b,ni,(85.5,62.0));tr(b,ni,F,[(85.5,62.0),(88.0,62.0)]);tr(b,ni,F,[(88.0,59.0),(88.0,62.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
