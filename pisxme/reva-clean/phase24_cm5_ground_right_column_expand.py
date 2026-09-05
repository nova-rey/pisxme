"""Disposable expansion of the accepted right-column CM5-ground collector."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_CM5_GROUND_RIGHT_COLUMN_EXPAND.kicad_pcb'
OUT=R/'PHASE24_CM5_GROUND_RIGHT_COLUMN_EXPAND_V3.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('/CORE_CM5/POWER_GND')
V=lambda x,y:pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(a,z):
    t=pcbnew.PCB_TRACK(b);t.SetLayer(pcbnew.F_Cu);t.SetNet(n);t.SetWidth(pcbnew.FromMM(.20));t.SetStart(V(*a));t.SetEnd(V(*z));b.Add(t)
for y in (102.3,103.5,104.7,105.9):tr((66.96,y),(65.50,y))
tr((65.50,102.3),(65.50,117.9))
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
