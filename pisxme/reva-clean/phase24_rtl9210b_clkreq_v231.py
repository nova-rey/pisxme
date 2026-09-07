"""V231: move only the R3 CLKREQ return west of the RSET diagonal."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CLKREQ_R3_U113_J1_52_V230.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CLKREQ_R3_U113_J1_52_V231.kicad_pcb'
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def main():
    b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('CLKREQ_N'); code=n.GetNetCode()
    old={(92.0,42.0,80.0,42.0),(80.0,42.0,80.0,69.5),(80.0,69.5,102.4,69.5)}
    items=list(b.GetTracks())
    for t in items:
        if t.GetNetCode()==code and type(t).__name__=='PCB_TRACK':
            a=(round(t.GetStart().x/1e6,1),round(t.GetStart().y/1e6,1),round(t.GetEnd().x/1e6,1),round(t.GetEnd().y/1e6,1))
            if a in old or a in {(z[2],z[3],z[0],z[1]) for z in old}: b.Remove(t)
    for v in items:
        if type(v).__name__=='PCB_VIA' and v.GetNetCode()==code and round(v.GetPosition().x/1e6,1)==92.0 and round(v.GetPosition().y/1e6,1)==42.0: b.Remove(v)
    def add(a,z,l):
        q=pcbnew.PCB_TRACK(b);q.SetStart(p(*a));q.SetEnd(p(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(code);b.Add(q)
    v=pcbnew.PCB_VIA(b);v.SetPosition(p(92,42));v.SetNet(n);v.SetNetCode(code);b.Add(v)
    add((92,42),(75,42),pcbnew.B_Cu);add((75,42),(75,69.5),pcbnew.B_Cu);add((75,69.5),(102.4,69.5),pcbnew.B_Cu)
    b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__': main()
