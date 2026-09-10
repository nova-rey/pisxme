"""V96: U13 storage-rail branch on an ordinary-via B.Cu perimeter corridor."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / 'PHASE24_STORAGE_AUTHORITY_J3_VERTICAL_V94.kicad_pcb'
OUT = R / 'PHASE24_STORAGE_RAIL_U13_BRANCH_V96.kicad_pcb'

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def track(board, net, layer, a, z, width=0.25):
    t = pcbnew.PCB_TRACK(board)
    t.SetLayer(layer)
    t.SetStart(P(*a)); t.SetEnd(P(*z))
    t.SetWidth(pcbnew.FromMM(width)); t.SetNet(net); t.SetNetCode(net.GetNetCode())
    board.Add(t)

def via(board, net, at):
    v = pcbnew.PCB_VIA(board)
    v.SetPosition(P(*at)); v.SetDrill(pcbnew.FromMM(0.30)); v.SetWidth(pcbnew.FromMM(0.60))
    v.SetNet(net); v.SetNetCode(net.GetNetCode()); board.Add(v)

b = pcbnew.LoadBoard(str(BASE)); n = b.FindNet('STORAGE_3V3'); assert n
# Leave both QFN and U14 pads with short F.Cu dogbones; keep the long branch on B.Cu.
track(b, n, pcbnew.F_Cu, (181.5, 135.0), (180.0, 135.0))
via(b, n, (180.0, 135.0))
track(b, n, pcbnew.B_Cu, (180.0, 135.0), (180.0, 120.0))
track(b, n, pcbnew.B_Cu, (180.0, 120.0), (210.0, 120.0))
track(b, n, pcbnew.B_Cu, (210.0, 120.0), (210.0, 149.05))
via(b, n, (210.0, 149.05))
track(b, n, pcbnew.F_Cu, (210.0, 149.05), (211.1, 149.05))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
