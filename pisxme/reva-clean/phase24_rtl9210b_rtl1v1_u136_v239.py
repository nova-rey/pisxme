"""V239: separate U1.36 1V1 from the U1.39 3V3 vertical."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_RTL1V1_U136_V238.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_V239.kicad_pcb'
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,l,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,x,y):
    v=pcbnew.PCB_VIA(b);v.SetPosition(p(x,y));v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def main():
    b=pcbnew.LoadBoard(str(BASE));n3=b.FindNet('RTL_3V3');code=n3.GetNetCode()
    items=list(b.GetTracks())
    old={(94.05,60.4,92.5,60.4),(92.5,60.4,92.5,56.5),(92.5,56.5,93.8,56.5)}
    for t in items:
        if t.GetNetCode()==code and type(t).__name__=='PCB_TRACK':
            a=(round(t.GetStart().x/1e6,2),round(t.GetStart().y/1e6,2),round(t.GetEnd().x/1e6,2),round(t.GetEnd().y/1e6,2))
            if a in old or (a[2],a[3],a[0],a[1]) in old: b.Remove(t)
    for v in items:
        if type(v).__name__=='PCB_VIA' and v.GetNetCode()==code and round(v.GetPosition().x/1e6,1)==92.5 and round(v.GetPosition().y/1e6,1)==60.4: b.Remove(v)
    add(b,n3,pcbnew.F_Cu,(94.05,60.4),(91.0,60.4));via(b,n3,91.0,60.4);add(b,n3,pcbnew.B_Cu,(91.0,60.4),(91.0,56.5));add(b,n3,pcbnew.B_Cu,(91.0,56.5),(93.8,56.5))
    b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
