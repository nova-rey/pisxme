"""Disposable correction of missing U7 clock pad net ownership.

The net names come from the native Phase 24 netlist; this script only repairs
serialized pad ownership before routing and does not synthesize connectivity.
"""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_U7_RXN_CURRENT_LOCAL.kicad_pcb'; OUT=R/'PHASE24_U7_CLOCK_PAD_NET_AUTHORITY.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U7')
for num,name in [('52','/STORAGE/BRIDGE_XI'),('53','/STORAGE/BRIDGE_VSSOSC'),('54','/STORAGE/BRIDGE_XO')]:
    p=next(p for p in u.Pads() if p.GetNumber()==num); n=b.FindNet(name)
    if n is None: raise RuntimeError(name)
    p.SetNet(n)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
