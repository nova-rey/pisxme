"""Disposable QFN source partition: far RTL_1V1 and parallel SPI escapes."""
from pathlib import Path
import pcbnew
BASE=Path("PHASE24_RTL9210B_1V1_CRYSTAL_RSET_STAGED_V4.kicad_pcb")
OUT=Path("PHASE24_RTL9210B_QFN_SPI_POWER_PARTITION_V1.kicad_pcb")
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def p(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(p(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def route(b,n,src,esc,spine,target):
 s(b,n,F,src,esc);v(b,n,esc);s(b,n,B,esc,spine);s(b,n,B,spine,(target[0],spine[1]));v(b,n,(target[0],spine[1]));s(b,n,F,(target[0],spine[1]),target)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet("RTL_1V1");spics=b.FindNet("SPICS");spiso=b.FindNet("SPISO")
 spiso3=b.FindNet("SPISO3");spiclk=b.FindNet("SPICLK");spisi=b.FindNet("SPISI")
 for item in list(b.GetTracks()):
  if item.GetNetname()=="RTL_1V1":b.Remove(item)
 # Pad-aware 1V1: left pads exit left; top pads exit upward; the two
 # right/bottom pads exit into a lower B.Cu collector without crossing U1.17.
 for a,z in [((76.05,60),(74.8,60)),((76.05,62),(74.8,62)),((76.05,63.2),(74.8,63.2)),
             ((77.2,58.05),(77.2,55.5)),((81.2,58.05),(81.2,55.5)),((82.8,58.05),(82.8,55.5)),
             ((83.95,62.4),(85.5,61.5)),((82.8,65.95),(81.5,67.5))]:s(b,n,F,a,z);v(b,n,z)
 for a,z in [((74.8,60),(74.8,63.2)),((77.2,55.5),(82.8,55.5)),((74.8,55.5),(77.2,55.5)),
             ((74.8,63.2),(74.8,69)),((74.8,69),(85.5,69)),((85.5,69),(85.5,61.5)),
             ((81.5,67.5),(81.5,69)),((82.8,55.5),(82.8,41)),((82.8,41),(123.4,41))]:s(b,n,B,a,z)
 v(b,n,(123.4,41));s(b,n,F,(123.4,41),(123.4,51))
 # Native-style SPI escape corridors from the proven V7 routing trial.
 for name,src,a,bend,sv,dv in [
   ("SPICS",(83.95,62.8),(85.0,62.8),(85.0,61.0),(86.0,61.0),(90.8,48.0)),
   ("SPISO",(83.95,63.2),(85.5,63.2),(85.5,62.0),(87.0,62.0),(92.0,49.0)),
   ("SPISO3",(83.95,63.6),(86.0,63.6),(86.0,63.0),(88.0,63.0),(98.0,50.0))]:
  q=b.GetNetsByName() if False else None
  nn={"SPICS":spics,"SPISO":spiso,"SPISO3":spiso3}[name]
  for x,y in [(src,a),(a,bend)]:s(b,nn,F,x,y)
  s(b,nn,F,bend,sv);v(b,nn,sv);s(b,nn,B,sv,(sv[0],dv[1]));s(b,nn,B,(sv[0],dv[1]),dv);v(b,nn,dv);s(b,nn,F,dv,(dv[0],58.0))
 nn=spiclk;s(b,nn,F,(83.95,64.8),(89.0,64.8));v(b,nn,(89.0,64.8));s(b,nn,B,(89.0,64.8),(89.0,52.0));s(b,nn,B,(89.0,52.0),(100.0,52.0));s(b,nn,B,(100.0,52.0),(100.0,55.5));s(b,nn,B,(100.0,55.5),(96.8,55.5));v(b,nn,(96.8,55.5));s(b,nn,F,(96.8,55.5),(96.8,58.0))
 nn=spisi;s(b,nn,F,(83.95,65.2),(85.5,65.2));s(b,nn,F,(85.5,65.2),(85.5,70));s(b,nn,F,(85.5,70),(95.6,70));s(b,nn,F,(95.6,70),(95.6,46));s(b,nn,F,(95.6,46),(95.6,58))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
