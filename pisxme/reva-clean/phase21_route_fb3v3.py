"""Co-locate the bridge 3V3 FB network and route its signal locally."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "PHASE21_CONTROLS_VCAP.kicad_pcb"
OUTPUT = ROOT / "PHASE21_CONTROLS_FB3V3.kicad_pcb"

def tr(board, net, start, end, width=.20, layer=pcbnew.F_Cu):
    t=pcbnew.PCB_TRACK(board); t.SetStart(pcbnew.VECTOR2I_MM(*start)); t.SetEnd(pcbnew.VECTOR2I_MM(*end))
    t.SetWidth(pcbnew.FromMM(width)); t.SetLayer(layer); t.SetNet(net); board.Add(t)

def main():
    board=pcbnew.LoadBoard(str(INPUT)); net=board.FindNet("/REGULATORS/FB_BRIDGE_3V3"); assert net
    for ref,pos in (("R11",(215,95)),("R12",(215,100)),("C18",(220,95))):
        fp=board.FindFootprintByReference(ref); fp.SetPosition(pcbnew.VECTOR2I_MM(*pos)); fp.SetOrientationDegrees(0)
    pg=board.FindNet("/REGULATORS/PG_BRIDGE_3V3")
    for item in board.GetTracks():
        if item.GetNetCode() == pg.GetNetCode(): item.SetWidth(pcbnew.FromMM(.13208))
    tr(board,net,(227.25,106.25),(228.5,106.25))
    tr(board,net,(228.5,106.25),(228.5,108.5))
    via=pcbnew.PCB_VIA(board); via.SetPosition(pcbnew.VECTOR2I_MM(228.5,108.5)); via.SetWidth(pcbnew.FromMM(.55)); via.SetDrill(pcbnew.FromMM(.30)); via.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); via.SetNet(net); board.Add(via)
    tr(board,net,(228.5,108.5),(228.5,93),.20,pcbnew.B_Cu)
    tr(board,net,(228.5,93),(215.5,93),.20,pcbnew.B_Cu)
    via=pcbnew.PCB_VIA(board); via.SetPosition(pcbnew.VECTOR2I_MM(215.5,93)); via.SetWidth(pcbnew.FromMM(.55)); via.SetDrill(pcbnew.FromMM(.30)); via.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); via.SetNet(net); board.Add(via)
    tr(board,net,(215.5,93),(215.5,95))
    tr(board,net,(215.5,95),(219.05,95))
    tr(board,net,(219.05,95),(217.5,95))
    tr(board,net,(217.5,95),(217.5,102))
    tr(board,net,(217.5,102),(214.5,102))
    tr(board,net,(214.5,102),(214.5,100))
    board.Save(str(OUTPUT)); print(OUTPUT)

if __name__ == "__main__": main()
