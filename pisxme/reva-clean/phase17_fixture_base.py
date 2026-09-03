"""Extract authoritative CM5/J7 and EDAC/J2 into a disposable fixture base."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
src = pcbnew.LoadBoard(str(ROOT / "ACREAGE_PCIE_PHASE16.kicad_pcb"))
j7_source = pcbnew.FOOTPRINT(src.FindFootprintByReference("J7"))
j2_source = pcbnew.FOOTPRINT(src.FindFootprintByReference("J2"))
tracks = list(src.GetTracks())
zones = list(src.Zones())
for item in tracks:
    src.Remove(item)
for item in zones:
    src.Remove(item)
src.DeleteAllFootprints()
# Preserve the exact CM5 Ethernet pad coordinates and names while removing
# unrelated CM5 pads from this disposable launch fixture. The full J7
# authority remains in the clean project; this isolates the Ethernet routing
# proof from unrelated native connector escape geometry.
j7 = pcbnew.FOOTPRINT(j7_source)
j2 = pcbnew.FOOTPRINT(j2_source)
ethernet_j7_pads = {"3", "4", "5", "6", "9", "10", "11", "12"}
for pad in list(j7.Pads()):
    if pad.GetNumber() not in ethernet_j7_pads:
        j7.Remove(pad)
src.Add(j7)
src.Add(j2)
out = ROOT / "SP3019_ETHERNET_FIXTURE_BASE.kicad_pcb"
src.Save(str(out))
print(out)
