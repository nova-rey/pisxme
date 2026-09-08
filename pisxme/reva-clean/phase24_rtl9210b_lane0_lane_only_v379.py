"""V379: exact V328 lane-0 geometry on the V372 support base.

This is a disposable isolation test.  RTL_1V1 and XTAL_OUT copper are removed
so the lane result is not confused with known support-route channel conflicts.
The RX source and connector launches are copied geometrically from the native
clean V328 trial; no expected-connectivity edges are synthesized.
"""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_SUPPORT_XTALOUT_DIRECT_V372.kicad_pcb"
SRC = H / "PHASE24_RTL9210B_LANE0_ROUTE_V328.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_LANE0_LANE_ONLY_V379.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def seg(board, net, layer, a, z):
    t = pcbnew.PCB_TRACK(board)
    t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(layer)
    t.SetWidth(W); t.SetNet(net); t.SetNetCode(net.GetNetCode())
    board.Add(t)

def via(board, net, q):
    v = pcbnew.PCB_VIA(board)
    v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(0.60))
    v.SetDrill(pcbnew.FromMM(0.30)); v.SetLayerPair(F, B)
    v.SetNet(net); v.SetNetCode(net.GetNetCode()); board.Add(v)

def main():
    board = pcbnew.LoadBoard(str(BASE))
    source = pcbnew.LoadBoard(str(SRC))
    for item in list(board.GetTracks()):
        if item.GetNetname() in ("RTL_1V1", "XTAL_OUT"):
            board.RemoveNative(item)
    for zone in list(board.Zones()):
        if zone.GetNetname() == "RTL_1V1":
            board.RemoveNative(zone)
    for item in source.GetTracks():
        if item.GetNetname() in ("LANE0_TXP", "LANE0_TXN"):
            board.Add(item.Duplicate())

    # Exact V328 RXP launch: source escape, B.Cu trunk, connector return.
    n = board.FindNet("LANE0_RXP")
    seg(board, n, F, (109.95, 60.4), (110.6, 60.4))
    seg(board, n, F, (110.6, 60.4), (110.6, 66.5))
    via(board, n, (110.6, 66.5))
    seg(board, n, B, (110.6, 66.5), (132.0, 66.5))
    via(board, n, (132.0, 66.5))
    seg(board, n, F, (132.0, 66.5), (134.25, 66.5))
    seg(board, n, F, (134.25, 66.5), (134.25, 62.725))

    # Exact V328 RXN launch, including its native stagger and return.
    n = board.FindNet("LANE0_RXN")
    seg(board, n, F, (109.95, 60.0), (111.5, 60.0))
    seg(board, n, F, (111.5, 60.0), (111.5, 64.5))
    via(board, n, (111.5, 64.5))
    seg(board, n, B, (111.5, 64.5), (132.0, 64.5))
    via(board, n, (132.0, 64.5))
    seg(board, n, F, (132.0, 64.5), (133.75, 64.5))
    seg(board, n, F, (133.75, 64.5), (133.75, 62.725))
    board.BuildListOfNets()
    board.Save(str(OUT))
    print(OUT)

if __name__ == "__main__":
    main()
