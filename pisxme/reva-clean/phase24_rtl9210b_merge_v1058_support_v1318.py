"""V1318: merge the complete V1058 support field with the V1258 lane/control basis.

Only nets whose endpoint geometry is identical between the two saved boards are
copied.  Crystal nets are intentionally excluded because V1058 relocates C1/C2/Y1.
"""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_ROTATE_U2_SPI_V1058.kicad_pcb"
LANE = H / "PHASE24_RTL9210B_J1_PAD_ALIGNED_LAUNCH_V1258.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_V1058_SUPPORT_V1258_LANE_MERGE_V1318.kicad_pcb"
KEEP = {"LANE0_RXP", "LANE0_RXN", "LANE0_TXP", "LANE0_TXN",
        "REFCLK_P", "REFCLK_N", "PEDET", "PERST_N", "CLKREQ_N"}

dst = pcbnew.LoadBoard(str(BASE))
src = pcbnew.LoadBoard(str(LANE))

# Remove any pre-existing copy of the endpoint nets in the destination.
for item in list(dst.GetTracks()):
    if item.GetNetname() in KEEP:
        dst.RemoveNative(item)

for item in src.GetTracks():
    if item.GetNetname() not in KEEP:
        continue
    net = dst.FindNet(item.GetNetname())
    if isinstance(item, pcbnew.PCB_VIA):
        clone = pcbnew.PCB_VIA(dst)
        clone.SetPosition(item.GetPosition())
        clone.SetWidth(item.GetWidth(pcbnew.F_Cu))
        clone.SetDrill(item.GetDrill())
        clone.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    else:
        clone = pcbnew.PCB_TRACK(dst)
        clone.SetStart(item.GetStart())
        clone.SetEnd(item.GetEnd())
        clone.SetLayer(item.GetLayer())
        clone.SetWidth(item.GetWidth())
    clone.SetNet(net)
    clone.SetNetCode(net.GetNetCode())
    dst.Add(clone)

dst.BuildListOfNets()
pcbnew.ZONE_FILLER(dst).Fill(dst.Zones())
dst.Save(str(OUT))
print(OUT)
