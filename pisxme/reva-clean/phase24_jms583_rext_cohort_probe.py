"""Add a relocated, native-pad REXT escape to the retained seven-net cohort."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_JMS583_SUPPORT_COHORT_PROBE.kicad_pcb"
OUT = R / "PHASE24_JMS583_SUPPORT_COHORT_REXT_V8.kicad_pcb"

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y)
def seg(b, n, a, z):
    t = pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z))
    t.SetLayer(pcbnew.F_Cu); t.SetWidth(pcbnew.FromMM(.20))
    t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)

b = pcbnew.LoadBoard(str(BASE))
u = b.FindFootprintByReference("U11"); r = b.FindFootprintByReference("R80")
n = b.FindNet("JMS_REXT")
if not u or not r or not n: raise RuntimeError("missing REXT objects")
r.SetPosition(P(148, 130))
for item in list(b.GetTracks()):
    if item.GetNetCode() == n.GetNetCode(): b.RemoveNative(item)
src = xy(u.FindPadByNumber("39")); dst = xy(r.FindPadByNumber("1"))
# Stay east of the AVDD33 y=140 corridor, then approach R80 from below.
points = [src, (147, src[1]), (147, 130), dst]
for a, z in zip(points, points[1:]):
    if a != z: seg(b, n, a, z)
b.Save(str(OUT)); print(OUT)
