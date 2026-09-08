"""V312: native RTL_5V closure trial from the V311 sideband basis."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_CLKREQ_ROUTE_V311.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_RTL5V_ROUTE_V312.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def seg(b, n, layer, a, z):
    t = pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(layer)
    t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b, n, q):
    v = pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(0.60))
    v.SetDrill(pcbnew.FromMM(0.30)); v.SetLayerPair(F, B); v.SetNet(n)
    v.SetNetCode(n.GetNetCode()); b.Add(v)

def main():
    b = pcbnew.LoadBoard(str(BASE)); n = b.FindNet("RTL_5V")
    # Escape the upper QFN pads to a B.Cu spine above the SPI field.
    seg(b,n,F,(95.2,58.05),(95.2,56.8)); via(b,n,(95.2,56.8))
    seg(b,n,B,(95.2,56.8),(101.95,56.8)); via(b,n,(101.95,56.8))
    seg(b,n,F,(101.95,56.8),(101.95,58.8))
    # Continue from the same spine to the local decoupler, outside the QFN.
    seg(b,n,B,(101.95,56.8),(116.4,56.8)); via(b,n,(116.4,56.8))
    seg(b,n,F,(116.4,56.8),(116.4,61.0))
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__ == "__main__": main()
