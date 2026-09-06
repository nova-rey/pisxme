"""Place the native-clean V2 clock fixture on the V26 U7 frame.

Unlike the rejected donor transplant, this uses the standalone fixture whose
clock graph has already passed native KiCad connectivity and short/crossing
checks.  It applies the footprint's required 180-degree transform and a
small south/east translation so the complete passive island stays outside
the U7/J7/USB3 pad fields.
"""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / 'PHASE24_SELECTED_MACRO_SWAP_STORAGE_SATA_PAIR_CORRIDOR_V26_AUTH_SKEW.kicad_pcb'
FIX = R / 'PHASE24_COMPLETE_CLOCK_FIXTURE_V2.kicad_pcb'
OUT = R / 'PHASE24_SELECTED_MACRO_STORAGE_V26_CLOCK_V2_SOUTH40.kicad_pcb'
CLOCK = {'/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC'}

def tr(p, src_u7, dst_u7):
    # 180 degrees about fixture U7, then anchor at base U7, with 10/20 mm
    # local clearance translation.  The passive island is deliberately well
    # south of U7; the acreage basis has inherited SATA copper immediately
    # north/east of the bridge.
    x = dst_u7.x - (p.x - src_u7.x) + pcbnew.FromMM(10)
    y = dst_u7.y - (p.y - src_u7.y) + pcbnew.FromMM(40)
    return pcbnew.VECTOR2I(x, y)

base = pcbnew.LoadBoard(str(BASE)); fix = pcbnew.LoadBoard(str(FIX))
bu7 = base.FindFootprintByReference('U7').GetPosition()
fu7 = fix.FindFootprintByReference('U7').GetPosition()
for item in list(base.GetTracks()):
    if item.GetNetname() in CLOCK: base.RemoveNative(item)

for ref in ('Y1','R23','C42','C43'):
    dst = base.FindFootprintByReference(ref); src = fix.FindFootprintByReference(ref)
    dst.SetPosition(tr(src.GetPosition(), fu7, bu7))
    dst.SetOrientationDegrees(src.GetOrientationDegrees() + 180)

for item in fix.GetTracks():
    if item.GetNetname() not in CLOCK: continue
    net = base.FindNet(item.GetNetname())
    if isinstance(item, pcbnew.PCB_VIA):
        out = pcbnew.PCB_VIA(base); out.SetPosition(tr(item.GetPosition(), fu7, bu7))
        out.SetWidth(item.GetWidth(pcbnew.F_Cu)); out.SetDrill(item.GetDrill())
        out.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    else:
        out = pcbnew.PCB_TRACK(base); out.SetStart(tr(item.GetStart(), fu7, bu7)); out.SetEnd(tr(item.GetEnd(), fu7, bu7))
        out.SetLayer(item.GetLayer()); out.SetWidth(item.GetWidth())
    out.SetNet(net); base.Add(out)
base.BuildListOfNets(); base.Save(str(OUT)); print(OUT)
