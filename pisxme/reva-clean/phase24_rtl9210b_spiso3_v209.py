"""V209: allocate the remaining U1.22-to-flash SPISO3 source field."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SPI_SOURCE_FIELD_V208.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SPISO3_U122_U2_V209.kicad_pcb"


def p(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def main():
    b = pcbnew.LoadBoard(str(BASE))
    n = b.FindNet("SPISO3")
    for a, z in [
        ((99.6, 58.05), (103.4, 58.05)),
        ((103.4, 58.05), (103.4, 74.0)),
        ((103.4, 74.0), (89.0, 74.0)),
        ((89.0, 74.0), (89.0, 72.0)),
    ]:
        t = pcbnew.PCB_TRACK(b)
        t.SetStart(p(*a)); t.SetEnd(p(*z)); t.SetLayer(pcbnew.F_Cu)
        t.SetWidth(pcbnew.FromMM(0.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode())
        b.Add(t)
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)


if __name__ == "__main__":
    main()
