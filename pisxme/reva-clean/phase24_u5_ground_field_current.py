"""Disposable U5 exposed POWER_GND field stitch on the current basis."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
b=pcbnew.LoadBoard(str(R/'PHASE24_CM5_GROUND_RIGHT_SAME_ROWS.kicad_pcb'))
n=b.FindNet('POWER_GND'); V=lambda x,y:pcbnew.VECTOR2I_MM(float(x),float(y))
for a,z in [((235,103.875),(235,106.125)),((232.75,105.75),(235,105.75)),((235,105.75),(237.25,105.75))]:
 t=pcbnew.PCB_TRACK(b);t.SetLayer(pcbnew.F_Cu);t.SetNet(n);t.SetWidth(pcbnew.FromMM(.20));t.SetStart(V(*a));t.SetEnd(V(*z));b.Add(t)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(R/'PHASE24_U5_GROUND_FIELD_CURRENT.kicad_pcb'))
