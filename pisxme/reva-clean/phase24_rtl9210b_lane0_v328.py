"""V328: corrected orthogonal RX launch/endpoint corridors."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_COHERENT_REORIENT_V323.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_LANE0_ROUTE_V328.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 for name,src,dst in [('LANE0_TXN',(109.95,59.2),(135.25,62.725)),('LANE0_TXP',(109.95,58.8),(135.75,62.725))]:
  n=b.FindNet(name);s(b,n,F,src,(dst[0],src[1]));s(b,n,F,(dst[0],src[1]),dst)
 for name,src,dst,x,y in [('LANE0_RXN',(109.95,60.0),(133.75,62.725),111.5,64.5),('LANE0_RXP',(109.95,60.4),(134.25,62.725),110.6,66.5)]:
  n=b.FindNet(name);s(b,n,F,src,(x,src[1]));s(b,n,F,(x,src[1]),(x,y));v(b,n,(x,y));s(b,n,B,(x,y),(132,y));v(b,n,(132,y));s(b,n,F,(132,y),(dst[0],y));s(b,n,F,(dst[0],y),dst)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
