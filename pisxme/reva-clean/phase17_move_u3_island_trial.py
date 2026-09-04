"""Disposable Phase 11/12 trial: translate the complete U3 regulator island."""
from pathlib import Path
import pcbnew
import os

ROOT = Path(__file__).resolve().parent
BASE = Path(os.environ.get("PISXME_BASE", ROOT / "ACREAGE_PCIE_PHASE16.kicad_pcb"))
OUT = Path(os.environ.get("PISXME_OUT", ROOT / "ACREAGE_PHASE17_U3_DOWN30.kicad_pcb"))
DX = float(os.environ.get("PISXME_U3_DX", "0"))
DY = float(os.environ.get("PISXME_U3_DY", "30"))
REFS = {"U3", "C5", "C6", "C7", "C8", "C9", "R3", "R4", "R5", "R6"}
LOCAL_NETS = {"/REGULATORS/CM5_5V", "/REGULATORS/FB_CM5_5V",
              "/REGULATORS/PG_CM5_5V", "/REGULATORS/RT_CM5_5V",
              "12V_PROTECTED", "POWER_GND"}


def mm(p):
    return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)


def V(x, y):
    return pcbnew.VECTOR2I_MM(x, y)


def main():
    b = pcbnew.LoadBoard(str(BASE))
    for ref in REFS:
        fp = b.FindFootprintByReference(ref)
        if fp is None:
            raise RuntimeError(ref)
        p = fp.GetPosition()
        fp.SetPosition(V(pcbnew.ToMM(p.x) + DX, pcbnew.ToMM(p.y) + DY))

    moved = 0
    for item in b.GetTracks():
        name = item.GetNetname()
        a = mm(item.GetStart()) if not isinstance(item, pcbnew.PCB_VIA) else mm(item.GetPosition())
        z = mm(item.GetEnd()) if not isinstance(item, pcbnew.PCB_VIA) else a
        if name not in LOCAL_NETS:
            continue
        if not (40 <= a[0] <= 100 and 55 <= a[1] <= 100 and
                40 <= z[0] <= 100 and 55 <= z[1] <= 100):
            continue
        if isinstance(item, pcbnew.PCB_VIA):
            item.SetPosition(V(a[0] + DX, a[1] + DY))
        else:
            item.SetStart(V(a[0] + DX, a[1] + DY))
            item.SetEnd(V(z[0] + DX, z[1] + DY))
        moved += 1
    b.Save(str(OUT))
    print(f"saved {OUT}; translated U3 island and {moved} local copper items by ({DX},{DY}) mm")


if __name__ == "__main__":
    main()
