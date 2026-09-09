"""V693: route U1.52 around the RSET endpoint on B.Cu."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_3V3_U139_JOG_V687.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_C2_GND_U152_RSET_V693.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n3=b.FindNet('RTL_3V3');ng=b.FindNet('GND')
for q in list(b.GetTracks()):
 if type(q).__name__=='PCB_VIA' and q.GetNetname()=='GND':
  p=q.GetPosition();xy=(round(pcbnew.ToMM(p.x),3),round(pcbnew.ToMM(p.y),3))
  if xy==(91.6,63.8):b.RemoveNative(q)
v(b,ng,(92.8,62.0));t(b,ng,F,(91.6,63.0),(92.8,62.0))
t(b,n3,F,(94.05,66.8),(91.5,66.8));t(b,n3,F,(91.5,66.8),(91.5,65.0));v(b,n3,(91.5,65.0));t(b,n3,B,(91.5,65.0),(91.5,58.0));t(b,n3,B,(91.5,58.0),(86.5,58.0));t(b,n3,B,(86.5,58.0),(86.5,55.0));t(b,n3,B,(86.5,55.0),(90.2,55.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
