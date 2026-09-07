"""V100: take the RTL_1V1 drop left of the XTAL_OUT horizontal span."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / 'PHASE24_RTL9210B_XTALOUT_U155_CELL_V97.kicad_pcb'
OUT = HERE / 'PHASE24_RTL9210B_XTALOUT_U155_LEFT_ESCAPE_V100.kicad_pcb'
F = pcbnew.F_Cu
B = pcbnew.B_Cu

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def endpoints(track):
    a, z = track.GetStart(), track.GetEnd()
    return {(round(a.x / 1e6, 3), round(a.y / 1e6, 3)),
            (round(z.x / 1e6, 3), round(z.y / 1e6, 3))}

def add_track(board, net, layer, start, end, width=.15):
    track = pcbnew.PCB_TRACK(board)
    track.SetStart(P(*start)); track.SetEnd(P(*end)); track.SetLayer(layer)
    track.SetWidth(pcbnew.FromMM(width)); track.SetNet(net)
    track.SetNetCode(net.GetNetCode()); board.Add(track)

def main():
    board = pcbnew.LoadBoard(str(BASE))
    net = board.FindNet('RTL_1V1')
    settings = board.GetDesignSettings()
    settings.m_TrackMinWidth = pcbnew.FromMM(.13208)
    settings.m_MinClearance = pcbnew.FromMM(.15)
    nc = settings.m_NetSettings.GetDefaultNetclass()
    nc.SetTrackWidth(pcbnew.FromMM(.13208)); nc.SetClearance(pcbnew.FromMM(.15))
    settings.m_NetSettings.SetDefaultNetclass(nc)
    settings.m_NetSettings.RecomputeEffectiveNetclasses()
    old = {(107.0, 73.8), (107.0, 69.5)}
    for item in list(board.GetTracks()):
        if (item.GetNetCode() == net.GetNetCode() and
                type(item).__name__ == 'PCB_TRACK' and endpoints(item) == old):
            board.Remove(item)
    # XTAL_OUT occupies B.Cu y=73.2 from x=95.6 through x=110.5.
    # Stay below it, go around its left endpoint, then join the existing
    # RTL_1V1 collector at y=69.5. No plane-layer signal is introduced.
    add_track(board, net, B, (107.0, 73.8), (94.8, 73.8))
    add_track(board, net, B, (94.8, 73.8), (94.8, 69.5))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)

if __name__ == '__main__':
    main()
