"""V186: join U1.20 into the proven V185 RTL_3V3 B.Cu rail."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_RTL3V3_U134_C3_V185.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_RTL3V3_U134_PAD20_V186.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu


def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))


def main():
    board = pcbnew.LoadBoard(str(BASE))
    net = board.FindNet("RTL_3V3")
    track = pcbnew.PCB_TRACK(board)
    track.SetStart(P(100.4, 58.05)); track.SetEnd(P(100.4, 56.5))
    track.SetLayer(F); track.SetWidth(pcbnew.FromMM(0.20))
    track.SetNet(net); track.SetNetCode(net.GetNetCode()); board.Add(track)
    via = pcbnew.PCB_VIA(board); via.SetPosition(P(100.4, 56.5))
    via.SetWidth(pcbnew.FromMM(0.60)); via.SetDrill(pcbnew.FromMM(0.30))
    via.SetLayerPair(F, B); via.SetNet(net); via.SetNetCode(net.GetNetCode())
    board.Add(via)
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
