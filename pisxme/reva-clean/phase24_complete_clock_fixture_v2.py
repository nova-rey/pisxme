"""Complete U7 clock fixture with VSSOSC on a separate surface layer."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb"
OUT = R / "PHASE24_COMPLETE_CLOCK_FIXTURE_V2.kicad_pcb"
NAMES = {"XI": "/STORAGE/BRIDGE_XI", "VS": "/STORAGE/BRIDGE_VSSOSC", "XO": "/STORAGE/BRIDGE_XO"}
MAP = {"Y1": {"1":"XI", "2":"VS", "3":"XO", "4":"VS"},
       "R23": {"1":"XI", "2":"XO"}, "C42": {"1":"XI", "2":"VS"},
       "C43": {"1":"XO", "2":"VS"}}
LIB = {"Y1":"Crystal_3225_4Pad", "R23":"R_0402_1005Metric",
       "C42":"C_0402_1005Metric", "C43":"C_0402_1005Metric"}

def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y)
def P(f, n): return next(p for p in f.Pads() if str(p.GetNumber()) == str(n))
def S(b, n, a, z, layer):
    if a == z: return
    t = pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); b.Add(t)
def path(b, n, points, layer):
    for a, z in zip(points, points[1:]): S(b, n, a, z, layer)
def X(b, n, p):
    v = pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.50))
    v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    v.SetNet(n); b.Add(v)

def main():
    b = pcbnew.LoadBoard(str(BASE)); io = pcbnew.PCB_IO_KICAD_SEXPR()
    for item in list(b.GetTracks()): b.RemoveNative(item)
    for zone in list(b.Zones()): b.RemoveNative(zone)
    for fp in list(b.GetFootprints()):
        if fp.GetReference() != "U7": b.RemoveNative(fp)
    u = b.FindFootprintByReference("U7")
    u.SetPosition(V(100, 100)); u.SetOrientationDegrees(0)
    nets = {}
    for k, name in NAMES.items():
        nets[k] = b.FindNet(name)
        if nets[k] is None:
            nets[k] = pcbnew.NETINFO_ITEM(b, name)
            nets[k].SetNetCode(b.GetNetCount() + 1); b.Add(nets[k])
    parts = {}
    for ref, pos in {"Y1":(100,115), "R23":(100,125),
                     "C42":(94,125), "C43":(106,125)}.items():
        fp = io.FootprintLoad(str(R / "PiSXMe_RevA_Clean.pretty"), LIB[ref])
        fp.SetReference(ref); fp.SetPosition(V(*pos)); b.Add(fp); parts[ref] = fp
        for p in fp.Pads():
            n = nets[MAP[ref][str(p.GetNumber())]]
            p.SetNet(n); p.SetNetCode(n.GetNetCode())
            ls = pcbnew.LSET(); ls.AddLayer(pcbnew.F_Cu if MAP[ref][str(p.GetNumber())] == "VS" else pcbnew.B_Cu)
            p.SetLayerSet(ls)
    src = {k: P(u, n) for k, n in {"XI":"52", "VS":"53", "XO":"54"}.items()}
    for k, p in src.items(): p.SetNet(nets[k]); p.SetNetCode(nets[k].GetNetCode())
    # XI: B.Cu upper bus; XO: B.Cu lower bus. VSSOSC uses F.Cu perimeter.
    path(b, nets["XI"], [xy(src["XI"]), (97,108), (94,108)], pcbnew.F_Cu); X(b, nets["XI"], (94,108))
    path(b, nets["XI"], [(94,108), (92,122)], pcbnew.B_Cu)
    path(b, nets["XI"], [(92,122), (98.9,122), (98.9,114.15)], pcbnew.B_Cu)
    path(b, nets["XI"], [(92,122), (99.5,122), (99.5,125)], pcbnew.B_Cu)
    path(b, nets["XI"], [(92,122), (93.5,122), (93.5,125)], pcbnew.B_Cu)
    path(b, nets["XO"], [xy(src["XO"]), (98,106.5), (106,113)], pcbnew.F_Cu); X(b, nets["XO"], (106,113))
    path(b, nets["XO"], [(106,113), (108,128)], pcbnew.B_Cu)
    path(b, nets["XO"], [(108,128), (101.1,128), (101.1,115.85)], pcbnew.B_Cu)
    path(b, nets["XO"], [(108,128), (100.5,128), (100.5,125)], pcbnew.B_Cu)
    path(b, nets["XO"], [(108,128), (105.5,128), (105.5,125)], pcbnew.B_Cu)
    path(b, nets["VS"], [xy(src["VS"]), (97.5,109.0), (90,109.0), (90,135)], pcbnew.F_Cu)
    for ref, pn in [("Y1","2"), ("Y1","4"), ("C42","2"), ("C43","2")]:
        q = xy(P(parts[ref], pn)); path(b, nets["VS"], [(90,135), (90,q[1]), q], pcbnew.F_Cu)
    b.Save(str(OUT)); print(OUT)

if __name__ == "__main__": main()
