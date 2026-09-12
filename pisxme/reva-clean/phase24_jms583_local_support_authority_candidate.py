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
fp(b, 'L10').SetPosition(P(142.00, 130.00))

# The crystal pair is kept together in the immediate U11 north escape.  The
# 0.4-mm-pitch JMS583 field needs a local 0.10-mm trace/clearance exception;
# the route hands back to the normal 0.15/0.20-mm profile outside this field.
path(b, 'XIN', ('U11','50'), ('Y10','1'),
     [(136.60,130.00),(136.60,125.55)], width=.10)
path(b, 'XOUT', ('U11','51'), ('Y10','2'),
     [(138.40,130.00),(138.40,127.25)], width=.10)

# Use separated local corridors for the two L10 terminations. The VDDREG
# branch transitions outside both pads; no via-in-pad is used.
n = clear(b, 'JMS_VDDREG_5V')
src = pos(b, 'U11', '1'); dst = pos(b, 'L10', '2')
track(b, n, src, (135.60,130.20), F, .15)
via(b, n, (135.60,130.20))
track(b, n, (135.60,130.20), (135.60,128.80), B, .15)
track(b, n, (135.60,128.80), (142.00,128.80), B, .15)
via(b, n, (142.00,128.80))
track(b, n, (142.00,128.80), dst, F, .15)

n = clear(b, 'LXO')
src = pos(b, 'U11', '64'); dst = pos(b, 'L10', '1')
track(b, n, src, (144.50,131.40), F, .15)
via(b, n, (144.50,131.40))
track(b, n, (144.50,131.40), (144.50,129.50), B, .15)
track(b, n, (144.50,129.50), (140.85,129.50), B, .15)
via(b, n, (140.85,129.50))
track(b, n, (140.85,129.50), dst, F, .15)

b.BuildListOfNets(); b.Save(a.output); print(a.output)
