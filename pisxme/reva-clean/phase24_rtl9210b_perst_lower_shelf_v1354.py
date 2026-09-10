"""V1354: co-author CLKREQ source and PERST on separated lower shelves."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / 'PHASE24_RTL9210B_CLKREQ_OVERPASS_V1347.kicad_pcb'
OUT = H / 'PHASE24_RTL9210B_PERST_LOWER_SHELF_V1354.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def track(board, net, layer, a, z):
    t = pcbnew.PCB_TRACK(board); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(layer)
    t.SetWidth(W); t.SetNet(net); t.SetNetCode(net.GetNetCode()); board.Add(t)
def via(board, net, xy):
    v = pcbnew.PCB_VIA(board); v.SetPosition(P(*xy)); v.SetWidth(pcbnew.FromMM(0.60))
    v.SetDrill(pcbnew.FromMM(0.30)); v.SetLayerPair(F, B); v.SetNet(net); v.SetNetCode(net.GetNetCode()); board.Add(v)
def clear_net(board, name):
    for item in list(board.GetTracks()):
        if item.GetNetname() == name: board.RemoveNative(item)

board = pcbnew.LoadBoard(str(BASE))
clk = board.FindNet('CLKREQ_N'); per = board.FindNet('PERST_N')
assert clk is not None and per is not None
clear_net(board, 'CLKREQ_N')
clear_net(board, 'PERST_N')

# CLKREQ source: move its first transition left so U1.14 can descend cleanly.
track(board, clk, F, (99.6, 73.95), (99.6, 75.0))
track(board, clk, F, (99.6, 75.0), (98.8, 75.0))
track(board, clk, F, (98.8, 75.0), (98.8, 76.0)); via(board, clk, (98.8, 76.0))
track(board, clk, B, (98.8, 76.0), (107.0, 76.0))
track(board, clk, B, (107.0, 76.0), (107.0, 74.0))
track(board, clk, B, (107.0, 74.0), (119.2, 74.0)); via(board, clk, (119.2, 74.0))
track(board, clk, F, (119.2, 74.0), (120.0, 75.0))
track(board, clk, F, (120.0, 75.0), (120.0, 72.0)); track(board, clk, F, (120.0, 72.0), (128.0, 72.0))
via(board, clk, (128.0, 72.0)); track(board, clk, B, (128.0, 72.0), (128.0, 58.0))
track(board, clk, B, (128.0, 58.0), (138.0, 58.0)); via(board, clk, (138.0, 58.0))
track(board, clk, F, (138.0, 58.0), (138.0, 68.5)); track(board, clk, F, (138.0, 68.5), (136.5, 68.5))
track(board, clk, F, (136.5, 68.5), (136.5, 70.275))

# PERST source and connector launch on a lower B.Cu shelf.
track(board, per, F, (100.0, 73.95), (100.0, 78.8)); track(board, per, F, (100.0, 78.8), (102.0, 78.8))
via(board, per, (102.0, 78.8)); track(board, per, B, (102.0, 78.8), (134.0, 78.8)); via(board, per, (134.0, 78.8))
track(board, per, F, (134.0, 78.8), (134.0, 70.275)); track(board, per, F, (134.0, 70.275), (136.0, 70.275))

board.BuildListOfNets(); pcbnew.ZONE_FILLER(board).Fill(board.Zones()); board.Save(str(OUT)); print(OUT)
