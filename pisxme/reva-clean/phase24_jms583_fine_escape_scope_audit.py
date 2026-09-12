"""Fail-closed saved-board audit for the JMS583 local fine escape."""
from pathlib import Path
import argparse
import pcbnew

ap = argparse.ArgumentParser()
ap.add_argument("pcb", type=Path)
a = ap.parse_args()
b = pcbnew.LoadBoard(str(a.pcb))
if b is None:
    raise SystemExit("FAIL cannot load PCB")
fine = []
for t in b.GetTracks():
    if t.GetNetname() in {"XIN", "XOUT"} and type(t).__name__ == "PCB_TRACK":
        fine.append(t)
        w = pcbnew.ToMM(t.GetWidth())
        points = (t.GetStart(), t.GetEnd())
        for p in points:
            x, y = pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
            if not (134.5 <= x <= 139.0 and 124.8 <= y <= 132.0):
                raise SystemExit(f"FAIL {t.GetNetname()} escape leaves local window at {x:.4f},{y:.4f}")
        if abs(w - 0.10) > 0.001:
            raise SystemExit(f"FAIL {t.GetNetname()} track width {w:.4f} mm")
if not fine:
    raise SystemExit("FAIL no XIN/XOUT fine escape tracks")
if any(type(v).__name__ == "PCB_VIA" and v.GetNetname() in {"XIN", "XOUT"}
       for v in b.GetTracks()):
    raise SystemExit("FAIL unexpected XIN/XOUT via in local escape")
print(f"PASS JMS583 fine escape scope: {len(fine)} saved 0.10-mm tracks, no fine-net vias")
