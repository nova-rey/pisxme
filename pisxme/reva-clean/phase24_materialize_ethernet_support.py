"""Materialize schematic-owned Ethernet support on a disposable PCB.

No copper is authored here.  This is the parity boundary: footprints and
actual pad net ownership are copied from the saved schematic netlist before
any support routing is attempted.
"""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_SELECTED_MACRO_PARENT_20260905.kicad_pcb"
OUT = R / "PHASE24_ETHERNET_SUPPORT_MATERIALIZED.kicad_pcb"
LIB = R / "PiSXMe_RevA_Clean.pretty"

PARTS = {
    "C48": ("C_0603_1608Metric", {"1": "/ETHERNET/ETH_CT1", "2": "/ETHERNET/ETH_CT_BRANCH_1"}, (23, 115)),
    "R26": ("R_0402_1005Metric", {"1": "/ETHERNET/ETH_CT_BRANCH_1", "2": "/ETHERNET/ETH_CT_COMMON"}, (28, 115)),
    "C49": ("C_0603_1608Metric", {"1": "/ETHERNET/ETH_CT2", "2": "/ETHERNET/ETH_CT_BRANCH_2"}, (23, 121)),
    "R27": ("R_0402_1005Metric", {"1": "/ETHERNET/ETH_CT_BRANCH_2", "2": "/ETHERNET/ETH_CT_COMMON"}, (28, 121)),
    "C50": ("C_0603_1608Metric", {"1": "/ETHERNET/ETH_CT3", "2": "/ETHERNET/ETH_CT_BRANCH_3"}, (23, 127)),
    "R28": ("R_0402_1005Metric", {"1": "/ETHERNET/ETH_CT_BRANCH_3", "2": "/ETHERNET/ETH_CT_COMMON"}, (28, 127)),
    "C51": ("C_0603_1608Metric", {"1": "/ETHERNET/ETH_CT4", "2": "/ETHERNET/ETH_CT_BRANCH_4"}, (23, 133)),
    "R29": ("R_0402_1005Metric", {"1": "/ETHERNET/ETH_CT_BRANCH_4", "2": "/ETHERNET/ETH_CT_COMMON"}, (28, 133)),
    "C52": ("C_1206_3216Metric", {"1": "/ETHERNET/ETH_CT_COMMON", "2": "GBE_SHIELD"}, (17, 121)),
    "R30": ("R_0402_1005Metric", {"1": "ETH_LEDY", "2": "/ETHERNET/GBE_LED_Y_K"}, (17, 127)),
    "R31": ("R_0402_1005Metric", {"1": "ETH_LEDG", "2": "/ETHERNET/GBE_LED_G_K"}, (17, 133)),
}


def main():
    board = pcbnew.LoadBoard(str(BASE))
    io = pcbnew.PCB_IO_KICAD_SEXPR()
    names = sorted({net for _, mapping, _ in PARTS.values() for net in mapping.values()})
    nets = {}
    for name in names:
        net = board.FindNet(name)
        if net is None:
            net = pcbnew.NETINFO_ITEM(board, name)
            net.SetNetCode(board.GetNetCount() + 1)
            board.Add(net)
        nets[name] = net
    for ref, (lib, mapping, pos) in PARTS.items():
        old = board.FindFootprintByReference(ref)
        if old is not None:
            board.Remove(old)
        fp = io.FootprintLoad(str(LIB), lib)
        fp.SetReference(ref)
        fp.SetLayer(pcbnew.B_Cu)
        fp.SetPosition(pcbnew.VECTOR2I_MM(*pos))
        board.Add(fp)
        bottom_layers = pcbnew.LSET()
        bottom_layers.AddLayer(pcbnew.B_Cu)
        bottom_layers.AddLayer(pcbnew.B_Mask)
        bottom_layers.AddLayer(pcbnew.B_Paste)
        for pad in fp.Pads():
            net = nets[mapping[str(pad.GetNumber())]]
            pad.SetLayerSet(bottom_layers)
            pad.SetNet(net)
            pad.SetNetCode(net.GetNetCode())
    board.Save(str(OUT))
    print(OUT)


if __name__ == "__main__":
    main()
