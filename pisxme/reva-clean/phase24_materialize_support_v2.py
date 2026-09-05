"""Materialize the schematic support omitted by the Phase 23 PCB ancestor.

This candidate is deliberately local: it derives U7 pad coordinates from the
loaded board and uses an open south-east acreage corridor for the oscillator.
It is disposable until native DRC and parity checks pass.
"""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb"
OUT = ROOT / "PHASE24_SUPPORT_V2.kicad_pcb"

def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def pos(p): return (pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y))
def P(f, n): return next(p for p in f.Pads() if str(p.GetNumber()) == str(n))
def net(board, name):
    n = board.FindNet(name)
    if n is None:
        n = pcbnew.NETINFO_ITEM(board, name)
        n.SetNetCode(board.GetNetCount() + 1)
        board.Add(n)
    return n
def setnet(p, n): p.SetNet(n); p.SetNetCode(n.GetNetCode())
def seg(board, n, a, b, layer, width=.20):
    t = pcbnew.PCB_TRACK(board); t.SetStart(V(*a)); t.SetEnd(V(*b));
    t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(width)); t.SetNet(n); board.Add(t)
def via(board, n, xy):
    v = pcbnew.PCB_VIA(board); v.SetPosition(V(*xy)); v.SetWidth(pcbnew.FromMM(.50));
    v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); v.SetNet(n); board.Add(v)

CLOCK = {
    "Y1": {"1":"/STORAGE/BRIDGE_XI", "2":"/STORAGE/BRIDGE_VSSOSC", "3":"/STORAGE/BRIDGE_XO", "4":"/STORAGE/BRIDGE_VSSOSC"},
    "R23": {"1":"/STORAGE/BRIDGE_XI", "2":"/STORAGE/BRIDGE_XO"},
    "C42": {"1":"/STORAGE/BRIDGE_XI", "2":"/STORAGE/BRIDGE_VSSOSC"},
    "C43": {"1":"/STORAGE/BRIDGE_XO", "2":"/STORAGE/BRIDGE_VSSOSC"},
}
LIB = {"Y1":"Crystal_3225_4Pad", "R23":"R_0402_1005Metric", "C42":"C_0402_1005Metric", "C43":"C_0402_1005Metric"}

def main():
    b = pcbnew.LoadBoard(str(BASE)); io = pcbnew.PCB_IO_KICAD_SEXPR()
    names = {x for m in CLOCK.values() for x in m.values()} | {"/REGULATORS/BRIDGE_1V1", "POWER_GND"}
    nets = {n: net(b, n) for n in names}
    u7 = b.FindFootprintByReference("U7")
    for number, name in (("52", "/STORAGE/BRIDGE_XI"), ("53", "/STORAGE/BRIDGE_VSSOSC"), ("54", "/STORAGE/BRIDGE_XO")):
        setnet(P(u7, number), nets[name])

    # Open acreage; all four support footprints remain on the underside.
    placements = {"Y1":((155,155),180), "R23":((155,165),0),
                  "C42":((149,165),0), "C43":((161,165),0)}
    fs = {}
    for ref, (xy, rot) in placements.items():
        f = io.FootprintLoad(str(ROOT / "PiSXMe_RevA_Clean.pretty"), LIB[ref])
        f.SetReference(ref); f.SetPosition(V(*xy)); f.SetOrientationDegrees(rot); f.SetLayer(pcbnew.B_Cu); b.Add(f)
        fs[ref] = f
        for p in f.Pads(): setnet(p, nets[CLOCK[ref][str(p.GetNumber())]])

    # Three independent U7 escapes.  The lanes are spaced before the first
    # transition, so they do not enter the existing SATA pad field together.
    up = {n: pos(P(u7, p)) for n,p in (("/STORAGE/BRIDGE_XI","52"), ("/STORAGE/BRIDGE_VSSOSC","53"), ("/STORAGE/BRIDGE_XO","54"))}
    # Spread the three exits immediately below the actual pad row.  In
    # particular, VSSOSC exits to the right and XO exits to the left; a
    # shared diagonal from the old trial crossed U7 pad 54.
    lanes = {"/STORAGE/BRIDGE_XI": (130.0, (130.0,155.85)),
             "/STORAGE/BRIDGE_VSSOSC": (122.5, (122.5,154.15)),
             "/STORAGE/BRIDGE_XO": (118.0, (118.0,154.15))}
    for name, (x, end) in lanes.items():
        a = up[name]
        e = (x, 145.0)
        seg(b, nets[name], a, e, pcbnew.F_Cu); via(b, nets[name], e); seg(b, nets[name], e, end, pcbnew.B_Cu)

    # B.Cu monotonic buses to the crystal field, with branches kept in their
    # own x corridors.  The local return is tied to the dedicated U7 VSSOSC
    # net, as required by the schematic authority.
    XI, VS, XO = (nets[x] for x in ("/STORAGE/BRIDGE_XI", "/STORAGE/BRIDGE_VSSOSC", "/STORAGE/BRIDGE_XO"))
    yp = {str(p.GetNumber()):pos(p) for p in fs["Y1"].Pads()}
    rp = {str(p.GetNumber()):pos(p) for p in fs["R23"].Pads()}
    c2 = {r:{str(p.GetNumber()):pos(p) for p in fs[r].Pads()} for r in ("C42","C43")}
    # XI left/top bus and XO right/bottom bus.
    seg(b, XI, (130,145), (130,155.85), pcbnew.B_Cu); seg(b, XI, (130,155.85), yp["1"], pcbnew.B_Cu)
    seg(b, XI, yp["1"], (147,160), pcbnew.B_Cu); seg(b, XI, (147,160), rp["1"], pcbnew.B_Cu)
    seg(b, XI, (147,160), (143,160), pcbnew.B_Cu); seg(b, XI, (143,160), c2["C42"]["1"], pcbnew.B_Cu)
    seg(b, XO, (118,145), (118,154.15), pcbnew.B_Cu); seg(b, XO, (118,154.15), yp["3"], pcbnew.B_Cu)
    seg(b, XO, yp["3"], (163,158), pcbnew.B_Cu); seg(b, XO, (163,158), rp["2"], pcbnew.B_Cu)
    seg(b, XO, (163,158), (159,160), pcbnew.B_Cu); seg(b, XO, (159,160), c2["C43"]["1"], pcbnew.B_Cu)
    # VSSOSC runs around the lower edge of the crystal; the two crystal pads
    # are joined locally and the load returns remain on separate dogbones.
    seg(b, VS, (122.5,145), (122.5,154.15), pcbnew.B_Cu); seg(b, VS, (122.5,154.15), yp["2"], pcbnew.B_Cu)
    # The second VSSOSC crystal pad is reached around the left and bottom of
    # the package, avoiding both the XO launch and the XI pad.
    seg(b, VS, yp["2"], (158,152.5), pcbnew.B_Cu); seg(b, VS, (158,152.5), (152.5,152.5), pcbnew.B_Cu)
    seg(b, VS, (152.5,152.5), (152.5,155.85), pcbnew.B_Cu); seg(b, VS, (152.5,155.85), yp["4"], pcbnew.B_Cu)
    seg(b, VS, yp["2"], (150,160), pcbnew.B_Cu); seg(b, VS, (150,160), c2["C42"]["2"], pcbnew.B_Cu)
    seg(b, VS, yp["4"], (162,160), pcbnew.B_Cu); seg(b, VS, (162,160), c2["C43"]["2"], pcbnew.B_Cu)

    # Add the four schematic-authoritative U5 bulk capacitors as an unshared,
    # coherent rail/return island.  Their copper is intentionally left for a
    # subsequent obstacle-aware pass if this clock candidate is clean.
    rail, gnd = nets["/REGULATORS/BRIDGE_1V1"], nets["POWER_GND"]
    for ref, xy in {"C44":(246,120), "C45":(252,120), "C46":(246,126), "C47":(252,126)}.items():
        f = io.FootprintLoad(str(ROOT / "PiSXMe_RevA_Clean.pretty"), "C_1210_3225Metric")
        f.SetReference(ref); f.SetPosition(V(*xy)); b.Add(f)
        setnet(P(f,"1"), rail); setnet(P(f,"2"), gnd)
    b.Save(str(OUT)); print(OUT)
if __name__ == "__main__": main()
