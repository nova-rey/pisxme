"""Build a minimal native J7-to-U7 USB3 routing fixture.

Only the exact saved J7/U7 footprints and their real net objects are retained;
all inherited copper, zones, and unrelated footprints are removed. This is a
discriminating geometry fixture, not an acreage candidate.
"""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_MACRO_FRESH_STORAGE_LOCAL_J3_EDGE.kicad_pcb"
OUT = R / "PHASE24_USB3_MINIMAL_NATIVE_FIXTURE.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.13208)

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def native_pad(board, ref, number):
    p = board.FindFootprintByReference(ref).FindPadByNumber(str(number))
    if p is None: raise RuntimeError(f"missing {ref}.{number}")
    return p.GetPosition()
def track(board, net, a, z, layer, width=W):
    if a == z: return
    q = pcbnew.PCB_TRACK(board); q.SetStart(a); q.SetEnd(z); q.SetLayer(layer)
    q.SetWidth(width); q.SetNet(net); board.Add(q)
def via(board, net, p):
    q = pcbnew.PCB_VIA(board); q.SetPosition(p); q.SetWidth(pcbnew.FromMM(.50))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F, B); q.SetNet(net); board.Add(q)

b = pcbnew.LoadBoard(str(BASE))
if b is None: raise RuntimeError("native board load failed")
ends = {
    "CM5_USB3_RX_N": ("128", "42", V(72, 103.9), V(81, 120)),
    "CM5_USB3_RX_P": ("130", "43", V(72, 103.5), V(82, 120.5)),
    "CM5_USB3_TX_N": ("140", "45", V(78, 108.0), V(83, 121.5)),
    "CM5_USB3_TX_P": ("142", "46", V(80, 109.0), V(84, 122)),
}
native = {n: (native_pad(b, "J7", jp), native_pad(b, "U7", up)) for n, (jp, up, _sv, _ev) in ends.items()}

for item in list(b.GetFootprints()):
    if item.GetReference() not in ("J7", "U7"):
        b.RemoveNative(item)
tracks = b.Tracks()
for item in [tracks[i] for i in range(tracks.size())]:
    b.Remove(item)
for zone in list(b.Zones()):
    b.RemoveNative(zone)

for name, (_jp, _up, src_via, end_via) in ends.items():
    net = b.FindNet("/CORE_CM5/" + name)
    if net is None: raise RuntimeError(f"missing net {name}")
    src, dst = native[name]
    launch = V(71.2, pcbnew.ToMM(src.y))
    if name.endswith("RX_P"): launch = V(71.2, 104.8)
    elif name.endswith("TX_N"): launch = V(71.2, 106.3)
    elif name.endswith("TX_P"): launch = V(71.2, 106.7)
    if name.endswith("RX_P"):
        launch = V(70.8, 103.5)
        track(b, net, src, launch, F); track(b, net, launch, src_via, F)
    else:
        track(b, net, src, launch, F); track(b, net, launch, src_via, F)
    via(b, net, src_via); track(b, net, src_via, end_via, B)
    via(b, net, end_via); track(b, net, end_via, dst, F)

b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
