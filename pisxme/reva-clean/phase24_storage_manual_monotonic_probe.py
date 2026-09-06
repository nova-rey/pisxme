"""Disposable native-pad storage escape probe for STORAGE_LOCAL_CLEAR2.

This is a route-development experiment only.  Terminals and nets come from
the saved board; the explicit lane corridors are routing geometry, not
synthetic connectivity edges.
"""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_MACRO_FRESH_STORAGE_LOCAL_J3_EDGE.kicad_pcb"
OUT = R / "PHASE24_STORAGE_LOCAL_J3_EDGE_MANUAL_MONOTONIC.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.15)

def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def net(b, name):
    n = b.FindNet(name)
    if n is None: raise RuntimeError(f"missing net {name}")
    return n
def pad(b, ref, number):
    p = b.FindFootprintByReference(ref).FindPadByNumber(str(number))
    if p is None: raise RuntimeError(f"missing {ref}.{number}")
    return p
def add_track(b, n, a, z, layer):
    t = pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z));
    t.SetLayer(layer); t.SetWidth(W); t.SetNet(n); b.Add(t)
def add_via(b, n, p):
    v = pcbnew.PCB_VIA(b); v.SetPosition(V(*p));
    v.SetWidth(pcbnew.FromMM(.50)); v.SetDrill(pcbnew.FromMM(.30));
    v.SetLayerPair(F, B); v.SetNet(n); b.Add(v)
def emit(b, n, points):
    prev = points[0]
    for cur in points[1:]:
        if cur[2] != prev[2]:
            add_via(b, n, prev[:2])
        else:
            add_track(b, n, prev[:2], cur[:2], cur[2])
        prev = cur

b = pcbnew.LoadBoard(str(BASE))
affected = ('CM5_USB3_', 'BRIDGE_SATA_', 'SATA_M2_', 'BRIDGE_XI', 'BRIDGE_XO')
jobs = [
    ('CM5_USB3_RX_N', '128', '42', [(72.0,103.9,F),(72.0,103.9,B),(82.0,103.9,B),(82.0,103.9,F),(82.0,118.0,F)]),
    ('CM5_USB3_RX_P', '130', '43', [(72.0,104.8,F),(72.0,104.8,B),(83.0,108.8,B),(83.0,108.8,F),(83.0,119.0,F)]),
    ('CM5_USB3_TX_N', '140', '45', [(72.0,106.3,F),(72.0,106.3,B),(72.0,109.5,B),(80.0,110.5,B),(80.0,110.5,F),(80.0,117.0,F)]),
    ('CM5_USB3_TX_P', '142', '46', [(73.0,106.7,F),(73.0,106.7,B),(73.0,111.0,B),(81.5,112.0,B),(81.5,112.0,F),(81.5,119.0,F)]),
]
# Cache native terminal coordinates before mutation; KiCad 10 invalidates
# footprint proxies when tracks are removed from a loaded board.
terminals = [(name, xy(pad(b,'J7',sp).GetPosition()),
              xy(pad(b,'U7',tp).GetPosition()), lane)
             for name,sp,tp,lane in jobs]
for t in list(b.Tracks()):
    if any(k in t.GetNetname() for k in affected): b.Remove(t)
for name, source, target, lane in terminals:
    n = net(b, '/CORE_CM5/' + name)
    points = [(source[0], source[1], F)] + lane + [(target[0], target[1], F)]
    emit(b, n, points)
    print(name, source, target)
b.Save(str(OUT)); print(OUT)
