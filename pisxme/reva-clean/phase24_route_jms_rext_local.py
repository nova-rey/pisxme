"""Add a native-pad JMS_REXT escape to the current reset-local base."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_STORAGE_MKEY_USB3_RESET_LOCAL_20260912.kicad_pcb"
OUT = R / "PHASE24_STORAGE_MKEY_USB3_REXT_LOCAL_20260912.kicad_pcb"

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y)

def seg(board, net, a, z):
    if a == z: return
    t = pcbnew.PCB_TRACK(board)
    t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(pcbnew.F_Cu)
    t.SetWidth(pcbnew.FromMM(0.20)); t.SetNet(net)
    t.SetNetCode(net.GetNetCode()); board.Add(t)

board = pcbnew.LoadBoard(str(BASE))
u11 = board.FindFootprintByReference("U11")
r80 = board.FindFootprintByReference("R80")
net = board.FindNet("JMS_REXT")
if not u11 or not r80 or not net:
    raise RuntimeError("missing REXT endpoint")

# Put the resistor in the open east support pocket.  The route stays outside
# the accepted AVDD33/VCCO/reset support channels and approaches pad 1 from
# below; this is a disposable local primitive, not a global placement change.
r80.SetPosition(P(148.0, 130.0))
for item in list(board.GetTracks()):
    if item.GetNetCode() == net.GetNetCode():
        board.RemoveNative(item)
src = xy(u11.FindPadByNumber("39"))
dst = xy(r80.FindPadByNumber("1"))
points = [src, (147.0, src[1]), (147.0, 130.0), dst]
for a, z in zip(points, points[1:]):
    seg(board, net, a, z)
board.Save(str(OUT))
print(OUT)
