"""Materialize the source-approved J3 power-net rename on a V75 descendant.

This is a disposable regeneration aid: it changes only J3 pads whose saved
net is M2_3V3 to the existing STORAGE_3V3 PCB net. It is not a synthetic
connectivity edge and does not author copper.
"""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_STORAGE_CM5_USB4_MONOTONIC_V75_BRIDGE_R1RTN_R24_SIDE.kicad_pcb"
OUT = H / "PHASE24_STORAGE_CM5_USB4_MONOTONIC_V79_M2_POWER_OWNER.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))
old = b.FindNet("M2_3V3")
new = b.FindNet("STORAGE_3V3")
assert old and new
j3 = b.FindFootprintByReference("J3")
assert j3
pads = [p for p in j3.Pads() if p.GetNetCode() == old.GetNetCode()]
assert len(pads) == 9, len(pads)
for p in pads:
    p.SetNet(new)
b.BuildListOfNets()
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(f"materialized {len(pads)} J3 M2 power pads onto STORAGE_3V3: {OUT}")
