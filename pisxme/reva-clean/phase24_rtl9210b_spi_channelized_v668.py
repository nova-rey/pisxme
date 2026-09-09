"""V668: staggered native QFN SPI source escapes and separated channels.

Disposable Path-B experiment.  The V595 rail/sideband field is retained, but
each SPI source is allocated a distinct B.Cu channel and a bottom endpoint
return.  No expected connectivity is synthesized and no design rule is
relaxed.
"""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_SUPPORT_COALLOCATED_V595_CLKREQ_LOCAL.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_SPI_CHANNELIZED_NATIVE_V668.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def track(board, net, layer, a, z):
    q = pcbnew.PCB_TRACK(board)
    q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer)
    q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode())
    board.Add(q)

def via(board, net, xy):
    q = pcbnew.PCB_VIA(board)
    q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(0.60))
    q.SetDrill(pcbnew.FromMM(0.30)); q.SetLayerPair(F, B)
    q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)

def main():
    board = pcbnew.LoadBoard(str(BASE))
    # Native source pad, source dogbone, F/B transition, separated B.Cu
    # channel, bottom return, and native U2 endpoint.  Channels are ordered
    # by available corridor rather than by schematic signal order.
    routes = {
        "SPISI": ((102.05, 58.8), (100.8, 57.8), (96.0, 57.8), (96.0, 76.0), (96.1, 70.0)),
        "SPICLK": ((102.05, 59.2), (100.4, 56.6), (95.0, 56.6), (95.0, 77.0), (97.3, 70.0)),
        "SPISO3": ((102.05, 60.4), (100.8, 62.0), (94.0, 62.0), (94.0, 78.0), (98.5, 70.0)),
        "SPISO": ((102.05, 60.8), (100.4, 63.5), (93.0, 63.5), (93.0, 79.0), (92.5, 70.0)),
        "SPICS": ((102.05, 61.2), (99.8, 64.8), (92.0, 64.8), (92.0, 80.0), (91.3, 70.0)),
    }
    for name, (src, transition, channel_start, channel_end, endpoint) in routes.items():
        net = board.FindNet(name)
        track(board, net, F, src, transition)
        via(board, net, transition)
        track(board, net, B, transition, channel_start)
        track(board, net, B, channel_start, channel_end)
        via(board, net, channel_end)
        track(board, net, F, channel_end, endpoint)
    board.BuildListOfNets()
    pcbnew.ZONE_FILLER(board).Fill(board.Zones())
    board.Save(str(OUT))
    print(OUT)

if __name__ == "__main__":
    main()
