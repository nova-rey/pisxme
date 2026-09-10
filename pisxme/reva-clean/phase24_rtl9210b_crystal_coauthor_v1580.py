"""V1580: co-author both crystal nets in the frozen 0-degree west pocket."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
base = H / "PHASE24_RTL9210B_RSET_WEST_V1508.kicad_pcb"
out = H / "PHASE24_RTL9210B_CRYSTAL_COAUTHOR_V1580.kicad_pcb"
b = pcbnew.LoadBoard(str(base)); F = pcbnew.F_Cu
V = lambda x, y: pcbnew.VECTOR2I_MM(float(x), float(y))
for pad in b.FindFootprintByReference("U1").Pads():
    pad.SetLocalClearance(pcbnew.FromMM(0.15))
for net_name in ("XTAL_IN", "XTAL_OUT"):
    for item in list(b.GetTracks()):
        if item.GetNetname() == net_name: b.RemoveNative(item)

def tr(name, a, z, width=.20):
    n = b.FindNet(name); t = pcbnew.PCB_TRACK(b)
    t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(F); t.SetWidth(pcbnew.FromMM(width))
    t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)

# Separate, monotonic F.Cu lanes: XTAL_IN uses y=65.2; XTAL_OUT uses y=69.0.
tr("XTAL_IN", (94.05,67.2), (92.8,67.2))
tr("XTAL_IN", (92.8,67.2), (92.8,65.2))
tr("XTAL_IN", (92.8,65.2), (88.0,65.2))
tr("XTAL_IN", (88.0,65.2), (88.0,62.0))
tr("XTAL_IN", (88.0,62.0), (88.0,59.0))
tr("XTAL_OUT", (94.05,67.6), (93.6,67.6))
tr("XTAL_OUT", (93.6,67.6), (93.6,69.0))
tr("XTAL_OUT", (93.6,69.0), (91.0,69.0))
tr("XTAL_OUT", (91.0,69.0), (91.0,62.0))
tr("XTAL_OUT", (91.0,62.0), (90.5,60.5))
tr("XTAL_OUT", (90.5,60.5), (89.4,59.0))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
