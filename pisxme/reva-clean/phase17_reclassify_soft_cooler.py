"""Disposable Phase-17 mechanical interpretation trial.

Reclassifies only the project-authored soft V100 cooling reservation from
F.CrtYd to Dwgs.User.  The measured envelope remains visible; real component
courtyards, mounting hardware, and connector bodies are untouched.
"""
from pathlib import Path
import os
import pcbnew

root = Path(__file__).resolve().parent
base = Path(os.environ.get("PISXME_BASE", root / "ACREAGE_PHASE17_F1RIGHT40_ETH_GROUND_FIXED.kicad_pcb"))
out = Path(os.environ.get("PISXME_OUT", root / "ACREAGE_PHASE17_SOFT_COOLER_TRIAL.kicad_pcb"))
b = pcbnew.LoadBoard(str(base))
f = b.FindFootprintByReference("MECH_V100")
if f is None:
    raise RuntimeError("MECH_V100 not found")
changed = 0
for g in list(f.GraphicalItems()):
    if g.GetLayer() == pcbnew.F_CrtYd:
        g.SetLayer(pcbnew.Dwgs_User)
        changed += 1
pcbnew.SaveBoard(str(out), b)
print(f"saved {out}; reclassified {changed} soft-envelope graphics")
