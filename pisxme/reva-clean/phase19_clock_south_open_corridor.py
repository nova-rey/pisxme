"""Disposable Phase 19 clock route in the measured south acreage corridor."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / 'ACREAGE_PHASE19_CLOCK_COORDINATED3.kicad_pcb'
OUT = R / 'PHASE19_COORDINATED_CLOCK_SOUTH_OPEN.kicad_pcb'

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def xy(p): return pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y)
def T(b, n, a, z, layer=pcbnew.F_Cu):
    t = pcbnew.PCB_TRACK(b)
    t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(.2)); t.SetNet(n); b.Add(t)

def main():
    b = pcbnew.LoadBoard(str(BASE))
    names = ('/STORAGE/BRIDGE_XI', '/STORAGE/BRIDGE_XO',
             '/STORAGE/BRIDGE_VSSOSC', '/STORAGE/BRIDGE_3V3')
    nets = {n: b.FindNet(n) for n in names}
    if any(v is None for v in nets.values()): raise RuntimeError('clock net missing')
    codes = {n.GetNetCode() for n in nets.values()}
    for t in list(b.GetTracks()):
        if t.GetNetCode() in codes: b.Remove(t)

    # The entire low-profile support island is below the measured live copper
    # envelope.  The tall J3 body remains at the board edge; this does not
    # change connector access or the validated storage architecture.
    for ref, pos in {'Y1': (250, 150), 'R23': (270, 149),
                     'C42': (250, 170), 'C43': (270, 170)}.items():
        f = b.FindFootprintByReference(ref)
        f.SetPosition(V(*pos)); f.SetOrientationDegrees(0)
        padmap = {
            'Y1': {'1': '/STORAGE/BRIDGE_XI', '2': '/STORAGE/BRIDGE_VSSOSC',
                   '3': '/STORAGE/BRIDGE_XO', '4': '/STORAGE/BRIDGE_VSSOSC'},
            'R23': {'1': '/STORAGE/BRIDGE_XI', '2': '/STORAGE/BRIDGE_XO'},
            'C42': {'1': '/STORAGE/BRIDGE_XI', '2': '/STORAGE/BRIDGE_VSSOSC'},
            'C43': {'1': '/STORAGE/BRIDGE_XO', '2': '/STORAGE/BRIDGE_VSSOSC'},
        }[ref]
        for p in f.Pads():
            p.SetNet(nets[padmap[str(p.GetNumber())]])
            p.SetNetCode(nets[padmap[str(p.GetNumber())]].GetNetCode())

    u = b.FindFootprintByReference('U7')
    for pin, name in (('30', names[3]), ('31', names[3]),
                      ('52', names[0]), ('53', names[2]), ('54', names[1])):
        p = next(p for p in u.Pads() if str(p.GetNumber()) == pin)
        p.SetNet(nets[name]); p.SetNetCode(nets[name].GetNetCode())

    # U7 is at (140,110), rotation 180: clock row is 52=(143,105.5),
    # 53=(142.5,105.5), 54=(142,105.5).  Escape perpendicular to the row,
    # then use separate monotonic lanes around the existing SATA field.
    xi, xo, vs, v33 = (nets[n] for n in names)
    T(b, xi, (143,105.5), (143,101)); T(b, xi, (143,101), (110,101))
    X = lambda n, p: (lambda v: (v.SetPosition(V(*p)), v.SetWidth(pcbnew.FromMM(.5)), v.SetDrill(pcbnew.FromMM(.3)), v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu), v.SetNet(n), b.Add(v))[-1])(pcbnew.PCB_VIA(b))
    X(xi, (110,101)); T(b, xi, (110,101), (190,101), pcbnew.B_Cu)
    X(xi, (190,101)); T(b, xi, (190,101), (190,140), pcbnew.B_Cu)
    T(b, xi, (190,140), (248,145), pcbnew.B_Cu); X(xi, (248,145))
    T(b, xi, (248,145), (248.9,149.15))
    T(b, xo, (142,105.5), (142,99)); T(b, xo, (142,99), (108,99))
    X(xo, (108,99)); T(b, xo, (108,99), (195,99), pcbnew.B_Cu)
    X(xo, (195,99)); T(b, xo, (195,99), (195,145), pcbnew.B_Cu)
    T(b, xo, (195,145), (252,146), pcbnew.B_Cu); X(xo, (252,146))
    T(b, xo, (252,146), (251.1,150.85))
    T(b, vs, (142.5,105.5), (142.5,97)); T(b, vs, (142.5,97), (106,97))
    X(vs, (106,97)); T(b, vs, (106,97), (200,97), pcbnew.B_Cu)
    X(vs, (200,97)); T(b, vs, (200,97), (200,165), pcbnew.B_Cu)
    # Local branches are separated by net/lane, with no via required in this
    # open corridor.  Pad coordinates are explicit for the selected 3225 and
    # 0402 footprints.
    T(b, xi, (248.9,149.15), (249.5,170.0))      # Y1.1 to C42.1
    T(b, xi, (248.9,149.15), (269.5,149.0))       # Y1.1 to R23.1
    T(b, xo, (251.1,150.85), (270.5,149.0))      # Y1.3 to R23.2
    T(b, xo, (251.1,150.85), (269.5,170.0))      # Y1.3 to C43.1
    # VSSOSC remains on B.Cu after the ordinary U7 transition.  Each SMD
    # return pad gets a nearby through-via and only a short F.Cu dogbone.
    for p, q in [((248.9,153.0),(248.9,150.85)),
                 ((251.1,153.0),(251.1,149.15)),
                 ((249.5,173.0),(250.5,170.0)),
                 ((269.5,173.0),(270.5,170.0))]:
        X(vs, p); T(b, vs, p, q, pcbnew.F_Cu)
    T(b, vs, (200,165), (248.9,153.0), pcbnew.B_Cu)
    T(b, vs, (248.9,153.0), (251.1,153.0), pcbnew.B_Cu)
    T(b, vs, (251.1,153.0), (249.5,173.0), pcbnew.B_Cu)
    T(b, vs, (249.5,173.0), (269.5,173.0), pcbnew.B_Cu)

    # FREQSEL0/FREQSEL1 high, using the existing 3V3 net and a local branch.
    T(b, v33, (142.5,114.5), (142.5,117)); T(b, v33, (142.5,117), (146,117))
    T(b, v33, (146,117), (146,114.5)); T(b, v33, (146,114.5), (142,114.5))
    b.Save(str(OUT)); print(OUT)

if __name__ == '__main__': main()
