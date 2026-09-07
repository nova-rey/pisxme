"""V141: join the shared M.2 SSD_3V3 contact row on the V137 basis."""
from pathlib import Path
import pcbnew

HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_RTL5V_BELOW_C5_V137.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_SSD33_SOCKET_JOIN_V141.kicad_pcb'

def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z):
    q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(pcbnew.F_Cu)
    q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)

def main():
    b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('SSD_3V3'); y=62.725
    for a,z in zip((114.75,115.25,115.75),(115.25,115.75,116.25)):
        tr(b,n,(a,y),(z,y))
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)

if __name__=='__main__': main()
