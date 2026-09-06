"""Route the official-placement Ethernet CT/support island on B.Cu."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_OFFICIAL_ETH_SUPPORT_MATERIALIZED.kicad_pcb'
OUT=R/'PHASE24_OFFICIAL_ETH_CT_SUPPORT_ROUTED.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def P(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def seg(b,net,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(B);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(net);b.Add(t)
def path(b,net,pts):
    for a,z in zip(pts,pts[1:]): seg(b,net,a,z)
b=pcbnew.LoadBoard(str(BASE))
J=b.FindFootprintByReference('J2')
# Reverse-order CT endpoints are separated into four explicit B.Cu staging
# lanes; no guessed schematic coordinates are used.
ct=[('ETH_CT1','11','C48','1',100,66),('ETH_CT2','12','C49','1',104,64),('ETH_CT3','13','C50','1',108,62),('ETH_CT4','14','C51','1',112,60)]
for netn,jpn,cr,cp,x,y in ct:
    net=b.FindNet(netn); a=xy(P(b,'J2',jpn)); z=xy(P(b,cr,cp)); path(b,net,[a,(x,a[1]),(x,y),(z[0],y),z])
# Each 75-ohm branch is a local pad-to-pad connection.
for c,r in [('C48','R26'),('C49','R27'),('C50','R28'),('C51','R29')]:
    net=b.FindNet('ETH_CT_BRANCH_'+str(int(c[1:])-47)); path(b,net,[xy(P(b,c,'2')),xy(P(b,r,'1'))])
# Common return is one deliberate bus, not separate synthetic joins.
common=b.FindNet('ETH_CT_COMMON')
for r in ['R26','R27','R28','R29']:
    q=xy(P(b,r,'2')); path(b,common,[q,(q[0],78)])
path(b,common,[(68.5,78),(92.5,78),(74.9,78),xy(P(b,'C52','1'))])
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
