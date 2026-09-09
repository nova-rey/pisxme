"""V14: lateral TXN offset to clear the adjacent U11 pad field."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
b = pcbnew.LoadBoard(str(R / "PHASE24_STORAGE_USB_TX_PAIR_UPPER_DETOUR_V13.kicad_pcb"))
F = pcbnew.F_Cu

def V(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def xy(ref, pad):
    p = b.FindFootprintByReference(ref).FindPadByNumber(str(pad)).GetPosition()
    return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)

def track(net, a, z, width):
    t = pcbnew.PCB_TRACK(b)
    t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(F)
    t.SetWidth(pcbnew.FromMM(width)); t.SetNet(net); t.SetNetCode(net.GetNetCode())
    b.Add(t)

net = b.FindNet("USB_TXN1")
for item in list(b.GetTracks()):
    if item.GetNetCode() == net.GetNetCode():
        b.RemoveNative(item)

# Keep V13's source dogbone and destination launch, moving only the vertical
# leg from x=140.6 to x=140.4 so it clears U11 pad 23 with real margin.
points = [xy("U11", 22), (141.0, 139.0), (140.4, 139.4),
          (140.4, 146.0), (146.5, 146.0), xy("C87", 1)]
for i, (a, z) in enumerate(zip(points, points[1:])):
    track(net, a, z, .15 if i < 2 else .2)

b.BuildListOfNets()
out = R / "PHASE24_STORAGE_USB_TX_PAIR_LOWER_CLEARANCE_V14.kicad_pcb"
b.Save(str(out))
print(out)
