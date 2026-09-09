"""Disposable replacement for the four selector-side SATA U13 escapes."""
from pathlib import Path
import os
import pcbnew

R = Path(__file__).resolve().parent
base = R / os.environ.get("P24_SEL_SATA_BASE", "PHASE24_STORAGE_M2_LAUNCH_V6.kicad_pcb")
out = R / os.environ.get("P24_SEL_SATA_OUT", "PHASE24_STORAGE_SELECTOR_SATA_ESCAPE_V1.kicad_pcb")
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.20)
def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y)
def seg(n, a, z, layer):
    t = pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(n, p):
    q = pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.50))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F, B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)

b = pcbnew.LoadBoard(str(base))
if b is None: raise SystemExit("cannot load base")
specs = (
    # C30..C33 pad 1 is F.Cu-only.  Each branch therefore needs a real
    # capacitor-side via before entering its B.Cu corridor; beginning a
    # B.Cu segment at the F.Cu pad is only graphical and is not native
    # connectivity.  Keep the source vias outside the capacitor bodies.
    ("TUSB_SATA_TXP", "C30", "38", (106.0,116.0), (130,118), (172,145), (184.0,130.8)),
    ("TUSB_SATA_TXN", "C31", "37", (106.0,132.0), (130,120), (174,147), (184.0,132.0)),
    ("TUSB_SATA_RXP", "C32", "36", (106.0,120.0), (130,122), (176,149), (184.0,133.2)),
    # RXN's direct diagonal would intersect an inherited CM5 USB3 via.  This
    # bounded candidate takes the outer acreage edge before returning to the
    # right-side U13 escape field.
    ("TUSB_SATA_RXN", "C33", "35", (106.0,128.0), (130,160), (190,160), (184.0,134.4)),
)
for name, cap, u13pin, src_via, bend0, bend1, end_via in specs:
    n = b.FindNet(name)
    if n is None: raise SystemExit(f"missing {name}")
    # Resolve flattened and hierarchical aliases to the existing native net
    # object; display-name equality alone does not create PCB connectivity.
    for fp in b.GetFootprints():
        for p in fp.Pads():
            if p.GetNetname().rsplit('/', 1)[-1] == name:
                p.SetNet(n); p.SetNetCode(n.GetNetCode())
    for item in list(b.GetTracks()):
        if item.GetNetCode() == n.GetNetCode(): b.RemoveNative(item)
    src, dst = xy(b.FindFootprintByReference(cap).FindPadByNumber("1")), xy(b.FindFootprintByReference("U13").FindPadByNumber(u13pin))
    via(n, src_via)
    via(n, end_via)
    seg(n, src, src_via, F)
    seg(n, src_via, bend0, B); seg(n, bend0, bend1, B)
    seg(n, bend1, end_via, B); seg(n, end_via, dst, F)
b.BuildListOfNets(); b.Save(str(out)); print(out)
