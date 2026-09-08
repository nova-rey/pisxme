"""Fail-closed audit of every populated JMS583 U11 PCB pad net."""
from pathlib import Path
import pcbnew
from phase24_integrate_dual_mode_storage import JMS

ROOT = Path(__file__).resolve().parent
BOARD = ROOT / "PHASE24_DUAL_MODE_STORAGE_PLACEMENT_CURRENT.kicad_pcb"
b = pcbnew.LoadBoard(str(BOARD))
f = b.FindFootprintByReference("U11")
if f is None:
    raise SystemExit("FAIL missing U11")
failures = []
for number, expected in sorted(JMS.items()):
    p = f.FindPadByNumber(str(number))
    if p is None:
        failures.append(f"missing U11.{number}")
        continue
    actual = p.GetNetname().lstrip("/").split("/")[-1]
    if actual != expected:
        failures.append(f"U11.{number}: expected {expected}, got {actual}")
if failures:
    for failure in failures: print("FAIL", failure)
    raise SystemExit(1)
print("PASS U11 64-pad native PCB net authority")
