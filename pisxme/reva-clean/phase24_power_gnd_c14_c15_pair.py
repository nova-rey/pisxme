"""Disposable adjacent POWER_GND return-pair test."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
b=pcbnew.LoadBoard(str(R/'PHASE24_CM5_GROUND_RIGHT_SAME_ROWS.kicad_pcb'))
n=b.FindNet('POWER_GND')
V=lambda x,y:pcbnew.VECTOR2I_MM(float(x),float(y))
t=pcbnew.PCB_TRACK(b);t.SetLayer(pcbnew.F_Cu);t.SetNet(n);t.SetWidth(pcbnew.FromMM(.20));t.SetStart(V(71.10,120));t.SetEnd(V(79.10,120));b.Add(t)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(R/'PHASE24_POWER_GND_C14_C15_PAIR.kicad_pcb'))
