"""Disposable clock escape trial in the materialized U7 open-side corridor."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "ACREAGE_CLOCK_CANDIDATE5.kicad_pcb"
OUT = R / "PHASE19_CLOCK_OPEN_CORRIDOR.kicad_pcb"

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def T(b, n, a, z, layer=pcbnew.F_Cu):
    t = pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(.2)); t.SetNet(n); b.Add(t)
def X(b, n, p):
    v = pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3))
    v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); v.SetNet(n); b.Add(v)

def main():
    b = pcbnew.LoadBoard(str(BASE)); io = pcbnew.PCB_IO_KICAD_SEXPR()
    nets = {name: b.FindNet(name) for name in (
        "/STORAGE/BRIDGE_XI", "/STORAGE/BRIDGE_XO", "/STORAGE/BRIDGE_VSSOSC",
        "/STORAGE/BRIDGE_3V3")}
    if any(n is None for n in nets.values()): raise RuntimeError("clock net missing")
    # The materialized donor may contain a prior clock trial. Remove only
    # those clock-net tracks so this experiment has a single serialized route
    # per net and its DRC delta is attributable.
    clock_codes = {n.GetNetCode() for n in nets.values()}
    for t in list(b.GetTracks()):
        if t.GetNetCode() in clock_codes:
            b.Remove(t)
    pos = {"Y1": (255, 112), "R23": (261, 112), "C42": (255, 118), "C43": (261, 118)}
    mapping = {
        "Y1": {"1":"/STORAGE/BRIDGE_XI", "2":"/STORAGE/BRIDGE_VSSOSC", "3":"/STORAGE/BRIDGE_XO", "4":"/STORAGE/BRIDGE_VSSOSC"},
        "R23": {"1":"/STORAGE/BRIDGE_XI", "2":"/STORAGE/BRIDGE_XO"},
        "C42": {"1":"/STORAGE/BRIDGE_XI", "2":"/STORAGE/BRIDGE_VSSOSC"},
        "C43": {"1":"/STORAGE/BRIDGE_XO", "2":"/STORAGE/BRIDGE_VSSOSC"},
    }
    pads = {}
    for ref, p in pos.items():
        name = "Crystal_3225_4Pad" if ref == "Y1" else ("R_0402_1005Metric" if ref == "R23" else "C_0402_1005Metric")
        f = b.FindFootprintByReference(ref)
        if f is None: raise RuntimeError(ref)
        f.SetPosition(V(*p))
        pads[ref] = {str(q.GetNumber()): q.GetPosition() for q in f.Pads()}
        for q in f.Pads():
            n = nets[mapping[ref][str(q.GetNumber())]]; q.SetNet(n); q.SetNetCode(n.GetNetCode())
    u = b.FindFootprintByReference("U7")
    for pin, name in (("30","/STORAGE/BRIDGE_3V3"),("31","/STORAGE/BRIDGE_3V3"),("52","/STORAGE/BRIDGE_XI"),("53","/STORAGE/BRIDGE_VSSOSC"),("54","/STORAGE/BRIDGE_XO")):
        q = next(q for q in u.Pads() if str(q.GetNumber()) == pin); q.SetNet(nets[name]); q.SetNetCode(nets[name].GetNetCode())
    # Exact U7 clock pad coordinates are (247.0,109.5), (247.5,109.5),
    # (248.0,109.5) in this materialized 0-degree placement.  Keep the
    # three escapes monotonic and reserve B.Cu for VSSOSC.
    xi, xo, vs, v33 = (nets[x] for x in ("/STORAGE/BRIDGE_XI","/STORAGE/BRIDGE_XO","/STORAGE/BRIDGE_VSSOSC","/STORAGE/BRIDGE_3V3"))
    # Perpendicular-first breakout: never run along the 0.5 mm pitch row.
    T(b, xi, (247,109.5), (247,111.5)); T(b, xi, (247,111.5), (250,111.5)); T(b, xi, (250,111.5), (253.9,111.15))
    T(b, xi, (253.9,111.15), (253.9,110.0)); T(b, xi, (253.9,110.0), (260.5,110.0)); T(b, xi, (260.5,110.0), (260.5,112.0));
    T(b, xi, (253.9,111.15), (252.0,111.15)); T(b, xi, (252.0,111.15), (252.0,118.0)); T(b, xi, (252.0,118.0), (254.5,118.0));
    T(b, xo, (248,109.5), (248,111.5)); T(b, xo, (248,111.5), (251,111.5)); T(b, xo, (251,111.5), (256.1,114.0));
    T(b, xo, (256.1,114.0), (256.1,112.85)); T(b, xo, (256.1,112.85), (261.5,112.0)); T(b, xo, (256.1,112.85), (258.5,118.0)); T(b, xo, (258.5,118.0), (260.5,118.0))
    # VSSOSC is a private local return, kept on B.Cu after ordinary via
    # transitions outside every SMD pad; it is not aliased to board GND.
    T(b, vs, (247.5,109.5), (247.5,113.5), pcbnew.F_Cu); X(b, vs, (247.5,113.5)); T(b, vs, (247.5,113.5), (252,113.5), pcbnew.B_Cu); T(b, vs, (252,113.5), (252,116), pcbnew.B_Cu)
    X(b, vs, (252,116)); T(b, vs, (252,116), (253.9,112.85), pcbnew.F_Cu); T(b, vs, (253.9,112.85), (256.1,112.85), pcbnew.F_Cu)
    T(b, vs, (256.1,112.85), (256.1,111.15), pcbnew.F_Cu); T(b, vs, (252,116), (255.5,118), pcbnew.F_Cu); T(b, vs, (256.1,112.85), (258.5,118), pcbnew.F_Cu); T(b, vs, (258.5,118), (261.5,118), pcbnew.F_Cu)
    # FREQSEL0/1 both high for the authoritative 40 MHz crystal mode.
    T(b, v33, (248,100.5), (247.5,99.0)); T(b, v33, (247.5,99.0), (246.5,99.0))
    T(b, v33, (247.5,100.5), (246.5,99.0))
    b.Save(str(OUT)); print(OUT)

if __name__ == "__main__": main()
