"""Materialize the schematic-authoritative U7 clock pad nets."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_LOCAL_REPAIRS_U7_RXN.kicad_pcb"
OUT = ROOT / "PHASE24_U7_CLOCK_NET_AUTHORITY.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))
u = b.FindFootprintByReference("U7")
for num, name in (("52", "/STORAGE/BRIDGE_XI"),
                  ("53", "/STORAGE/BRIDGE_VSSOSC"),
                  ("54", "/STORAGE/BRIDGE_XO")):
    p = next(x for x in u.Pads() if str(x.GetNumber()) == num)
    n = b.FindNet(name)
    if n is None:
        raise RuntimeError(name)
    p.SetNet(n); p.SetNetCode(n.GetNetCode())
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
