"""V1277: co-author U1.33 RTL_5V with U1.25 RTL_1V1 source transition."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_COUPLED_PAD39_3V3_PAD40_1V1_V1275.kicad_pcb';OUT=H/'PHASE24_RTL9210B_COUPLED_5V_1V1_SOURCEFIELD_V1277.kicad_pcb';F,B,W=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));r1=b.FindNet('RTL_1V1');r5=b.FindNet('RTL_5V')
# Remove only the U1.25 F.Cu vertical and its source via; retain the pad drop.
for q in list(b.GetTracks()):
 if q.GetNetname()=='RTL_1V1':
  a=(round(pcbnew.ToMM(q.GetStart().x),3),round(pcbnew.ToMM(q.GetStart().y),3));z=(round(pcbnew.ToMM(q.GetEnd().x),3),round(pcbnew.ToMM(q.GetEnd().y),3))
  if (a==(101.95,70.4) or z==(101.95,70.4) or (a==(103.0,70.4) and z==(103.0,60.0)) or (a==(103.0,60.0) and z==(103.0,70.4)) or (isinstance(q,pcbnew.PCB_VIA) and a==(103.0,70.4))): b.Remove(q)
# Reuse the existing U1.25 source drop, but continue on B.Cu to the collector.
s(b,r1,F,[(101.95,70.4),(103.0,70.4)]);v(b,r1,(103.0,70.4));s(b,r1,B,[(103.0,70.4),(87.0,70.4),(87.0,60.0)])
# 5V leaves U1.33 on F.Cu before its own transition and uses a separate B.Cu trunk.
s(b,r5,F,[(101.95,67.2),(103.5,67.2),(103.5,65.5)]);v(b,r5,(103.5,65.5));s(b,r5,B,[(103.5,65.5),(126.4,65.5),(126.4,51.0)]);v(b,r5,(126.4,51.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
