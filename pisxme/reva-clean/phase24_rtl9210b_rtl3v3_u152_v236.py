"""V236: move the U1.52 3V3 via left of RSET and pad 49."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_RTL3V3_U139_V232.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RTL3V3_U152_V236.kicad_pcb'
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,l,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,x,y):
    v=pcbnew.PCB_VIA(b);v.SetPosition(p(x,y));v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def main():
    b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
    add(b,n,pcbnew.F_Cu,(94.8,65.95),(93.0,65.95));add(b,n,pcbnew.F_Cu,(93.0,65.95),(93.0,64.5));via(b,n,93.0,64.5)
    add(b,n,pcbnew.B_Cu,(93.0,64.5),(93.0,56.5));add(b,n,pcbnew.B_Cu,(93.0,56.5),(93.8,56.5))
    b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
