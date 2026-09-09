"""V1275: co-author U1.39 RTL_3V3 and U1.40 RTL_1V1 source escapes."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_PAD25_1V1_V1272.kicad_pcb';OUT=H/'PHASE24_RTL9210B_COUPLED_PAD39_3V3_PAD40_1V1_V1275.kicad_pcb';F,B,W=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));r1=b.FindNet('RTL_1V1');r3=b.FindNet('RTL_3V3')
# Relocate only U1.40's existing RTL_1V1 source cohort.
for q in list(b.GetTracks()):
 if q.GetNetname()=='RTL_1V1':
  a=(round(pcbnew.ToMM(q.GetStart().x),3),round(pcbnew.ToMM(q.GetStart().y),3));z=(round(pcbnew.ToMM(q.GetEnd().x),3),round(pcbnew.ToMM(q.GetEnd().y),3))
  if a==(99.2,66.05) or z==(99.2,66.05) or a==(99.2,64.8) or z==(99.2,64.8):b.Remove(q)
s(b,r1,F,[(99.2,66.05),(99.2,64.8),(97.5,64.8)]);v(b,r1,(97.5,64.8));s(b,r1,B,[(97.5,64.8),(87.0,64.8)])
# Add U1.39's 3V3 branch in the vacated field.
s(b,r3,F,[(99.6,66.05),(99.6,64.0),(99.6,63.5)]);v(b,r3,(99.6,63.5));s(b,r3,B,[(99.6,63.5),(102.2,64.5)]);v(b,r3,(120.4,51.0));s(b,r3,B,[(102.2,64.5),(120.4,64.5),(120.4,51.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
