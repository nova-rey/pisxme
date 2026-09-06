"""Refresh J3 from the saved authority footprint without changing copper."""
from pathlib import Path
import sys
import pcbnew

ROOT = Path(__file__).resolve().parent
src = Path(sys.argv[1])
dst = Path(sys.argv[2])
board = pcbnew.LoadBoard(str(src))
old = board.FindFootprintByReference("J3")
if old is None:
    raise RuntimeError("J3 is absent")

io = pcbnew.PCB_IO_KICAD_SEXPR()
new = io.FootprintLoad(
    str(ROOT / "PiSXMe_RevA_Clean.pretty"),
    "JAE_SM3ZS067U410ABR1000_BKEY",
)
if new is None:
    raise RuntimeError("authoritative J3 footprint could not be loaded")
new.SetReference("J3")
new.SetValue(old.GetValue())
new.SetPosition(old.GetPosition())
new.SetOrientationDegrees(old.GetOrientationDegrees())
new.SetLayer(old.GetLayer())

board.Remove(old)
board.Add(new)
# Preserve the saved board's actual schematic net ownership by pad number;
# bind after attachment so KiCad resolves the net into this board's net table.
for pad in new.Pads():
    prior = old.FindPadByNumber(pad.GetNumber())
    if prior is None:
        raise RuntimeError(f"authority footprint added unknown pad {pad.GetNumber()}")
    name = prior.GetNetname()
    resolved = board.FindNet(name) if name else None
    pad.SetNet(resolved)
    pad.SetNetCode(resolved.GetNetCode() if resolved else 0)
board.BuildListOfNets()
board.Save(str(dst))
print(dst)
