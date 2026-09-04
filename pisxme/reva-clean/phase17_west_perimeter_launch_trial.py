"""Phase-17 perimeter-launch experiment; disposable and MDI-only."""
from pathlib import Path
import pcbnew

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'ACREAGE_PHASE17_F1RIGHT40_ETH_GROUND_FIXED.kicad_pcb'
OUT=ROOT/'ACREAGE_PHASE17_WEST_PERIMETER_MDI.kicad_pcb'
W=pcbnew.FromMM(.13208)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def P(b,r,n): return (pcbnew.ToMM(b.FindFootprintByReference(r).FindPadByNumber(str(n)).GetPosition().x), pcbnew.ToMM(b.FindFootprintByReference(r).FindPadByNumber(str(n)).GetPosition().y))
def N(b,n): return b.FindNet(n) or b.FindNet('/ETHERNET/'+n)
def A(b,n,pts,layer=pcbnew.F_Cu):
    for a,z in zip(pts,pts[1:]):
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer); t.SetWidth(W); t.SetNet(n); b.Add(t)
def via(b,n,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(n); b.Add(q)

b=pcbnew.LoadBoard(str(BASE))
for r,pos,ang in [('U9',(220,25),0),('U6',(230,25),0),('J2',(282.5,25),180)]:
    f=b.FindFootprintByReference(r); f.SetPosition(V(*pos)); f.SetOrientationDegrees(ang)
spec={
 'CM5_GBE_TD3_P':(3,5,6,9),'CM5_GBE_TD3_N':(5,4,7,10),'CM5_GBE_TD2_N':(9,2,9,8),'CM5_GBE_TD2_P':(11,1,10,7),
 'CM5_GBE_TD1_P':(4,5,6,3),'CM5_GBE_TD1_N':(6,4,7,6),'CM5_GBE_TD0_N':(10,2,9,2),'CM5_GBE_TD0_P':(12,1,10,1)}
esdref={'CM5_GBE_TD3_P':'U9','CM5_GBE_TD3_N':'U9','CM5_GBE_TD2_N':'U9','CM5_GBE_TD2_P':'U9',
        'CM5_GBE_TD1_P':'U6','CM5_GBE_TD1_N':'U6','CM5_GBE_TD0_N':'U6','CM5_GBE_TD0_P':'U6'}
ep={n:(P(b,'J7',j7),P(b,esdref[n],es),P(b,esdref[n],ed),P(b,'J2',j2)) for n,(j7,es,ed,j2) in spec.items()}
for t in list(b.GetTracks()):
    if t.GetNetname().split('/')[-1].startswith(('CM5_GBE_TD','ETH_','GBE_')): b.Remove(t)

# Source order is chosen to match the physical left-side ESD land rows. The
# unique west x offsets and ascending top lanes avoid shared verticals.
source_order=('CM5_GBE_TD2_P','CM5_GBE_TD2_N','CM5_GBE_TD3_N','CM5_GBE_TD3_P',
              'CM5_GBE_TD0_P','CM5_GBE_TD0_N','CM5_GBE_TD1_N','CM5_GBE_TD1_P')
for i,n in enumerate(source_order):
    q=N(b,n); s,e=ep[n][0],ep[n][1]
    # Keep the two J7 source columns on independent initial escapes.  The
    # right column must not use the short x=2..10 offsets: those horizontals
    # would pass through the left-column pads at the shared row y values.
    if i < 4:
        x=4.0+i*2.0; y=12.0+i*1.1; tx=219.0-i*0.25
        A(b,q,[s,(x,s[1]),(x,y),(tx,y),(tx,e[1]),e])
    else:
        x=38.0+(i-4)*2.0; y=16.0+(i-4)*1.1; tx=229.0-(i-4)*0.25
        # The right J7 column is transitioned immediately and kept on B.Cu
        # for the west/top perimeter run. This prevents its source fanout
        # from crossing the left J7 column or the U9 package escape.
        v=(x,s[1]); A(b,q,[s,v],pcbnew.F_Cu); via(b,q,v)
        vend=(tx,e[1]); A(b,q,[v,(x,y),(tx,y),vend],pcbnew.B_Cu); via(b,q,vend)
        A(b,q,[vend,e],pcbnew.F_Cu)
    # The USON source lands share an x coordinate.  Stagger the final
    # approach x positions in reverse row order so no later vertical can
    # pierce an earlier horizontal dogbone.

# The right-side ESD lands launch into monotonic lanes; through-hole J2 pads
# are reached by short vertical dogbones at their actual centers.
dest_order=('CM5_GBE_TD3_N','CM5_GBE_TD3_P','CM5_GBE_TD2_N','CM5_GBE_TD2_P',
            'CM5_GBE_TD1_N','CM5_GBE_TD1_P','CM5_GBE_TD0_N','CM5_GBE_TD0_P')
for i,n in enumerate(dest_order):
    q=N(b,n); s,d=ep[n][2],ep[n][3]; y=38.0+i*1.1; x=s[0]+(1.5 if s[0]<225 else -1.5)
    # Give each shared USON destination row its own outward dogbone x.
    x=s[0]+1.5+i*0.25
    if i >= 4:
        # Keep the U6-to-MagJack corridors on B.Cu so they cannot intersect
        # the U9 package escape or the U9 F.Cu lanes. The transition is
        # outside the package pad; the PTH MagJack pad is the legal B.Cu
        # landing.
        v=(x,s[1]); A(b,q,[s,v],pcbnew.F_Cu); via(b,q,v)
        A(b,q,[v,(x,y),(d[0],y),d],pcbnew.B_Cu)
    else:
        A(b,q,[s,(x,s[1]),(x,y),(d[0],y),d])
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print('saved',OUT)
