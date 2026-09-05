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
    for ref, pos in {'Y1': (220, 150), 'R23': (230, 150),
                     'C42': (220, 160), 'C43': (230, 160)}.items():
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
    T(b, xi, (143,105.5), (143,100)); T(b, xi, (143,100), (155,98))
    T(b, xi, (155,98), (155,140)); T(b, xi, (155,140), (218.9,149.15))
    T(b, xo, (142,105.5), (142,99)); T(b, xo, (142,99), (157,97))
    T(b, xo, (157,97), (157,145)); T(b, xo, (157,145), (218.9,150.85))
    T(b, vs, (142.5,105.5), (142.5,98)); T(b, vs, (142.5,98), (159,96))
    T(b, vs, (159,96), (159,165)); T(b, vs, (159,165), (218.9,159.15))

    # Local branches are separated by net/lane, with no via required in this
    # open corridor.  Pad coordinates are explicit for the selected 3225 and
    # 0402 footprints.
    T(b, xi, (218.9,149.15), (218.9,149.15))      # Y1.1
    T(b, xi, (218.9,149.15), (219.5,160.0))       # C42.1
    T(b, xi, (218.9,149.15), (229.5,150.0))       # R23.1
    T(b, xo, (218.9,150.85), (221.1,150.85)); T(b, xo, (221.1,150.85), (230.5,150.0)) # R23.2
    T(b, xo, (221.1,150.85), (229.5,160.0))      # C43.1
    T(b, vs, (218.9,159.15), (218.9,150.85))      # Y1.2
    T(b, vs, (218.9,159.15), (221.1,149.15))      # Y1.4
    T(b, vs, (218.9,159.15), (220.5,160.0))       # C42.2
    T(b, vs, (218.9,159.15), (230.5,160.0))       # C43.2

    # FREQSEL0/FREQSEL1 high, using the existing 3V3 net and a local branch.
    T(b, v33, (142.5,114.5), (142.5,117)); T(b, v33, (142.5,117), (146,117))
    T(b, v33, (146,117), (146,114.5)); T(b, v33, (146,114.5), (142,114.5))
    b.Save(str(OUT)); print(OUT)

if __name__ == '__main__': main()
