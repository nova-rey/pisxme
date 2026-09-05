"""Disposable correction: top-side clock support SMD pads belong on F.Cu."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_U7_3V3_CURRENT_LOCAL.kicad_pcb'; OUT=R/'PHASE24_CLOCK_TOPSIDE_PAD_LAYERS.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE))
for ref in ('Y1','R23','C42','C43'):
 f=b.FindFootprintByReference(ref)
 for p in f.Pads():
  if p.GetNumber() not in ('1','2','3','4'): continue
  s=pcbnew.LSET(); s.AddLayer(pcbnew.F_Cu); s.AddLayer(pcbnew.F_Mask); s.AddLayer(pcbnew.F_Paste); p.SetLayerSet(s)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
