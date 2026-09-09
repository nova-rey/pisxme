"""V851: extend V850 with monotonic SPISO/SPICS endpoint corridors."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / 'PHASE24_RTL9210B_ROTATE_FLASH_270_SPI_CLEAN_CONTROLS_V850.kicad_pcb'
OUT = H / 'PHASE24_RTL9210B_ROTATE_FLASH_270_SPI_CLEAN_CONTROLS_V851.kicad_pcb'
F = pcbnew.F_Cu
W = pcbnew.FromMM(.20)

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def T(board, net_name, points):
    net = board.FindNet(net_name)
    for a, z in zip(points, points[1:]):
        track = pcbnew.PCB_TRACK(board)
        track.SetStart(P(*a)); track.SetEnd(P(*z)); track.SetLayer(F)
        track.SetWidth(W); track.SetNet(net); track.SetNetCode(net.GetNetCode())
        board.Add(track)

board = pcbnew.LoadBoard(str(BASE))
for track in list(board.GetTracks()):
    if track.GetNetname() in ('SPISO', 'SPICS'):
        board.RemoveNative(track)

# The lower two target pads retain their source order after the 270-degree
# rotation: SPISO -> U2.2 at y=52.4, SPICS -> U2.1 at y=51.2.
T(board, 'SPISO', [(94.05, 68.8), (87.0, 68.8), (87.0, 52.4), (88.0, 52.4)])
T(board, 'SPICS', [(94.05, 69.2), (86.0, 69.2), (86.0, 51.2), (88.0, 51.2)])
board.BuildListOfNets()
pcbnew.ZONE_FILLER(board).Fill(board.Zones())
board.Save(str(OUT))
print(OUT)
