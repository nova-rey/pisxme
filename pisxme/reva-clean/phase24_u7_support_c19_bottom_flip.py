"""Disposable true backside C19 variant using KiCad footprint flip semantics."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; src=R/'PHASE24_STORAGE_NATIVE_ORACLE_SUPPORT_TRANSPLANT.kicad_pcb'; out=R/'PHASE24_STORAGE_NATIVE_ORACLE_SUPPORT_C19_BOTTOM_FLIPPED.kicad_pcb'
b=pcbnew.LoadBoard(str(src)); f=b.FindFootprintByReference('C19'); f.SetLayerAndFlip(pcbnew.B_Cu); b.BuildListOfNets(); b.Save(str(out)); print(out)
