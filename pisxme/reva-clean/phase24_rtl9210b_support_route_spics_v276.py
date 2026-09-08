"""V276: test an F.Cu outer SPICS corridor over the retained V274 basis."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SUPPORT_ROUTE_RAILS_V274.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SUPPORT_ROUTE_SPICS_V276.kicad_pcb"
F = pcbnew.F_Cu


def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def tr(board, net, a, z):
    item = pcbnew.PCB_TRACK(board)
    item.SetStart(P(*a)); item.SetEnd(P(*z)); item.SetLayer(F)
    item.SetWidth(pcbnew.FromMM(0.20)); item.SetNet(net)
    item.SetNetCode(net.GetNetCode()); board.Add(item)


def main():
    board = pcbnew.LoadBoard(str(BASE))
    net = board.FindNet("SPICS")
    # Actual pads: U1.24=(98.8,58.05), U2.1=(83.3,70.0).
    # Keep the route outside the retained crystal B.Cu trunks.
    path = [(98.8, 58.05), (98.8, 57.0), (82.0, 57.0),
            (82.0, 70.0), (83.3, 70.0)]
    for a, z in zip(path, path[1:]):
        tr(board, net, a, z)
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__":
    main()
