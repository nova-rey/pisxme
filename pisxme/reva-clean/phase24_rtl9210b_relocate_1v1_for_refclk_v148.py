"""V148: move the U1 bottom RTL_1V1 collector to clear REFCLK escapes."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SSD33_ON_V143_V144.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RELOCATE_1V1_FOR_REFCLK_V148.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return (round(p.x/1e6,3),round(p.y/1e6,3))
def tr(b,n,l,a,z,w=.15):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
 remove={((96.0,74.8),(103.0,74.8)),((98.0,74.8),(103.0,74.8)),((96.0,73.95),(96.0,74.8)),((98.0,73.95),(98.0,74.8)),((99.2,73.95),(99.2,74.8)),((103.0,74.8),(103.0,73.8))}
 for x in list(b.GetTracks()):
  if x.GetNetname()!='RTL_1V1' or type(x).__name__!='PCB_TRACK': continue
  pair=(xy(x.GetStart()),xy(x.GetEnd()))
  if pair in remove or pair[::-1] in remove: b.RemoveNative(x)
 for x,esc in ((96.0,95.5),(98.0,97.5),(99.2,100.0)):
  tr(b,n,F,(x,73.95),(esc,75.6));via(b,n,(esc,75.6));tr(b,n,B,(esc,75.6),(esc,77.5))
 tr(b,n,B,(95.5,77.5),(100.0,77.5));tr(b,n,B,(100.0,77.5),(103.0,77.5));tr(b,n,B,(103.0,77.5),(103.0,73.8))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
