"""V317: alternating-layer lane-0 escape trial from V311."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CLKREQ_ROUTE_V311.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_LANE0_ROUTE_V317.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 rows=[('LANE0_RXP',(99.6,65.95),(134.25,62.725),68.0,F),('LANE0_RXN',(100.0,65.95),(133.75,62.725),68.8,B),('LANE0_TXN',(100.8,65.95),(135.25,62.725),69.6,F),('LANE0_TXP',(101.2,65.95),(135.75,62.725),70.4,B)]
 for name,a,z,y,l in rows:
  n=b.FindNet(name)
  if l==F: s(b,n,F,a,(a[0],y));s(b,n,F,(a[0],y),(130,y));s(b,n,F,(130,y),z)
  else:
   s(b,n,F,a,(103,y));v(b,n,(103,y));s(b,n,B,(103,y),(130,y));v(b,n,(130,y));s(b,n,F,(130,y),z)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
