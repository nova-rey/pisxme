"""Disposable native-control transplant for the proven storage topology.

This deliberately restores the donor's validated U7/J3/support placement on
the selected macro board and copies only native storage copper.  It is a
control for the route-authoring path, not a promotion of the selected macro
placement: an exact donor-style result separates route-tool failure from
placement adaptation failure.
"""
from pathlib import Path
import os
import pcbnew

R = Path(__file__).resolve().parent
BASE = Path(os.environ.get("PISXME_STORAGE_CONTROL_BASE", str(R / "PHASE24_MACRO_FRESH_STORAGE_LOCAL_J3_EDGE.kicad_pcb")))
DONOR = Path(os.environ.get("PISXME_STORAGE_CONTROL_DONOR", str(R / "PHASE24_SELECTED_MACRO_STORAGE_PROVEN_USB3_SATA_RXN_STITCH_CAPS_BOTTOM.kicad_pcb")))
OUT = Path(os.environ.get("PISXME_STORAGE_CONTROL_OUT", str(R / "PHASE24_STORAGE_REFERENCE_CONTROL.kicad_pcb")))
NET_PARTS = ("CM5_USB3_", "BRIDGE_SATA_", "SATA_M2_", "BRIDGE_XI", "BRIDGE_XO", "BRIDGE_VSSOSC")
REFS = ("U7", "J3", "C30", "C31", "C32", "C33", "Y1", "R23", "C42", "C43")

def vec(p):
    return pcbnew.VECTOR2I(p.x, p.y)

def relevant(name):
    return any(part in name for part in NET_PARTS)

b = pcbnew.LoadBoard(str(BASE))
d = pcbnew.LoadBoard(str(DONOR))
if b is None or d is None:
    raise RuntimeError("native board load failed")
bt = b.Tracks()
dt = d.Tracks()
donor_items = []
for i in range(dt.size()):
    item = dt[i]
    name = str(item.GetNetname())
    if not relevant(name):
        continue
    if isinstance(item, pcbnew.PCB_VIA):
        donor_items.append(("via", name, vec(item.GetPosition()), item.GetWidth(item.TopLayer()), item.GetDrill(), item.TopLayer(), item.BottomLayer()))
    else:
        donor_items.append(("track", name, vec(item.GetStart()), vec(item.GetEnd()), item.GetLayer(), item.GetWidth()))

# Keep the donor placement and pad authority as the control condition.
for ref in REFS:
    src = d.FindFootprintByReference(ref)
    dst = b.FindFootprintByReference(ref)
    if src is None or dst is None:
        raise RuntimeError(f"missing storage footprint {ref}")
    dst.SetPosition(vec(src.GetPosition()))
    dst.SetOrientationDegrees(src.GetOrientationDegrees())

for item in [bt[i] for i in range(bt.size())]:
    if relevant(str(item.GetNetname())):
        b.Remove(item)

for item in donor_items:
    name = item[1]
    net = b.FindNet(name)
    if net is None:
        raise RuntimeError(f"missing target net {name}")
    if item[0] == "via":
        q = pcbnew.PCB_VIA(b)
        q.SetPosition(item[2])
        q.SetWidth(item[3])
        q.SetDrill(item[4])
        q.SetLayerPair(item[5], item[6])
    else:
        q = pcbnew.PCB_TRACK(b)
        q.SetStart(item[2])
        q.SetEnd(item[3])
        q.SetLayer(item[4])
        q.SetWidth(item[5])
    q.SetNet(net)
    b.Add(q)

b.BuildListOfNets()
b.Save(str(OUT))
print(OUT)
