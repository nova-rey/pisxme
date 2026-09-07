"""V212: PEDET U1.8 to M.2 contact 69 sideband launch."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SPISO3_U122_U2_V211.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_PEDET_U18_J1_69_V212.kicad_pcb'
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,l,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,x,y):
    v=pcbnew.PCB_VIA(b);v.SetPosition(p(x,y));v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def main():
    b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('PEDET')
    add(b,n,pcbnew.F_Cu,(101.95,62.4),(103.2,62.4));via(b,n,103.2,62.4)
    add(b,n,pcbnew.B_Cu,(103.2,62.4),(139.0,62.4));via(b,n,139.0,62.4)
    add(b,n,pcbnew.F_Cu,(139.0,62.4),(140.75,62.73))
    b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
