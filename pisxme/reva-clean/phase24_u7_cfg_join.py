"""Disposable U7 BRIDGE_CFG repeated-pad join."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_LOCAL_REPAIRS_U7_RXN.kicad_pcb"
OUT = ROOT / "PHASE24_LOCAL_REPAIRS_U7_CFG.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))
n = b.FindNet("/STORAGE/BRIDGE_CFG")
t = pcbnew.PCB_TRACK(b)
t.SetLayer(pcbnew.F_Cu); t.SetNet(n); t.SetWidth(pcbnew.FromMM(0.20))
points = ((117.5, 144.5), (114.0, 144.5), (114.0, 141.0),
          (126.0, 141.0), (126.0, 144.5), (124.5, 144.5))
for a, z in zip(points, points[1:]):
    t = pcbnew.PCB_TRACK(b); t.SetLayer(pcbnew.F_Cu); t.SetNet(n)
    t.SetWidth(pcbnew.FromMM(0.20)); t.SetStart(pcbnew.VECTOR2I_MM(*a))
    t.SetEnd(pcbnew.VECTOR2I_MM(*z)); b.Add(t)
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
