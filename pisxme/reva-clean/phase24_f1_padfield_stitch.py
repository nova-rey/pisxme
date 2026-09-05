"""Disposable same-net F1 fuse-pad field joins."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb"
OUT = ROOT / "PHASE24_F1_PADFIELD_STITCH.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))


def p(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def add(net_name, a, z):
    n = b.FindNet(net_name)
    t = pcbnew.PCB_TRACK(b)
    t.SetLayer(pcbnew.F_Cu)
    t.SetNet(n)
    t.SetWidth(pcbnew.FromMM(0.30))
    t.SetStart(p(*a))
    t.SetEnd(p(*z))
    b.Add(t)


add("/POWER_INPUT/12V_IN_A", (233.6, 38.75), (233.6, 41.25))
add("/POWER_INPUT/12V_IN_A", (237.1, 38.75), (237.1, 41.25))
add("/POWER_INPUT/12V_IN_A", (233.6, 38.75), (237.1, 38.75))
add("/POWER_INPUT/FUSED_12V_A", (242.9, 38.75), (242.9, 41.25))
add("/POWER_INPUT/FUSED_12V_A", (246.4, 38.75), (246.4, 41.25))
add("/POWER_INPUT/FUSED_12V_A", (242.9, 38.75), (246.4, 38.75))

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
