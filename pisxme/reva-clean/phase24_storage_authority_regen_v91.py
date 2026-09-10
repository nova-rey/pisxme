"""Regenerate two retained package/net authority corrections on V79.

This disposable authoring step mirrors the reviewed generator authority:
U13's package exposed pad is POWER_GND and the source-corrected J3 supply
contacts are STORAGE_3V3.  It authors real pad net ownership only; no graph
edges or copper are synthesized.
"""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V79_M2_POWER_OWNER.kicad_pcb'
OUT=R/'PHASE24_STORAGE_AUTHORITY_REGEN_V91.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); g=b.FindNet('POWER_GND'); s=b.FindNet('STORAGE_3V3'); assert g and s
u=b.FindFootprintByReference('U13'); j=b.FindFootprintByReference('J3'); assert u and j
u.FindPadByNumber('43').SetNet(g)
for p in j.Pads():
 if p.GetNumber() in {'2','4','12','14','16','18','70','72','74'}: p.SetNet(s)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
