#!/usr/bin/env python3
"""Print native RTL9210B QFN escape geometry for route planning."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BOARD = ROOT / "PHASE24_RTL9210B_5V_PAD17_V3.kicad_pcb"
b = pcbnew.LoadBoard(str(BOARD))
u = b.FindFootprintByReference("U1")
print("U1 native pads")
for p in u.Pads():
    pos = p.GetPosition(); net = p.GetNetname() or "<none>"
    print(f"pad {p.GetNumber():>2}  {net:<12} {pos.x/1e6:7.3f} {pos.y/1e6:7.3f} size {p.GetSize().x/1e6:.3f}x{p.GetSize().y/1e6:.3f}")
print("\nobjects in QFN escape window x=73..87, y=56..68")
for t in b.GetTracks():
    a, z = t.GetStart(), t.GetEnd()
    coords = [a, z]
    if any(73e6 <= q.x <= 87e6 and 56e6 <= q.y <= 68e6 for q in coords):
        print(f"track {t.GetNetname():<12} {b.GetLayerName(t.GetLayer()):<5} ({a.x/1e6:.3f},{a.y/1e6:.3f})->({z.x/1e6:.3f},{z.y/1e6:.3f})")
for item in b.GetTracks():
    if not isinstance(item, pcbnew.PCB_VIA):
        continue
    p = item.GetPosition()
    if 73e6 <= p.x <= 87e6 and 56e6 <= p.y <= 68e6:
        print(f"via   {item.GetNetname():<12} ({p.x/1e6:.3f},{p.y/1e6:.3f}) size {item.GetWidth(pcbnew.F_Cu)/1e6:.3f} drill {item.GetDrill()/1e6:.3f}")
