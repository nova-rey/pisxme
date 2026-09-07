"""V221: complete CLKREQ with R3.1 return around the left field."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CLKREQ_U113_J1_52_V220.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CLKREQ_R3_U113_J1_52_V221.kicad_pcb'
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,l,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,x,y):
    v=pcbnew.PCB_VIA(b);v.SetPosition(p(x,y));v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def main():
    b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('CLKREQ_N')
    add(b,n,pcbnew.F_Cu,(92.0,48.0),(92.0,44.0));via(b,n,92.0,44.0)
    add(b,n,pcbnew.B_Cu,(92.0,44.0),(80.0,44.0));add(b,n,pcbnew.B_Cu,(80.0,44.0),(80.0,61.0));add(b,n,pcbnew.B_Cu,(80.0,61.0),(97.5,61.0))
    b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
