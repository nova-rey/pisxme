"""V252: clear the final V251 REFCLK corner and XTAL_IN-via contact."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V242.kicad_pcb';OUT=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V252.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.13)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.50));q.SetDrill(pcbnew.FromMM(.25));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def ep(t):return {(round(t.GetStart().x/1e6,2),round(t.GetStart().y/1e6,2)),(round(t.GetEnd().x/1e6,2),round(t.GetEnd().y/1e6,2))}
def scrub(b,net,sets,vias):
 for t in list(b.GetTracks()):
  if t.GetNetCode()==net.GetNetCode() and type(t).__name__=='PCB_TRACK' and ep(t) in sets:b.RemoveNative(t)
 for t in list(b.GetTracks()):
  if type(t).__name__=='PCB_VIA' and t.GetNetCode()==net.GetNetCode() and any(abs(t.GetPosition().x/1e6-x)<.01 and abs(t.GetPosition().y/1e6-y)<.01 for x,y in vias):b.RemoveNative(t)
def main():
 b=pcbnew.LoadBoard(str(BASE));r1=b.FindNet('RTL_1V1');rp=b.FindNet('REFCLK_P');rn=b.FindNet('REFCLK_N');r3=b.FindNet('RTL_3V3')
 scrub(b,rp,[{(98.4,65.95),(98.2,66.8)},{(98.2,66.8),(98.2,60.0)}],[(98.2,66.8)])
 scrub(b,rn,[{(98.8,65.95),(99.0,66.8)},{(99.0,66.8),(99.0,60.8)}],[(99.0,66.8)])
 scrub(b,r3,[{(94.8,65.95),(94.5,65.95)},{(94.5,65.95),(94.5,63.5)},{(94.5,63.5),(93.0,63.5)},{(93.0,63.5),(93.0,56.5)}],[(93.0,63.5)])
 tr(b,rp,F,(98.4,65.95),(98.4,67.8));tr(b,rp,F,(98.4,67.8),(97.4,68.8));via(b,rp,(97.4,68.8));tr(b,rp,B,(97.4,68.8),(97.4,60.0));tr(b,rp,B,(97.4,60.0),(98.2,60.0))
 tr(b,rn,F,(98.8,65.95),(98.8,67.6));tr(b,rn,F,(98.8,67.6),(100.8,68.6));via(b,rn,(100.8,68.6));tr(b,rn,B,(100.8,68.6),(100.8,60.8));tr(b,rn,B,(100.8,60.8),(99.0,60.8))
 tr(b,r3,F,(94.8,65.95),(94.8,64.6));tr(b,r3,F,(94.8,64.6),(92.5,64.6));tr(b,r3,F,(92.5,64.6),(92.5,64.8));via(b,r3,(92.5,64.8));tr(b,r3,B,(92.5,64.8),(92.5,56.5));tr(b,r3,B,(92.5,56.5),(93.8,56.5))
 tr(b,r1,F,(98.0,65.95),(98.0,67.6));tr(b,r1,F,(98.0,67.6),(103.0,67.6));tr(b,r1,F,(103.0,67.6),(103.0,65.8));via(b,r1,(103.0,65.8));tr(b,r1,B,(103.0,65.8),(103.5,65.8));via(b,r1,(103.5,65.8));tr(b,r1,F,(103.5,65.8),(106.0,65.8));via(b,r1,(106.0,65.8));tr(b,r1,B,(106.0,65.8),(107.0,65.8));tr(b,r1,B,(107.0,65.8),(107.0,63.0));via(b,r1,(107.0,63.0));tr(b,r1,F,(107.0,63.0),(107.0,54.5));via(b,r1,(107.0,54.5));tr(b,r1,B,(107.0,54.5),(104.0,55.0));tr(b,r1,F,(99.2,65.95),(99.2,67.6))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
