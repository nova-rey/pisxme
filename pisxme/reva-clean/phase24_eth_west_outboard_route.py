"""Disposable live-pad routing trial for the mechanically clear west island."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_CM5_GROUND_RIGHT_SAME_ROWS.kicad_pcb'; OUT=R/'PHASE24_ETH_WEST_MONOTONIC_ROUTE.kicad_pcb'
W=pcbnew.FromMM(.13208)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def pad(b,r,k): return xy(b.FindFootprintByReference(r).FindPadByNumber(str(k)).GetPosition())
def seg(b,n,a,z,l):
 q=pcbnew.PCB_TRACK(b); q.SetStart(V(*a)); q.SetEnd(V(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); b.Add(q)
def route(b,n,pts,l):
 for a,z in zip(pts,pts[1:]): seg(b,n,a,z,l)
def via(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(n); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for r,p,o in [('U9',(20,90),-90),('U6',(26,90),-90),('J2',(15,145),180)]:
 f=b.FindFootprintByReference(r); f.SetPosition(V(*p)); f.SetOrientationDegrees(o)
M={'TD3_P':('J7','3','U9','5','J2','9'),'TD3_N':('J7','5','U9','4','J2','10'),
   'TD2_N':('J7','9','U9','2','J2','8'),'TD2_P':('J7','11','U9','1','J2','7'),
   'TD1_P':('J7','4','U6','5','J2','3'),'TD1_N':('J7','6','U6','4','J2','6'),
   'TD0_N':('J7','10','U6','2','J2','2'),'TD0_P':('J7','12','U6','1','J2','1')}
E={k:(pad(b,a,ap),pad(b,u,up),pad(b,j,jp),b.FindNet('CM5_GBE_'+k)) for k,(a,ap,u,up,j,jp) in M.items()}
for t in list(b.GetTracks()):
 if str(t.GetNetname()).rsplit('/',1)[-1].startswith(('CM5_GBE_TD','ETH_','GBE_')): b.Remove(t)
# Source fanout is all F.Cu. U9 owns the left CM5 group and U6 the right
# group, matching the native CM5 breakout order.
F=pcbnew.F_Cu; B=pcbnew.B_Cu
left={'TD3_P':[(32.96,99.1),(30.5,96.0),(25.0,92.0)],
      'TD3_N':[(32.96,99.5),(30.9,96.5),(25.5,92.5)],
      'TD2_N':[(32.96,100.3),(31.3,97.0),(26.5,93.0)],
      'TD2_P':[(32.96,100.7),(31.7,97.5),(27.0,93.5)]}
for k,pts in left.items(): route(b,E[k][3],[E[k][0]]+pts[1:]+[E[k][1]],F)
right={'TD1_P':[(36.04,99.1),(37.0,94.0),(30.0,89.0),(25.0,89.615)],
       'TD1_N':[(36.04,99.5),(37.5,94.5),(30.5,89.5),(25.5,89.615)],
       'TD0_N':[(36.04,100.3),(38.0,95.0),(31.0,90.0),(26.5,89.615)],
       'TD0_P':[(36.04,100.7),(38.5,95.5),(31.5,90.5),(27.0,89.615)]}
for k,pts in right.items(): route(b,E[k][3],[E[k][0]]+pts[1:]+[E[k][1]],F)
# West-edge connector corridors are separated on F/B copper and approach
# the through-hole MagJack directly; no plane-layer signals are used.
# Connector launch uses the 180-degree J2 MDI order and approaches the
# through-hole pads from below, leaving CT/LED/shield pads above untouched.
out={'TD3_P':[(19,90.385),(16,120),(10.555,153.89)],
 'TD3_N':[(19.5,90.385),(17,122),(9.285,151.35)],
 'TD2_N':[(20.5,90.385),(18,124),(11.825,151.35)],
 'TD2_P':[(21,90.385),(19,126),(13.095,153.89)],
 'TD1_P':[(25,90.385),(22,128),(18.175,153.89)],
 'TD1_N':[(25.5,90.385),(23,130),(14.365,151.35)],
 'TD0_N':[(26.5,90.385),(24,132),(19.445,151.35)],
 'TD0_P':[(27,90.385),(25,134),(20.715,153.89)]}
for k,pts in out.items(): route(b,E[k][3],pts+[E[k][2]],F)
b.Save(str(OUT)); print(OUT)
