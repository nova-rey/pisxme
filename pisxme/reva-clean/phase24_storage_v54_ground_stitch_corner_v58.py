"""V58: single clear-corner POWER_GND stitch from V54."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V54_STORAGE_GND_SOLID.kicad_pcb'
OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V58_GND_CORNER_STITCH.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('POWER_GND'); assert n
v=pcbnew.PCB_VIA(b); v.SetPosition(pcbnew.VECTOR2I_MM(78,108)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
