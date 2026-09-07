"""V241: orthogonal U1.36 1V1 handoff outside SPISI."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V240.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V241.kicad_pcb'
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,l,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def main():
    b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1'); code=n.GetNetCode()
    for t in list(b.GetTracks()):
        if t.GetNetCode()==code and type(t).__name__=='PCB_TRACK' and round(t.GetStart().x/1e6,1)==102.5 and round(t.GetStart().y/1e6,1)==55.0 and round(t.GetEnd().x/1e6,1)==103.5: b.Remove(t)
    add(b,n,pcbnew.F_Cu,(102.5,55.0),(103.5,55.0));add(b,n,pcbnew.F_Cu,(103.5,55.0),(103.5,57.5))
    b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
