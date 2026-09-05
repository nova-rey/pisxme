"""Disposable POWER_GND chain for the outboard capacitor return row."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_CM5_GROUND_RIGHT_SAME_ROWS.kicad_pcb"
OUT = R / "PHASE24_POWER_GND_C14_C19_CHAIN.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))
n = b.FindNet("POWER_GND")
V = lambda x, y: pcbnew.VECTOR2I_MM(float(x), float(y))

# These pads are on one clear horizontal return row; use native pad centers
# and no vias or plane-layer signal routing.
xs = (71.10, 79.10, 87.35, 95.35, 111.35)
for a, z in zip(xs, xs[1:]):
    t = pcbnew.PCB_TRACK(b)
    t.SetLayer(pcbnew.F_Cu); t.SetNet(n); t.SetWidth(pcbnew.FromMM(.20))
    t.SetStart(V(a, 120.0)); t.SetEnd(V(z, 120.0)); b.Add(t)
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
