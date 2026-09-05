"""Disposable live-pad Ethernet routing discriminator.

Moves only the Ethernet island, removes its prior copper, and routes the
CM5IO-authoritative eight MDI nets through native destination pads. This is a
bounded experiment; no result is promoted automatically.
"""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_CM5_GROUND_RIGHT_SAME_ROWS.kicad_pcb'; OUT=R/'PHASE24_ETH_EAST_ESD_WEST_ROUTE.kicad_pcb'
W=pcbnew.FromMM(.13208)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def n(b,name): return b.FindNet(name)
def pad(b,ref,num): return xy(b.FindFootprintByReference(ref).FindPadByNumber(str(num)).GetPosition())
def route(b,net,pts,layer):
    for a,z in zip(pts,pts[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(V(*a)); q.SetEnd(V(*z)); q.SetLayer(layer); q.SetWidth(W); q.SetNet(net); b.Add(q)
def via(b,net,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(net); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for ref,pos in {'U9':(76,104),'U6':(82,104),'J2':(15,145)}.items():
    f=b.FindFootprintByReference(ref); f.SetPosition(V(*pos)); f.SetOrientationDegrees(180 if ref=='J2' else -90)
names={
 'CM5_GBE_TD3_P':('J7','3','U9','5','J2','9'), 'CM5_GBE_TD3_N':('J7','5','U9','4','J2','10'),
 'CM5_GBE_TD2_N':('J7','9','U9','2','J2','8'), 'CM5_GBE_TD2_P':('J7','11','U9','1','J2','7'),
 'CM5_GBE_TD1_P':('J7','4','U6','5','J2','3'), 'CM5_GBE_TD1_N':('J7','6','U6','4','J2','6'),
 'CM5_GBE_TD0_N':('J7','10','U6','2','J2','2'), 'CM5_GBE_TD0_P':('J7','12','U6','1','J2','1')}
ep={name:(pad(b,a,ap),pad(b,u,up),pad(b,j,jp)) for name,(a,ap,u,up,j,jp) in names.items()}
for item in list(b.GetTracks()):
    if str(item.GetNetname()).rsplit('/',1)[-1].startswith(('CM5_GBE_TD','ETH_','GBE_')): b.Remove(item)
F=pcbnew.F_Cu; B=pcbnew.B_Cu
# Left CM5 group: pair-preserving F.Cu corridors to U9.
left={
 'CM5_GBE_TD3_P':[(32.96,99.10),(45,94.0),(62,94.0),(72,102.8),ep['CM5_GBE_TD3_P'][1]],
 'CM5_GBE_TD3_N':[(32.96,99.50),(45,94.8),(62.8,94.8),(72.4,103.6),ep['CM5_GBE_TD3_N'][1]],
 'CM5_GBE_TD2_N':[(32.96,100.30),(45,96.0),(63.6,96.0),(73.0,102.8),ep['CM5_GBE_TD2_N'][1]],
 'CM5_GBE_TD2_P':[(32.96,100.70),(45,96.8),(64.4,96.8),(73.4,103.6),ep['CM5_GBE_TD2_P'][1]]}
for name,pts in left.items(): route(b,n(b,name),[ep[name][0]]+pts[1:],F)
# Right CM5 group: transition outside the J7 pad field, B.Cu over In4,
# and return beside the east-side ESD footprint.
right={
 'CM5_GBE_TD1_P':(ep['CM5_GBE_TD1_P'][0],(40,98.0),(72,98.0),(78,103.6)),
 'CM5_GBE_TD1_N':(ep['CM5_GBE_TD1_N'][0],(40,99.0),(72.8,99.0),(78.4,104.4)),
 'CM5_GBE_TD0_N':(ep['CM5_GBE_TD0_N'][0],(40,101.0),(73.6,101.0),(80,103.6)),
 'CM5_GBE_TD0_P':(ep['CM5_GBE_TD0_P'][0],(40,102.0),(74.4,102.0),(80.4,104.4))}
for name,(start,a,z,end) in right.items():
    q=n(b,name); v0=a; v1=z; route(b,q,[start,v0],F); via(b,q,v0); route(b,q,[v0,v1],B); via(b,q,v1); route(b,q,[v1,end],F)
# Connector-side corridors stay west of power entry and below J7.  The
# MagJack is through-hole, so the final pad launches are layer-agnostic.
out={
 'CM5_GBE_TD3_P':(ep['CM5_GBE_TD3_P'][1],[(72,112),(66,138),(28,138),ep['CM5_GBE_TD3_P'][2]],F),
 'CM5_GBE_TD3_N':(ep['CM5_GBE_TD3_N'][1],[(73,113),(67,140),(29,140),ep['CM5_GBE_TD3_N'][2]],F),
 'CM5_GBE_TD2_N':(ep['CM5_GBE_TD2_N'][1],[(74,114),(68,142),(30,142),ep['CM5_GBE_TD2_N'][2]],F),
 'CM5_GBE_TD2_P':(ep['CM5_GBE_TD2_P'][1],[(75,115),(69,144),(31,144),ep['CM5_GBE_TD2_P'][2]],F)}
for name,(start,mid,layer) in out.items(): route(b,n(b,name),[start]+mid,layer)
outb={
 'CM5_GBE_TD1_P':(ep['CM5_GBE_TD1_P'][1],[(78,116),(70,146),(27,146),ep['CM5_GBE_TD1_P'][2]]),
 'CM5_GBE_TD1_N':(ep['CM5_GBE_TD1_N'][1],[(79,117),(71,148),(28,148),ep['CM5_GBE_TD1_N'][2]]),
 'CM5_GBE_TD0_N':(ep['CM5_GBE_TD0_N'][1],[(80,118),(72,150),(29,150),ep['CM5_GBE_TD0_N'][2]]),
 'CM5_GBE_TD0_P':(ep['CM5_GBE_TD0_P'][1],[(81,119),(73,152),(30,152),ep['CM5_GBE_TD0_P'][2]])}
for name,(start,mid) in outb.items():
    q=n(b,name); v=(start[0],start[1]+1); route(b,q,[start,v],F); via(b,q,v); route(b,q,[v]+mid,B)
b.Save(str(OUT)); print(OUT)
