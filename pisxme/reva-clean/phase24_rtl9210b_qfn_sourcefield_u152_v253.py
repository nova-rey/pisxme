"""V253: move the U1.52 3V3 handoff clear of XTAL_IN."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V252.kicad_pcb';OUT=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V253.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.13)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.50));q.SetDrill(pcbnew.FromMM(.25));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def ep(t):return {(round(t.GetStart().x/1e6,2),round(t.GetStart().y/1e6,2)),(round(t.GetEnd().x/1e6,2),round(t.GetEnd().y/1e6,2))}
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3');old=[{(94.8,65.95),(94.8,64.6)},{(94.8,64.6),(92.5,64.6)},{(92.5,64.6),(92.5,64.8)},{(92.5,64.8),(92.5,56.5)},{(92.5,56.5),(93.8,56.5)}]
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode() and type(t).__name__=='PCB_TRACK' and ep(t) in old:b.RemoveNative(t)
 for t in list(b.GetTracks()):
  if type(t).__name__=='PCB_VIA' and t.GetNetCode()==n.GetNetCode() and abs(t.GetPosition().x/1e6-92.5)<.01 and abs(t.GetPosition().y/1e6-64.8)<.01:b.RemoveNative(t)
 tr(b,n,F,(94.8,65.95),(94.8,64.6));tr(b,n,F,(94.8,64.6),(91.5,64.6));tr(b,n,F,(91.5,64.6),(91.5,64.8));via(b,n,(91.5,64.8));tr(b,n,B,(91.5,64.8),(91.5,56.5));tr(b,n,B,(91.5,56.5),(93.8,56.5));b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
