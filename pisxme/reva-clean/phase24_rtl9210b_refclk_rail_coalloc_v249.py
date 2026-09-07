"""V249: co-author REFCLK transitions with the U1.60/U1.63 rail escape."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V242.kicad_pcb';OUT=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V249.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def ep(t):return {(round(t.GetStart().x/1e6,2),round(t.GetStart().y/1e6,2)),(round(t.GetEnd().x/1e6,2),round(t.GetEnd().y/1e6,2))}
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1');rp=b.FindNet('REFCLK_P');rn=b.FindNet('REFCLK_N')
 # remove only the current REFCLK local source drops and first B.Cu verticals
 old={rp.GetNetCode():[{(98.4,65.95),(98.2,66.8)},{(98.2,66.8),(98.2,60.0)}],rn.GetNetCode():[{(98.8,65.95),(99.0,66.8)},{(99.0,66.8),(99.0,60.8)}]}
 for t in list(b.GetTracks()):
  if t.GetNetCode() in old and ep(t) in old[t.GetNetCode()]: b.RemoveNative(t)
 for t in list(b.GetTracks()):
  if type(t).__name__=='PCB_VIA' and t.GetNetCode()==rp.GetNetCode() and abs(t.GetPosition().x/1e6-98.2)<.01: b.RemoveNative(t)
  if type(t).__name__=='PCB_VIA' and t.GetNetCode()==rn.GetNetCode() and abs(t.GetPosition().x/1e6-99.0)<.01: b.RemoveNative(t)
 tr(b,rp,F,(98.4,65.95),(97.4,66.8));via(b,rp,(97.4,66.8));tr(b,rp,B,(97.4,66.8),(97.4,60.0));tr(b,rp,B,(97.4,60.0),(98.2,60.0))
 tr(b,rn,F,(98.8,65.95),(100.8,66.8));via(b,rn,(100.8,66.8));tr(b,rn,B,(100.8,66.8),(100.8,60.8));tr(b,rn,B,(100.8,60.8),(99.0,60.8))
 tr(b,n,F,(98.0,65.95),(98.0,67.5));tr(b,n,F,(98.0,67.5),(103.0,67.5));tr(b,n,F,(103.0,67.5),(103.0,65.8));via(b,n,(103.0,65.8));tr(b,n,B,(103.0,65.8),(103.5,65.8));via(b,n,(103.5,65.8));tr(b,n,F,(103.5,65.8),(106.0,65.8));via(b,n,(106.0,65.8));tr(b,n,B,(106.0,65.8),(107.0,65.8));tr(b,n,B,(107.0,65.8),(107.0,63.0));via(b,n,(107.0,63.0));tr(b,n,F,(107.0,63.0),(107.0,54.5));via(b,n,(107.0,54.5));tr(b,n,B,(107.0,54.5),(104.0,55.0));tr(b,n,F,(99.2,65.95),(99.2,67.5))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
