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
OUT = R / 'PHASE24_SELECTED_MACRO_STORAGE_V26_CLOCK_V2_NATIVE_ANCHOR.kicad_pcb'
CLOCK = {'/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC'}

def tr(p, src_u7, dst_u7):
    # 180 degrees about fixture U7, then anchor at base U7, with 10/20 mm
    # No translation: retain the fixture's native U7-relative launch first.
    x = dst_u7.x - (p.x - src_u7.x) + pcbnew.FromMM(10)
    y = dst_u7.y - (p.y - src_u7.y)
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
    # Preserve the fixture's per-pad copper-layer sets explicitly.  The
    # acreage placeholders may be on B.Cu as a mechanical experiment and
    # must not silently turn fixture F.Cu return pads into B.Cu pads.
    for pad, source_pad in zip(dst.Pads(), src.Pads()):
        layers = pcbnew.LSET()
        if source_pad.GetLayerSet().Contains(pcbnew.F_Cu): layers.AddLayer(pcbnew.F_Cu)
        if source_pad.GetLayerSet().Contains(pcbnew.B_Cu): layers.AddLayer(pcbnew.B_Cu)
        pad.SetLayerSet(layers)
        net = base.FindNet(pad.GetNetname())
        if net is None: raise RuntimeError(f'missing clock net {pad.GetNetname()}')
        pad.SetNet(net); pad.SetNetCode(net.GetNetCode())

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

# The translated passive island is intentionally south of U7, so its former
# fixture launch points are no longer on the U7 pads.  Add ordinary through
# vias outside the QFN field and three monotonic return legs to those launch
# points; this is the only new copper in the experiment.
launch = {'52': ('/STORAGE/BRIDGE_XI', 0.75),
          '53': ('/STORAGE/BRIDGE_VSSOSC', 0.25),
          '54': ('/STORAGE/BRIDGE_XO', -0.25)}
u7 = base.FindFootprintByReference('U7')
for number, (name, off) in launch.items():
    pad = next(p for p in u7.Pads() if p.GetNumber() == number)
    net = base.FindNet(name)
    start = pad.GetPosition()
    via_xy = pcbnew.VECTOR2I(start.x + pcbnew.FromMM(off), start.y + pcbnew.FromMM(1.0))
    # The exact transformed launch is the endpoint on the copied clock
    # graph nearest the corresponding transformed U7 pad.
    candidates = []
    srcpad = next(p for p in fix.FindFootprintByReference('U7').Pads() if p.GetNumber() == number)
    target = tr(srcpad.GetPosition(), fu7, bu7)
    if abs(target.x - start.x) < pcbnew.FromMM(.01) and abs(target.y - start.y) < pcbnew.FromMM(.01):
        continue
    via = pcbnew.PCB_VIA(base); via.SetPosition(via_xy); via.SetWidth(pcbnew.FromMM(.5)); via.SetDrill(pcbnew.FromMM(.3)); via.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); via.SetNet(net); base.Add(via)
    dog = pcbnew.PCB_TRACK(base); dog.SetStart(start); dog.SetEnd(via_xy); dog.SetLayer(pcbnew.F_Cu); dog.SetWidth(pcbnew.FromMM(.15)); dog.SetNet(net); base.Add(dog)
    leg = pcbnew.PCB_TRACK(base); leg.SetStart(via_xy); leg.SetEnd(pcbnew.VECTOR2I(via_xy.x, target.y)); leg.SetLayer(pcbnew.B_Cu); leg.SetWidth(pcbnew.FromMM(.15)); leg.SetNet(net); base.Add(leg)
    leg2 = pcbnew.PCB_TRACK(base); leg2.SetStart(pcbnew.VECTOR2I(via_xy.x, target.y)); leg2.SetEnd(target); leg2.SetLayer(pcbnew.B_Cu); leg2.SetWidth(pcbnew.FromMM(.15)); leg2.SetNet(net); base.Add(leg2)
base.BuildListOfNets(); base.Save(str(OUT)); print(OUT)
