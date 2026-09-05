"""Disposable same-row-only CM5-ground bridge experiment."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_CM5_GROUND_LOWER_COMB.kicad_pcb'
OUT=R/'PHASE24_CM5_GROUND_UPPER_BRIDGES_ONLY.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('/CORE_CM5/POWER_GND')
V=lambda x,y:pcbnew.VECTOR2I_MM(float(x),float(y))
for y in (98.7,99.9,101.1):
    t=pcbnew.PCB_TRACK(b);t.SetLayer(pcbnew.F_Cu);t.SetNet(n);t.SetWidth(pcbnew.FromMM(.20));t.SetStart(V(32.96,y));t.SetEnd(V(36.04,y));b.Add(t)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
