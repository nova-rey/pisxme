"""Disposable exact rotated-U7 clock oracle transplant into the current base."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_U7_CLOCK_NET_AUTHORITY.kicad_pcb"
ORACLE = ROOT / "PHASE19_PASS_CLOCK_ROT180_S20.kicad_pcb"
OUT = ROOT / "PHASE24_CLOCK_ORACLE_COORDINATED.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE)); o = pcbnew.LoadBoard(str(ORACLE))
names = {"/STORAGE/BRIDGE_XI", "/STORAGE/BRIDGE_XO", "/STORAGE/BRIDGE_VSSOSC"}
nets = {name: b.FindNet(name) for name in names}


def mm(v): return float(v) / 1_000_000.0


def xy(q): return (mm(q.x), mm(q.y))


def pt(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))


for ref in ("Y1", "R23", "C42", "C43"):
    src = o.FindFootprintByReference(ref)
    dst = b.FindFootprintByReference(ref)
    if src is None or dst is None:
        raise RuntimeError(ref)
    dst.SetPosition(src.GetPosition())
    dst.SetOrientationDegrees(src.GetOrientationDegrees())
    for p in dst.Pads():
        name = p.GetNetname()
        if name in nets:
            p.SetNet(nets[name]); p.SetNetCode(nets[name].GetNetCode())

for item in o.GetTracks():
    if item.GetNetname() not in names:
        continue
    n = nets[item.GetNetname()]
    if item.Type() == pcbnew.PCB_VIA_T:
        v = pcbnew.PCB_VIA(b); v.SetPosition(item.GetPosition())
        v.SetWidth(item.GetWidth(pcbnew.F_Cu)); v.SetDrill(item.GetDrill())
        v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); v.SetNet(n); b.Add(v)
    else:
        t = pcbnew.PCB_TRACK(b); t.SetStart(item.GetStart()); t.SetEnd(item.GetEnd())
        t.SetLayer(item.GetLayer()); t.SetWidth(item.GetWidth()); t.SetNet(n); b.Add(t)

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT)); print(OUT)
