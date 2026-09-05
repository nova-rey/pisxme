"""Route the two LM74700 gate controls in separate B.Cu perimeter corridors."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "PHASE21_CONTROLS_VCAP.kicad_pcb"
OUTPUT = ROOT / "PHASE21_CONTROLS_VCAP_GATES.kicad_pcb"

def point(x, y): return pcbnew.VECTOR2I_MM(x, y)

def add_track(board, net, layer, start, end, width=.20):
    t = pcbnew.PCB_TRACK(board); t.SetStart(point(*start)); t.SetEnd(point(*end))
    t.SetWidth(pcbnew.FromMM(width)); t.SetLayer(layer); t.SetNet(net); board.Add(t)

def add_via(board, net, xy):
    v = pcbnew.PCB_VIA(board); v.SetPosition(point(*xy)); v.SetWidth(pcbnew.FromMM(.55))
    v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    v.SetNet(net); board.Add(v)

def main():
    board = pcbnew.LoadBoard(str(INPUT))
    routes = {
        "/POWER_INPUT/GATE_A": ((19.5, 76.45), (18.0, 76.45), (18.0, 20.0),
                                (218.0, 20.0), (218.0, 31.5), (217.54, 30.0)),
        "/POWER_INPUT/GATE_B": ((19.5, 96.45), (18.0, 96.45), (18.0, 160.0),
                                (218.0, 160.0), (218.0, 148.5), (217.54, 150.0)),
    }
    for name, pts in routes.items():
        net = board.FindNet(name); assert net is not None
        add_track(board, net, pcbnew.F_Cu, pts[0], pts[1])
        add_via(board, net, pts[1])
        for a, b in zip(pts[1:-2], pts[2:-1]): add_track(board, net, pcbnew.B_Cu, a, b)
        add_via(board, net, pts[-2])
        add_track(board, net, pcbnew.F_Cu, pts[-2], pts[-1])
    board.Save(str(OUTPUT)); print(OUTPUT)

if __name__ == "__main__": main()
