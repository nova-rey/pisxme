"""Extract authoritative CM5/J7 and EDAC/J2 into a disposable fixture base."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
src = pcbnew.LoadBoard(str(ROOT / "ACREAGE_PCIE_PHASE16.kicad_pcb"))
j7 = pcbnew.FOOTPRINT(src.FindFootprintByReference("J7"))
j2 = pcbnew.FOOTPRINT(src.FindFootprintByReference("J2"))
tracks = list(src.GetTracks())
zones = list(src.Zones())
for item in tracks:
    src.Remove(item)
for item in zones:
    src.Remove(item)
src.DeleteAllFootprints()
src.Add(j7)
src.Add(j2)
out = ROOT / "SP3019_ETHERNET_FIXTURE_BASE.kicad_pcb"
src.Save(str(out))
print(out)
