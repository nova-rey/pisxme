"""V163: co-author XTAL_OUT and upper REFCLK escapes from V160."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / 'PHASE24_RTL9210B_LOWER_1V1_HANDOFF_V160.kicad_pcb'
OUT = HERE / 'PHASE24_RTL9210B_REFCLK_SUPPORT_V163.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p): return (round(p.x / 1e6, 3), round(p.y / 1e6, 3))
def tr(board, net, layer, a, z, width=0.2):
    q = pcbnew.PCB_TRACK(board)
    q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer)
    q.SetWidth(pcbnew.FromMM(width)); q.SetNet(net); q.SetNetCode(net.GetNetCode())
    board.Add(q)
def via(board, net, a):
    q = pcbnew.PCB_VIA(board); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(0.6))
    q.SetDrill(pcbnew.FromMM(0.3)); q.SetLayerPair(F, B)
    q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)
def remove_net(board, name):
    for item in list(board.GetTracks()):
        if item.GetNetname() == name:
            board.RemoveNative(item)
def main():
    board = pcbnew.LoadBoard(str(BASE))
    for name in ('XTAL_OUT',): remove_net(board, name)
    xt = board.FindNet('XTAL_OUT')
    # Move XTAL_OUT below the exposed-pad lower edge, clear of the REFCLK pair.
    tr(board, xt, F, (95.6, 73.95), (95.6, 71.8))
    via(board, xt, (95.6, 71.8))
    tr(board, xt, B, (95.6, 71.8), (110.5, 71.8))
    via(board, xt, (110.5, 71.8))
    tr(board, xt, F, (110.5, 71.8), (110.5, 76.8))
    tr(board, xt, F, (110.5, 76.8), (109.7, 75.8))
    tr(board, xt, F, (109.7, 75.8), (111.4, 78.0))
    p, n = board.FindNet('REFCLK_P'), board.FindNet('REFCLK_N')
    # Separate the source escapes on F.Cu, then carry the pair on B.Cu.
    tr(board, p, F, (98.4, 73.95), (98.4, 72.6)); via(board, p, (98.4, 72.6))
    tr(board, p, B, (98.4, 72.6), (137.75, 72.6)); via(board, p, (137.75, 72.6))
    tr(board, p, F, (137.75, 72.6), (137.75, 62.725)); via(board, p, (137.75, 62.725))
    tr(board, p, F, (137.75, 62.725), (137.25, 62.725))
    tr(board, n, F, (98.8, 73.95), (98.8, 73.2)); via(board, n, (98.8, 73.2))
    tr(board, n, B, (98.8, 73.2), (136.25, 73.2)); via(board, n, (136.25, 73.2))
    tr(board, n, F, (136.25, 73.2), (136.25, 62.0)); via(board, n, (136.25, 62.0))
    tr(board, n, F, (136.25, 62.0), (136.75, 62.725))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)
if __name__ == '__main__': main()
