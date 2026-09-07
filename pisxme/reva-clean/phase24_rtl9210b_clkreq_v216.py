"""V216: CLKREQ U1.13 to M.2 contact 52 launch."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_PEDET_R2_U18_J1_69_V215.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CLKREQ_U113_J1_52_V216.kicad_pcb'
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,l,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,x,y):
    v=pcbnew.PCB_VIA(b);v.SetPosition(p(x,y));v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def main():
    b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('CLKREQ_N')
    add(b,n,pcbnew.F_Cu,(101.95,60.4),(104.0,60.4));add(b,n,pcbnew.F_Cu,(104.0,60.4),(104.0,68.4));via(b,n,104.0,68.4)
    add(b,n,pcbnew.B_Cu,(104.0,68.4),(135.5,68.4));via(b,n,135.5,68.4)
    add(b,n,pcbnew.F_Cu,(135.5,68.4),(136.5,70.28))
    b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
