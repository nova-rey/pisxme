"""V242: move the U1.36 1V1 handoff via outboard of SPISI."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V240.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V242.kicad_pcb'
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,l,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,x,y):
    v=pcbnew.PCB_VIA(b);v.SetPosition(p(x,y));v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def main():
    b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1');code=n.GetNetCode()
    items=list(b.GetTracks())
    for t in items:
        if t.GetNetCode()==code and type(t).__name__=='PCB_TRACK' and round(t.GetStart().x/1e6,1)==102.5 and round(t.GetStart().y/1e6,1)==55.0: b.Remove(t)
    for v in items:
        if type(v).__name__=='PCB_VIA' and v.GetNetCode()==code and round(v.GetPosition().x/1e6,1)==102.5 and round(v.GetPosition().y/1e6,1)==55.0: b.Remove(v)
    add(b,n,pcbnew.B_Cu,(102.5,55.0),(104.0,55.0))
    add(b,n,pcbnew.F_Cu,(104.0,55.0),(103.5,55.0));add(b,n,pcbnew.F_Cu,(103.5,55.0),(103.5,57.5));via(b,n,104.0,55.0)
    b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
