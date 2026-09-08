"""V281: SPISO with north U1 escape and a dogbone below SPICS."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SUPPORT_ROUTE_SPICS_V278.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SUPPORT_ROUTE_SPISO_V281.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu


def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def tr(b, n, l, a, z):
    q = pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l)
    q.SetWidth(pcbnew.FromMM(.20)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b, n, xy):
    q = pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.50))
    q.SetDrill(pcbnew.FromMM(.25)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)


def main():
    b = pcbnew.LoadBoard(str(BASE)); n = b.FindNet('SPISO')
    tr(b,n,F,(99.2,58.05),(99.2,56.0)); tr(b,n,F,(99.2,56.0),(96.0,56.0)); via(b,n,(96.0,56.0))
    tr(b,n,B,(96.0,56.0),(96.0,78.0)); tr(b,n,B,(96.0,78.0),(84.5,78.0))
    tr(b,n,B,(84.5,78.0),(84.5,73.5)); via(b,n,(84.5,73.5)); tr(b,n,F,(84.5,73.5),(84.5,70.0))
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)


if __name__ == '__main__': main()
