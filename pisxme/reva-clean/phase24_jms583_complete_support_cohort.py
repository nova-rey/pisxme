"""Add the remaining REXT/crystal escapes to the native JMS support cohort."""
from pathlib import Path
import os
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / os.environ.get("PISXME_COMPLETE_SUPPORT_BASE", "PHASE24_DUAL_MODE_STORAGE_NC39_SUPPORT_COHORT.kicad_pcb")
OUT = R / os.environ.get("PISXME_COMPLETE_SUPPORT_OUT", "PHASE24_DUAL_MODE_STORAGE_NC39_COMPLETE_SUPPORT.kicad_pcb")

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y)
def seg(b, n, a, z, layer=pcbnew.F_Cu, width=.15):
    if a == z: return
    t = pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z))
    t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(width)); t.SetNet(n)
    t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b, n, q):
    v = pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.55))
    v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
def pad(b, ref, number):
    return b.FindFootprintByReference(ref).FindPadByNumber(str(number))
def remove_net(b, name):
    n = b.FindNet(name)
    for item in list(b.GetTracks()):
        if item.GetNetCode() == n.GetNetCode(): b.RemoveNative(item)
    return n

b = pcbnew.LoadBoard(str(BASE))

# REXT: leave U11 pad 39 laterally, then approach R80 from above. This keeps
# the path out of adjacent QFN pads and uses no via-in-pad.
n = remove_net(b, "JMS_REXT")
s = xy(pad(b, "U11", 39)); d = xy(pad(b, "R80", 1))
seg(b, n, s, (145.0, s[1])); seg(b, n, (145.0, s[1]), (145.0, d[1])); seg(b, n, (145.0, d[1]), d)

# Crystal nets use separate B.Cu horizontal corridors and return on F.Cu at
# ordinary vias outside the QFN and crystal pads.
for name, up, yp, x_escape, y_lane in (
    ("XIN", 50, 1, 134.0, 110.0),
    ("XOUT", 51, 2, 132.0, 112.0),
):
    n = remove_net(b, name)
    s = xy(pad(b, "U11", up)); d = xy(pad(b, "Y10", yp))
    a = (x_escape, s[1]); v1 = (x_escape, y_lane); v2 = (d[0], y_lane)
    seg(b, n, s, a); seg(b, n, a, v1); via(b, n, v1)
    seg(b, n, v1, v2, pcbnew.B_Cu); via(b, n, v2); seg(b, n, v2, d)

b.Save(str(OUT)); print(OUT)
