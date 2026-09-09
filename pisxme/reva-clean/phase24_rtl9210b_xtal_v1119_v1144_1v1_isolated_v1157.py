"""V1157: V1119/V1144 pair with local 1V1 source-field branches isolated."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_QFN_GND_ATTACH_V1123.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_XTAL_V1119_V1144_1V1_ISOLATED_V1157.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def key(a,z): return frozenset(((round(a[0],4),round(a[1],4)),(round(z[0],4),round(z[1],4))))
def ends(x):
 if type(x).__name__=='PCB_VIA': p=(x.GetX()/1e6,x.GetY()/1e6); return p,p
 a=x.GetStart();z=x.GetEnd();return (a.x/1e6,a.y/1e6),(z.x/1e6,z.y/1e6)
def tr(b,c,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNetCode(c);b.Add(q)
def via(b,c,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNetCode(c);b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); ni=b.FindNet('XTAL_IN').GetNetCode(); no=b.FindNet('XTAL_OUT').GetNetCode(); n1=b.FindNet('RTL_1V1').GetNetCode()
targets={key((94.05,68.0),(92.8,68.0)),key((92.8,68.0),(92.8,69.3)),key((92.8,69.3),(92.8,75.0)),key((94.05,70.0),(92.8,70.0)),key((92.8,70.0),(92.8,75.0)),key((94.05,71.2),(92.8,71.2)),key((92.8,71.2),(92.8,75.0))}
old=[x for x in list(b.GetTracks()) if x.GetNetCode()==n1 and key(*ends(x)) in targets]; assert len(old)>=7, len(old)
for x in old:b.Remove(x)
u1=(94.05,67.2);u2=(94.05,67.6)
tr(b,ni,F,[u1,(93.5,67.2),(93.0,67.5),(91.5,68.6)]);via(b,ni,(91.5,68.6));tr(b,ni,B,[(91.5,68.6),(91.5,75),(85.5,75),(85.5,62)]);via(b,ni,(85.5,62));tr(b,ni,F,[(85.5,62),(88,62),(88,59)])
tr(b,no,F,[u2,(93.4,67.6),(91.5,67.6)]);via(b,no,(91.5,67.6));tr(b,no,B,[(91.5,67.6),(88,68),(88,58)]);via(b,no,(88,58));tr(b,no,F,[(88,58),(89.4,58),(89.4,59),(90.5,59),(90.5,60.5),(91,62)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT,'removed RTL_1V1',len(old))
