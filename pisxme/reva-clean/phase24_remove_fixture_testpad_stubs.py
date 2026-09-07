"""Remove only copper stubs whose endpoint was a disposable TP1..TP8 pad."""
from pathlib import Path
import pcbnew

BASE = Path("PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V4_NO_TESTPADS.kicad_pcb")
ORIGINAL = Path("PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V3.kicad_pcb")
OUT = Path("PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V5_NO_FIXTURE_STUBS.kicad_pcb")

def main():
    old = pcbnew.LoadBoard(str(ORIGINAL))
    points = set()
    for fp in old.GetFootprints():
        if fp.GetReference() in {f"TP{i}" for i in range(1, 9)}:
            points.update((p.GetPosition().x, p.GetPosition().y) for p in fp.Pads())
    board = pcbnew.LoadBoard(str(BASE))
    removed = 0
    for item in list(board.GetTracks()):
        if not isinstance(item, pcbnew.PCB_TRACK):
            continue
        ends = [(item.GetStart().x, item.GetStart().y), (item.GetEnd().x, item.GetEnd().y)]
        if any(p in points for p in ends):
            board.Remove(item)
            removed += 1
    board.BuildListOfNets()
    board.Save(str(OUT))
    print(f"removed {removed} fixture stubs -> {OUT}")

if __name__ == "__main__":
    main()
