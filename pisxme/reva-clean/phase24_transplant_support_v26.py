"""Transform the native U7 support oracle onto the V26 data-route basis.

The donor's original absolute placement is not portable: its support island
was north-west of U7 and collides with J7 after the V26 U7 move.  This script
therefore tests rigid rotations of the complete support island about U7,
with optional local translation, while preserving actual donor copper/net
identity.
"""
import os
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_SELECTED_MACRO_SWAP_STORAGE_SATA_PAIR_CORRIDOR_V26_AUTH_SKEW.kicad_pcb"
DONOR = ROOT / "PHASE24_U7_STORAGE_3V3_PAD24_CURRENT.kicad_pcb"
ROT = int(os.environ.get("PISXME_SUPPORT_ROT", "270")) % 360
SHIFT_X = int(os.environ.get("PISXME_SUPPORT_DX", "15"))
SHIFT_Y = int(os.environ.get("PISXME_SUPPORT_DY", "0"))
OUT = ROOT / f"PHASE24_SELECTED_MACRO_STORAGE_V26_SUPPORT_R{ROT}_{SHIFT_X}_{SHIFT_Y}.kicad_pcb"
SUPPORT = {
    "/STORAGE/BRIDGE_3V3", "/REGULATORS/BRIDGE_3V3",
    "/STORAGE/BRIDGE_RESET", "/STORAGE/BRIDGE_XI",
    "/STORAGE/BRIDGE_XO", "/STORAGE/BRIDGE_VSSOSC",
}
PARTS = ("C16", "C17", "C19", "Y1", "R23", "C42", "C43")

def rotate_about(p, origin, deg):
    x, y = p.x - origin.x, p.y - origin.y
    if deg == 0:
        rx, ry = x, y
    elif deg == 90:
        rx, ry = -y, x
    elif deg == 180:
        rx, ry = -x, -y
    elif deg == 270:
        rx, ry = y, -x
    else:
        raise ValueError("support rotation must be a right angle")
    return pcbnew.VECTOR2I(origin.x + rx + SHIFT_X * 1_000_000,
                           origin.y + ry + SHIFT_Y * 1_000_000)

base = pcbnew.LoadBoard(str(BASE))
donor = pcbnew.LoadBoard(str(DONOR))
bu7 = base.FindFootprintByReference("U7").GetPosition()
du7 = donor.FindFootprintByReference("U7").GetPosition()
dx, dy = bu7.x - du7.x, bu7.y - du7.y

def transform(p):
    # Rotate in donor coordinates around donor U7, then anchor at base U7.
    r = rotate_about(p, du7, ROT)
    return pcbnew.VECTOR2I(r.x + dx, r.y + dy)

for ref in PARTS:
    src = donor.FindFootprintByReference(ref)
    dst = base.FindFootprintByReference(ref)
    if src is None or dst is None:
        raise RuntimeError(f"missing support footprint {ref}")
    dst.SetPosition(transform(src.GetPosition()))
    dst.SetOrientationDegrees(src.GetOrientationDegrees() + ROT)

for item in list(base.GetTracks()):
    if item.GetNetname() in SUPPORT:
        base.Remove(item)

for item in donor.GetTracks():
    if item.GetNetname() not in SUPPORT:
        continue
    net = base.FindNet(item.GetNetname())
    if net is None:
        raise RuntimeError(f"missing base net {item.GetNetname()}")
    if isinstance(item, pcbnew.PCB_VIA):
        copy = pcbnew.PCB_VIA(base)
        copy.SetPosition(transform(item.GetPosition()))
        copy.SetWidth(item.GetWidth(pcbnew.F_Cu))
        copy.SetDrill(item.GetDrill())
        copy.SetLayerPair(item.TopLayer(), item.BottomLayer())
    else:
        copy = pcbnew.PCB_TRACK(base)
        copy.SetStart(transform(item.GetStart()))
        copy.SetEnd(transform(item.GetEnd()))
        copy.SetLayer(item.GetLayer())
        copy.SetWidth(item.GetWidth())
    copy.SetNet(net)
    base.Add(copy)

base.BuildListOfNets()
base.Save(str(OUT))
print(OUT)
