"""Create the first local SATA corridor from the validated Phase 18 board."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb"
OUT = ROOT / "ACREAGE_PHASE19_SATA_LOCAL.kicad_pcb"
WIDTH = pcbnew.FromMM(0.15)  # conservative prototype width; stack receipt owns field solve


def add_track(board, net, a, b, layer=pcbnew.F_Cu):
    t = pcbnew.PCB_TRACK(board)
    t.SetStart(pcbnew.VECTOR2I_MM(*a)); t.SetEnd(pcbnew.VECTOR2I_MM(*b))
    t.SetLayer(layer); t.SetWidth(WIDTH); t.SetNet(net); board.Add(t)


def main():
    board = pcbnew.LoadBoard(str(BASE))
    u7 = board.FindFootprintByReference("U7")
    j3 = board.FindFootprintByReference("J3")
    if not u7 or not j3: raise RuntimeError("U7/J3 missing")
    u7.SetPosition(pcbnew.VECTOR2I_MM(110, 105)); u7.SetOrientationDegrees(180)
    # Outboard acreage placement: preserve U7/USB3 and keep the 2280 body
    # clear of the PCIe fanout and nearby connector hardware.
    j3.SetPosition(pcbnew.VECTOR2I_MM(140, 130)); j3.SetOrientationDegrees(0)
    pairs = (("BRIDGE_SATA_TX_P", "57", "1"),
             ("BRIDGE_SATA_TX_N", "56", "2"),
             ("BRIDGE_SATA_RX_P", "60", "3"),
             ("BRIDGE_SATA_RX_N", "59", "4"))
    for name, up, jp in pairs:
        net = board.FindNet("/STORAGE/" + name)
        if not net: raise RuntimeError("missing net " + name)
        a = next(p for p in u7.Pads() if str(p.GetNumber()) == up)
        b = next(p for p in j3.Pads() if str(p.GetNumber()) == jp)
        a.SetNet(net); b.SetNet(net)
        add_track(board, net,
                  (pcbnew.ToMM(a.GetPosition().x), pcbnew.ToMM(a.GetPosition().y)),
                  (pcbnew.ToMM(b.GetPosition().x), pcbnew.ToMM(b.GetPosition().y)))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
