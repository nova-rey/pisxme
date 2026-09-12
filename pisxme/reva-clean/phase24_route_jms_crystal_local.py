"""Add a coupled native-pad XIN/XOUT escape to the REXT storage base."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_STORAGE_MKEY_USB3_REXT_LOCAL_20260912.kicad_pcb"
OUT = R / "PHASE24_STORAGE_MKEY_USB3_CRYSTAL_LOCAL_20260912.kicad_pcb"

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y)

def add_track(board, net, a, z, layer):
    if a == z: return
    t = pcbnew.PCB_TRACK(board); t.SetStart(P(*a)); t.SetEnd(P(*z))
    t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(0.20)); t.SetNet(net)
    t.SetNetCode(net.GetNetCode()); board.Add(t)

def add_via(board, net, p):
    v = pcbnew.PCB_VIA(board); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(0.60))
    v.SetDrill(pcbnew.FromMM(0.30)); v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    v.SetNet(net); v.SetNetCode(net.GetNetCode()); board.Add(v)

board = pcbnew.LoadBoard(str(BASE))
u11 = board.FindFootprintByReference("U11")
y10 = board.FindFootprintByReference("Y10")
if not u11 or not y10: raise RuntimeError("missing U11/Y10")
y10.SetPosition(P(150, 125))

# Ordered, coupled escapes: the two QFN pads leave west, then use adjacent
# B.Cu channels and return together at the crystal's west side.
paths = (
    ("XIN", "50", "1", ((137.4,131.4),(135.0,131.4),(135.0,128.0)), (148.0,128.0)),
    ("XOUT", "51", "2", ((137.8,131.4),(136.0,131.4),(136.0,129.5)), (149.0,129.5)),
)
for name, up, yp, fpts, bpoint in paths:
    net = board.FindNet(name)
    if not net: raise RuntimeError("missing " + name)
    for item in list(board.GetTracks()):
        if item.GetNetCode() == net.GetNetCode(): board.RemoveNative(item)
    src = xy(u11.FindPadByNumber(up)); dst = xy(y10.FindPadByNumber(yp))
    for a, z in zip((src, *fpts), (*fpts,)):
        add_track(board, net, a, z, pcbnew.F_Cu)
    add_via(board, net, fpts[-1])
    add_track(board, net, fpts[-1], bpoint, pcbnew.B_Cu)
    add_via(board, net, bpoint)
    add_track(board, net, bpoint, (bpoint[0], dst[1]), pcbnew.F_Cu)
    add_track(board, net, (bpoint[0], dst[1]), dst, pcbnew.F_Cu)
board.Save(str(OUT)); print(OUT)
