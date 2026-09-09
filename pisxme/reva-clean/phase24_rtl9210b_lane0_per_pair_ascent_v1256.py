"""V1256: per-pair layer-swapped ascent into separated upper lanes."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_LANE0_ALL_LOWER_LEFT_V1250.kicad_pcb';OUT=H/'PHASE24_RTL9210B_LANE0_PER_PAIR_ASCENT_V1256.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def inside(p):return 85<=pcbnew.ToMM(p.x)<=116 and 56<=pcbnew.ToMM(p.y)<=80
def upper(q):
 xs=[pcbnew.ToMM(q.GetStart().x),pcbnew.ToMM(q.GetEnd().x)];ys=[pcbnew.ToMM(q.GetStart().y),pcbnew.ToMM(q.GetEnd().y)]
 return max(xs)>=64 and min(xs)<=145 and max(ys)>=39 and min(ys)<=56
def s(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for q in list(b.GetTracks()):
 if inside(q.GetStart()) or inside(q.GetEnd()) or upper(q):b.RemoveNative(q)
for q in list(b.GetTracks()):
 if type(q).__name__=='PCB_VIA' and (inside(q.GetPosition()) or upper(q)):b.RemoveNative(q)
u=b.FindFootprintByReference('U1')
# Existing V1250 source exits; each pair swaps to F.Cu at a distinct outer
# column, ascends, and returns to B.Cu at a separated upper-row transition.
R=[('LANE0_RXP','64',[(94.05,71.6),(95.0,71.6),(95.0,72.4)],(95.0,72.4),(106.0,72.4),42.0),('LANE0_RXN','65',[(94.05,72.0),(92.8,72.0),(92.8,70.8)],(92.8,70.8),(108.0,70.8),43.0),('LANE0_TXN','67',[(94.05,72.8),(92.2,72.8),(92.2,72.6)],(92.2,72.6),(110.0,74.4),44.0),('LANE0_TXP','68',[(94.05,73.2),(90.8,73.2),(90.8,76.8)],(90.8,76.8),(104.5,76.8),45.0)]
for name,pad,fp,sv,sw,row in R:
 n=b.FindNet(name);s(b,n,F,fp);v(b,n,sv)
 if name in ('LANE0_RXN','LANE0_TXN'):s(b,n,B,[sv,(sv[0],sw[1]),sw])
 else:s(b,n,B,[sv,sw])
 v(b,n,sw);s(b,n,F,[sw,(sw[0],row)]);v(b,n,(sw[0],row));s(b,n,B,[(sw[0],row),(128.0,row)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
