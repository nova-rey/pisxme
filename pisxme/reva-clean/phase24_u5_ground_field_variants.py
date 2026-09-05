"""Generate one-segment U5 POWER_GND field discriminators."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
segments=[((235,103.875),(235,106.125)),((232.75,105.75),(235,105.75)),((235,105.75),(237.25,105.75))]
V=lambda x,y:pcbnew.VECTOR2I_MM(float(x),float(y))
for i,(a,z) in enumerate(segments,1):
 b=pcbnew.LoadBoard(str(R/'PHASE24_CM5_GROUND_RIGHT_SAME_ROWS.kicad_pcb'));n=b.FindNet('POWER_GND')
 t=pcbnew.PCB_TRACK(b);t.SetLayer(pcbnew.F_Cu);t.SetNet(n);t.SetWidth(pcbnew.FromMM(.20));t.SetStart(V(*a));t.SetEnd(V(*z));b.Add(t)
 pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(R/f'PHASE24_U5_GROUND_FIELD_V{i}.kicad_pcb'))
