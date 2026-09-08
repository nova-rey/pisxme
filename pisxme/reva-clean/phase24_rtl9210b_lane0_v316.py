"""V316: monotonic RTL9210B lane-0 corridor trial from V311."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CLKREQ_ROUTE_V311.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_LANE0_ROUTE_V316.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.13)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(F);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 pairs=[('LANE0_RXP',(99.6,65.95),(134.25,62.725),68.0),
        ('LANE0_RXN',(100.0,65.95),(133.75,62.725),68.8),
        ('LANE0_TXN',(100.8,65.95),(135.25,62.725),69.6),
        ('LANE0_TXP',(101.2,65.95),(135.75,62.725),70.4)]
 for name,a,z,y in pairs:
  n=b.FindNet(name);s(b,n,a,(a[0],y));s(b,n,(a[0],y),(130.0,y));s(b,n,(130.0,y),z)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
