"""Try a pad-field-safe, ordinary-via SATA fanout for Phase 19."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb"
OUT = ROOT / "ACREAGE_PHASE19_SATA_VIA_LOCAL.kicad_pcb"
WIDTH = pcbnew.FromMM(0.15)


def v(x, y): return pcbnew.VECTOR2I_MM(x, y)


def track(board, net, a, b, layer):
    q = pcbnew.PCB_TRACK(board); q.SetStart(v(*a)); q.SetEnd(v(*b))
    q.SetLayer(layer); q.SetWidth(WIDTH); q.SetNet(net); board.Add(q)


def via(board, net, x, y):
    q = pcbnew.PCB_VIA(board); q.SetPosition(v(x, y))
    q.SetWidth(pcbnew.FromMM(0.50)); q.SetDrill(pcbnew.FromMM(0.30))
    q.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); q.SetNet(net); board.Add(q)


def main():
    board = pcbnew.LoadBoard(str(BASE))
    u7 = board.FindFootprintByReference("U7"); j3 = board.FindFootprintByReference("J3")
    if not u7 or not j3: raise RuntimeError("U7/J3 missing")
    u7.SetPosition(v(110, 105)); u7.SetOrientationDegrees(180)
    j3.SetPosition(v(140, 130)); j3.SetOrientationDegrees(90)
    pairs = (("BRIDGE_SATA_RX_P", "60", "3", (108, 98), pcbnew.F_Cu),
             ("BRIDGE_SATA_RX_N", "59", "4", (109.5, 99), pcbnew.F_Cu),
             ("BRIDGE_SATA_TX_P", "57", "1", (111, 98), pcbnew.B_Cu),
             ("BRIDGE_SATA_TX_N", "56", "2", (112.5, 99), pcbnew.B_Cu))
    for name, up, jp, first, layer in pairs:
        net = board.FindNet("/STORAGE/" + name)
        if not net: raise RuntimeError("missing net " + name)
        a = next(p for p in u7.Pads() if str(p.GetNumber()) == up)
        b = next(p for p in j3.Pads() if str(p.GetNumber()) == jp)
        a.SetNet(net); b.SetNet(net)
        pa=(pcbnew.ToMM(a.GetPosition().x),pcbnew.ToMM(a.GetPosition().y))
        pb=(pcbnew.ToMM(b.GetPosition().x),pcbnew.ToMM(b.GetPosition().y))
        track(board, net, pa, first, pcbnew.F_Cu); via(board, net, *first)
        track(board, net, first, pb, layer)
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
