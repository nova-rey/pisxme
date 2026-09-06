"""Disposable monotonic USB3 channel probe for STORAGE_LOCAL_J3_EDGE.

This fixture removes only the inherited USB3 and SERVICE_RD_B copper, then
authors four ordered B.Cu channels from native J7/U7 pad coordinates. It is
not an integrated-board candidate; it discriminates corridor topology from
inherited inter-island crossings.
"""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_MACRO_FRESH_STORAGE_LOCAL_J3_EDGE.kicad_pcb"
OUT = R / "PHASE24_STORAGE_USB3_MONOTONIC_CHANNEL.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.13208)

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def pad(b, ref, number):
    p = b.FindFootprintByReference(ref).FindPadByNumber(str(number))
    if p is None: raise RuntimeError(f"missing {ref}.{number}")
    return p.GetPosition()
def seg(b, net, a, z, layer):
    if a == z: return
    t = pcbnew.PCB_TRACK(b); t.SetStart(a); t.SetEnd(z); t.SetLayer(layer)
    t.SetWidth(W); t.SetNet(net); b.Add(t)
def via(b, net, p):
    # 0.50 mm finished copper around the 0.30 mm drill meets the board's
    # 0.10 mm minimum annular-width rule.
    q = pcbnew.PCB_VIA(b); q.SetPosition(p); q.SetWidth(pcbnew.FromMM(.50))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F, B); q.SetNet(net); b.Add(q)

b = pcbnew.LoadBoard(str(BASE))
if b is None: raise RuntimeError("native board load failed")
names = ("CM5_USB3_RX_N", "CM5_USB3_RX_P", "CM5_USB3_TX_N", "CM5_USB3_TX_P")
ends = {
    "CM5_USB3_RX_N": ("128", "42", V(72, 103.9), V(81, 120)),
    "CM5_USB3_RX_P": ("130", "43", V(73, 104.8), V(82, 120.5)),
    "CM5_USB3_TX_N": ("140", "45", V(76, 108.0), V(83, 121.5)),
    "CM5_USB3_TX_P": ("142", "46", V(77, 109.0), V(84, 122)),
}
native = {n: (pad(b, "J7", jp), pad(b, "U7", up)) for n, (jp, up, _sv, _ev) in ends.items()}
items = b.Tracks()
for item in [items[i] for i in range(items.size())]:
    name = str(item.GetNetname())
    if any(x in name for x in names) or "SERVICE_RD_B" in name:
        b.Remove(item)

for name, (_jp, _up, src_via, end_via) in ends.items():
    net = b.FindNet("/CORE_CM5/" + name)
    if net is None: raise RuntimeError(f"missing {name}")
    src, dst = native[name]
    launch = V(71.2, pcbnew.ToMM(src.y))
    if name.endswith("RX_P"): launch = V(71.2, 104.8)
    elif name.endswith("TX_N"): launch = V(71.2, 106.3)
    elif name.endswith("TX_P"): launch = V(71.2, 106.7)
    seg(b, net, src, launch, F); seg(b, net, launch, src_via, F); via(b, net, src_via)
    # Both source and endpoint transitions preserve the native pair order;
    # direct monotonic segments avoid artificial vertical-channel crossings.
    seg(b, net, src_via, end_via, B); via(b, net, end_via)
    seg(b, net, end_via, dst, F)

b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
