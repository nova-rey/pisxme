"""V325: corrected orthogonal TX launch on the V323 placement."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_COHERENT_REORIENT_V323.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_LANE0_ROUTE_V325.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 for name,src,dst in [('LANE0_TXN',(109.95,59.2),(135.25,62.725)),('LANE0_TXP',(109.95,58.8),(135.75,62.725))]:
  n=b.FindNet(name); s(b,n,F,src,(dst[0],src[1])); s(b,n,F,(dst[0],src[1]),dst)
 for name,src,dst,y in [('LANE0_RXN',(109.95,60.0),(133.75,62.725),64.5),('LANE0_RXP',(109.95,60.4),(134.25,62.725),65.3)]:
  n=b.FindNet(name); s(b,n,F,src,(112,y)); v(b,n,(112,y)); s(b,n,B,(112,y),(132,y)); v(b,n,(132,y)); s(b,n,F,(132,y),dst)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
