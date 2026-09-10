"""V55: add sparse ordinary POWER_GND stitching to V54's storage F.Cu zone."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V54_STORAGE_GND_SOLID.kicad_pcb'; OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V55_STORAGE_GND_STITCH.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('POWER_GND'); assert n
for x,y in [(78,108),(78,172),(228,108),(228,172),(120,108),(200,108),(120,172),(200,172)]:
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(x,y)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
