"""V54: probe solid connection for the bounded storage POWER_GND zone."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V53_STORAGE_GND_ACCESS.kicad_pcb'; OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V54_STORAGE_GND_SOLID.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); zs=[z for z in b.Zones() if z.GetNetname()=='POWER_GND' and z.GetLayer()==pcbnew.F_Cu]; assert zs
for z in zs: z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
