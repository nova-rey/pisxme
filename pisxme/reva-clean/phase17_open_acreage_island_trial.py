"""Phase-17 fresh acreage Ethernet island discriminator.

This deliberately regenerates the MDI graph from pad centers after moving the
complete ESD/MagJack island into the open lower-right acreage region.  It is a
disposable placement/routing experiment; center-tap support is retained from
the accepted ancestor for the later full-island pass.
"""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "ACREAGE_PHASE17_F1RIGHT40_ETH_GROUND_FIXED.kicad_pcb"
OUT = ROOT / "ACREAGE_PHASE17_OPEN_ACREAGE_MDI.kicad_pcb"
W = pcbnew.FromMM(0.13208)

def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return (pcbnew.ToMM(p.x), pcbnew.ToMM(p.y))
def N(b,name):
    q=b.FindNet(name) or b.FindNet('/ETHERNET/'+name) or b.FindNet('/'+name)
    if q is None: raise RuntimeError(name)
    return q
def P(b,ref,num):
    p=b.FindFootprintByReference(ref).FindPadByNumber(str(num))
    if p is None: raise RuntimeError(f'{ref}.{num}')
    return xy(p.GetPosition())
def seg(b,n,a,z,layer=pcbnew.F_Cu):
    t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer); t.SetWidth(W); t.SetNet(n); b.Add(t)
def route(b,n,points,layer=pcbnew.F_Cu):
    for a,z in zip(points,points[1:]): seg(b,n,a,z,layer)
def via(b,n,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(n); b.Add(q)

b=pcbnew.LoadBoard(str(BASE))
b.FindFootprintByReference('U9').SetPosition(V(205,140)); b.FindFootprintByReference('U9').SetOrientationDegrees(270)
b.FindFootprintByReference('U6').SetPosition(V(215,140)); b.FindFootprintByReference('U6').SetOrientationDegrees(270)
b.FindFootprintByReference('J2').SetPosition(V(282.5,140)); b.FindFootprintByReference('J2').SetOrientationDegrees(180)
spec={
 'CM5_GBE_TD3_P':('J7',3,'U9',5,6,'J2',9),'CM5_GBE_TD3_N':('J7',5,'U9',4,7,'J2',10),
 'CM5_GBE_TD2_N':('J7',9,'U9',2,9,'J2',8),'CM5_GBE_TD2_P':('J7',11,'U9',1,10,'J2',7),
 'CM5_GBE_TD1_P':('J7',4,'U6',5,6,'J2',3),'CM5_GBE_TD1_N':('J7',6,'U6',4,7,'J2',6),
 'CM5_GBE_TD0_N':('J7',10,'U6',2,9,'J2',2),'CM5_GBE_TD0_P':('J7',12,'U6',1,10,'J2',1)}
ep={n:(P(b,a,ap),P(b,c,cp),P(b,c,cd),P(b,d,dp)) for n,(a,ap,c,cp,cd,d,dp) in spec.items()}
for item in list(b.GetTracks()):
    if item.GetNetname().split('/')[-1].startswith(('CM5_GBE_TD','ETH_','GBE_')): b.Remove(item)

# Source-side lanes descend monotonically from the CM5 launch into the open
# lower-right acreage. Each initial dogbone has a distinct x coordinate.
source_lanes={
 'CM5_GBE_TD3_P':(25.0,155.0,195.0,155.0,200.0), 'CM5_GBE_TD3_N':(27.0,153.0,195.0,153.0,200.0),
 'CM5_GBE_TD2_N':(29.0,151.0,195.0,151.0,200.0), 'CM5_GBE_TD2_P':(31.0,149.0,195.0,149.0,200.0),
 'CM5_GBE_TD1_P':(40.0,147.0,205.0,147.0,210.0), 'CM5_GBE_TD1_N':(42.0,145.0,205.0,145.0,210.0),
 'CM5_GBE_TD0_N':(44.0,143.0,205.0,143.0,210.0), 'CM5_GBE_TD0_P':(46.0,141.0,205.0,141.0,210.0)}
for i,(n,(x,y,ex,ey,_)) in enumerate(source_lanes.items()):
    q=N(b,n); s=ep[n][0]; e=ep[n][1]
    if i in (2,3,6,7):
        v0=(x,y); route(b,q,[s,(x,s[1]),v0]); via(b,q,v0); route(b,q,[v0,(ex,ey)],pcbnew.B_Cu); via(b,q,(ex,ey)); route(b,q,[(ex,ey),e])
    else: route(b,q,[s,(x,s[1]),(x,y),(ex,ey),e])

# Connector-side lanes run back from each ESD package to the right-edge
# MagJack. F.Cu carries TD3/TD1; TD2/TD0 use ordinary transitions and B.Cu.
dest_lanes={
 'CM5_GBE_TD3_P':(202.0,125.0,275.0,125.0), 'CM5_GBE_TD3_N':(203.0,123.0,277.0,123.0),
 'CM5_GBE_TD2_N':(204.0,121.0,278.0,121.0), 'CM5_GBE_TD2_P':(206.0,119.0,279.0,119.0),
 'CM5_GBE_TD1_P':(212.0,117.0,282.0,117.0), 'CM5_GBE_TD1_N':(213.0,115.0,284.0,115.0),
 'CM5_GBE_TD0_N':(214.0,113.0,286.0,113.0), 'CM5_GBE_TD0_P':(216.0,111.0,288.0,111.0)}
for i,(n,(x,y,ex,ey)) in enumerate(dest_lanes.items()):
    q=N(b,n); s=ep[n][2]; d=ep[n][3]
    if i in (2,3,6,7):
        v0=(x,y); route(b,q,[s,(x,s[1]),v0]); via(b,q,v0); v1=(ex,ey); route(b,q,[v0,v1],pcbnew.B_Cu); via(b,q,v1); route(b,q,[v1,d])
    else: route(b,q,[s,(x,s[1]),(x,y),(ex,ey),d])
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); pcbnew.SaveBoard(str(OUT),b); print('saved',OUT)
