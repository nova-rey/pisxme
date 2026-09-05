"""Disposable complete TUSB9261 clock/support fixture with native pad graph."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb"
OUT = R / "PHASE24_COMPLETE_CLOCK_FIXTURE.kicad_pcb"

def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y)
def P(f, n): return next(p for p in f.Pads() if str(p.GetNumber()) == str(n))
def net(b, name):
    n = b.FindNet(name)
    if n is None:
        n = pcbnew.NETINFO_ITEM(b, name); n.SetNetCode(b.GetNetCount() + 1); b.Add(n)
    return n
def setpad(p, n, layer=pcbnew.B_Cu):
    p.SetNet(n); p.SetNetCode(n.GetNetCode()); ls = pcbnew.LSET(); ls.AddLayer(layer); p.SetLayerSet(ls)
def seg(b, n, a, z, layer=pcbnew.B_Cu):
    t = pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); b.Add(t)
def via(b, n, p):
    v = pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.50)); v.SetDrill(pcbnew.FromMM(.30))
    v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); v.SetNet(n); b.Add(v)
def path(b, n, points):
    for a, z in zip(points, points[1:]): seg(b, n, a, z)

MAP = {
    "Y1": {"1":"/STORAGE/BRIDGE_XI", "2":"/STORAGE/BRIDGE_VSSOSC", "3":"/STORAGE/BRIDGE_XO", "4":"/STORAGE/BRIDGE_VSSOSC"},
    "R23": {"1":"/STORAGE/BRIDGE_XI", "2":"/STORAGE/BRIDGE_XO"},
    "C42": {"1":"/STORAGE/BRIDGE_XI", "2":"/STORAGE/BRIDGE_VSSOSC"},
    "C43": {"1":"/STORAGE/BRIDGE_XO", "2":"/STORAGE/BRIDGE_VSSOSC"},
}
LIB = {"Y1":"Crystal_3225_4Pad", "R23":"R_0402_1005Metric", "C42":"C_0402_1005Metric", "C43":"C_0402_1005Metric"}

def main():
    b = pcbnew.LoadBoard(str(BASE)); io = pcbnew.PCB_IO_KICAD_SEXPR()
    keep = {"U7"}
    tracks = list(b.GetTracks()); zones = list(b.Zones()); footprints = list(b.GetFootprints())
    for t in tracks: b.Remove(t)
    for z in zones: b.Remove(z)
    for f in footprints:
        if f.GetReference() not in keep: b.Remove(f)
    u = b.FindFootprintByReference("U7"); u.SetPosition(V(100, 100)); u.SetOrientationDegrees(0)
    nets = {name: net(b, name) for name in {x for m in MAP.values() for x in m.values()}}
    fs = {}
    positions = {"Y1":(100,115), "R23":(100,125), "C42":(94,125), "C43":(106,125)}
    for ref, pos in positions.items():
        f = io.FootprintLoad(str(R / "PiSXMe_RevA_Clean.pretty"), LIB[ref]); f.SetReference(ref); f.SetPosition(V(*pos)); b.Add(f); fs[ref] = f
        for p in f.Pads(): setpad(p, nets[MAP[ref][str(p.GetNumber())]])
    sources = {"XI":P(u,"52"), "VS":P(u,"53"), "XO":P(u,"54")}
    n = {"XI":nets["/STORAGE/BRIDGE_XI"], "VS":nets["/STORAGE/BRIDGE_VSSOSC"], "XO":nets["/STORAGE/BRIDGE_XO"]}
    for k, p in sources.items(): p.SetNet(n[k]); p.SetNetCode(n[k].GetNetCode())
    # Per-net F.Cu launch, via, and separated B.Cu buses.
    exits = {"XI":(94,109), "VS":(90,111), "XO":(106,113)}
    buses = {"XI":(92,122), "VS":(90,130), "XO":(108,128)}
    for k, p in sources.items():
        a = xy(p); e = exits[k]; mid=(a[0], e[1]); seg(b,n[k],a,mid,pcbnew.F_Cu); seg(b,n[k],mid,e,pcbnew.F_Cu); via(b,n[k],e); path(b,n[k],[e,buses[k]])
    targets = {k:[] for k in n}
    for ref, f in fs.items():
        for p in f.Pads(): targets[{'/STORAGE/BRIDGE_XI':'XI','/STORAGE/BRIDGE_XO':'XO','/STORAGE/BRIDGE_VSSOSC':'VS'}[MAP[ref][str(p.GetNumber())]]].append(xy(p))
    # Approach the crystal on its natural perimeter: XI from the upper-left,
    # XO from the lower-right, and VSSOSC around the outside of both rows.
    y = {str(p.GetNumber()): xy(p) for p in fs["Y1"].Pads()}
    path(b,n["XI"],[(y["1"]),(97.5,114.15),(97.5,122),(92,122)])
    path(b,n["XO"],[(y["3"]),(104.5,115.85),(104.5,128),(108,128)])
    path(b,n["VS"],[(y["2"]),(97.0,115.85),(97.0,130),(90,130)])
    path(b,n["VS"],[(y["4"]),(103.0,114.15),(103.0,130),(90,130)])
    # Each passive pad reaches its matching perimeter bus without entering the
    # crystal field a second time.
    for p in (P(fs["R23"],"1"), P(fs["C42"],"1")):
        q=xy(p); path(b,n["XI"],[q,(q[0],122),(92,122)])
    for p in (P(fs["R23"],"2"), P(fs["C43"],"1")):
        q=xy(p); path(b,n["XO"],[q,(104.5,q[1]),(104.5,128),(108,128)])
    for p in (P(fs["C42"],"2"), P(fs["C43"],"2")):
        q=xy(p); path(b,n["VS"],[q,(q[0],130),(90,130)])
    b.Save(str(OUT)); print(OUT)

if __name__ == "__main__": main()
