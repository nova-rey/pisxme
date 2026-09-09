"""V1263: move only the LANE0_RXN source transition to free QFN support space."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_J1_PAD_ALIGNED_LAUNCH_V1258.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_RXN_SOURCE_REHOME_FOR_SUPPORT_V1263.kicad_pcb'
F,B,W=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('LANE0_RXN')
for q in list(b.GetTracks()):
 if q.GetNetname()=='LANE0_RXN':
  a=(round(pcbnew.ToMM(q.GetStart().x),3),round(pcbnew.ToMM(q.GetStart().y),3));z=(round(pcbnew.ToMM(q.GetEnd().x),3),round(pcbnew.ToMM(q.GetEnd().y),3))
  if (92.8 in (a[0],z[0]) and 70.8 in (a[1],z[1])) or (a==(108.0,70.8) or z==(108.0,70.8)) or (isinstance(q,pcbnew.PCB_VIA) and a==(92.8,70.8)):
   b.Remove(q)
# Re-enter on B.Cu below the U1 edge, then use the existing upper corridor.
s(b,n,F,[(94.05,72.0),(91.0,72.0),(91.0,69.8)]);v(b,n,(91.0,69.8))
s(b,n,B,[(91.0,69.8),(108.0,69.8)]);v(b,n,(108.0,69.8))
s(b,n,F,[(108.0,69.8),(108.0,43.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
