"""Disposable native-pad RSET escape probe for the Path-A storage basis."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_DUAL_MODE_STORAGE_PLACEMENT_CURRENT.kicad_pcb"
OUT = R / "PHASE24_JMS583_RSET_ESCAPE_PROBE.kicad_pcb"

def mm(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p):
    q = p.GetPosition()
    return pcbnew.ToMM(q.x), pcbnew.ToMM(q.y)

b = pcbnew.LoadBoard(str(BASE))
u11 = b.FindFootprintByReference("U11")
r80 = b.FindFootprintByReference("R80")
if u11 is None or r80 is None:
    raise RuntimeError("missing U11/R80")
r80.SetPosition(mm(148.0, 140.0))
net = b.FindNet("JMS_REXT")
if net is None:
    raise RuntimeError("missing JMS_REXT")
for item in list(b.GetTracks()):
    if item.GetNetCode() == net.GetNetCode():
        b.RemoveNative(item)
src = xy(u11.FindPadByNumber("39"))
dst = xy(r80.FindPadByNumber("1"))
pts = [src, (145.0, src[1]), (145.0, dst[1]), dst]
for a, z in zip(pts, pts[1:]):
    if a == z: continue
    t = pcbnew.PCB_TRACK(b)
    t.SetStart(mm(*a)); t.SetEnd(mm(*z)); t.SetLayer(pcbnew.F_Cu)
    t.SetWidth(pcbnew.FromMM(0.20)); t.SetNet(net); t.SetNetCode(net.GetNetCode())
    b.Add(t)
b.BuildListOfNets()
b.Save(str(OUT))
print(OUT)
