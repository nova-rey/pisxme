"""Disposable native-pad-aware REXT repair on the integrated storage basis."""
from pathlib import Path
import os
import pcbnew

R = Path(__file__).resolve().parent
base = R / os.environ.get("P24_REXT_BASE", "PHASE24_STORAGE_AUTHORITY_CORRECTED_USB3_SATA_ZONES_FINAL.kicad_pcb")
out = R / os.environ.get("P24_REXT_OUT", "PHASE24_STORAGE_REXT_REPAIR_V1.kicad_pcb")
b = pcbnew.LoadBoard(str(base))
if b is None:
    raise SystemExit("cannot load base")

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))
def mm(p):
    return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def pad(ref, number):
    return b.FindFootprintByReference(ref).FindPadByNumber(str(number))
def track(net, a, z, layer):
    t = pcbnew.PCB_TRACK(b)
    t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(net); t.SetNetCode(net.GetNetCode())
    b.Add(t)

net = b.FindNet("JMS_REXT")
for item in list(b.GetTracks()):
    if item.GetNetCode() == net.GetNetCode():
        b.RemoveNative(item)
src = mm(pad("U11", 39).GetPosition())
dst = mm(pad("R80", 1).GetPosition())
# Leave the 0.4-mm QFN row to the west, transition once outside the field,
# and return on F.Cu through a short dogbone. No via is placed in a pad.
vsrc = (src[0] - 1.0, src[1])
track(net, src, vsrc, pcbnew.F_Cu)
track(net, vsrc, (vsrc[0], dst[1]), pcbnew.F_Cu)
track(net, (vsrc[0], dst[1]), dst, pcbnew.F_Cu)
b.BuildListOfNets(); b.Save(str(out)); print(out)
