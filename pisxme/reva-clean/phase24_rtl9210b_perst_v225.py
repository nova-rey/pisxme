"""V225: PERST exits horizontally before rising to its via."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_PEDET_R2_U18_J1_69_V215.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_PERST_U114_J1_50_V225.kicad_pcb'
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,l,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,x,y):
    v=pcbnew.PCB_VIA(b);v.SetPosition(p(x,y));v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def main():
    b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('PERST_N')
    add(b,n,pcbnew.F_Cu,(101.95,60.0),(102.8,60.0));add(b,n,pcbnew.F_Cu,(102.8,60.0),(103.0,58.2));via(b,n,103.0,58.2)
    add(b,n,pcbnew.B_Cu,(103.0,58.2),(97.5,58.2));add(b,n,pcbnew.B_Cu,(97.5,58.2),(97.5,72.0));add(b,n,pcbnew.B_Cu,(97.5,72.0),(134.5,72.0));via(b,n,134.5,72.0)
    add(b,n,pcbnew.F_Cu,(134.5,72.0),(136.0,70.28))
    b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
