"""V852: separate the lower SPI pair on B.Cu with ordinary vias."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / 'PHASE24_RTL9210B_ROTATE_FLASH_270_SPI_CLEAN_CONTROLS_V850.kicad_pcb'
OUT = H / 'PHASE24_RTL9210B_ROTATE_FLASH_270_SPI_CLEAN_CONTROLS_V852.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.20)

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def track(board, net_name, layer, points):
    net = board.FindNet(net_name)
    for a, z in zip(points, points[1:]):
        q = pcbnew.PCB_TRACK(board); q.SetStart(P(*a)); q.SetEnd(P(*z))
        q.SetLayer(layer); q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode())
        board.Add(q)
def via(board, net_name, x, y):
    q = pcbnew.PCB_VIA(board); q.SetPosition(P(x, y)); q.SetWidth(pcbnew.FromMM(.60))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(board.FindNet(net_name))
    q.SetNetCode(board.FindNet(net_name).GetNetCode()); board.Add(q)

board = pcbnew.LoadBoard(str(BASE))
for q in list(board.GetTracks()):
    if q.GetNetname() in ('SPISO', 'SPICS'):
        board.RemoveNative(q)

# F.Cu source dogbones, B.Cu long corridors, F.Cu target dogbones. Vias are
# outside both QFN pad fields and are ordinary drilled through-vias.
via(board, 'SPISO', 87.0, 68.8); via(board, 'SPISO', 87.0, 52.4)
track(board, 'SPISO', F, [(94.05, 68.8), (87.0, 68.8)])
track(board, 'SPISO', B, [(87.0, 68.8), (87.0, 52.4)])
track(board, 'SPISO', F, [(87.0, 52.4), (88.0, 52.4)])
via(board, 'SPICS', 85.0, 69.2); via(board, 'SPICS', 85.0, 51.2)
track(board, 'SPICS', F, [(94.05, 69.2), (85.0, 69.2)])
track(board, 'SPICS', B, [(85.0, 69.2), (85.0, 51.2)])
track(board, 'SPICS', F, [(85.0, 51.2), (88.0, 51.2)])
board.BuildListOfNets(); pcbnew.ZONE_FILLER(board).Fill(board.Zones())
board.Save(str(OUT)); print(OUT)
