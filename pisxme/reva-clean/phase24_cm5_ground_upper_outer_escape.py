"""Disposable upper J7 ground outer escapes, without pad-field bridges."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_CM5_GROUND_RIGHT_SAME_ROWS.kicad_pcb"
OUT = R / "PHASE24_CM5_GROUND_UPPER_OUTER_ESCAPE.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))
n = b.FindNet("/CORE_CM5/POWER_GND")
V = lambda x, y: pcbnew.VECTOR2I_MM(float(x), float(y))

def tr(a, z):
    t = pcbnew.PCB_TRACK(b)
    t.SetLayer(pcbnew.F_Cu); t.SetNet(n); t.SetWidth(pcbnew.FromMM(.20))
    t.SetStart(V(*a)); t.SetEnd(V(*z)); b.Add(t)

# Escape only ground pads on the three upper rows to the outside of the
# connector.  Keep the two columns separate; no trace traverses the live
# Ethernet/service pad-field corridor.
for y in (98.7, 99.9, 101.1):
    tr((32.96, y), (31.40, y))
    tr((36.04, y), (37.60, y))
tr((31.40, 98.7), (31.40, 101.1))
tr((37.60, 98.7), (37.60, 101.1))
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
