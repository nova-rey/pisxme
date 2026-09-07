"""Add SPISO/SPICS using separated B.Cu lanes to the native V24 source field."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_ROTATE_U1_90_MIXED_V24.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SPI_SOURCE_ALLOCATOR_V27.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def track(board, net, layer, a, z):
    q = pcbnew.PCB_TRACK(board)
    q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer)
    q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode())
    board.Add(q)

def via(board, net, xy):
    q = pcbnew.PCB_VIA(board)
    q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(0.60))
    q.SetDrill(pcbnew.FromMM(0.30)); q.SetLayerPair(F, B)
    q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)

def remove_net(board, name):
    for item in list(board.GetTracks()):
        if item.GetNetname() == name:
            board.RemoveNative(item)

def main():
    board = pcbnew.LoadBoard(str(BASE))
    remove_net(board, "SPISO")
    remove_net(board, "SPICS")

    # SPISO: rightward source dogbone, then isolated upper B.Cu lane to U2.2.
    n = board.FindNet("SPISO")
    track(board, n, F, (99.2, 66.05), (99.2, 62.0))
    track(board, n, F, (99.2, 62.0), (102.4, 62.0))
    via(board, n, (102.4, 62.0))
    track(board, n, B, (102.4, 62.0), (83.0, 62.0))
    track(board, n, B, (83.0, 62.0), (83.0, 78.0))
    via(board, n, (83.0, 78.0))
    track(board, n, F, (83.0, 78.0), (83.0, 80.0))

    # SPICS: left source departure and a separate higher B.Cu lane to U2.1.
    n = board.FindNet("SPICS")
    track(board, n, F, (98.8, 66.05), (98.8, 57.5))
    via(board, n, (98.8, 57.5))
    track(board, n, B, (98.8, 57.5), (81.8, 57.5))
    track(board, n, B, (81.8, 57.5), (81.8, 78.0))
    via(board, n, (81.8, 78.0))
    track(board, n, F, (81.8, 78.0), (81.8, 80.0))

    board.BuildListOfNets()
    board.Save(str(OUT))
    print(OUT)

if __name__ == "__main__":
    main()
