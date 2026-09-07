"""V210: SPISO3 source dogbone to an outboard F.Cu corridor."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SPI_SOURCE_FIELD_V208.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SPISO3_U122_U2_V210.kicad_pcb"


def p(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))


def add(b, n, layer, a, z):
    t = pcbnew.PCB_TRACK(b); t.SetStart(p(*a)); t.SetEnd(p(*z)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(0.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)


def via(b, n, x, y):
    v = pcbnew.PCB_VIA(b); v.SetPosition(p(x, y)); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)


def main():
    b = pcbnew.LoadBoard(str(BASE)); n = b.FindNet("SPISO3")
    add(b, n, pcbnew.F_Cu, (99.6, 58.05), (99.6, 56.8)); via(b, n, 99.6, 56.8)
    add(b, n, pcbnew.B_Cu, (99.6, 56.8), (104.0, 56.8)); via(b, n, 104.0, 56.8)
    add(b, n, pcbnew.F_Cu, (104.0, 56.8), (104.0, 74.0))
    add(b, n, pcbnew.F_Cu, (104.0, 74.0), (89.0, 74.0))
    add(b, n, pcbnew.F_Cu, (89.0, 74.0), (89.0, 72.0))
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)


if __name__ == '__main__': main()
