"""Apply only the proven three-exit JMS583 geometry to the FULL7 USB3 frame."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_DUAL_MODE_STORAGE_NC39_USB3_FULL7.kicad_pcb'
DONOR=R/'PHASE24_JMS583_THREE_EXIT_COAUTHOR.kicad_pcb'
OUT=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_THREE_EXITS.kicad_pcb'
NETS={'XIN','XOUT','JMS_XAVDDH'}
def T(q,dx,dy): return pcbnew.VECTOR2I(q.x+dx,q.y+dy)
b=pcbnew.LoadBoard(str(BASE)); d=pcbnew.LoadBoard(str(DONOR))
bu=b.FindFootprintByReference('U11').GetPosition(); du=d.FindFootprintByReference('U11').GetPosition(); dx,dy=bu.x-du.x,bu.y-du.y
for ref in ('Y10','C84'):
    s=d.FindFootprintByReference(ref); z=b.FindFootprintByReference(ref)
    z.SetPosition(T(s.GetPosition(),dx,dy)); z.SetOrientationDegrees(s.GetOrientationDegrees())
for item in list(b.GetTracks()):
    if item.GetNetname() in NETS: b.RemoveNative(item)
for item in d.GetTracks():
    if item.GetNetname() not in NETS: continue
    n=b.FindNet(item.GetNetname())
    if isinstance(item,pcbnew.PCB_VIA):
        q=pcbnew.PCB_VIA(b); q.SetPosition(T(item.GetPosition(),dx,dy)); q.SetWidth(item.GetWidth(pcbnew.F_Cu)); q.SetDrill(item.GetDrill()); q.SetLayerPair(item.TopLayer(),item.BottomLayer())
    else:
        q=pcbnew.PCB_TRACK(b); q.SetStart(T(item.GetStart(),dx,dy)); q.SetEnd(T(item.GetEnd(),dx,dy)); q.SetLayer(item.GetLayer()); q.SetWidth(item.GetWidth())
    q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
