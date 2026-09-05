"""Disposable composition of the previously accepted J1 ground columns."""
from collections import defaultdict
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_CM5_GROUND_RIGHT_SAME_ROWS.kicad_pcb"
OUT = R / "PHASE24_J1_GROUND_COLUMNS_CURRENT.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))
j1 = b.FindFootprintByReference("J1")
n = b.FindNet("POWER_GND")
V = lambda x, y: pcbnew.VECTOR2I_MM(float(x), float(y))
cols = defaultdict(list)
for pad in j1.Pads():
    if pad.GetNetCode() == n.GetNetCode():
        q = pad.GetPosition()
        cols[round(q.x / 1_000_000.0, 6)].append(q.y / 1_000_000.0)
if len(cols) != 7 or any(len(v) != 10 for v in cols.values()):
    raise RuntimeError("unexpected J1 ground field shape")
for x, ys in sorted(cols.items()):
    t = pcbnew.PCB_TRACK(b); t.SetLayer(pcbnew.F_Cu); t.SetNet(n)
    t.SetWidth(pcbnew.FromMM(.45)); t.SetStart(V(x, min(ys))); t.SetEnd(V(x, max(ys))); b.Add(t)
    v = pcbnew.PCB_VIA(b); v.SetNet(n); v.SetPosition(V(x, 98.0))
    v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); b.Add(v)
    t = pcbnew.PCB_TRACK(b); t.SetLayer(pcbnew.F_Cu); t.SetNet(n)
    t.SetWidth(pcbnew.FromMM(.45)); t.SetStart(V(x, max(ys))); t.SetEnd(V(x, 98.0)); b.Add(t)
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT)); print(OUT)
