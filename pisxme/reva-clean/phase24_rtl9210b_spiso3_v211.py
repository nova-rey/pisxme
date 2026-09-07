"""V211: diagonal SPISO3 dogbone clears the adjacent SPISO source."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SPI_SOURCE_FIELD_V208.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_SPISO3_U122_U2_V211.kicad_pcb'
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,l,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,x,y):
    v=pcbnew.PCB_VIA(b);v.SetPosition(p(x,y));v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def main():
    b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('SPISO3')
    add(b,n,pcbnew.F_Cu,(99.6,58.05),(99.8,57.4));add(b,n,pcbnew.F_Cu,(99.8,57.4),(99.8,56.8));via(b,n,99.8,56.8)
    add(b,n,pcbnew.B_Cu,(99.8,56.8),(104,56.8));via(b,n,104,56.8)
    add(b,n,pcbnew.F_Cu,(104,56.8),(104,74));add(b,n,pcbnew.F_Cu,(104,74),(89,74));add(b,n,pcbnew.F_Cu,(89,74),(89,72))
    b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
