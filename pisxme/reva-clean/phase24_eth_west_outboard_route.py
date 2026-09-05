"""Disposable live-pad routing trial for the mechanically clear west island."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_CM5_GROUND_RIGHT_SAME_ROWS.kicad_pcb'; OUT=R/'PHASE24_ETH_WEST_OUTBOARD_ROUTE.kicad_pcb'
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
for r,p,o in [('U9',(26,104),-90),('U6',(20,104),-90),('J2',(15,145),0)]:
 f=b.FindFootprintByReference(r); f.SetPosition(V(*p)); f.SetOrientationDegrees(o)
M={'TD3_P':('J7','3','U9','5','J2','9'),'TD3_N':('J7','5','U9','4','J2','10'),
   'TD2_N':('J7','9','U9','2','J2','8'),'TD2_P':('J7','11','U9','1','J2','7'),
   'TD1_P':('J7','4','U6','5','J2','3'),'TD1_N':('J7','6','U6','4','J2','6'),
   'TD0_N':('J7','10','U6','2','J2','2'),'TD0_P':('J7','12','U6','1','J2','1')}
E={k:(pad(b,a,ap),pad(b,u,up),pad(b,j,jp),b.FindNet('CM5_GBE_'+k)) for k,(a,ap,u,up,j,jp) in M.items()}
for t in list(b.GetTracks()):
 if str(t.GetNetname()).rsplit('/',1)[-1].startswith(('CM5_GBE_TD','ETH_','GBE_')): b.Remove(t)
# Source fanout uses two F.Cu pair corridors; the two interleaved pairs use
# ordinary through-vias outside the J7 pad field and B.Cu west lanes.
F=pcbnew.F_Cu; B=pcbnew.B_Cu
left={'TD3_P':[(32.96,99.1),(31.2,99.1),(29.8,101.4),(28.0,102.8)],
      'TD3_N':[(32.96,99.5),(31.6,99.5),(30.2,101.8),(28.5,103.2)],
      'TD2_N':[(32.96,100.3),(31.8,100.3),(30.8,102.6),(29.2,103.8)],
      'TD2_P':[(32.96,100.7),(32.0,100.7),(31.4,103.0),(29.8,104.2)]}
for k,pts in left.items(): route(b,E[k][3],[E[k][0]]+pts[1:]+[E[k][1]],F)
right={'TD1_P':[(36.04,99.1),(34.8,98.2),(31.0,97.2),(27.0,97.2)],
       'TD1_N':[(36.04,99.5),(35.0,99.0),(31.5,98.2),(27.5,98.2)],
       'TD0_N':[(36.04,100.3),(35.2,100.8),(32.0,99.2),(28.0,99.2)],
       'TD0_P':[(36.04,100.7),(35.4,101.2),(32.5,100.2),(28.5,100.2)]}
for k,pts in right.items():
 q=E[k][3]; p=pts[-1]; via(b,q,p); route(b,q,[E[k][0]]+pts[1:],B); route(b,q,[p,E[k][1]],F)
# West-edge connector corridors are separated on F/B copper and approach
# the through-hole MagJack directly; no plane-layer signals are used.
Fpaths={'TD3_P':[(25,103.615),(24,118),(22,132),E['TD3_P'][2]],
 'TD3_N':[(25.5,104.385),(24.5,119),(23,133),E['TD3_N'][2]],
 'TD2_N':[(26.5,103.615),(25.5,120),(24,134),E['TD2_N'][2]],
 'TD2_P':[(27,104.385),(26.5,121),(25,135),E['TD2_P'][2]]}
for k,pts in Fpaths.items(): route(b,E[k][3],pts,F)
Bpaths={'TD1_P':[(19,104.385),(18,122),(17,132),E['TD1_P'][2]],
 'TD1_N':[(19.5,103.615),(18.5,123),(18,133),E['TD1_N'][2]],
 'TD0_N':[(20.5,103.615),(20,124),(19,134),E['TD0_N'][2]],
 'TD0_P':[(21,104.385),(21.5,125),(20.5,135),E['TD0_P'][2]]}
for k,pts in Bpaths.items():
 q=E[k][3]; start=pts[0]; via(b,q,start); route(b,q,pts,B)
b.Save(str(OUT)); print(OUT)
