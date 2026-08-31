"""Materialize the reviewed Phase 16 Gen2 x1 PCIe launch recipe."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "ACREAGE_U5_VOUT_PHASE15.kicad_pcb"
OUTPUT = ROOT / "ACREAGE_PCIE_PHASE16.kicad_pcb"
WIDTH = 0.13208


def v(x, y): return pcbnew.VECTOR2I_MM(x, y)
def net(board, name):
    n = board.FindNet(name)
    if n is None: raise SystemExit(f"missing net {name}")
    return n
def segment(board, a, b, n, layer):
    t = pcbnew.PCB_TRACK(board); t.SetStart(v(*a)); t.SetEnd(v(*b))
    t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(WIDTH)); t.SetNet(n); board.Add(t)
def route(board, points, n, layer):
    for a, b in zip(points, points[1:]): segment(board, a, b, n, layer)
def via(board, point, n):
    x = pcbnew.PCB_VIA(board); x.SetPosition(v(*point)); x.SetWidth(pcbnew.FromMM(.50))
    x.SetDrill(pcbnew.FromMM(.30)); x.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    x.SetNet(n); board.Add(x)


def return_via(board, point, gnd):
    """Place a functional local reference transition outside connector pads."""
    via(board, point, gnd)


def apply_pcie_class(board):
    """Materialize the Phase 13 released 90-ohm outer-layer rules."""
    design = board.GetDesignSettings()
    # The generated acreage baseline carries KiCad's 0.20 mm global default;
    # the released JLC six-layer basis permits the 0.13208 mm PCIe class.
    design.m_TrackMinWidth = pcbnew.FromMM(0.13208)
    settings = board.GetDesignSettings().m_NetSettings
    cls = pcbnew.NETCLASS("HS_PCIE_90R")
    cls.SetTrackWidth(pcbnew.FromMM(0.13208))
    cls.SetDiffPairWidth(pcbnew.FromMM(0.13208))
    cls.SetDiffPairGap(pcbnew.FromMM(0.2032))
    cls.SetClearance(pcbnew.FromMM(0.20))
    cls.SetViaDiameter(pcbnew.FromMM(0.50))
    cls.SetViaDrill(pcbnew.FromMM(0.30))
    settings.SetNetclass("HS_PCIE_90R", cls)
    for name in ("/CORE_CM5/CM5_PER0_P", "/CORE_CM5/CM5_PER0_N",
                 "/CORE_CM5/CM5_REFCLK_P", "/CORE_CM5/CM5_REFCLK_N",
                 "/CORE_CM5/CM5_PET0_P", "/CORE_CM5/CM5_PET0_N",
                 "/V100_PCIE/V100_PET0_P", "/V100_PCIE/V100_PET0_N"):
        settings.SetNetclassPatternAssignment(name, "HS_PCIE_90R")


def main():
    b = pcbnew.LoadBoard(str(INPUT))
    apply_pcie_class(b)
    for ref, point in (("C1", (82,106)), ("C2", (82,110))):
        f=b.FindFootprintByReference(ref); f.SetPosition(v(*point)); f.SetOrientationDegrees(0)
    per_p=net(b,"/CORE_CM5/CM5_PER0_P"); per_n=net(b,"/CORE_CM5/CM5_PER0_N")
    ref_p=net(b,"/CORE_CM5/CM5_REFCLK_P"); ref_n=net(b,"/CORE_CM5/CM5_REFCLK_N")
    perst=net(b,"/CORE_CM5/CM5_PERST"); pet_p=net(b,"/CORE_CM5/CM5_PET0_P")
    pet_n=net(b,"/CORE_CM5/CM5_PET0_N"); vpet_p=net(b,"/V100_PCIE/V100_PET0_P")
    vpet_n=net(b,"/V100_PCIE/V100_PET0_N")
    gnd=net(b,"/CORE_CM5/POWER_GND")

    # PER0: F.Cu pair, no signal vias.  Launches approach the top connector
    # row from above; the reviewed asymmetric dogbones preserve pad spacing.
    route(b,[(70.04,101.50),(80.50,101.50),(80.50,82.00),(165,82),(173.495,82),(173.495,84.285)],per_p,pcbnew.F_Cu)
    route(b,[(70.04,101.90),(81.00,101.90),(81.00,82.40),(165,82.40),(172.225,82.40),(172.225,84.285)],per_n,pcbnew.F_Cu)

    # CM5 transmitter-side PET0 coupling, with no copper between capacitor
    # pad 1 and pad 2 except through the component itself.
    route(b,[(70.04,102.70),(76,102.70),(81.05,106)],pet_p,pcbnew.F_Cu)
    route(b,[(70.04,103.10),(76,103.10),(81.05,110)],pet_n,pcbnew.F_Cu)
    via(b,(84,106),vpet_p); via(b,(84,110),vpet_n)
    route(b,[(82.95,106),(84,106)],vpet_p,pcbnew.F_Cu)
    route(b,[(82.95,110),(84,110)],vpet_n,pcbnew.F_Cu)
    via(b,(175.40,92.54),vpet_p); via(b,(174.13,92.54),vpet_n)
    route(b,[(84,106),(100,106),(170,106),(170,85),(175.40,85),(175.40,92.54)],vpet_p,pcbnew.B_Cu)
    route(b,[(84,110),(100,110),(180,110),(180,100),(174.13,100),(174.13,92.54)],vpet_n,pcbnew.B_Cu)
    route(b,[(175.40,92.54),(174.765,91.905)],vpet_p,pcbnew.F_Cu)
    route(b,[(174.13,92.54),(173.495,91.905)],vpet_n,pcbnew.F_Cu)

    # Local reference transitions are deliberately outside the dense SMD
    # fields.  They are paired around each differential launch and are tied
    # to the solid GND reference layers by ordinary through vias.
    for point in ((75,97), (75,104), (86,104), (86,112)):
        return_via(b, point, gnd)

    # Common-clock REFCLK: symmetric CM5 dogbones and B.Cu corridor.
    via(b,(72.20,99.40),ref_p); via(b,(72.20,100.20),ref_n)
    route(b,[(70.04,100.30),(72.20,99.40)],ref_p,pcbnew.F_Cu)
    route(b,[(70.04,100.70),(72.20,100.20)],ref_n,pcbnew.F_Cu)
    via(b,(167.78,88.73),ref_p); via(b,(167.78,91.27),ref_n)
    route(b,[(72.20,99.40),(85,94),(100,76),(158,76),(167.78,88.73)],ref_p,pcbnew.B_Cu)
    route(b,[(72.20,100.20),(86,94.8),(100,80),(158,80),(167.78,91.27)],ref_n,pcbnew.B_Cu)
    route(b,[(167.78,88.73),(167.145,89.365)],ref_p,pcbnew.F_Cu)
    route(b,[(167.78,91.27),(167.145,90.635)],ref_n,pcbnew.F_Cu)

    # PERST: low-speed direct control, deliberately kept out of the high-speed
    # pair corridor and without a high-speed stub.
    route(b,[(66.96,100.30),(64,100.30),(64,150),(152.54,150),(152.54,88.73)],perst,pcbnew.F_Cu)
    route(b,[(152.54,88.73),(153.175,89.365)],perst,pcbnew.F_Cu)

    # Return-via locations remain a separate reviewed transition task; no
    # unproven via is placed into the dense CM5/SXM2 fields in this candidate.
    pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUTPUT))
    print("Phase 16 PCIe candidate: reviewed dogbone/transition recipe")


if __name__ == "__main__": main()
