"""Apply the bounded JMS583 local-support placement decision to a PCB copy."""
import argparse
import pcbnew

ap = argparse.ArgumentParser()
ap.add_argument("base")
ap.add_argument("output")
a = ap.parse_args()

F, B = pcbnew.F_Cu, pcbnew.B_Cu
def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y)
def fp(b, ref): return b.FindFootprintByReference(ref)
def pos(b, ref, n): return xy(fp(b, ref).FindPadByNumber(str(n)))
def track(b, net, p, q, layer=F, width=.15):
    t = pcbnew.PCB_TRACK(b); t.SetStart(P(*p)); t.SetEnd(P(*q))
    t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(width)); t.SetNet(net)
    t.SetNetCode(net.GetNetCode()); b.Add(t)
def via(b, net, p):
    v = pcbnew.PCB_VIA(b); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(.60))
    v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F, B); v.SetNet(net)
    v.SetNetCode(net.GetNetCode()); b.Add(v)
def clear(b, name):
    n = b.FindNet(name)
    for item in list(b.GetTracks()):
        if item.GetNetCode() == n.GetNetCode(): b.RemoveNative(item)
    return n
def path(b, name, src, dst, points, layer=F, width=.15):
    n = clear(b, name); pts = [pos(b, *src)] + points + [pos(b, *dst)]
    for p, q in zip(pts, pts[1:]): track(b, n, p, q, layer, width)

b = pcbnew.LoadBoard(a.base)
fp(b, 'Y10').SetPosition(P(138.20, 126.40))
fp(b, 'L10').SetPosition(P(141.00, 128.00))

# The crystal pair is kept together in the immediate U11 north escape.
path(b, 'XIN', ('U11','50'), ('Y10','1'), [(137.40,129.60),(137.10,128.40)])
path(b, 'XOUT', ('U11','51'), ('Y10','2'), [(137.80,129.20),(137.10,127.80)])

# Use separated local corridors for the two L10 terminations.  No plane-layer
# signal routing and no via-in-pad are introduced by this candidate.
path(b, 'JMS_VDDREG_5V', ('U11','1'), ('L10','2'),
     [(135.60,130.20),(135.60,128.80),(140.60,128.00)], B, .15)
path(b, 'LXO', ('U11','64'), ('L10','1'),
     [(144.00,130.20),(144.00,127.20),(139.85,127.20)], F, .15)

b.BuildListOfNets(); b.Save(a.output); print(a.output)
