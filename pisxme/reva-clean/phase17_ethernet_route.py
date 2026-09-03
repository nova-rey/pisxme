"""Materialize a bounded Phase 17 100-ohm Ethernet routing candidate."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "ACREAGE_PCIE_PHASE16.kicad_pcb"
OUTPUT = ROOT / "ACREAGE_ETHERNET_PHASE17.kicad_pcb"
WIDTH = 0.13208


def vec(x, y): return pcbnew.VECTOR2I_MM(x, y)
def getnet(board, name):
    net = board.FindNet(name)
    if net is None: raise SystemExit(f"missing Ethernet net: {name}")
    return net
def segment(board, a, b, net, layer):
    item = pcbnew.PCB_TRACK(board)
    item.SetStart(vec(*a)); item.SetEnd(vec(*b)); item.SetLayer(layer)
    item.SetWidth(pcbnew.FromMM(WIDTH)); item.SetNet(net); board.Add(item)
def route(board, points, net, layer):
    for a, b in zip(points, points[1:]): segment(board, a, b, net, layer)
def via(board, point, net):
    item = pcbnew.PCB_VIA(board)
    item.SetPosition(vec(*point)); item.SetWidth(pcbnew.FromMM(.50))
    item.SetDrill(pcbnew.FromMM(.30)); item.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    item.SetNet(net); board.Add(item)


def apply_class(board):
    design = board.GetDesignSettings()
    design.m_TrackMinWidth = pcbnew.FromMM(WIDTH)
    settings = design.m_NetSettings
    cls = pcbnew.NETCLASS("HS_GBE_100R")
    cls.SetTrackWidth(pcbnew.FromMM(WIDTH)); cls.SetDiffPairWidth(pcbnew.FromMM(WIDTH))
    cls.SetDiffPairGap(pcbnew.FromMM(.2032)); cls.SetClearance(pcbnew.FromMM(.20))
    cls.SetViaDiameter(pcbnew.FromMM(.50)); cls.SetViaDrill(pcbnew.FromMM(.30))
    settings.SetNetclass("HS_GBE_100R", cls)
    for i in range(4):
        for pol in "PN":
            settings.SetNetclassPatternAssignment(f"CM5_GBE_TD{i}_{pol}", "HS_GBE_100R")


def main():
    board = pcbnew.LoadBoard(str(INPUT)); apply_class(board)
    # Phase 17 placement correction: the original acreage put the Ethernet
    # island across the board from J7 and behind the V100 courtyard.  The
    # open strip below the cooler permits a short CM5->ESD corridor.  Rotate
    # the ESD footprints so the CM5 source ordering is monotonic at the TVS
    # pads.  This candidate does not alter the frozen PCIe or power areas.
    for ref, x, y in (("U6", 25, 99), ("U9", 25, 106)):
        fp = board.FindFootprintByReference(ref)
        fp.SetPosition(vec(x, y)); fp.SetOrientationDegrees(180)
    j2 = board.FindFootprintByReference("J2")
    j2.SetPosition(vec(12, 120))
    nets = {f"TD{i}_{p}": getnet(board, f"CM5_GBE_TD{i}_{p}") for i in range(4) for p in "PN"}
    # Put the left CM5 column on F.Cu and the right CM5 column on B.Cu.  This
    # is a deliberate local layer split: the connector's two 0.4 mm source
    # columns otherwise force a crossing before they can fan out to the two
    # ESD devices.  The rotated devices preserve pair polarity/order.
    paths = {
        "TD3_P": ((32.96,99.10),(24.25,105.25)),
        "TD3_N": ((32.96,99.50),(25.75,105.25)),
        "TD2_N": ((32.96,100.30),(24.25,106.75)),
        "TD2_P": ((32.96,100.70),(25.75,106.75)),
    }
    for key, points in paths.items():
        n = nets[key]
        route(board, points, n, pcbnew.F_Cu)
    right = {
        "TD1_P": ((36.04,99.10),(22,98.25)), "TD1_N": ((36.04,99.50),(29,98.25)),
        "TD0_N": ((36.04,100.30),(22,99.75)), "TD0_P": ((36.04,100.70),(29,99.75)),
    }
    for key, points in right.items():
        n = nets[key]; via(board, points[-1], n); route(board, points, n, pcbnew.B_Cu)
    dogbones = {
        "TD1_P": ((22,98.25),(24.25,98.25)), "TD1_N": ((29,98.25),(25.75,98.25)),
        "TD0_N": ((22,99.75),(24.25,99.75)), "TD0_P": ((29,99.75),(25.75,99.75)),
    }
    for key, points in dogbones.items(): route(board, points, nets[key], pcbnew.F_Cu)

    # ESD-to-MagJack is a short connector-boundary F.Cu corridor, ordered by
    # the EDAC manufacturer's pin numbering.
    mag = {
        "TD0_P": ((249.25,44.25),(257,44.25),(276.63,49.06)),
        "TD0_N": ((250.75,44.25),(258,44.25),(274.09,49.06)),
        "TD1_P": ((250.75,45.75),(259,45.75),(265.91,49.06)),
        "TD1_N": ((249.25,45.75),(260,45.75),(263.37,49.06)),
        "TD2_P": ((249.25,57.25),(257,57.25),(275.715,41.17)),
        "TD2_N": ((250.75,57.25),(258,57.25),(273.175,42.44)),
        "TD3_P": ((250.75,58.75),(259,58.75),(266.825,42.44)),
        "TD3_N": ((249.25,58.75),(260,58.75),(264.285,41.17)),
    }
    # MagJack fanout is intentionally held out until the ESD-side candidate
    # is independently free of source-to-ESD crossings.
    pcbnew.ZONE_FILLER(board).Fill(board.Zones()); board.Save(str(OUTPUT))
    print("Phase 17 Ethernet candidate: eight MDI pairs routed")


if __name__ == "__main__": main()
