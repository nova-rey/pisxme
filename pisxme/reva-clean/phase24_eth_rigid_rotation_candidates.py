"""Generate disposable CM5IO Ethernet rigid-rotation floorplan probes.

The transform rotates the complete official Ethernet copper about the native
J7 MDI launch center. J7 pads remain fixed; endpoint footprints and all
endpoint-side copper move coherently. No expected connectivity is added.
"""
from pathlib import Path
import math
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_SELECTED_MACRO_PLACEMENT.kicad_pcb'
ORACLE=R/'CM5IO_DIRECT_J7_ETHERNET_FIXTURE.kicad_pcb'
PIVOT=(35.0,100.0)
ANGLES=(-45.0,-30.0,30.0,45.0)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def rot(q,a):
    t=math.radians(a); x=q[0]-PIVOT[0]; y=q[1]-PIVOT[1]
    return (PIVOT[0]+x*math.cos(t)-y*math.sin(t),
            PIVOT[1]+x*math.sin(t)+y*math.cos(t))
def near_j7(board,q):
    f=board.FindFootprintByReference('J7')
    return any(abs(mm(p.GetPosition())[0]-q[0])<1e-5 and abs(mm(p.GetPosition())[1]-q[1])<1e-5 for p in f.Pads())
ot=pcbnew.LoadBoard(str(ORACLE))
for angle in ANGLES:
    b=pcbnew.LoadBoard(str(BASE))
    for t in list(b.GetTracks()):
        if any(k in t.GetNetname() for k in ('CM5_GBE_','/ETHERNET/','/GBE_')): b.Remove(t)
    for ref in ('U6','U9','J2'):
        f=ot.FindFootprintByReference(ref); q=rot(mm(f.GetPosition()),angle)
        dst=b.FindFootprintByReference(ref); dst.SetPosition(V(*q)); dst.SetOrientationDegrees(f.GetOrientation().AsDegrees()+angle)
    for item in ot.GetTracks():
        short=item.GetNetname().rsplit('/',1)[-1]
        if not short.startswith('CM5_GBE_TD'): continue
        n=b.FindNet(short)
        a=mm(item.GetStart()); z=mm(item.GetEnd())
        a=a if near_j7(ot,a) else rot(a,angle)
        z=z if near_j7(ot,z) else rot(z,angle)
        if a==z: continue
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(item.GetLayer()); t.SetWidth(item.GetWidth()); t.SetNet(n); b.Add(t)
    b.BuildListOfNets()
    out=R/f'PHASE24_ETH_RIGID_ROT{angle:+.0f}.kicad_pcb'; b.Save(str(out)); print(out)
