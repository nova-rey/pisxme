"""V256: clear the inherited U1.52 RTL_3V3 escape from U1.51 RSET."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V255.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V256.kicad_pcb"


def main():
    board = pcbnew.LoadBoard(str(BASE))
    net = board.FindNet("RTL_3V3")
    remove = {(94.8, 65.95, 94.5, 65.95), (94.5, 65.95, 94.5, 63.5)}
    for track in list(board.GetTracks()):
        start, end = track.GetStart(), track.GetEnd()
        key = (start.x / 1e6, start.y / 1e6, end.x / 1e6, end.y / 1e6)
        if track.GetNetname() == "RTL_3V3" and key in remove:
            board.Remove(track)

    def add(start, end):
        track = pcbnew.PCB_TRACK(board)
        track.SetStart(pcbnew.VECTOR2I_MM(*start))
        track.SetEnd(pcbnew.VECTOR2I_MM(*end))
        track.SetLayer(pcbnew.F_Cu)
        track.SetWidth(pcbnew.FromMM(0.2))
        track.SetNet(net)
        track.SetNetCode(net.GetNetCode())
        board.Add(track)

    add((94.8, 65.95), (94.7, 65.95))
    add((94.7, 65.95), (94.7, 63.5))
    board.BuildListOfNets()
    board.Save(str(OUT))
    print(OUT)


if __name__ == "__main__":
    main()
