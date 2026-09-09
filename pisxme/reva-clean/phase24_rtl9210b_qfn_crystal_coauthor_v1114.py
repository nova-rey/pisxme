"""V1115: V1114 with 3V3 transition moved beyond the pad-hole field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BAS=H/'PHASE24_RTL9210B_RSET_V1092.kicad_pcb';OUT=H/'PHASE24_RTL9210B_QFN_CRYSTAL_COAUTHOR_V1115.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BAS))
for q in list(b.GetTracks()):
 a,z=q.GetStart(),q.GetEnd();n=q.GetNetname()
 if n in ('XTAL_IN',):b.RemoveNative(q)
 if n=='RTL_3V3' and (a==P(94.05,66.8) or z==P(94.05,66.8) or a==P(93,66.8) or z==P(93,66.8) or a==P(93,68.4) or z==P(93,68.4)):b.RemoveNative(q)
 if n=='RTL_1V1' and (a==P(94.05,68) or z==P(94.05,68) or a==P(92.8,68) or z==P(92.8,68) or a==P(92.8,69.3) or z==P(92.8,69.3) or a==P(92.8,75) or z==P(92.8,75)):b.RemoveNative(q)
for q in list(b.GetTracks()):
 if type(q).__name__=='PCB_VIA' and q.GetNetname()=='RTL_3V3' and q.GetPosition()==P(93,66.8):b.RemoveNative(q)
 if type(q).__name__=='PCB_VIA' and q.GetNetname()=='RTL_1V1' and q.GetPosition() in (P(92.8,70),P(92.8,71.2),P(92.8,75)):b.RemoveNative(q)
n3,n1,ni,no=(b.FindNet(x) for x in ('RTL_3V3','RTL_1V1','XTAL_IN','XTAL_OUT'))
t(b,n3,F,[(94.05,66.8),(95.0,66.8),(101.0,67.3)]);v(b,n3,(101.0,67.3));t(b,n3,B,[(101.0,67.3),(101.0,68.4),(100.9,68.4)])
t(b,n1,F,[(94.05,68),(95,68)]);v(b,n1,(95,68));t(b,n1,B,[(95,68),(95,75),(102.5,75)])
t(b,ni,F,[(94.05,67.2),(93.5,67.2),(93.0,67.5),(91.5,68.6)]);v(b,ni,(91.5,68.6));t(b,ni,B,[(91.5,68.6),(91.5,75),(85.5,75),(85.5,62)]);v(b,ni,(85.5,62));t(b,ni,F,[(85.5,62),(88,62),(88,59)])
t(b,no,F,[(94.05,67.6),(92.0,67.6),(90.5,68.8)]);v(b,no,(90.5,68.8));t(b,no,B,[(90.5,68.8),(90.5,57.5),(89.4,57.5)]);v(b,no,(89.4,57.5));t(b,no,F,[(89.4,57.5),(89.4,59.0)]);t(b,no,B,[(89.4,57.5),(91.0,57.5),(91.0,62.0)]);v(b,no,(91.0,62.0));t(b,no,F,[(91.0,62.0),(91.0,62.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
