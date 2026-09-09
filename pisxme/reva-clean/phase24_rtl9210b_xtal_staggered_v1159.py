"""V1159: remove exact local rail field, then use outboard XTAL_IN transition."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_QFN_GND_ATTACH_V1123.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_XTAL_STAGGERED_V1159.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def pos(x): return (round(x/1e6,4),round(x/1e6,4))
def ep(x):
 if type(x).__name__=='PCB_VIA': return [(round(x.GetX()/1e6,4),round(x.GetY()/1e6,4))]
 return [(round(x.GetStart().x/1e6,4),round(x.GetStart().y/1e6,4)),(round(x.GetEnd().x/1e6,4),round(x.GetEnd().y/1e6,4))]
def tr(b,c,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNetCode(c);b.Add(q)
def via(b,c,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNetCode(c);b.Add(q)
b=pcbnew.LoadBoard(str(BASE));ni=b.FindNet('XTAL_IN').GetNetCode();no=b.FindNet('XTAL_OUT').GetNetCode();n1=b.FindNet('RTL_1V1').GetNetCode();n3=b.FindNet('RTL_3V3').GetNetCode()
targets={(94.05,68.0),(92.8,68.0),(92.8,69.3),(92.8,70.0),(92.8,71.2),(92.8,75.0)}
old=[]
for x in list(b.GetTracks()):
 if x.GetNetCode()==n1 and any(p in targets for p in ep(x)): old.append(x)
assert len(old)>=10, len(old)
for x in old:b.Remove(x)
railvias=[x for x in list(b.GetTracks()) if x.GetNetCode()==n3 and type(x).__name__=='PCB_VIA' and round(x.GetX()/1e6,4)==93.0 and round(x.GetY()/1e6,4)==66.8]
assert railvias
for x in railvias:b.Remove(x)
xt=[x for x in list(b.GetTracks()) if x.GetNetCode() in (ni,no)]
for x in xt:b.Remove(x)
tr(b,ni,F,[(94.05,67.2),(93.5,67.2),(92.5,66.8)]);via(b,ni,(92.5,66.8));tr(b,ni,B,[(92.5,66.8),(94.5,66.8),(94.5,75),(85.5,75),(85.5,62)]);via(b,ni,(85.5,62));tr(b,ni,F,[(85.5,62),(88,62),(88,59)])
tr(b,no,F,[(94.05,67.6),(93.4,67.6),(91.5,67.6)]);via(b,no,(91.5,67.6));tr(b,no,B,[(91.5,67.6),(88,68),(88,58)]);via(b,no,(88,58));tr(b,no,F,[(88,58),(89.4,58),(89.4,59),(90.5,59),(90.5,60.5),(91,62)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT,'removed rail objects',len(old)+len(railvias))
