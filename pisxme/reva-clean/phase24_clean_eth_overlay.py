"""Build a disposable clean-neighborhood Ethernet overlay.

All affected high-speed copper is removed from the selected macro copy before
the unmodified CM5IO Ethernet route is transplanted at its native geometry.
This is a discriminator, not an acreage promotion.
"""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_SELECTED_MACRO_PLACEMENT.kicad_pcb'
ORACLE=R/'CM5IO_DIRECT_J7_ETHERNET_FIXTURE.kicad_pcb'
OUT=R/'PHASE24_CLEAN_ETH_OVERLAY.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
b=pcbnew.LoadBoard(str(BASE)); o=pcbnew.LoadBoard(str(ORACLE)); oracle_tracks=list(o.GetTracks())
affected=('CM5_GBE_','/ETHERNET/','/GBE_','CM5_USB3_','/STORAGE/','/CLOCK/')
for ref in ('U6','U9','J2'):
    src=o.FindFootprintByReference(ref); dst=b.FindFootprintByReference(ref)
    dst.SetPosition(src.GetPosition()); dst.SetOrientationDegrees(src.GetOrientation().AsDegrees())
for t in list(b.GetTracks()):
    if any(k in t.GetNetname() for k in affected): b.Remove(t)
for item in oracle_tracks:
    short=item.GetNetname().rsplit('/',1)[-1]
    if not short.startswith('CM5_GBE_TD'): continue
    n=b.FindNet(short)
    t=pcbnew.PCB_TRACK(b);t.SetStart(item.GetStart());t.SetEnd(item.GetEnd());t.SetLayer(item.GetLayer());t.SetWidth(item.GetWidth());t.SetNet(n);b.Add(t)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
