"""Add storage-local mode-control copper using native pad locations."""
from pathlib import Path
import os
import pcbnew

R = Path(__file__).resolve().parent
base = R / os.environ.get("P24_MODE_BASE", "PHASE24_STORAGE_MODEFIX_PLACEMENT_V2.kicad_pcb")
out = R / os.environ.get("P24_MODE_OUT", "PHASE24_STORAGE_MODEFIX_MODE_ROUTE.kicad_pcb")
b = pcbnew.LoadBoard(str(base))
if b is None: raise SystemExit("target board load failed")
def pad(ref, num): return b.FindFootprintByReference(ref).FindPadByNumber(str(num))
def add(name, left, right, layer):
    n = nets[name]
    t = pcbnew.PCB_TRACK(b)
    t.SetStart(pad(*left).GetPosition()); t.SetEnd(pad(*right).GetPosition())
    t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(codes[name]); b.Add(t)
nets = {name: b.FindNet(name) for name in ("AUTO_PEDET", "MODE_IN", "STORAGE_SEL")}
if any(value is None for value in nets.values()): raise SystemExit("missing mode net")
codes = {name: value.GetNetCode() for name, value in nets.items()}
add("AUTO_PEDET", ("J3",69), ("J5",2), pcbnew.F_Cu)
add("MODE_IN", ("J5",4), ("U14",2), pcbnew.F_Cu)
add("STORAGE_SEL", ("U14",4), ("U13",9), pcbnew.F_Cu)
add("STORAGE_SEL", ("U14",4), ("U12",9), pcbnew.F_Cu)
b.BuildListOfNets(); b.Save(str(out)); print(out)
