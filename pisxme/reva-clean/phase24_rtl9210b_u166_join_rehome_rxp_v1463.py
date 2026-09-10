"""V1463: co-author the U1.65 RXP departure with a direct U1.66 GND join."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_U166_JOIN_REHOME_RXP_V1463.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)
board = pcbnew.LoadBoard(str(BASE))

def net(name):
    result = board.FindNet(name)
    assert result is not None, name
    return result

def point(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def remove_net(name):
    code = net(name).GetNetCode()
    for item in list(board.GetTracks()):
        if item.GetNetCode() == code:
            board.RemoveNative(item)

def segment(name, start, end, layer):
    n = net(name)
    item = pcbnew.PCB_TRACK(board)
    item.SetStart(point(*start))
    item.SetEnd(point(*end))
    item.SetLayer(layer)
    item.SetWidth(W)
    item.SetNet(n)
    item.SetNetCode(n.GetNetCode())
    board.Add(item)

def via(name, xy):
    n = net(name)
    item = pcbnew.PCB_VIA(board)
    item.SetPosition(point(*xy))
    item.SetWidth(pcbnew.FromMM(0.60))
    item.SetDrill(pcbnew.FromMM(0.30))
    item.SetLayerPair(F, B)
    item.SetNet(n)
    item.SetNetCode(n.GetNetCode())
    board.Add(item)

# Reuse the already-authoritative remote RXP corridor from V1428, but move
# only its package departure and first transition away from the exposed-pad
# bottom edge.  The U1.66 GND join then runs directly into U1.69.
remove_net("LANE0_RXP")
segment("LANE0_RXP", (94.05, 71.60), (89.80, 71.60), F)
segment("LANE0_RXP", (89.80, 71.60), (89.80, 70.00), F)
via("LANE0_RXP", (89.80, 70.00))
segment("LANE0_RXP", (89.80, 70.00), (89.80, 82.00), B)
via("LANE0_RXP", (89.80, 82.00))
segment("LANE0_RXP", (89.80, 82.00), (95.00, 82.00), F)
segment("GND", (94.05, 72.40), (95.60, 72.40), F)

board.BuildListOfNets()
pcbnew.ZONE_FILLER(board).Fill(board.Zones())
board.Save(str(OUT))
print(OUT)
