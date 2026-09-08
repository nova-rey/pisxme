"""V365: transplant retained RSET/crystal primitives onto V364 power fields."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
DST=H/'PHASE24_RTL9210B_1V1_3V3_COALLOCATE_V364.kicad_pcb'; RSET=H/'PHASE24_RTL9210B_RSET_ROUTE_V340.kicad_pcb'; XTAL=H/'PHASE24_RTL9210B_CRYSTAL_ROUTE_V339.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_SUPPORT_ON_POWER_V365.kicad_pcb'
b=pcbnew.LoadBoard(str(DST))
for srcpath,nets in [(RSET,('RSET',)),(XTAL,('XTAL_IN','XTAL_OUT'))]:
 s=pcbnew.LoadBoard(str(srcpath))
 for x in s.GetTracks():
  if x.GetNetname() in nets: b.Add(x.Duplicate())
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
