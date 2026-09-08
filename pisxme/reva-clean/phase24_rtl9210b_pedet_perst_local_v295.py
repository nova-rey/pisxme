"""V295: move the short PERST local transition to B.Cu for PEDET clearance."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_PEDET_ROUTE_V292.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_PEDET_PERST_LOCAL_V295.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.50));q.SetDrill(pcbnew.FromMM(.25));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE)); per=b.FindNet('PERST_N')
 for q in list(b.GetTracks()):
  if q.GetNetname()=='PERST_N' and q.GetLayerName()=='F.Cu' and abs(q.GetStart().x/1e6-104.5)<.01 and abs(q.GetEnd().x/1e6-104.5)<.01:
   b.RemoveNative(q)
 via(b,per,(104.5,60.0));tr(b,per,B,(104.5,60.0),(104.5,63.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
