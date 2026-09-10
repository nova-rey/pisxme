"""Disposable coordinated U1 pad-row departure repair for Path-B support."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_LOCAL_DEPARTURE_REPAIR.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
P = lambda x, y: pcbnew.VECTOR2I_MM(float(x), float(y))
W = pcbnew.FromMM(0.20)

b = pcbnew.LoadBoard(str(BASE))
def remove_local(net_name, x_max=110, y_min=73.0):
    for q in list(b.GetTracks()):
        pts = [q.GetPosition()] if isinstance(q, pcbnew.PCB_VIA) else [q.GetStart(), q.GetEnd()]
        xy = [(pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)) for p in pts]
        if q.GetNetname() == net_name and any(x <= x_max and y >= y_min for x, y in xy):
            b.RemoveNative(q)
for n in ("CLKREQ_N", "PERST_N", "RTL_5V"):
    remove_local(n)

def net(name):
    n = b.FindNet(name); assert n, name; return n
def track(n, a, z, layer=F):
    q = pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer)
    q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(n, x, y):
    q = pcbnew.PCB_VIA(b); q.SetPosition(P(x, y)); q.SetWidth(pcbnew.FromMM(0.6)); q.SetDrill(pcbnew.FromMM(0.3))
    q.SetLayerPair(F, B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)

# ISOLATEB: use the previously accepted pad-end escape class and hand off at
# y=78.5, above the PERST_N B.Cu departure below.
iso = net("ISOLATEB")
track(iso, (99.2, 73.5), (99.2, 78.5)); via(iso, 99.2, 78.5)
track(iso, (99.2, 78.5), (106, 78.5), B)

# CLKREQ_N: move its via/departure north of the PERST corridor and reconnect
# to the existing far-side continuation at x=119.2,y=74.
clk = net("CLKREQ_N")
track(clk, (99.6, 73.5), (99.6, 76.5)); via(clk, 99.6, 76.5)
track(clk, (99.6, 76.5), (107, 76.5), B); track(clk, (107, 76.5), (107, 74), B)
track(clk, (107, 74), (119.2, 74), B)

# PERST_N: retain the remote F.Cu/B.Cu/connector endpoint but move the local
# departure to a dedicated lower corridor.
per = net("PERST_N")
track(per, (100.0, 73.5), (100.0, 79.5)); via(per, 100, 79.5)
track(per, (100, 79.5), (134, 79.5), B); via(per, 134, 79.5)
track(per, (134, 79.5), (134, 70.275), F)

# RTL_5V: take the pad-end departure farther south, transition outboard, and
# rejoin the existing regulator branch at x=110,y=67.2.
five = net("RTL_5V")
track(five, (101.2, 73.5), (101.2, 82)); via(five, 101.2, 82)
track(five, (101.2, 82), (116, 82), B); via(five, 116, 82)
track(five, (116, 82), (116, 67.2), F); track(five, (116, 67.2), (110, 67.2), F)

pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
