"""V1266: co-author RXN source and two RTL_1V1 QFN escapes."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_RXN_SOURCE_REHOME_FOR_SUPPORT_V1263.kicad_pcb';OUT=H/'PHASE24_RTL9210B_COUPLED_RXN_1V1_SOURCEFIELD_V1266.kicad_pcb';F,B,W=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,ps,w=W):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(w);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));rx=b.FindNet('LANE0_RXN');r1=b.FindNet('RTL_1V1')
for q in list(b.GetTracks()):
 if q.GetNetname()=='LANE0_RXN':
  a=(round(pcbnew.ToMM(q.GetStart().x),3),round(pcbnew.ToMM(q.GetStart().y),3));z=(round(pcbnew.ToMM(q.GetEnd().x),3),round(pcbnew.ToMM(q.GetEnd().y),3))
  if (a[0]<=94.05 and z[0]<=94.05) or (a==(108.0,69.8) or z==(108.0,69.8)) or (isinstance(q,pcbnew.PCB_VIA) and (a==(91.0,69.8) or a==(108.0,69.8))): b.Remove(q)
s(b,rx,F,[(94.05,72.0),(89.5,72.0),(89.5,68.5),(89.0,68.5)]);v(b,rx,(89.0,68.5));s(b,rx,B,[(89.0,68.5),(108.0,68.5)]);v(b,rx,(108.0,68.5));s(b,rx,F,[(108.0,68.5),(108.0,43.0)])
s(b,r1,F,[(94.05,71.2),(93.2,71.2),(92.8,71.2)]);v(b,r1,(92.8,71.2));s(b,r1,F,[(94.05,70.0),(91.4,70.0)]);v(b,r1,(91.4,70.0))
s(b,r1,B,[(92.8,71.2),(87.0,71.2),(87.0,60.0),(103.0,60.0),(103.0,50.0),(123.4,50.0)]);s(b,r1,B,[(91.4,70.0),(87.0,70.0),(87.0,71.2)]);v(b,r1,(103.0,60.0));v(b,r1,(123.4,50.0));s(b,r1,F,[(123.4,50.0),(123.4,51.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
