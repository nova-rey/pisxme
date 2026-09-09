"""Replace the malformed CM5 USB3 right-side transition field.

The prior field placed its B.Cu/F.Cu transition vias inside J1 ground/no-net
pads.  This disposable author keeps the source escape and U12 endpoints, but
moves each transition outboard of the connector body.
"""
from pathlib import Path
import os
import pcbnew

R = Path(__file__).resolve().parent
base = R / os.environ.get("P24_USB3_LAUNCH_BASE", "PHASE24_STORAGE_SELECTOR_SATA_ESCAPE_V4_MODE.kicad_pcb")
out = R / os.environ.get("P24_USB3_LAUNCH_OUT", "PHASE24_STORAGE_USB3_RIGHT_LAUNCH_V1.kicad_pcb")
F, B = pcbnew.F_Cu, pcbnew.B_Cu
def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y)
def tr(n, layer, a, z):
    t = pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(n, q):
    v = pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.50))
    v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F, B); v.SetNet(n)
    v.SetNetCode(n.GetNetCode()); b.Add(v)

b = pcbnew.LoadBoard(str(base))
if b is None: raise SystemExit(f"cannot load {base}")
specs = (
    # (source transition, U12-side transition); the latter must be at the
    # transformed U12 escape Y, not at the J1-side source Y.
    ("CM5_USB3_RX_N", "128", "16", (73.0, 88.0), (155.0, 137.8)),
    ("CM5_USB3_RX_P", "130", "15", (75.0, 90.0), (157.0, 137.4)),
    ("CM5_USB3_TX_N", "140", "12", (77.0, 92.0), (159.0, 136.2)),
    ("CM5_USB3_TX_P", "142", "11", (79.0, 94.0), (161.0, 135.8)),
)
for name, j7pin, u12pin, source_via, dest_via in specs:
    n = b.FindNet(name)
    if n is None: raise SystemExit(f"missing {name}")
    for item in list(b.GetTracks()):
        if item.GetNetCode() == n.GetNetCode(): b.RemoveNative(item)
    src = xy(b.FindFootprintByReference("J7").FindPadByNumber(j7pin))
    dst = xy(b.FindFootprintByReference("U12").FindPadByNumber(u12pin))
    via(n, source_via); via(n, dest_via)
    tr(n, F, src, source_via)
    tr(n, B, source_via, dest_via)
    tr(n, F, dest_via, dst)
b.BuildListOfNets(); b.Save(str(out)); print(out)
