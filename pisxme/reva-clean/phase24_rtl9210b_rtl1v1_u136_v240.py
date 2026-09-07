"""V240: coordinated U1.36 1V1 return above the 3V3 trunks."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_RTL3V3_U152_V237.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V240.kicad_pcb'
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,l,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,x,y):
    v=pcbnew.PCB_VIA(b);v.SetPosition(p(x,y));v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def main():
    b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
    add(b,n,pcbnew.F_Cu,(94.05,59.2),(92.0,59.2));via(b,n,92.0,59.2)
    add(b,n,pcbnew.B_Cu,(92.0,59.2),(92.0,55.0));add(b,n,pcbnew.B_Cu,(92.0,55.0),(102.5,55.0));via(b,n,102.5,55.0)
    add(b,n,pcbnew.F_Cu,(102.5,55.0),(103.5,57.5))
    b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
