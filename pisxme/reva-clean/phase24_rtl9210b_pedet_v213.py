"""V213: complete PEDET by joining R2.1 into the V212 trunk."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_PEDET_U18_J1_69_V212.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_PEDET_R2_U18_J1_69_V213.kicad_pcb'
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,l,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,x,y):
    v=pcbnew.PCB_VIA(b);v.SetPosition(p(x,y));v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def main():
    b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('PEDET')
    add(b,n,pcbnew.F_Cu,(89.0,48.0),(80.0,48.0));via(b,n,80.0,48.0)
    add(b,n,pcbnew.B_Cu,(80.0,48.0),(80.0,62.4));add(b,n,pcbnew.B_Cu,(80.0,62.4),(103.2,62.4))
    b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
