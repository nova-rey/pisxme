"""Add the schematic support parts to the best disposable clock oracle."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_CLOCK_ASTAR_NEARWEST.kicad_pcb"
OUT = R / "PHASE24_SUPPORT_FROM_CLOCK_ORACLE.kicad_pcb"

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def xy(item): return pcbnew.ToMM(item.GetPosition().x), pcbnew.ToMM(item.GetPosition().y)
def pad(f, n): return next(p for p in f.Pads() if str(p.GetNumber()) == str(n))
def seg(b, net, a, z, layer=pcbnew.B_Cu, width=.1321):
    t = pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(width)); t.SetNet(net); b.Add(t)

def main():
    b = pcbnew.LoadBoard(str(BASE)); io = pcbnew.PCB_IO_KICAD_SEXPR()
    names = ["/STORAGE/BRIDGE_XI", "/STORAGE/BRIDGE_XO", "/STORAGE/BRIDGE_VSSOSC",
             "/REGULATORS/BRIDGE_1V1", "POWER_GND"]
    nets = {}
    for name in names:
        n = b.FindNet(name)
        if n is None:
            n = pcbnew.NETINFO_ITEM(b, name); n.SetNetCode(b.GetNetCount() + 1); b.Add(n)
        nets[name] = n

    # The clock passive island is deliberately kept west of Y1, away from the
    # inherited SATA/USB3 pad field.  All parts are backside SMD parts.
    libs = {"R23": "R_0402_1005Metric", "C42": "C_0402_1005Metric", "C43": "C_0402_1005Metric"}
    pos = {"R23": (101.0, 129.15), "C42": (101.0, 126.5), "C43": (101.0, 132.0)}
    maps = {"R23": ["/STORAGE/BRIDGE_XI", "/STORAGE/BRIDGE_XO"],
            "C42": ["/STORAGE/BRIDGE_XI", "/STORAGE/BRIDGE_VSSOSC"],
            "C43": ["/STORAGE/BRIDGE_XO", "/STORAGE/BRIDGE_VSSOSC"]}
    fs = {}
    for ref, lib in libs.items():
        f = io.FootprintLoad(str(R / "PiSXMe_RevA_Clean.pretty"), lib)
        f.SetReference(ref); f.SetPosition(V(*pos[ref])); f.SetLayer(pcbnew.B_Cu); b.Add(f); fs[ref] = f
        for p, name in zip(f.Pads(), maps[ref]):
            p.SetNet(nets[name]); p.SetNetCode(nets[name].GetNetCode())
            ls = pcbnew.LSET(); ls.AddLayer(pcbnew.B_Cu); p.SetLayerSet(ls)

    y = b.FindFootprintByReference("Y1")
    ypads = {str(p.GetNumber()): xy(p) for p in y.Pads()}
    # Connect each passive directly to the corresponding crystal pad through
    # short, separated B.Cu corridors.
    # Deliberate side-separated doglegs; XO stays below the crystal pad row,
    # while the VSSOSC branches leave on the far west side.
    routes = {
        "R23": [("XI", [(100.5,129.15), ypads["1"]]),
                ("XO", [(101.5,134.0),(109.1,134.0),ypads["3"]])],
        "C42": [("XI", [(100.5,124.0),(106.9,124.0),ypads["1"]]),
                ("VS", [(101.5,126.5),(99.0,126.5),(99.0,135.0),(118.0,135.0)])],
        "C43": [("XO", [(100.5,133.5),(109.1,133.5),ypads["3"]]),
                ("VS", [(101.5,132.0),(99.0,132.0),(99.0,135.0)])],
    }
    for ref, f in fs.items():
        for p, (name, points) in zip(f.Pads(), routes[ref]):
            points = [xy(p)] + points
            for a, z in zip(points, points[1:]): seg(b, nets["/STORAGE/BRIDGE_" + ("VSSOSC" if name == "VS" else name)], a, z)

    # Materialize the four bridge supply capacitors.  They remain a separate
    # local island and are intentionally not coupled to this clock proof.
    u5 = b.FindFootprintByReference("U5")
    cap_pos = {"C44": (242, 112), "C45": (248, 112), "C46": (242, 118), "C47": (248, 118)}
    for ref, position in cap_pos.items():
        f = io.FootprintLoad(str(R / "PiSXMe_RevA_Clean.pretty"), "C_1210_3225Metric")
        f.SetReference(ref); f.SetPosition(V(*position)); b.Add(f)
        p1, p2 = pad(f, "1"), pad(f, "2")
        for p, n in ((p1, nets["/REGULATORS/BRIDGE_1V1"]), (p2, nets["POWER_GND"])):
            p.SetNet(n); p.SetNetCode(n.GetNetCode())
    b.Save(str(OUT)); print(OUT)

if __name__ == "__main__": main()
