"""V232: join U1.39 RTL_3V3 into the promoted local rail trunk."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CLKREQ_R3_U113_J1_52_V231.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RTL3V3_U139_V232.kicad_pcb'
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,l,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,x,y):
    v=pcbnew.PCB_VIA(b);v.SetPosition(p(x,y));v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def main():
    b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
    add(b,n,pcbnew.F_Cu,(94.05,60.4),(92.5,60.4));via(b,n,92.5,60.4)
    add(b,n,pcbnew.B_Cu,(92.5,60.4),(92.5,56.5));add(b,n,pcbnew.B_Cu,(92.5,56.5),(93.8,56.5))
    b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
