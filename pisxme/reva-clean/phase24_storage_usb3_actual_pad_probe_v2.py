#!/usr/bin/env python3
"""Second disposable USB3 probe: direct B.Cu source fanout, one U12 transition.

All endpoints are read from the saved board's native pads.  The route uses
normal 0.20 mm traces and 0.60/0.30 mm through-vias, with separated source
fanout and connector-side transition lanes.
"""
from pathlib import Path
import argparse
import pcbnew

F, B = pcbnew.F_Cu, pcbnew.B_Cu
NETS = ("CM5_USB3_RX_N", "CM5_USB3_RX_P", "CM5_USB3_TX_N", "CM5_USB3_TX_P")
JOBS = (
    (NETS[0], "128", "16", 68.0, 94.0, 149.0, 133.8),
    (NETS[1], "130", "15", 66.0, 96.0, 149.0, 136.0),
    (NETS[2], "140", "12", 64.0, 98.0, 149.0, 138.2),
    (NETS[3], "142", "11", 62.0, 100.0, 149.0, 140.4),
)


def V(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def xy(pad):
    q = pad.GetPosition()
    return pcbnew.ToMM(q.x), pcbnew.ToMM(q.y)


def track(board, net, a, z, layer):
    item = pcbnew.PCB_TRACK(board)
    item.SetStart(V(*a)); item.SetEnd(V(*z)); item.SetLayer(layer)
    item.SetWidth(pcbnew.FromMM(0.20)); item.SetNet(net)
    item.SetNetCode(net.GetNetCode()); board.Add(item)


def via(board, net, point):
    item = pcbnew.PCB_VIA(board)
    item.SetPosition(V(*point)); item.SetWidth(pcbnew.FromMM(0.60))
    item.SetDrill(pcbnew.FromMM(0.30)); item.SetLayerPair(F, B)
    item.SetNet(net); item.SetNetCode(net.GetNetCode()); board.Add(item)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path); ap.add_argument("output", type=Path)
    args = ap.parse_args()
    board = pcbnew.LoadBoard(str(args.input))
    if board is None: raise SystemExit("cannot load board")
    for item in list(board.GetTracks()):
        if item.GetNetname() in NETS: board.RemoveNative(item)
    j7 = board.FindFootprintByReference("J7")
    u12 = board.FindFootprintByReference("U12")
    if j7 is None or u12 is None: raise SystemExit("missing J7/U12")
    for name, source_num, target_num, lane_x, lane_y, via_x, via_y in JOBS:
        net = board.FindNet(name)
        source = j7.FindPadByNumber(source_num)
        target = u12.FindPadByNumber(target_num)
        if net is None or source is None or target is None:
            raise SystemExit(f"missing native endpoint for {name}")
        s = xy(source); d = xy(target)
        # Source fanout is direct on B.Cu; the long section uses a separated
        # horizontal lane, then returns through one ordinary via near U12.
        track(board, net, s, (lane_x, s[1]), B)
        track(board, net, (lane_x, s[1]), (lane_x, lane_y), B)
        track(board, net, (lane_x, lane_y), (via_x, via_y), B)
        via(board, net, (via_x, via_y))
        track(board, net, (via_x, via_y), d, F)
    board.BuildListOfNets(); board.Save(str(args.output)); print(args.output)


if __name__ == "__main__": main()
